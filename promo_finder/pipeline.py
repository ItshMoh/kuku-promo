import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from .models import Assessment, Candidate, Episode, Fidelity, Judgement, Selection, weighted_total
from .parser import load_folder
from .provider import usage_summary
from .storage import read_json, write_json
from .validation import assemble_clip, candidate_id, eligibility, judgement_errors, selected_ids, validate_candidate

PROMPT_DIR = Path(__file__).parent / "prompts"


def prompt(name: str) -> str:
    return (PROMPT_DIR / f"{name}.txt").read_text(encoding="utf-8")


def source_payload(episode: Episode) -> dict:
    return {"episode_id": episode.id, "duration_cs": episode.duration_cs,
            "context_for_selector_only": {"logline": episode.logline, "continuity": episode.continuity},
            "scenes": [s.model_dump() for s in episode.scenes],
            "events": [e.model_dump() for e in episode.events]}


def process_episode(episode: Episode, provider, output: Path, rubric: str,
                    selector_model: str, judge_model: str, max_candidates: int) -> dict:
    result_path = output / "episodes" / f"{episode.id}.json"
    result = {"episode_id": episode.id, "number": episode.number, "status": "processing",
              "source": episode.model_dump(), "candidates": [], "errors": [], "episode_assessment": ""}
    try:
        selection = provider.call(stage=f"{episode.id}-selection", model=selector_model,
                                  system=prompt("selector"), schema=Selection,
                                  payload={"source": source_payload(episode), "rubric": rubric,
                                           "maximum_candidates": max_candidates})
    except Exception as exc:
        result.update(status="api_failed", errors=[str(exc)])
        write_json(result_path, result)
        return result
    result["episode_assessment"] = selection.episode_assessment
    result["no_candidate_reason"] = selection.no_candidate_reason
    if len(selection.candidates) > max_candidates:
        result["errors"].append("Selector exceeded candidate cap; all raw proposals retained for review")
    seen = set()
    for candidate in selection.candidates:
        cid = candidate_id(episode, candidate)
        validation = validate_candidate(episode, candidate)
        if cid in seen:
            validation["errors"].append("Duplicate candidate cut sequence")
        seen.add(cid)
        row = {"id": cid, "candidate": candidate.model_dump(), "validation": validation,
               "type": "continuous" if len(candidate.segments) == 1 else "joined",
               "status": "rejected", "score": None, "judge": None, "fidelity": None, "errors": []}
        if not validation["errors"]:
            try:
                clip = assemble_clip(episode, candidate)
                judge = provider.call(stage=f"{cid}-judge", model=judge_model, system=prompt("judge"),
                                      schema=Judgement, payload={"rubric": rubric, "clip": clip,
                                      "first_three_seconds": assemble_clip(episode, candidate, 300)})
                evidence_errors = judgement_errors(episode, candidate, judge)
                row["judge"] = judge.model_dump()
                row["score"] = weighted_total(judge)
                if len(candidate.segments) == 1:
                    fidelity = Fidelity(assessment=Assessment(status="pass", reason="One intact source interval; no temporal assembly",
                                        evidence_ids=sorted(selected_ids(episode, candidate))), omitted_context_risk="None introduced by joining")
                else:
                    fidelity = provider.call(stage=f"{cid}-fidelity", model=judge_model,
                                             system=prompt("fidelity"), schema=Fidelity,
                                             payload={"source": source_payload(episode), "clip": clip,
                                                      "segments": [s.model_dump() for s in candidate.segments]})
                    if set(fidelity.assessment.evidence_ids) - {e.id for e in episode.events}:
                        evidence_errors.append("Fidelity check cites unknown source events")
                    if fidelity.assessment.status == "pass" and not fidelity.assessment.evidence_ids:
                        evidence_errors.append("Fidelity pass lacks source evidence")
                row["fidelity"] = fidelity.model_dump()
                row["errors"] = evidence_errors
                row["status"] = eligibility(validation, judge, fidelity, evidence_errors)
            except Exception as exc:
                row.update(status="api_failed", errors=[str(exc)])
        result["candidates"].append(row)
        write_json(result_path, result)
    statuses = {c["status"] for c in result["candidates"]}
    if not result["candidates"]:
        result["status"] = "no_candidate"
    elif "api_failed" in statuses:
        result["status"] = "partial_failure"
    elif "qualified" in statuses:
        result["status"] = "has_qualified"
    elif "needs_review" in statuses:
        result["status"] = "needs_review"
    else:
        result["status"] = "no_qualifying_candidate"
    write_json(result_path, result)
    return result


def run_pipeline(*, folder: Path, output: Path, provider, rubric: str, selector_model: str,
                 judge_model: str, episode_numbers: set[int] | None = None, max_candidates: int = 3,
                 workers: int = 2, progress: Callable[[str], None] = print) -> dict:
    if not 1 <= max_candidates <= 6 or not 1 <= workers <= 8:
        raise ValueError("Use 1–6 candidates and 1–8 workers")
    episodes, parse_errors = load_folder(folder)
    if not episodes:
        raise ValueError("No episodes parsed successfully")
    if episode_numbers is not None and not episode_numbers <= {e.number for e in episodes}:
        raise ValueError("Requested episode numbers are missing or failed parsing")
    config = {"selector_model": selector_model, "judge_model": judge_model, "max_candidates": max_candidates,
              "scope": "episode_only", "rubric_hash": hashlib.sha256(rubric.encode()).hexdigest(),
              "source_hashes": {e.id: e.source_hash for e in episodes},
              "prompt_hashes": {n: hashlib.sha256(prompt(n).encode()).hexdigest() for n in ("selector", "judge", "fidelity")},
              "engine_version": hashlib.sha256(b"".join(p.read_bytes() for p in sorted(Path(__file__).parent.glob("*.py")))).hexdigest()}
    fingerprint = hashlib.sha256(json.dumps(config, sort_keys=True).encode()).hexdigest()
    manifest_path = output / "manifest.json"
    if manifest_path.exists():
        manifest = read_json(manifest_path)
        if manifest["fingerprint"] != fingerprint:
            raise ValueError("Run configuration or source changed. Choose a new output folder to preserve the old run")
    else:
        manifest = {"created_at": datetime.now(timezone.utc).isoformat(), "fingerprint": fingerprint, "config": config}
    write_json(manifest_path, manifest)
    write_json(output / "rubric.md.json", {"text": rubric})
    write_json(output / "inventory.json", {"episodes": [e.model_dump() for e in episodes], "errors": parse_errors})
    requested = [e for e in episodes if episode_numbers is None or e.number in episode_numbers]
    pending = []
    for episode in requested:
        path = output / "episodes" / f"{episode.id}.json"
        prior = read_json(path) if path.exists() else None
        if prior and prior["status"] not in ("processing", "api_failed", "partial_failure", "processing_failed"):
            progress(f"{episode.id}: using saved result")
        else:
            pending.append(episode)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(process_episode, e, provider, output, rubric, selector_model,
                               judge_model, max_candidates): e for e in pending}
        for future in as_completed(futures):
            episode = futures[future]
            try:
                result = future.result()
                progress(f"{episode.id}: {result['status']} ({len(result['candidates'])} candidates)")
            except Exception as exc:
                write_json(output / "episodes" / f"{episode.id}.json", {"episode_id": episode.id,
                           "number": episode.number, "status": "processing_failed", "source": episode.model_dump(),
                           "candidates": [], "errors": [type(exc).__name__]})
                progress(f"{episode.id}: processing_failed")
    summary = {"parsed_episodes": len(episodes), "parse_errors": parse_errors,
               "requested_episodes": [e.number for e in requested], "scope": "episode_only",
               "usage": usage_summary(output / "raw")}
    write_json(output / "summary.json", summary)
    return summary

import csv
import io
from pathlib import Path

from .models import WEIGHTS
from .parser import timestamp
from .storage import read_json, write_json


def load_results(run: Path) -> list[dict]:
    return [read_json(p) for p in sorted((run / "episodes").glob("*.json"))]


def load_reviews(run: Path) -> dict:
    return {p.stem: read_json(p) for p in (run / "reviews").glob("*.json")}


def segment_label(candidate: dict) -> str:
    return " → ".join(f"{s['episode_id']} {timestamp(s['start_cs'])}–{timestamp(s['end_cs'])}"
                      for s in candidate["segments"])


def comparison_rows(results: list[dict], reviews: dict | None = None) -> list[dict]:
    reviews = reviews or {}
    rows = []
    for episode in results:
        candidates = sorted(episode["candidates"], key=lambda c: c["score"] if c["score"] is not None else -1, reverse=True)
        qualifying_rank, qualified_count, prior_score = 0, 0, None
        for candidate in candidates:
            if candidate["status"] == "qualified":
                qualified_count += 1
                if candidate["score"] != prior_score:
                    qualifying_rank, prior_score = qualified_count, candidate["score"]
            draft = candidate["candidate"]
            row = {"id": candidate["id"], "episode": episode["number"], "title": draft["title"],
                   "type": candidate["type"], "status": candidate["status"],
                   "human_review": reviews.get(candidate["id"], {}).get("decision", "unreviewed"),
                   "episode_rank": qualifying_rank if candidate["status"] == "qualified" else None,
                   "global_rank": None, "score": candidate["score"],
                   "duration_seconds": candidate["validation"]["duration_cs"] / 100,
                   "segments": segment_label(draft), "opening_question": draft["opening_question"],
                   "ending_question": draft["ending_question"], "rationale": draft["rationale"],
                   "weakness": (candidate["judge"] or {}).get("main_weakness", draft["weakness"]),
                   "errors": " | ".join(candidate["validation"]["errors"] + candidate["errors"])}
            for key in WEIGHTS:
                row[key] = candidate["judge"]["scores"][key]["value"] if candidate["judge"] else None
            rows.append(row)
    qualified = sorted((r for r in rows if r["status"] == "qualified"), key=lambda r: (-r["score"], r["id"]))
    # Equal editorial totals share a rank; tiny subjective differences are not statistical evidence.
    prior, rank = None, 0
    for i, row in enumerate(qualified, 1):
        if row["score"] != prior:
            prior, rank = row["score"], i
        row["global_rank"] = rank
    return rows


def csv_text(rows: list[dict], fields: list[str] | None = None) -> str:
    output = io.StringIO()
    fields = fields or (list(rows[0]) if rows else ["id", "episode", "status"])
    writer = csv.DictWriter(output, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def export_report(run: Path) -> dict:
    inventory = read_json(run / "inventory.json")
    results = load_results(run)
    reviews = load_reviews(run)
    rows = comparison_rows(results, reviews)
    by_episode = {e["episode_id"]: e for e in results}
    coverage = []
    for source in inventory["episodes"]:
        result = by_episode.get(source["id"], {})
        candidates = [r for r in rows if r["episode"] == source["number"]]
        qualified = [c for c in candidates if c["status"] == "qualified"]
        best = sorted(qualified or candidates, key=lambda c: c["score"] if c["score"] is not None else -1, reverse=True)
        coverage.append({"episode": source["number"], "episode_id": source["id"],
                         "status": result.get("status", "not_processed"), "candidates": len(candidates),
                         "qualified": len(qualified), "best_available_candidate": best[0]["id"] if best else "",
                         "best_available_status": best[0]["status"] if best else "",
                         "source_warnings": " | ".join(source["warnings"])})
    exports = run / "exports"
    exports.mkdir(parents=True, exist_ok=True)
    write_json(exports / "candidates.json", {"scope": "episode_only", "rows": rows})
    write_json(exports / "coverage.json", {"rows": coverage, "parse_errors": inventory["errors"]})
    (exports / "candidates.csv").write_text(csv_text(rows), encoding="utf-8")
    (exports / "coverage.csv").write_text(csv_text(coverage), encoding="utf-8")
    text = ["# Episode-only promo report", "", "Editorial scores; no footage or audience-performance validation.",
            "Human decisions are recorded separately and do not rewrite model scores.", ""]
    for source in inventory["episodes"]:
        result = by_episode.get(source["id"], {})
        text.extend([f"## Episode {source['number']} — {result.get('status', 'not_processed')}", "",
                     result.get("episode_assessment", ""), result.get("no_candidate_reason", ""), ""])
        for c in [r for r in rows if r["episode"] == source["number"]]:
            text.extend([f"### {c['title']}", f"- ID: {c['id']}; {c['type']}; {c['status']}; score: {c['score']}",
                         f"- Segments: {c['segments']} ({c['duration_seconds']:.2f}s)",
                         f"- Opening question: {c['opening_question']}", f"- Ending question: {c['ending_question']}",
                         f"- Why: {c['rationale']}", f"- Weakness: {c['weakness']}",
                         f"- Human review: {c['human_review']}", f"- Validation issues: {c['errors'] or 'None'}", ""])
    (exports / "report.md").write_text("\n".join(text), encoding="utf-8")
    return {"coverage": coverage, "candidates": rows, "parse_errors": inventory["errors"]}

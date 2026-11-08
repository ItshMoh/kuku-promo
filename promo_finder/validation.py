import hashlib
import json

from .models import Candidate, Episode, Fidelity, Judgement


def candidate_id(episode: Episode, candidate: Candidate) -> str:
    cuts = [s.model_dump() for s in candidate.segments]
    digest = hashlib.sha256(json.dumps(cuts, sort_keys=True).encode()).hexdigest()[:10]
    return f"{episode.id}-{digest}"


def selected_ids(episode: Episode, candidate: Candidate) -> set[str]:
    return {e.id for e in episode.events for s in candidate.segments
            if s.episode_id == episode.id and e.start_cs < s.end_cs and e.end_cs > s.start_cs}


def validate_candidate(episode: Episode, candidate: Candidate) -> dict:
    errors, flags = [], []
    duration = sum(s.end_cs - s.start_cs for s in candidate.segments)
    if not 1 <= len(candidate.segments) <= 3:
        errors.append("Select between one and three source segments")
    if not 2000 <= duration <= 6000:
        errors.append("Combined duration must be 20–60 seconds")
    boundaries = {0, episode.duration_cs}
    for event in episode.events:
        boundaries.update((event.start_cs, event.end_cs))
    for scene in episode.scenes:
        boundaries.update((scene.start_cs, scene.end_cs))
    for i, segment in enumerate(candidate.segments):
        if segment.episode_id != episode.id:
            errors.append("Cross-episode content is disabled: every segment must belong to this episode")
        if not 0 <= segment.start_cs < segment.end_cs <= episode.duration_cs:
            errors.append(f"Segment {i + 1} is outside episode bounds or has no positive duration")
        if segment.start_cs not in boundaries or segment.end_cs not in boundaries:
            errors.append(f"Segment {i + 1} boundaries must match source event or scene timestamps")
        if i and segment.start_cs <= candidate.segments[i - 1].end_cs:
            errors.append("Segments must be chronological and separated; merge adjacent or overlapping intervals")
        for event in episode.events:
            if event.kind != "dialogue":
                continue
            if event.start_cs < segment.start_cs < event.end_cs or event.start_cs < segment.end_cs < event.end_cs:
                errors.append(f"Segment {i + 1} cuts dialogue event {event.id}")
    available = selected_ids(episode, candidate)
    for field in ("hook_event_ids", "cliffhanger_event_ids"):
        refs = getattr(candidate, field)
        if not refs:
            errors.append(f"{field} must cite source events")
        if set(refs) - available:
            errors.append(f"{field} cites events outside the selected clip")
    first = assemble_clip(episode, candidate, limit_cs=300)
    opening_ids = {e["event_id"] for seg in first["segments"] for e in seg["events"]}
    if not (set(candidate.hook_event_ids) & opening_ids):
        errors.append("No cited hook event occurs in the first three playback seconds")
    if len(candidate.segments) > 1:
        flags.append("Joined selection: review omitted context and transition continuity")
    if any(e.kind == "dialogue" and e.id in candidate.hook_event_ids
           and e.text.lstrip('\"“').startswith("...") for e in episode.events):
        flags.append("Opening includes a continuation line; check whether it works independently")
    if any(e["kind"] == "dialogue" and e["partial"] for s in first["segments"] for e in s["events"]):
        flags.append("Opening contains partial dialogue: precise first-three-second words need footage review")
    return {"errors": sorted(set(errors)), "flags": flags, "duration_cs": duration,
            "source_event_ids": sorted(available)}


def assemble_clip(episode: Episode, candidate: Candidate, limit_cs: int | None = None) -> dict:
    """Build the actual playback sequence, including events already active at each cut."""
    output, offset = [], 0
    speakers = {name: f"speaker-{i + 1}" for i, name in enumerate(dict.fromkeys(
        e.speaker for e in episode.events if e.speaker))}
    for index, segment in enumerate(candidate.segments):
        if segment.episode_id != episode.id:
            continue  # Validation rejects this; never accidentally resolve a foreign segment locally.
        start, end = segment.start_cs, segment.end_cs
        if limit_cs is not None:
            if offset >= limit_cs:
                break
            end = min(end, start + limit_cs - offset)
        if end <= start:
            continue
        events = []
        for event in sorted(episode.events, key=lambda e: (e.start_cs, e.id)):
            lo, hi = max(start, event.start_cs), min(end, event.end_cs)
            if lo >= hi:
                continue
            partial = lo != event.start_cs or hi != event.end_cs
            body = event.text
            if partial and event.kind == "dialogue":
                body = "[Partial dialogue: exact audible words cannot be inferred from line-level timing.]"
            events.append({"event_id": event.id, "kind": event.kind,
                           "speaker": speakers.get(event.speaker),
                           "playback_start_cs": offset + lo - start,
                           "playback_end_cs": offset + hi - start,
                           "source_start_cs": lo, "source_end_cs": hi,
                           "partial": partial, "text": body})
        output.append({"segment_number": index + 1, "playback_start_cs": offset,
                       "playback_end_cs": offset + end - start, "source_start_cs": start,
                       "source_end_cs": end, "events": events})
        offset += end - start
    return {"duration_cs": offset, "segments": output}


def judgement_errors(episode: Episode, candidate: Candidate, judgement: Judgement) -> list[str]:
    allowed = selected_ids(episode, candidate)
    errors = []
    assessments = [judgement.opening_hook, judgement.standalone_meaning,
                   judgement.unresolved_ending, judgement.existing_material, judgement.transition_coherence]
    for assessment in assessments:
        if set(assessment.evidence_ids) - allowed:
            errors.append("Judge cites evidence outside the selected clip")
        if assessment.status == "pass" and not assessment.evidence_ids:
            errors.append("Passing judgement lacks source evidence")
    for score in judgement.scores.model_dump().values():
        if set(score["evidence_ids"]) - allowed or (score["value"] > 0 and not score["evidence_ids"]):
            errors.append("Score evidence is missing or outside the clip")
    first_ids = {e["event_id"] for s in assemble_clip(episode, candidate, 300)["segments"] for e in s["events"]}
    for score in (judgement.scores.opening_impact, judgement.scores.opening_curiosity):
        if set(score.evidence_ids) - first_ids:
            errors.append("Opening score cites an event outside the first three seconds")
    if set(judgement.opening_hook.evidence_ids) - first_ids:
        errors.append("Opening hook assessment cites an event outside the first three seconds")
    return sorted(set(errors))


def eligibility(validation: dict, judgement: Judgement | None, fidelity: Fidelity | None,
                evidence_errors: list[str]) -> str:
    if validation["errors"]:
        return "rejected"
    # An invalid judge citation is an evaluation failure, not proof that the source clip is bad.
    # Keep it out of qualifying ranks and ask for review instead of conflating the two.
    if evidence_errors:
        return "needs_review"
    if judgement is None or fidelity is None:
        return "needs_review"
    checks = [judgement.opening_hook, judgement.standalone_meaning, judgement.unresolved_ending,
              judgement.existing_material, judgement.transition_coherence, fidelity.assessment]
    if any(a.status == "fail" for a in checks):
        return "rejected"
    if any(a.status == "needs_review" for a in checks):
        return "needs_review"
    return "qualified"

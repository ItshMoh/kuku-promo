from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


class Event(Model):
    id: str
    scene_id: str
    kind: Literal["camera", "action", "dialogue", "sound"]
    speaker: str | None
    direction: str | None
    start_cs: int
    end_cs: int
    text: str
    line: int


class Scene(Model):
    id: str
    heading: str
    start_cs: int
    end_cs: int


class Episode(Model):
    id: str
    number: int
    source_path: str
    source_hash: str
    logline: str
    continuity: str
    duration_cs: int
    scenes: list[Scene]
    events: list[Event]
    warnings: list[str]


class Segment(Model):
    episode_id: str
    start_cs: int
    end_cs: int


class Candidate(Model):
    title: str
    segments: list[Segment]
    appeal: str
    hook_event_ids: list[str]
    opening_question: str
    emotional_stakes: str
    cliffhanger_event_ids: list[str]
    ending_question: str
    rationale: str
    weakness: str
    transition_explanation: str


class Selection(Model):
    candidates: list[Candidate]
    episode_assessment: str
    no_candidate_reason: str


Status = Literal["pass", "fail", "needs_review"]


class Assessment(Model):
    status: Status
    reason: str
    evidence_ids: list[str]


class Score(Model):
    value: int = Field(ge=0, le=5)
    reason: str
    evidence_ids: list[str]


class Scores(Model):
    opening_impact: Score
    emotional_investment: Score
    opening_curiosity: Score
    newcomer_clarity: Score
    momentum: Score
    ending_cliffhanger: Score


class Judgement(Model):
    opening_hook: Assessment
    standalone_meaning: Assessment
    unresolved_ending: Assessment
    existing_material: Assessment
    transition_coherence: Assessment
    scores: Scores
    newcomer_situation: str
    continuation_question: str
    main_weakness: str
    footage_review: str


class Fidelity(Model):
    assessment: Assessment
    omitted_context_risk: str


WEIGHTS = {
    "opening_impact": 20,
    "emotional_investment": 20,
    "opening_curiosity": 10,
    "newcomer_clarity": 15,
    "momentum": 10,
    "ending_cliffhanger": 25,
}


def weighted_total(judgement: Judgement) -> float:
    return round(sum(WEIGHTS[k] * getattr(judgement.scores, k).value / 5 for k in WEIGHTS), 2)

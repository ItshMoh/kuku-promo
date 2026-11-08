import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from promo_finder.models import Assessment, Candidate, Fidelity, Judgement, Score, Scores, Segment, Selection, WEIGHTS, weighted_total
from promo_finder.parser import load_folder, parse_episode, parse_time, timestamp
from promo_finder.pipeline import run_pipeline
from promo_finder.provider import ModelCallError, OpenAIProvider
from promo_finder.reporting import export_report
from promo_finder.validation import assemble_clip, eligibility, judgement_errors, validate_candidate
from promo_finder import cli

ROOT = Path(__file__).resolve().parent.parent


def candidate(joined=False):
    cuts = [(0, 1000), (2000, 3500)] if joined else [(0, 3500)]
    return Candidate(title="A signature before midnight", segments=[Segment(episode_id="ep-001", start_cs=s, end_cs=e) for s, e in cuts],
                     appeal="impossible choice", hook_event_ids=["ep-001-b0002"], opening_question="Will she surrender the deed?",
                     emotional_stakes="Her brother may die.", cliffhanger_event_ids=["ep-001-b0007"],
                     ending_question="Will she sign before the bell rings?", rationale="Clear threat and unresolved choice.",
                     weakness="Threat depends on delivery.", transition_explanation="The omitted clock shot does not alter dialogue.")


def judge():
    opening = Assessment(status="pass", reason="A threat within two seconds.", evidence_ids=["ep-001-b0002"])
    general = Assessment(status="pass", reason="The signature is still unresolved.", evidence_ids=["ep-001-b0007"])
    scores = {key: Score(value=3, reason="Clear but unverified in footage.",
                        evidence_ids=["ep-001-b0002" if key.startswith("opening") else "ep-001-b0007"])
              for key in WEIGHTS}
    return Judgement(opening_hook=opening, standalone_meaning=general, unresolved_ending=general,
                     existing_material=general, transition_coherence=general, scores=Scores(**scores),
                     newcomer_situation="A courier must sign to save her brother.", continuation_question="Will she sign?",
                     main_weakness="Delivery unknown.", footage_review="Synthetic scripted example, no footage.")


class FakeProvider:
    """Deterministic test double, never represented as an actual model judgement."""
    def __init__(self):
        self.calls = []

    def call(self, **kwargs):
        self.calls.append(kwargs)
        if kwargs["schema"] is Selection:
            return Selection(candidates=[candidate(), candidate(True)], episode_assessment="Synthetic test only.", no_candidate_reason="")
        if kwargs["schema"] is Judgement:
            return judge()
        return Fidelity(assessment=Assessment(status="pass", reason="Clock shot omitted.", evidence_ids=["ep-001-b0005"]),
                        omitted_context_risk="None in fixture.")


class SourceTests(unittest.TestCase):
    def setUp(self):
        self.episode = parse_episode(ROOT / "examples" / "episode-001.txt")

    def test_parallel_tracks_do_not_add_duration(self):
        self.assertEqual(self.episode.duration_cs, 6000)
        self.assertEqual(len(self.episode.events), 9)
        self.assertEqual(self.episode.events[1].start_cs, 0)

    def test_uppercase_and_source_lines(self):
        self.assertEqual(self.episode.scenes[0].heading, "INT. CLOCK TOWER - NIGHT")
        source_lines = Path(self.episode.source_path).read_text().splitlines()
        for event in self.episode.events:
            self.assertTrue(source_lines[event.line - 1].startswith("**"))

    def test_timestamp_arithmetic_is_exact(self):
        self.assertEqual(parse_time("01:09.20") - parse_time("00:44.00"), 2520)
        self.assertEqual(timestamp(20075), "03:20.75")
        with self.assertRaises(ValueError):
            parse_time("00:60.00")

    def test_continuous_and_joined_are_valid(self):
        self.assertEqual(validate_candidate(self.episode, candidate())["errors"], [])
        validation = validate_candidate(self.episode, candidate(True))
        self.assertEqual(validation["errors"], [])
        self.assertEqual(validation["duration_cs"], 2500)

    def test_foreign_episode_is_rejected(self):
        cut = candidate()
        cut.segments[0].episode_id = "ep-002"
        self.assertIn("Cross-episode", " ".join(validate_candidate(self.episode, cut)["errors"]))

    def test_cutting_dialogue_and_overlap_are_rejected(self):
        cut = candidate()
        cut.segments[0].start_cs = 100
        self.assertIn("cuts dialogue", " ".join(validate_candidate(self.episode, cut)["errors"]))
        cut = candidate(True)
        cut.segments[1].start_cs = 500
        self.assertIn("overlapping", " ".join(validate_candidate(self.episode, cut)["errors"]))

    def test_preview_includes_active_camera_and_hides_partial_dialogue(self):
        cut = candidate()
        cut.segments[0].start_cs = 100
        first = assemble_clip(self.episode, cut, 100)
        events = first["segments"][0]["events"]
        self.assertIn("ep-001-b0001", [e["event_id"] for e in events])
        dialogue = next(e for e in events if e["kind"] == "dialogue")
        self.assertTrue(dialogue["partial"])
        self.assertNotIn("brother dies", dialogue["text"])

    def test_joined_preview_uses_playback_not_source_time(self):
        cut = candidate(True)
        cut.segments[0].end_cs = 200
        first = assemble_clip(self.episode, cut, 300)
        self.assertEqual(first["duration_cs"], 300)
        self.assertEqual(first["segments"][1]["source_start_cs"], 2000)
        self.assertEqual(first["segments"][1]["playback_start_cs"], 200)

    def test_judge_cannot_cite_later_hook_or_outside_clip(self):
        output = judge()
        output.scores.opening_impact.evidence_ids = ["ep-001-b0008"]
        errors = judgement_errors(self.episode, candidate(), output)
        self.assertTrue(errors)

    def test_failed_eligibility_cannot_be_offset_by_score(self):
        output = judge()
        output.unresolved_ending.status = "fail"
        fidelity = Fidelity(assessment=output.existing_material, omitted_context_risk="None")
        self.assertEqual(weighted_total(output), 60)
        self.assertEqual(eligibility(validate_candidate(self.episode, candidate()), output, fidelity, []), "rejected")

    def test_judge_citation_failure_requires_review_instead_of_rejecting_source_clip(self):
        output = judge()
        fidelity = Fidelity(assessment=output.existing_material, omitted_context_risk="None")
        self.assertEqual(eligibility(validate_candidate(self.episode, candidate()), output, fidelity,
                                     ["Opening hook assessment cites an event outside the first three seconds"]),
                         "needs_review")

    def test_malformed_event_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.txt"
            path.write_text((ROOT / "examples" / "episode-001.txt").read_text().replace("End: (00:02.00)", "End: (bad)"))
            episodes, errors = load_folder(Path(folder))
            self.assertEqual(episodes, [])
            self.assertEqual(len(errors), 1)

    def test_private_input_pack_when_present(self):
        folder = ROOT / "I Married a Broken Soldier. He was a Duke"
        if not folder.is_dir():
            self.skipTest("Confidential input pack is not distributed with code")
        episodes, errors = load_folder(folder)
        self.assertEqual(errors, [])
        self.assertEqual(len(episodes), 50)
        self.assertEqual(sum(len(e.events) for e in episodes), 3727)
        self.assertEqual(min(e.duration_cs for e in episodes), 7050)
        self.assertEqual(max(e.duration_cs for e in episodes), 20075)


class WorkflowTests(unittest.TestCase):
    def test_key_added_after_blank_template_is_loaded_without_replacing_existing_key(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / ".env").write_text("OPENAI_API_KEY=fixture-value\n")
            with patch.object(cli, "ROOT", base), patch.dict(os.environ, {"OPENAI_API_KEY": ""}):
                cli.load_environment()
                self.assertEqual(os.environ["OPENAI_API_KEY"], "fixture-value")
                os.environ["OPENAI_API_KEY"] = "existing-value"
                cli.load_environment()
                self.assertEqual(os.environ["OPENAI_API_KEY"], "existing-value")

    def test_judge_is_blind_full_run_exports_and_resume(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            provider = FakeProvider()
            kwargs = dict(folder=ROOT / "examples", output=output, provider=provider, rubric="rubric-v1",
                          selector_model="test-selector", judge_model="test-judge", workers=1, progress=lambda _: None)
            run_pipeline(**kwargs)
            exported = export_report(output)
            self.assertEqual(len(exported["coverage"]), 1)
            self.assertEqual(len(exported["candidates"]), 2)
            self.assertEqual({r["status"] for r in exported["candidates"]}, {"qualified"})
            self.assertEqual({r["global_rank"] for r in exported["candidates"]}, {1})
            judge_calls = [c for c in provider.calls if c["schema"] is Judgement]
            self.assertEqual(len(judge_calls), 2)
            for call in judge_calls:
                payload = json.dumps(call["payload"])
                self.assertNotIn("context_for_selector_only", payload)
                self.assertNotIn("logline", payload)
                self.assertNotIn("Clear threat and unresolved choice", payload)
            count = len(provider.calls)
            run_pipeline(**kwargs)
            self.assertEqual(len(provider.calls), count)
            kwargs["rubric"] = "rubric-v2"
            with self.assertRaisesRegex(ValueError, "configuration or source changed"):
                run_pipeline(**kwargs)

    def test_raw_refusal_is_retained_and_not_cached_as_success(self):
        with tempfile.TemporaryDirectory() as folder:
            provider = OpenAIProvider(Path(folder), "test-key")
            response = Mock(status="completed", output_text="")
            response.model_dump_json.return_value = '{"status":"completed","output":[{"type":"refusal"}]}'
            provider.client = Mock()
            provider.client.responses.create.return_value = response
            with self.assertRaises(ModelCallError):
                provider.call(stage="test", model="test", system="test", payload={}, schema=Selection)
            self.assertEqual(len(list(Path(folder).glob("*/*.response.json"))), 1)
            self.assertEqual(list(Path(folder).glob("*/parsed.json")), [])


if __name__ == "__main__":
    unittest.main()

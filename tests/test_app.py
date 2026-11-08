import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest

from promo_finder import cli
from promo_finder.pipeline import run_pipeline
from promo_finder.storage import read_json
from test_pipeline import FakeProvider, ROOT


class AppTests(unittest.TestCase):
    def test_source_view_without_key_and_saved_joined_review(self):
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            (base / "criteria.md").write_text("Synthetic test rubric")
            run = base / "runs" / "synthetic-test"
            run_pipeline(folder=ROOT / "examples", output=run, provider=FakeProvider(),
                         rubric="Synthetic test rubric", selector_model="test-selector", judge_model="test-judge",
                         workers=1, progress=lambda _: None)
            with patch.object(cli, "ROOT", base), patch.object(cli, "DEFAULT_INPUT", ROOT / "examples"):
                app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=20).run()
                self.assertEqual(list(app.exception), [])
                self.assertEqual(app.metric[0].value, "1")
                app.sidebar.selectbox[0].select("runs/synthetic-test").run()
                self.assertEqual(list(app.exception), [])
                self.assertEqual(app.metric[2].value, "2")
                candidate_picker = next(s for s in app.selectbox if s.label == "Candidate")
                candidate_picker.select_index(1).run()
                save = next(b for b in app.button if b.label == "Save human review")
                save.click().run()
                self.assertEqual(list(app.exception), [])
                saved = list((run / "reviews").glob("*.json"))
                self.assertEqual(len(saved), 1)
                self.assertFalse(read_json(saved[0])["model_scores_visible"])
                app.sidebar.checkbox[0].check().run()
                self.assertEqual(list(app.exception), [])
                self.assertEqual(app.metric[3].value, "2")


if __name__ == "__main__":
    unittest.main()

# Kuku promo finder

Select and compare 20–60-second promos from timestamped episode scripts. **Every candidate uses content from exactly one episode.** Continuous clips and chronological joins of up to three moments within that episode are supported. Cross-episode series promos are deferred.

Luna proposes candidates from a complete episode. Code validates the cuts and reconstructs their actual source timeline. Sol judges the assembled clip without the episode logline or the selector's rationale. A separate Sol check inspects omitted source context for joined clips. Human reviews are stored separately.

## Setup

Python 3.11 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
python -m pip install -e .
cp .env.example .env
```

Set `OPENAI_API_KEY` in your local `.env` file. Model defaults are `gpt-6-luna` for selection and `gpt-6.1-sol` for judging. Model availability depends on the API account. Do not commit keys or confidential source-bearing outputs. The original Kuku input folder is intentionally ignored by Git; use your authorized local copy. A synthetic screenplay is provided in `examples/`.

The lock file records the dependency versions used for the local verification run. After adding a key while Streamlit is open, click **Recheck API configuration** or refresh the page. Existing nonempty environment settings take precedence over `.env`.

## Commands

Parse the full supplied input folder without an API key:

```bash
python -m promo_finder parse
```

Run a small pilot before the full pack:

```bash
python -m promo_finder run --episodes 3,6,12,23,45,50 --output runs/pilot-v2
```

Review the pilot, record disagreements, and use a new output folder when changing prompts, code, models, or the rubric. To resume an interrupted run, repeat the same command. Successful requests are reused; failures can be retried. Repeating a failed request may incur another API charge.

After calibration and verification, process all episodes:

```bash
python -m promo_finder run --output runs/full
```

Run on a new input and override models independently:

```bash
python -m promo_finder run examples --output runs/synthetic --selector-model gpt-6-luna --judge-model gpt-6.1-sol
```

Launch the local review app:

```bash
python -m streamlit run app.py
```

Rebuild exports from saved results without making API calls:

```bash
python -m promo_finder report runs/pilot-v2
```

## Review and outputs

The app opens in source-only mode when no run is selected. Choose a saved run in the sidebar. Model scores and explanations are hidden by default so you can record a first impression independently. Each candidate exposes its first three playback seconds, full assembled source timeline, source line references, validation issues, and a human review form. Select **Show model scores and explanations** to inspect Sol's six scores, eligibility assessments, and evidence.

`runs/<name>/` stores:

- `inventory.json`: all parsed episodes, source hashes, original event text, and parse failures.
- `raw/`: complete requests and unedited serialized model responses, including unsuccessful attempts. No API keys.
- `episodes/`: candidate cuts, validation, evaluations, and per-episode processing status.
- `manifest.json`, `summary.json`: model/prompt/source/code fingerprints and actual token usage.
- `reviews/`: human decisions and explanations, separate from original outputs.
- `exports/`: candidate JSON/CSV, episode coverage JSON/CSV, and a Markdown report.

All source-bearing outputs remain local and ignored by Git. Share real-input raw outputs only through the assignment's intended submission channel. The synthetic fixture can be shared with the runnable code.

The coverage export includes every parsed episode, even when not processed, no candidate is returned, every selection fails, or an API call fails. A best available candidate can be reported as rejected or needing review; it is not promoted to a qualifying selection. Global ranking compares episode-only promos and does not assemble a series promo. Equal global scores share rank. Human approval/rejection never silently rewrites model scores.

## Rubric and limits

`criteria.md` is the scoring reference: opening impact 20%, emotional investment 20%, opening curiosity 10%, newcomer clarity 15%, momentum 10%, ending cliffhanger 25%. Each 0–5 score contributes `weight * score / 5`. Eligibility failures cannot be compensated by a high total.

- Camera, action, sound and dialogue tracks overlap; their lengths must not be added to estimate clip duration.
- Source times use integer centiseconds. Boundaries must exist in the script. Cutting through a dialogue event fails validation.
- The first-three-second preview withholds text from partially included dialogue events because line-level timestamps cannot locate individual words. Partial visual descriptions are flagged, not assumed to occur entirely inside the fragment.
- Screenplay labels and camera directions are not proof that an audience sees the intended emotion or understands a hidden identity. Footage review remains necessary.
- Same-episode joins need both clip-level coherence and a source-context fidelity check. Candidate search is bounded, not exhaustive.
- Editorial scores are subjective, uncalibrated predictions of neither conversion nor virality. Human calibration and audience testing are different forms of evidence.
- A two-page submission PDF and claims about real model quality must be based on actual runs and review. No fabricated scores, model failures, or campaign metrics are shipped.

## Verification

```bash
python -m unittest discover -s tests -v
```

Tests exercise episode isolation, parallel timing, dialogue boundaries, missing event handling, first-three-second reconstruction, blinded evaluation, evidence validation, score gates, resume fingerprints, and raw refusal retention. A deterministic test double verifies the workflow; its output is never presented as actual Luna/Sol results.

Official references: [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).

If a running development server reports a stale import after source changes, restart it with the same Streamlit command. The project enables polling to reload source modules; saved runs remain on disk. The current verified six-episode pilot is `runs/pilot-v2`.

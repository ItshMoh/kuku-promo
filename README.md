# KuKu-Promo

Kuku Promo Studio finds 20–60-second promos from timestamped episode scripts. It gives editors source cut lists, hooks, cliffhangers, explanations and a suggested posting order. The objective is **show continuation**: help a new viewer understand the situation, care about the outcome and want to keep watching.

[Live Streamlit app](https://kuku-promo-z8wqktysaxybc5dxxlmwed.streamlit.app/) · [Presentation video](https://drive.google.com/file/d/1-eHujpzfuODN01KMQyHxXAUf0dnTzAfd/view?usp=sharing) · [GitHub repository](https://github.com/ItshMoh/kuku-promo)

## Results and exports

- **All 50 selected promo scores and reasons:** [CSV](exports/episode_recommendations.csv) · [JSON](exports/episode_recommendations.json).
- **Qualified posting queue, one promo per episode:** [episode_posting_order.csv](exports/episode_posting_order.csv).
- **All 95 alternatives and criterion scores:** [candidates.csv](exports/candidates.csv).
- **Detailed episode explanations and file guide:** [report.md](exports/report.md).

The saved run covers **50 episodes and 95 candidates**: 86 continuous and 9 joined. Of these, **26 qualify, 37 need review and 32 are rejected**. The qualified episode posting queue contains **23 episodes**. Every episode retains a best available cut, with its status visible; not every cut is recommended for posting.

**First recommendation: Episode 23**, `01:19.00–02:11.50`, **52.5 seconds, 74/100**. “Someone is poisoning her” supplies an immediate hook; unfinished treatment and an opening door leave the rescue unresolved. The visitor is not established as the poisoner.

Rank exact promo cuts, not entire episodes. Qualified cuts are ordered by score; ties retain equal rank. Posting priority breaks ties by cliffhanger, newcomer clarity, opening impact and finally a stable ID. Episode number earns no preference. Episode 12 also scores 74, but Episode 23 leads through the tie-break.

## Scope

**Every candidate uses content from exactly one episode:** either one continuous interval or two to three chronological, non-overlapping intervals. Cross-episode promos are deferred. Selection uses existing dialogue, visuals and sound; no invented narration, overlays or added music. The app provides text previews and editing instructions, not rendered videos. The target is an unfamiliar English-speaking US viewer.

## Approach

1. **Parse:** Extract timestamped scenes, camera directions, action, dialogue and sound with traceable event IDs. Preserve simultaneous tracks and source cut boundaries.
2. **Select:** Luna proposes alternative cuts from one complete episode, explaining the opening hook, emotional stakes, unresolved ending and main weakness. The candidate limit is a maximum, not a required count.
3. **Validate:** Code checks duration, same-episode boundaries, chronology, overlap and whole dialogue lines. Reconstruct the promo and its first three seconds, withholding words whose exact timing is unknown.
4. **Judge:** Sol independently evaluates the assembled cut without Luna's rationale, the episode logline or prior-episode context. It scores evidence against the rubric; a separate full-source check tests whether joined clips preserve meaning.
5. **Review and rank:** Calibrate on a six-episode pilot, process the full pack and retain failures. Editors compare alternatives and record decisions. Save outputs for reuse, then rank qualified cuts across episodes.

## Judging criteria

**Eligibility comes first.** Each candidate must meet all six requirements before ranking:

1. **Duration:** selected segments total 20–60 seconds.
2. **Opening hook:** an identifiable hook occurs within the first three seconds.
3. **Standalone meaning:** a newcomer can understand the basic conflict or situation.
4. **Unresolved ending:** a meaningful, consequential outcome remains open at the cut point.
5. **Source fidelity:** timestamps are traceable and the selected segments preserve the story's meaning.
6. **Existing material:** the hook and context work without invented dialogue, narration, added music or text overlays.

Checks return **pass, fail or needs review**. A high score cannot compensate for a failed requirement.

| Criterion | Weight | Main question |
| --- | ---: | --- |
| Opening impact | 20% | Is there an immediately understandable reason to stop within three seconds? |
| Emotional investment | 20% | Who matters, and what do they want or stand to lose? |
| Opening curiosity | 10% | What specific question encourages continued attention? |
| Newcomer clarity | 15% | Are the conflict, relationships and stakes understandable without prior episodes? |
| Momentum | 10% | Does the situation develop, escalate or change through the clip? |
| Ending cliffhanger | 25% | What consequential outcome makes us want the next scene? |

Rate each criterion **0–5**; calculate `sum(weight × rating / 5)` using the percentage weights as points for a total out of 100. Use 0 for absent, 1 for weak, 3 for clear and reasonably compelling, and 5 for exceptionally strong; 2 and 4 are intermediate ratings. Each score requires source evidence.

The ending has the largest weight because the objective is continuation. Opening curiosity carries the viewer into the clip; the ending cliffhanger carries them beyond it. Romance, revenge, betrayal, status reversal and rescue are appeal labels, not automatic bonus points. These are proposed editorial weights, not validated predictions of views or conversion. See the [full rubric and scoring anchors](criteria.md).

## Review and outputs

The app opens the full-pack run when available, otherwise the bundled synthetic demo or source-only mode. Choose a saved run in the sidebar. Model scores and explanations are hidden by default so you can record a first impression independently. Each candidate exposes its first three playback seconds, full assembled source timeline, source line references, validation issues, and a human review form. Select **Show model scores and explanations** to inspect Sol's six scores, eligibility assessments, and evidence. [Editor workflow](docs/USER_GUIDE.md) explains folder, upload and paste input.

`runs/<name>/` stores:

- `inventory.json`: all parsed episodes, source hashes, original event text, and parse failures.
- `raw/`: complete requests and unedited serialized model responses, including unsuccessful attempts. No API keys.
- `episodes/`: candidate cuts, validation, evaluations, and per-episode processing status.
- `manifest.json`, `summary.json`: model/prompt/source/code fingerprints and actual token usage.
- `reviews/`: human decisions and explanations, separate from original outputs.
- `exports/`: candidate JSON/CSV, episode coverage JSON/CSV, and a Markdown report.

The complete run also exports `global_ranking.csv` (all qualifying candidates in posting-priority order), `episode_posting_order.csv` (one best qualifying cut per episode), and `episode_recommendations.csv` (a result for every episode, including weak or uncertain options). Score ties remain ties; suggested queue order breaks ties by cliffhanger, newcomer clarity, opening impact, then stable ID. Episode number earns no preference. Human-rejected candidates are excluded from posting queues.

The linked `exports/` folder contains the saved selection results. Original Kuku inputs and full `runs/` artifacts remain local and ignored by Git. Share real-input raw outputs only through the assignment's intended submission channel. The synthetic fixture and its cached real model run can be shared with the runnable code. The source archive includes that synthetic demo; the separate confidential raw-output archive can be extracted into the project to populate `runs/full` for API-free review.

The coverage export includes every parsed episode, even when not processed, no candidate is returned, every selection fails, or an API call fails. A best available candidate can be reported as rejected or needing review; it is not promoted to a qualifying selection. Global ranking compares episode-only promos and does not assemble a series promo. Equal global scores share rank. Human approval/rejection never silently rewrites model scores.

## Where the logic can fail

1. **Script versus footage:** Missing or inaccurate timestamps, broad camera descriptions and line-level dialogue timing can misrepresent the actual opening. Episode 45's initial marriage declaration arrived at 3.60 seconds. Boundary checks help, but an editor must verify footage and audible words. Camera, action, sound and dialogue tracks overlap, so their lengths must not be added to estimate duration. Source times use integer centiseconds; boundaries must exist in the script and cutting through a dialogue event fails validation. The first-three-second preview withholds partially included dialogue and flags partial visual descriptions.
2. **Story interpretation:** Models can infer missing context, confuse intensity with emotional stakes or misread a resolved scene as a cliffhanger. Independent judging and citation checks reduce errors, but shared biases remain. Additional full-source fidelity checking currently covers joins only; continuous excerpts can also omit essential context.
3. **Search and ranking:** Limited proposals and conservative cut rules can miss stronger edits. The qualified Episode 45 join required a focused supplemental search. Subjective scores do not optimize campaign variety, spoilers or release timing. Audience testing is needed to establish actual performance.
4. **Review and deployment:** Notes do not regenerate candidates or update scores. Human rejection excludes a cut from posting queues; human needs-review does not currently block a model-qualified cut. Shared server storage lacks user separation and durable history. A fuller product needs a revision workflow, publication controls and persistent storage.

## Verification

The recorded verification run passed **18 automated tests** covering timing, episode isolation, evidence, eligibility, ranking, saved reviews and resumability. Tests also exercise dialogue boundaries, missing event handling, first-three-second reconstruction, blinded evaluation, resume fingerprints and raw refusal retention. A deterministic test double verifies the workflow; its output is never presented as actual Luna/Sol results.

Human feedback covered two pilot cases, not a representative audience study. The remaining editorial step is footage review; retention, show starts and continued viewing require distribution tests.

Official references: [Luna](https://developers.openai.com/api/docs/models/gpt-6-luna), [Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol), [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).

## Setup

### Install and configure

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

### Launch the review app

```bash
python -m streamlit run app.py
```

If a running development server reports a stale import after source changes, restart it with the same command. The project enables polling to reload source modules; saved runs remain on disk. The complete verified 50-episode result set is `runs/full`; the earlier pilot is retained in `runs/pilot-v2`.

### Run the pipeline

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

Rebuild exports from saved results without making API calls:

```bash
python -m promo_finder report runs/pilot-v2
```

### Run tests

```bash
python -m unittest discover -s tests -v
```

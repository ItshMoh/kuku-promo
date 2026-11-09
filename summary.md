# Kuku Promo Studio: solution summary

Kuku Promo Studio finds 20–60-second promos from timestamped episode scripts. It gives editors source cut lists, hooks, cliffhangers, explanations and a suggested posting order. The objective is **show continuation**: help a new viewer understand the situation, care about the outcome and want to keep watching.

## Application and results

[Live Streamlit app](https://kuku-promo-z8wqktysaxybc5dxxlmwed.streamlit.app/) · [GitHub repository](https://github.com/ItshMoh/kuku-promo)

- **All 50 selected promo scores and reasons:** [CSV](https://github.com/ItshMoh/kuku-promo/blob/master/exports/episode_recommendations.csv) · [JSON](https://github.com/ItshMoh/kuku-promo/blob/master/exports/episode_recommendations.json).
- **Qualified posting queue, one promo per episode:** [episode_posting_order.csv](https://github.com/ItshMoh/kuku-promo/blob/master/exports/episode_posting_order.csv).
- **All 95 alternatives and criterion scores:** [candidates.csv](https://github.com/ItshMoh/kuku-promo/blob/master/exports/candidates.csv).
- **Detailed episode explanations and file guide:** [report.md](https://github.com/ItshMoh/kuku-promo/blob/master/exports/report.md).

## Scope

Each candidate uses one episode: either one continuous interval or two to three chronological, non-overlapping intervals. Cross-episode promos are deferred. Selection uses existing dialogue, visuals and sound; no invented narration, overlays or added music. The app provides text previews and editing instructions, not rendered videos. The target is an unfamiliar English-speaking US viewer.

## Approach: five phases

1. **Parse:** Extract timestamped scenes, camera directions, action, dialogue and sound with traceable event IDs. Preserve simultaneous tracks and source cut boundaries.

2. **Select:** Luna proposes alternative cuts from one complete episode, explaining the opening hook, emotional stakes, unresolved ending and main weakness. The candidate limit is a maximum, not a required count.

3. **Validate:** Code checks duration, same-episode boundaries, chronology, overlap and whole dialogue lines. Reconstruct the promo and its first three seconds, withholding words whose exact timing is unknown.

4. **Judge:** Sol independently evaluates the assembled cut without Luna's rationale or prior-episode context. It scores evidence against the rubric; a separate full-source check tests whether joined clips preserve meaning.

5. **Review and rank:** Calibrate on a six-episode pilot, process the full pack and retain failures. Editors compare alternatives and record decisions. Save outputs for reuse, then rank qualified cuts across episodes.

## Judging criteria

**Eligibility first:** a candidate must last 20–60 seconds, hook within three seconds, make sense to a newcomer, leave a consequential outcome unresolved and preserve source meaning using existing material. Checks return pass, fail or needs review. A high score cannot compensate for a failed requirement.

| Criterion | Weight | Main question |
| --- | ---: | --- |
| Opening impact | 20% | Is there an immediately understandable reason to stop? |
| Emotional investment | 20% | Who matters, and what could they lose? |
| Opening curiosity | 10% | What specific question encourages continued attention? |
| Newcomer clarity | 15% | Are the conflict, relationships and stakes understandable? |
| Momentum | 10% | Does the situation develop or escalate? |
| Ending cliffhanger | 25% | What consequential outcome makes us want the next scene? |

Rate each criterion **0–5**; calculate `sum(weight × rating / 5)` for a total out of 100. The ending has the largest weight because the objective is continuation. Romance, revenge, betrayal, status reversal and rescue are appeal labels, not automatic bonus points. These are proposed editorial weights, not validated predictions of views or conversion. [Full rubric](https://github.com/ItshMoh/kuku-promo/blob/master/criteria.md).

## Results and posting order

The saved run covers **50 episodes and 95 candidates**: 86 continuous and 9 joined. Of these, **26 qualify, 37 need review and 32 are rejected**. The qualified episode posting queue contains **23 episodes**. Every episode retains a best available cut, with its status visible; not every cut is recommended for posting.

**First recommendation: Episode 23**, `01:19.00–02:11.50`, **52.5 seconds, 74/100**. “Someone is poisoning her” supplies an immediate hook; unfinished treatment and an opening door leave the rescue unresolved. The visitor is not established as the poisoner.

Rank exact promo cuts, not entire episodes. Qualified cuts are ordered by score; ties retain equal rank. Posting priority breaks ties by cliffhanger, newcomer clarity, opening impact and finally a stable ID. Episode number earns no preference. Episode 12 also scores 74, but Episode 23 leads through the tie-break.

## Where the logic can fail

1. **Script versus footage:** Missing or inaccurate timestamps, broad camera descriptions and line-level dialogue timing can misrepresent the actual opening. Episode 45's initial marriage declaration arrived at 3.60 seconds. Boundary checks help, but an editor must verify footage and audible words.

2. **Story interpretation:** Models can infer missing context, confuse intensity with emotional stakes or misread a resolved scene as a cliffhanger. Independent judging and citation checks reduce errors, but shared biases remain. Additional full-source fidelity checking currently covers joins only; continuous excerpts can also omit essential context.

3. **Search and ranking:** Limited proposals and conservative cut rules can miss stronger edits. The qualified Episode 45 join required a focused supplemental search. Subjective scores do not optimize campaign variety, spoilers or release timing. Audience testing is needed to establish actual performance.

4. **Review and deployment:** Notes do not regenerate candidates or update scores. Human rejection excludes a cut from posting queues; human needs-review does not currently block a model-qualified cut. Shared server storage lacks user separation and durable history. A fuller product needs a revision workflow, publication controls and persistent storage.

## Validation

The recorded verification run passed **18 automated tests** covering timing, episode isolation, evidence, eligibility, ranking, saved reviews and resumability. Human feedback covered two pilot cases, not a representative audience study. The remaining editorial step is footage review; retention, show starts and continued viewing require distribution tests.

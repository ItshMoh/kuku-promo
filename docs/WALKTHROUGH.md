# Three-minute walkthrough outline

Record in your own voice. This file is an outline, not a fabricated recording.

## 0:00-0:25 - Problem and scope

Explain that an editor needs promising, precisely traceable promos across a show. The chosen objective is show continuation for a newcomer. Each candidate uses one episode; a later episode can provide the first promo to post.

## 0:25-0:55 - Run on a new input

Show the synthetic screenplay in `examples/episode-001.txt`. In Prepare & run, demonstrate folder/upload/paste input and the parsed episode count. Show that selector and judge model names are configurable. If recording a cached demonstration, say explicitly that it is a saved real run, rather than pretending an API request is happening live.

## 0:55-1:40 - Inspect one real selection

Open the completed full-pack run. Choose a recommended candidate. Show its ordered source timestamps and duration, the first three seconds, and the full text sequence. Explain the hook, what the character could lose, and the ending's specific unanswered question. Show a joined example if useful, emphasizing that both cuts belong to the same episode.

## 1:40-2:15 - Compare and rank

Show the six criterion scores with source evidence, then the global posting order and episode-level comparison. Explain that earlier episode numbers earn no priority. Show the export files and coverage for all 50 episodes.

## 2:15-2:45 - Honest failure

Use the quality report's documented Episode 45 timing error or Episode 6's weak domestic selections. Show why the first-three-second or cliffhanger check prevented an overconfident recommendation. Note that scripts cannot establish exact word timing or footage performance.

## 2:45-3:00 - What AI and code do

Luna selects; Sol evaluates in fresh requests; code checks timestamps, references, source isolation and arithmetic; an editor makes the publication decision. Mention measured run cost, saved raw outputs and the README's rerun command. Do not claim audience-performance validation.

# Episode-only promo report

## Export file guide

This folder contains the promo-selection outputs for all 50 episodes: 95 proposed candidates, including 26 qualified candidates. The files contain source cut timestamps and editorial explanations, not rendered promo videos. Every promo uses content from one episode only.

Start with [episode_recommendations.csv](episode_recommendations.csv) for one best available cut per episode, then [episode_posting_order.csv](episode_posting_order.csv) for the suggested posting queue. Use [candidates.csv](candidates.csv) to inspect all alternatives. CSV files are convenient for reading in a spreadsheet; the matching JSON files contain the same core rows for use in an app, sometimes with extra metadata.

| File | Rows | What it represents |
| --- | ---: | --- |
| [episode_recommendations.csv](episode_recommendations.csv) | 50 | One best available promo per episode, in episode order. Includes episode number, candidate ID, source segments, duration, hook explanation, cliffhanger explanation, why it works, weakness, score, selection status and human-review decision. If an episode has no qualified option, its best available cut is still included with its rejected or needs-review status. |
| [episode_recommendations.json](episode_recommendations.json) | 50 | The same episode recommendations as structured JSON under `rows`, suitable for loading into an app or another program. Includes the reasons and limitations for each selected cut. |
| [all_episode_best.csv](all_episode_best.csv) | 50 | The same set of best available episode cuts, ordered by editorial score across episodes. Adds display order, tied score rank and `qualified_for_posting`. This is a comparison of all 50 episodes, including weak or uncertain cuts; it is not the qualified posting queue. |
| [candidates.csv](candidates.csv) | 95 | Every proposed promo, including multiple alternatives within an episode and qualified, needs-review and rejected candidates. Includes cut timestamps, type, duration, appeal, opening and ending questions, rationale, hook and cliffhanger explanations, weaknesses, errors, total score and all six criterion ratings. |
| [candidates.json](candidates.json) | 95 | The complete candidate comparison data as JSON under `rows`, plus the `episode_only` scope. Use this when an app needs all alternatives and their reasons rather than only the selected cut for each episode. |
| [global_ranking.csv](global_ranking.csv) | 26 | All qualified candidates in suggested posting order across episodes, excluding human-rejected cuts. Can contain more than one candidate from the same episode. Includes the candidate explanations, scores, ranks, posting priority and posting reason. |
| [global_ranking.json](global_ranking.json) | 26 | The same global candidate ranking as JSON under `rows`, with the episode-only scope and an explicit description of the ranking tie-break rule. |
| [episode_posting_order.csv](episode_posting_order.csv) | 23 | A posting queue containing one selected qualified promo per episode. Only 23 episodes have a qualified option in this run. Includes source cuts, editorial explanations and posting reasons; use `episode_posting_priority` for the consecutive order within this queue. |
| [episode_posting_order.json](episode_posting_order.json) | 23 | The same one-per-episode posting queue as structured JSON under `rows`, suitable for displaying the recommended release order in an app. |
| [coverage.csv](coverage.csv) | 50 | Processing coverage for every episode: status, number of candidates, number of qualified candidates, best available candidate ID and status, and source timing warnings. Use it to check completeness and identify episodes that need more work; it does not contain the full promo explanations. |
| [coverage.json](coverage.json) | 50 | The same episode coverage rows as JSON, with a separate `parse_errors` list for input files that could not be parsed. This run has no parse errors. |

Read `selection_status` or `status` alongside the score: `qualified` means the candidate passed the model's eligibility checks, `needs_review` means an unresolved issue remains, and `rejected` means it failed a requirement. A best available cut is not automatically a posting recommendation. Human decisions are recorded separately; a human rejection excludes a cut from posting queues, while human approval does not automatically clear a model eligibility issue.

Scores are editorial assessments out of 100, not predictions of views or conversions. Equal total scores share a rank. Posting priority breaks ties by cliffhanger strength, newcomer clarity, opening impact and finally a stable candidate ID; episode number earns no preference. The six individual criterion ratings in the candidate and ranking files are out of 5.

The detailed episode report below retains all candidates and their original selection explanations. A positive selector rationale can appear beside a rejected result: read the final status and judged weakness before deciding whether a cut is suitable.

---

Editorial scores; no footage or audience-performance validation.
Human decisions are recorded separately and do not rewrite model scores.

## Episode 1 — no_qualifying_candidate

This episode offers two usable continuous selections from one extended cathedral confrontation: the public altar betrayal and the family's subsequent rejection. Both open with immediate, understandable stakes and end before Juliana's response is resolved; the second is more dependent on the viewer inferring context from the wedding setting.


### At the altar, he chooses her sister
- ID: ep-001-ec0f2cacc8; continuous; rejected; score: 45.0
- Segments: ep-001 00:32.80–01:19.00 (46.20s)
- Opening question: Why is the groom holding another woman's hand at the altar, and what does that mean for the bride?
- Ending question: After learning her sister knew Gerald would never marry her, what will Juliana do?
- Why: The altar reveal is visible at the opening, and Juliana's question about Gerald holding the woman's hand quickly makes the betrayal legible. The sequence develops from shock, to the sister's claim, to Juliana's accusation and the sister's admission of prior knowledge. It ends on that specific betrayal without resolving Juliana's response. The continuous cut runs 46.2 seconds.
- Weakness: The ending confirms the humiliation without opening a concrete next outcome, while the recognizable betrayal arrives after the three-second window. Weighted editorial score: 45/100; this cut does not meet all qualifying requirements.
- Human review: unreviewed
- Validation issues: None

### Her family chooses her sister
- ID: ep-001-a000bf5277; continuous; rejected; score: 36.0
- Segments: ep-001 01:19.00–01:53.00 (34.00s)
- Opening question: Will Juliana's father help her stop this rejection, or is she facing it alone?
- Ending question: Now that her sister has openly claimed the family's favor, will Juliana accept being cast aside or challenge them?
- Why: The opening quickly establishes Juliana's appeal for help; her father's silence and the Matriarch's rebuke escalate the rejection. The sister's final declaration provides a clear, consequential ending point. The continuous cut runs 34 seconds.
- Weakness: The scene delivers humiliation without a concrete pending outcome: the final insult reinforces the existing conflict rather than opening a consequential next step. Weighted editorial score: 36/100; the unresolved-ending requirement fails.
- Human review: unreviewed
- Validation issues: None

## Episode 2 — has_qualified

The episode provides a clear self-contained altar betrayal and a satisfying dignity reversal, but its final speech largely resolves Juliana's immediate public-shame conflict. The strongest unresolved cuts occur before the father's answer or Gerald's response; neither establishes what happens to Juliana afterward.


### Jilted at the altar, will her father stand by her?
- ID: ep-002-3ae595ac64; continuous; qualified; score: 71.0
- Segments: ep-002 00:00.00–00:37.10 (37.10s)
- Opening question: After Gerald refuses to marry her in front of the congregation, will anyone in her family defend her?
- Ending question: Will her father intervene after she asks him not to let Gerald humiliate her?
- Why: A 37.1-second continuous passage opens on Gerald's blunt refusal, establishes that Juliana's promised groom has chosen another woman, and escalates from her appeal to him to her plea to her father. It ends on her complete question to her father, before he answers, leaving a specific family decision unresolved.
- Weakness: Repeated insults occupy much of the clip before the appeal to her father creates a new development. That appeal supplies a viable ending, but the father’s authority and possible response are not established. Weighted editorial score: 71/100.
- Human review: unreviewed
- Validation issues: None

### Ordered out of the chapel, Juliana refuses to be shamed
- ID: ep-002-6abd70c812; continuous; rejected; score: 43.0
- Segments: ep-002 01:06.00–01:26.50 (20.50s)
- Opening question: Why is Juliana being told she should be grateful just to attend this wedding?
- Ending question: Will Gerald answer Juliana's challenge, or can she keep control of the public confrontation?
- Why: This 20.5-second continuous cut moves from the matriarch's wedding-related scolding to Gerald ordering Juliana out, then gives her a defiant change in posture and a direct rebuke. It ends on her complete challenge, before Gerald's response.
- Weakness: The ending promises resistance without establishing what Juliana might do or what Gerald could lose. The weighted editorial score is 44/100, and the unresolved-ending requirement is not met strongly enough to qualify.
- Human review: unreviewed
- Validation issues: None

## Episode 3 — has_qualified

The episode offers two distinct promo shapes: a rescue that culminates in an unanswered proposal, and a shorter rescue standoff. Both have identifiable hooks and consequential unresolved outcomes. The proposal cut has stronger romantic continuation stakes, though its action-first opening omits the setup; the standoff cut is easier to follow immediately but leaves more background unexplained.


### The stranger’s proposal
- ID: ep-003-b5abe64e2a; continuous; qualified; score: 72.0
- Segments: ep-003 01:24.00–02:20.50 (56.50s)
- Opening question: Why is this guard attacking the stranger—and will he protect Juliana?
- Ending question: Will Juliana accept the stranger’s offer of his hand?
- Why: A continuous 56.5-second cut opens on a guard charging and being felled, then develops into the stranger checking on Juliana, offering her a ring, and making his proposal. It ends after the offer but before her response, leaving a specific romantic decision unresolved.
- Weakness: The opening supplies a fight before supplying a personal reason to care, so its initial curiosity is weaker than the eventual proposal cliffhanger. The middle also spends time reinforcing reassurance before the ring changes the situation. Weighted editorial score: 72/100.
- Human review: unreviewed
- Validation issues: None

### Guards seize Juliana; a stranger intervenes
- ID: ep-003-036d0e2c10; continuous; qualified; score: 58.0
- Segments: ep-003 00:58.30–01:24.00 (25.70s)
- Opening question: Will anyone stop the guards from dragging Juliana out of the church?
- Ending question: Will the stranger make the guard release Juliana, or will the guard attack him?
- Why: This continuous 25.7-second cut starts with the matriarch ordering Juliana removed, shows the guards taking hold of her and her plea for help, then introduces the stranger’s challenge. It ends on his complete demand—“...let her go.”—before the guard charges, leaving the rescue unresolved.
- Weakness: The immediate danger is clear, but neither the reason for the expulsion nor the intervening man's connection to the woman is supplied. This limits investment in this particular story beyond the rescue situation. Weighted editorial score: 58/100. Main appeal: danger and rescue.
- Human review: unreviewed
- Validation issues: None

## Episode 4 — has_qualified

This episode offers several usable continuous cuts from a single chapel confrontation. The strongest unresolved choices are Juliana’s response to the proposal and her response to family rejection; the episode’s final departure resolves the latter, so the proposed cuts end before that outcome.


### What does he see in her?
- ID: ep-004-f5a9abec2e; continuous; qualified; score: 61.0
- Segments: ep-004 00:25.90–01:12.00 (46.10s)
- Opening question: Why would a kneeling stranger offer Juliana his name when he barely knows her?
- Ending question: Will Juliana accept his offer and leave the familiar world behind?
- Why: This continuous 46.1-second cut opens on Juliana asking why he offers her his name. His answers address her fear of pity, while her final thought—that he looked at her when everyone else turned away—sets up the choice without revealing her acceptance.
- Weakness: The opening withholds the offer's practical meaning, while the middle spends several beats reaffirming her isolation. The strongest dignity conflict arrives much later. Weighted editorial score: 61/100.
- Human review: unreviewed
- Validation issues: None

### A vow against the family’s contempt
- ID: ep-004-a834976db9; continuous; rejected; score: 60.0
- Segments: ep-004 00:07.50–01:05.50 (58.00s)
- Opening question: Will Juliana accept the proposal of a stranger her family is mocking?
- Ending question: Will Juliana trust his vow enough to accept his proposal?
- Why: A continuous 58-second cut opens on Clarissa’s cruel laughter, quickly makes the insult explicit, then follows Juliana’s doubts and the stranger’s answer through his declaration, “It is a vow.” The hook and stakes are understandable without prior context, and the choice remains open at the end.
- Weakness: The opening withholds the meaningful conflict until after the three-second boundary. The later dignity-versus-pity choice creates investment, but cannot rescue the opening requirement. Weighted editorial score: 60/100.
- Human review: unreviewed
- Validation issues: None

### The wedding ends in disownment
- ID: ep-004-7a41b1cf6b; continuous; needs_review; score: 46.0
- Segments: ep-004 01:40.20–02:14.50 (34.30s)
- Opening question: What will this marriage cost Juliana when her family sees her choose this man?
- Ending question: Now that her mother has disowned her, will Juliana leave with her new husband?
- Why: The continuous 34.3-second cut opens on the ring being placed, establishes the marriage through the priest’s pronouncement, then turns sharply to Gerald’s and Lady Ashcroft’s opposition. It ends on a specific, consequential family rejection before Juliana responds.
- Weakness: The opening shows routine wedding action rather than the conflict that makes this particular marriage interesting. Weighted editorial score: 44/100; opening eligibility remains unconfirmed.
- Human review: unreviewed
- Validation issues: None

## Episode 5 — needs_review

Two distinct, continuous cuts meet the requested duration and offer different entry points: family disownment and the threatened keepsake, followed by the ledger’s destruction and the husband’s defense. Both have an understandable opening hook and leave a consequential conflict unresolved.


### Disowned at the church
- ID: ep-005-1939504cea; continuous; needs_review; score: 47.0
- Segments: ep-005 00:04.20–00:49.00 (44.80s)
- Opening question: Will Juliana’s father really cast her off for marrying, and what is her stepmother claiming from her?
- Ending question: Will Juliana be able to keep the ledger her stepmother says belongs to the family?
- Why: The cut opens on Lord Ashcroft addressing Juliana, then delivers his rejection within the first three seconds. Her reply establishes the marriage conflict; his loss of inheritance and her stepmother’s claim on the ledger escalate the stakes. It ends on a specific dispute before Juliana responds.
- Weakness: The strongest stakes arrive after the three-second window, while the ending shifts to an object whose importance is unexplained. Weighted editorial score: 47/100; eligibility remains unconfirmed.
- Human review: unreviewed
- Validation issues: None

### Her mother’s ledger—and a warning
- ID: ep-005-d4a812b28a; continuous; rejected; score: None
- Segments: ep-005 00:49.00–01:41.50 (52.50s)
- Opening question: Will Juliana’s family take the only keepsake she has left of her mother?
- Ending question: Will Juliana’s husband act on his warning when Gerald continues to humiliate them?
- Why: The opening immediately states what the ledger means to Juliana, then shows it being taken and thrown away. Her husband’s retrieval and reassurance offer a meaningful turn, before Gerald’s insult and the husband’s cold warning set up an unresolved confrontation.
- Weakness: The warning is strong, but the clip ends before any response or action, so the exact consequence for Gerald remains uncertain.
- Human review: unreviewed
- Validation issues: cliffhanger_event_ids cites events outside the selected clip

## Episode 6 — no_qualifying_candidate

The episode offers clear emotional stakes and a warm progression from hardship toward tentative comfort, but few strong unresolved outcomes. The two candidates use distinct moments: Juliana’s first reaction to the cottage, and her attempt to make it a home.


### Making a home from what remains
- ID: ep-006-7353879491; continuous; rejected; score: 31.0
- Segments: ep-006 01:04.10–01:33.80 (29.70s)
- Opening question: Can Juliana make this poor cottage feel like a home after losing the life she knew?
- Ending question: Will Juliana feel that what her husband can offer is enough for tonight?
- Why: Juliana’s declaration that this is their home gives the opening a clear purpose. Her grief deepens the stakes, and his practical help changes the moment from solitary coping to tentative partnership. The cut ends after his modest admission, before her response.
- Weakness: This functions as a gentle, largely resolved bonding scene rather than a continuation-driven promo. It lacks both a three-second hook and a meaningful cliffhanger. Weighted editorial score: 31/100; the failed qualifying checks prevent recommendation as supplied.
- Human review: unreviewed
- Validation issues: None

### A bride arrives at a leaking cottage
- ID: ep-006-7554ccb329; continuous; rejected; score: 26.0
- Segments: ep-006 00:33.70–01:04.10 (30.40s)
- Opening question: What kind of home has Juliana entered, and how will she respond to what her husband can offer?
- Ending question: If Juliana is disappointed, what has she lost—and what does she need from this marriage?
- Why: The door opening into a bare room and the leaking roof establish the immediate situation visually. The husband’s apology and admission make the material stakes clear, while Juliana’s quiet response, “I am. But not because of you,” leaves her disappointment’s source open.
- Weakness: The selection offers a gentle acceptance exchange rather than an immediate hook or a consequential cliffhanger. Weighted editorial score: 26/100; it does not meet the qualifying requirements.
- Human review: unreviewed
- Validation issues: None

## Episode 7 — needs_review

One promising continuous candidate: Juliana's defense of her dignity builds into Gerald's threat and the husband's arrival, with the confrontation still unresolved at the cut.


### A threat at the cottage gate
- ID: ep-007-def5467542; continuous; needs_review; score: 60.0
- Segments: ep-007 00:22.00–01:15.50 (53.50s)
- Opening question: Why have these well-dressed visitors come to mock Juliana, and will she stand up to them?
- Ending question: Now that Juliana's husband is approaching, will Gerald carry out his threat—or will the husband stop him?
- Why: The clip opens on the direct insult, then establishes the conflict through Juliana's defiant replies and Gerald's grievance that she chose another man. His threat and question about her husband lead into the husband's ominous approach, ending before their confrontation. The continuous 53.5-second cut preserves the causal sequence and leaves a specific, consequential outcome unresolved.
- Weakness: The opening withholds the clear conflict until after three seconds, and repeated insults delay the consequential threat. Weighted editorial score: 60/100; the opening-hook qualification remains under review despite the stronger ending.
- Human review: unreviewed
- Validation issues: None

## Episode 8 — no_qualifying_candidate

The episode is a quiet bonding scene with no strong opening hook or consequential unresolved ending in the available material. This cut has clear, gentle chemistry, but its promo value is limited.


### “Not Yet”: The Beard Bargain
- ID: ep-008-a27a1dd4c1; continuous; rejected; score: 32.0
- Segments: ep-008 00:24.30–00:51.30 (27.00s)
- Opening question: Will Alexander let Juliana change his rugged appearance, or does he want to keep it as it is?
- Ending question: Will Juliana ever trim his beard—and will Alexander let her?
- Why: A continuous 27-second cut. Juliana notices Alexander's hair and beard, offers to trim them, and he catches her wrist and says, “Not yet.” He explains that he prefers to let them grow; their teasing continues until he answers her promise to trim his beard someday with “We'll see.” The exchange is understandable without prior-episode context and ends on a specific, though low-stakes, unresolved possibility.
- Weakness: The scene offers gentle romantic playfulness rather than a continuation-driving conflict. It lacks both a three-second hook and a meaningful unresolved outcome. Weighted editorial score: 32/100.
- Human review: unreviewed
- Validation issues: None

## Episode 9 — no_qualifying_candidate

Two distinct, standalone promo options are supported: a rescue that turns into a warning about gossip, and a rumor that triggers a nobleman's alarm. The rescue option benefits from its joined structure but skips the treatment itself; the rumor option is clearer as a compact mystery, though its personal stakes are less established.


### The Scar Behind the Rumor
- ID: ep-009-5528ed2575; continuous; rejected; score: 32.0
- Segments: ep-009 01:28.00–01:55.50 (27.50s)
- Opening question: What rumor is serious enough to disturb the lord?
- Ending question: Who is the scarred veteran, and what will the shaken nobleman do about the rumor?
- Why: The report of a rumor is immediately understandable as news, then becomes specific: resemblance to a dead Duke and a matching scar. The nobleman's abrupt demand for the man's location, followed by his shaken reaction alone, leaves both the veteran's identity and the nobleman's response unresolved.
- Weakness: The clip withholds the rumor's substance beyond the opening window and never establishes the consequences of its being true. It offers a legible mystery, but little reason to care about its answer. Weighted editorial score: 32/100.
- Human review: unreviewed
- Validation issues: None

### A Cure—and a Dangerous Rumor
- ID: ep-009-1422ca0e32; joined; rejected; score: None
- Segments: ep-009 00:02.80–00:40.00 → ep-009 00:58.80–01:21.60 (60.00s)
- Opening question: Who is pounding at the door, and can Juliana help the sick child the mother is carrying?
- Ending question: What danger will the village gossip bring to Juliana and Alexander?
- Why: The pounding and Alexander's protective response open on an immediate disruption. The mother's plea establishes clear stakes, and Juliana's remedy preparations lead into the mother's report that the fever is breaking. The final warning shifts the outcome from rescue to the unresolved risk of being talked about.
- Weakness: The joined cut skips the actual treatment and the mother's departure, so the passage from preparation to recovery is abrupt. The warning suggests danger but does not explain its exact form.
- Human review: unreviewed
- Validation issues: Segment 1 boundaries must match source event or scene timestamps | Segment 1 cuts dialogue event ep-009-b0031

## Episode 10 — has_qualified

Two continuous selections offer different entry points into this episode: immediate danger and care, or developing romantic tension. Both meet the requested duration and leave a specific outcome open; neither requires prior-episode knowledge to follow its basic situation.


### The wounded stranger refuses to admit how badly he is hurt
- ID: ep-010-200beae62a; continuous; qualified; score: 67.0
- Segments: ep-010 00:02.10–00:33.20 (31.10s)
- Opening question: Alexander arrives bleeding, but is his injury really just a scratch—and will he let Juliana see it?
- Ending question: What will Juliana find when Alexander finally lets her see beneath his clothes?
- Why: The door crashes open at the start, revealing a bloodied Alexander. Juliana challenges his claim that the wound is minor, orders him to sit, and presses him to undress for an examination. The cut at 33.20 seconds holds on her guarded anticipation, just before the reveal. Continuous 31.1-second selection with a clear immediate problem and an unresolved medical concern.
- Weakness: The strong injured arrival develops mainly into repeated resistance to care. The ending delays examination without introducing a sharper complication or deeper personal stakes. Weighted editorial score: 67/100.
- Human review: unreviewed
- Validation issues: None

### A wound-care moment turns into a confession
- ID: ep-010-e88856d0b1; continuous; rejected; score: 32.0
- Segments: ep-010 01:00.00–01:34.00 (34.00s)
- Opening question: Why is Alexander watching Juliana so intently while she treats his wound?
- Ending question: After Alexander tells her that her touch is the only medicine that eases his pain, will Juliana return his feelings?
- Why: The opening gaze prompts Juliana to ask why he looks at her that way. His answer deepens the intimacy; they draw closer, and he takes her hands before making a direct emotional confession. The clip ends on Juliana's captivated reaction without a verbal answer. Continuous 34-second selection with a distinct romantic hook and unresolved response.
- Weakness: The scene delivers a tender romantic development rather than a compelling reason to continue: the opening is only a gaze, and the ending supplies apparent mutual attraction without a consequential unresolved outcome. Weighted editorial score: 33/100.
- Human review: unreviewed
- Validation issues: None

## Episode 11 — has_qualified

This episode offers two distinct continuous promo angles: the initial accusation and impending search, and the later apparent discovery of the stolen watch. Both have immediate conflict and consequential unresolved outcomes; the second has a stronger reveal but leaves the frame-up unproven within the clip.


### The accusation and the search
- ID: ep-011-373804d767; continuous; qualified; score: 65.0
- Segments: ep-011 00:16.80–00:53.60 (36.80s)
- Opening question: Did Alexander steal Gerald’s watch, or is Gerald using the accusation to punish him and Juliana?
- Ending question: What will the constable find when he searches the cottage—and what will that mean for Alexander?
- Why: The opening names the alleged crime immediately. Juliana’s defense, Gerald’s taunt, the constable’s demand to search, and Alexander’s unexpected permission build a clear progression to the unanswered search. The single continuous segment lasts 36.8 seconds.
- Weakness: The ending offers a solid but conventional search-result question; no concrete evidence yet makes either possible outcome especially surprising. Weighted editorial score: 65/100.
- Human review: unreviewed
- Validation issues: None

### The watch in the coat
- ID: ep-011-8b9d85022b; continuous; rejected; score: None
- Segments: ep-011 01:07.40–01:52.75 (45.35s)
- Opening question: Is Gerald right that Alexander is a thief—or has someone planted the watch to destroy him?
- Ending question: Will Alexander be treated as a thief, and will Juliana believe the watch was planted?
- Why: Gerald’s accusation hooks immediately, then Juliana directly alleges he fabricated it. The constable finds a gold watch in Alexander’s coat, Gerald celebrates, and the shot holds on the evidence without resolving what happens to Alexander or the marriage. The continuous segment lasts 45.35 seconds.
- Weakness: The discovery visually supports Gerald’s accusation before the clip can establish that Juliana’s frame-up claim is true, which may temporarily leave a newcomer unsure whom to believe.
- Human review: unreviewed
- Validation issues: Segment 1 cuts dialogue event ep-011-b0059

## Episode 12 — has_qualified

The episode offers a clear escalation from an arrest over an alleged theft to Clarissa's coercive bargain and Juliana's decision to act. The strongest standalone selection is the later ultimatum: it communicates the physical danger and the husband's threatened execution within the clip. The earlier arrest sequence is a distinct, weaker option focused on the accusation.


### The price of saving her husband
- ID: ep-012-52f22135ea; continuous; qualified; score: 74.0
- Segments: ep-012 00:43.70–01:24.70 (41.00s)
- Opening question: Why does Clarissa want her sister to crawl, and what will she demand?
- Ending question: Will Juliana retrieve the ring in time to save her husband from the gallows?
- Why: The cruel demand lands in the opening seconds, then the clip explains the dangerous task and its consequence. Alexander's plea and Juliana's resolve deepen the emotional stakes; her final request for the garden's location commits her to act but leaves the outcome open. This is one continuous interval, so no transition is needed.
- Weakness: The concrete life-or-death stakes arrive only around halfway through the clip; before that, the ring-and-thorns explanation risks stretching the initial humiliation hook. Weighted editorial score: 74/100.
- Human review: unreviewed
- Validation issues: None

### The planted-watch accusation
- ID: ep-012-96a00c55b9; continuous; needs_review; score: 55.0
- Segments: ep-012 00:00.00–00:28.00 (28.00s)
- Opening question: Is Alexander guilty of theft, or was the watch planted to frame him?
- Ending question: Will the Constable believe Juliana's accusation before Alexander is arrested?
- Why: The opening arrest order establishes immediate danger. Juliana's defense, Gerald's appearance, and her direct accusation develop the dispute in a clear, chronological sequence. The selection ends after her charge that Gerald planted the watch, leaving the accusation and arrest unresolved. It is a single continuous interval.
- Weakness: The three-second hook is not securely established by the supplied timing. Beyond that, the confrontation offers a clear threat but ends on an accusation rather than new evidence or a decisive reversal. Weighted editorial score: 55/100.
- Human review: unreviewed
- Validation issues: None

## Episode 13 — needs_review

The episode offers a clear sacrifice-and-rescue ordeal, with a strong visual progression from entering the briars to finding the ring. The later passage better states the search's consequence for a newcomer, while the earlier passage gives more room to establish Juliana and Alexander's bond.


### She risks the thorns for him
- ID: ep-013-752f70c825; continuous; needs_review; score: 56.0
- Segments: ep-013 00:04.20–01:01.80 (57.60s)
- Opening question: Why is Juliana willing to risk the thorns despite Alexander's warning?
- Ending question: Will Juliana endure the briars and find a way to help Alexander before he faces the gallows?
- Why: 54.6 seconds. The warning arrives within the first two seconds, and the clip establishes a clear, self-sacrificing choice before escalating to her bleeding hands and the onlookers' taunts. Editorial rubric scores (opening, emotional pull, opening curiosity, clarity, momentum, ending): 4/5, 5/5, 4/5, 4/5, 4/5, 3/5; weighted total 79/100. The ending leaves her ordeal open, but does not yet explain what she is searching for.
- Weakness: The clip establishes why Juliana cares, but not what completing the ordeal requires or why it could save him. Its opening also depends on a relatively weak visual alarm cue unless the warning becomes intelligible within three seconds. Weighted editorial score: 57/100.
- Human review: unreviewed
- Validation issues: None

### Her bloody search may hold his freedom
- ID: ep-013-551f0c78fa; continuous; needs_review; score: 50.0
- Segments: ep-013 01:02.00–01:58.88 (56.88s)
- Opening question: Can Juliana find the thing that Gerald says may secure her husband's freedom?
- Ending question: Will the emerald ring in Juliana's bleeding fist actually secure Alexander's freedom?
- Why: 56.88 seconds. Gerald's taunt states the stakes immediately; the search then escalates through injuries, Alexander's distress, and Juliana's discovery of the ring. The final image holds on the ring rather than showing its consequence. Editorial rubric scores (opening, emotional pull, opening curiosity, clarity, momentum, ending): 4/5, 5/5, 4/5, 4/5, 5/5, 4/5; weighted total 86/100.
- Weakness: The three-second hook is not established by the supplied timing, and the ending foregrounds a completed search more strongly than the pending release. Weighted editorial score: 50/100; qualification remains under review.
- Human review: unreviewed
- Validation issues: None

## Episode 14 — no_qualifying_candidate

Two distinct selections offer different entry points: a rescue built around Juliana retrieving the ring, and a quieter aftermath that develops the couple's bond before ending on a threatening gesture. Both leave a meaningful consequence unresolved; the rescue version relies on a substantial chronological skip.


### The ring buys her husband's freedom
- ID: ep-014-19f3068f7c; joined; rejected; score: 49.0
- Segments: ep-014 00:00.00–00:32.50 → ep-014 01:16.00–01:27.63 (44.13s)
- Opening question: What did Juliana risk to retrieve the ring, and will it be enough to free her husband?
- Ending question: Who will Alexander confront, and what will he do to keep Juliana from being hurt again?
- Why: The ring in Juliana's torn, bloodied hand is an immediate visual hook; her demand to release her husband clarifies what is at stake, and the freed-husband beat pays off that immediate goal. The later vow and fist turn the rescue into an unresolved threat.
- Weakness: The strongest concrete outcome is resolved before the ending. The revenge gesture does not establish a substantial new cliffhanger, and the opening hook also requires timing review. Weighted editorial score: 49/100; not qualifying as submitted.
- Human review: unreviewed
- Validation issues: None

### A promise after the bandaging
- ID: ep-014-abce8366e4; continuous; rejected; score: 48.0
- Segments: ep-014 00:47.00–01:27.63 (40.63s)
- Opening question: How did Juliana come so close to losing her hands, and why does Alexander fear losing her?
- Ending question: Will Alexander act on his vow, and who might face the consequences?
- Why: The opening line immediately establishes the severity of Juliana's injury, while the exchange develops their attachment and his remorse. His protective vow, followed by the bloodied water and clenched fist, leaves a consequential next step unresolved.
- Weakness: The cut delivers emotional reassurance rather than a consequential cliffhanger. Suggested vengeance is too unspecific to strongly motivate continuation. Weighted editorial score: 48/100; the unresolved-ending requirement fails.
- Human review: unreviewed
- Validation issues: None

## Episode 15 — has_qualified

Two continuous selections meet the 20–60-second duration range and provide distinct angles on the same garden attack: sustained escalation toward an imminent blow, and a compressed danger-to-rescue confrontation. Both leave a consequential outcome open without requiring prior-episode knowledge.


### The garden under attack
- ID: ep-015-926022384a; continuous; qualified; score: 65.0
- Segments: ep-015 00:03.60–01:02.00 (58.40s)
- Opening question: Why are these men destroying the garden, and can Juliana stop them?
- Ending question: Will the thug bring his raised club down on the remaining herbs—and on Juliana, who is standing in his way?
- Why: The opening lands directly on a planter being smashed. The clip then makes the conflict legible through Juliana's protests, the thugs' contempt, her stand for her home, and their escalation to physical violence. It ends with the club raised and Juliana shouting to stop, before that immediate threat is resolved. Duration: 58.4 seconds.
- Weakness: The lengthy cycle of destruction, pleading, and mockery offers limited change before ending on another threatened act of destruction. The stakes are clear, but the continuation pull is stronger emotionally than narratively. Weighted editorial score: 65/100.
- Human review: unreviewed
- Validation issues: None

### A defender arrives
- ID: ep-015-0da5506303; continuous; qualified; score: 58.0
- Segments: ep-015 01:00.00–01:26.00 (26.00s)
- Opening question: Will anyone stop the thug from striking the remaining herbs while Juliana is right there?
- Ending question: Will Alexander fight the three thugs and protect Juliana?
- Why: The poised club supplies an immediate visual hook, followed by footsteps, Alexander charging in, and his taking a position between Juliana and the intruders. The thug's challenge and Juliana's anxious look leave the confrontation unresolved. Duration: 26 seconds.
- Weakness: The rescue stakes are understandable but thinly individualized: neither the herbs' importance nor the relationship behind Juliana's relief is established. Much of the runtime stages Alexander's arrival rather than adding complications. Weighted editorial score: 58/100.
- Human review: unreviewed
- Validation issues: None

## Episode 16 — has_qualified

The episode offers a clear rescue-to-betrayal progression. This continuous 55.2-second selection has an immediate confrontation, understandable danger, and a consequential reveal with an emotional reaction. Its main clarity limit is that Gerald’s significance to Juliana is not established within the clip.


### The attack on Juliana’s garden
- ID: ep-016-f828198782; continuous; qualified; score: 53.0
- Segments: ep-016 00:00.00–00:55.20 (55.20s)
- Opening question: Will Alexander protect the injured woman behind him from the three armed attackers?
- Ending question: Now that Juliana has heard Gerald Harrington was behind the attack, what will she do about the betrayal?
- Why: The confrontation is legible from the opening: armed men threaten a visibly injured woman, and Alexander stands between them. The clip escalates through his defense of her into an interrogation; a thug names the person who paid them, and Juliana’s shocked reaction leaves the personal consequence unresolved. The selected interval is 55.2 seconds.
- Weakness: The ending relies on an unexplained personal connection to Gerald after resolving the immediate rescue. It offers less continuation urgency than the opening danger promises. Weighted editorial score: 53/100.
- Human review: unreviewed
- Validation issues: None

## Episode 17 — no_qualifying_candidate

Two distinct, source-grounded options: one centers on a protective vow challenged by Juliana; the other ends on her fear of losing Alexander. Neither offers a major new external threat, so both rely on emotional continuation.


### A promise she says he can't make
- ID: ep-017-92fc6350e4; continuous; rejected; score: 42.0
- Segments: ep-017 00:00.00–00:34.50 (34.50s)
- Opening question: What happened to Juliana's ruined garden, and can she feel safe after the attack?
- Ending question: How will Alexander answer Juliana's challenge that he cannot promise to keep her safe?
- Why: The devastated garden and Juliana's bandages provide an immediate visual disruption. The scene then makes the danger legible through her thanks, builds into Alexander's vow, and ends on her direct challenge before his reply. The clip is understandable without prior-episode context and ends on a specific, unresolved exchange.
- Weakness: The ending expresses vulnerability rather than suspending a concrete consequential outcome. The scene builds sympathy, but supplies little specific reason to continue beyond its protective exchange. Weighted editorial score: 42/100.
- Human review: unreviewed
- Validation issues: None

### “Of losing you”
- ID: ep-017-633459eef9; continuous; rejected; score: 36.0
- Segments: ep-017 00:40.00–01:02.20 (22.20s)
- Opening question: Why is Juliana tending Alexander's wounds, and what are they to each other?
- Ending question: How will Alexander respond to Juliana admitting she was afraid of losing him?
- Why: The wound care gives the exchange a visual and relational starting point. Their mutual concern turns into Juliana's personal confession, and the cut leaves his response unseen. This is a compact, distinct romantic beat with a clear emotional question.
- Weakness: The strongest beat is an emotional answer rather than a consequential cliffhanger. The opening is also quiet and timing-dependent. Weighted editorial score: 37/100; the unresolved-ending requirement fails despite understandable emotional context.
- Human review: unreviewed
- Validation issues: None

## Episode 18 — has_qualified

The episode offers three distinct continuous cuts: an immediate escape-and-keepsake choice, the rescue from a collapsing room, and the aftermath that turns loss into a question about retaliation. The first two communicate danger clearly but begin before the characters’ situation is fully explained; the aftermath cut is easier to follow but its final question is about an unspecified plan.


### A Home Lost, a Vow Unanswered
- ID: ep-018-073dde50d6; continuous; qualified; score: 59.0
- Segments: ep-018 02:14.50–03:12.00 (57.50s)
- Opening question: Who destroyed their home, and what will Alexander do about it?
- Ending question: What is Alexander going to do, and how far will he go to protect them?
- Why: The opening shows the cottage consumed by flames, then Juliana names the loss. Alexander’s suspicion and vow turn grief into a new unresolved conflict; Juliana asks what he will do, and the episode ends on his unspeaking, resolute hold.
- Weakness: The ending promises a response without specifying an actionable choice or opponent, while prolonged reaction beats dilute momentum. The opening creates attention more effectively than story-specific curiosity. Weighted editorial score: 59/100.
- Human review: unreviewed
- Validation issues: None

### Fire at the Bedroom Door
- ID: ep-018-7e9100acae; continuous; needs_review; score: 54.0
- Segments: ep-018 00:06.00–01:02.50 (56.50s)
- Opening question: Can Juliana and Alexander get out of the burning cottage?
- Ending question: Will Juliana abandon the ledger and escape before the fire traps them?
- Why: The opening immediately shows Juliana seeing the glow beneath the door and calling for Alexander. The clip establishes the fire, their escape attempt, and the ledger's personal importance; it ends on her refusal, with their survival and the ledger's fate unresolved.
- Weakness: The final conflict depends on a ledger whose importance is never explained, so survival is more compelling than the specific reason Juliana resists rescue. Weighted editorial score: 54/100; qualification remains pending the opening-hook timing check.
- Human review: unreviewed
- Validation issues: None

### The Ledger in the Flames
- ID: ep-018-33b7471397; continuous; rejected; score: 53.0
- Segments: ep-018 00:52.50–01:38.50 (46.00s)
- Opening question: Will Juliana risk the fire to save the ledger?
- Ending question: Now that Alexander has shielded Juliana from the falling beam, can they both escape the burning cottage?
- Why: The burning ledger is an immediate, concrete hook. The conflict escalates from Alexander telling her to leave it, to Juliana retrieving it, to a beam falling and Alexander covering her. His reassurance does not settle whether either of them can get out.
- Weakness: The ending delivers the scene's rescue payoff instead of a strong continuation hook. Weighted editorial score: 54/100; the unresolved-ending requirement fails despite clear action and understandable stakes.
- Human review: unreviewed
- Validation issues: None

## Episode 19 — needs_review

The covert forest meeting is the clearest standalone promo: it quickly reveals a hidden status, an encroaching rival, and a family member in danger, then ends on Alexander's unresolved intention. The ruined-home scene has a legible emotional hook but a softer ending after the villagers offer assistance.


### A Home Reduced to Ashes
- ID: ep-019-a4d7a2946a; continuous; rejected; score: 51.0
- Segments: ep-019 00:00.00–00:41.50 (41.50s)
- Opening question: What will Juliana and Alexander do now that their home has burned?
- Ending question: With their home gone and only temporary shelter, how will they begin again?
- Why: The ruined cottage and Juliana's first line immediately establish a concrete loss. The villagers' offer gives the scene a human response, and the couple's departure leaves their future uncertain.
- Weakness: The scene delivers consolation and closure rather than a strong reason to enter the next scene. Weighted editorial score: 51/100; the unresolved-ending requirement fails despite understandable stakes and genuine emotional appeal.
- Human review: unreviewed
- Validation issues: None

### The Duke They Think Is Dead
- ID: ep-019-396fb90d36; continuous; needs_review; score: 48.0
- Segments: ep-019 00:41.50–01:29.50 (48.00s)
- Opening question: Why is this scarred stranger being addressed as “Your Grace,” and what has happened to his home and family?
- Ending question: Can Alexander obtain the proof he needs and reclaim Ashburg before his enemies make their hold permanent?
- Why: The informant's formal address lands within three seconds, then the report escalates from political takeover to the confinement of Alexander's mother. Alexander's vow to make Ashburg remember who it belongs to ends on a specific, consequential but unresolved aim.
- Weakness: The opening spends its crucial three seconds establishing a meeting rather than the personal threat or presumed-dead revelation. The weighted editorial score is 48/100; later story stakes do not resolve the opening qualification uncertainty.
- Human review: unreviewed
- Validation issues: None

## Episode 20 — needs_review

Two distinct continuous selections offer clear, self-contained stakes: a power grab at the manor and Juliana’s effort to help the sick villagers. The latter has a more direct personal vulnerability; the former makes the succession conflict explicit. No joined selection is necessary.


### “I am the only healer these people have left”
- ID: ep-020-3c1a4276a2; continuous; rejected; score: 39.0
- Segments: ep-020 01:02.60–01:28.20 (25.60s)
- Opening question: Why is an injured woman refusing to stop working in a freezing barn?
- Ending question: Can Juliana save the villagers from the fever when she is their only healer and is already injured?
- Why: The opening warning quickly establishes Juliana’s vulnerability; her refusal, Seamus’s grief over her changed circumstances, and her explanation of the village’s need build a clear reason to care. She ends by insisting she is not finished, leaving the villagers’ fate unresolved.
- Weakness: The scene establishes admirable resolve but largely settles its immediate disagreement. Its final declaration does not introduce a concrete next challenge. Weighted editorial score: 39/100; the opening timing also remains unverified.
- Human review: unreviewed
- Validation issues: None

### “I marry the Lord of Ashbury”
- ID: ep-020-92e9acebf9; continuous; needs_review; score: 37.0
- Segments: ep-020 00:18.80–00:56.00 (37.20s)
- Opening question: Can Catherine and Rupert claim Ashbury, and what stands between them and the title?
- Ending question: Will Rupert and Catherine actually gain power while the Dowager Duchess remains alive and Alexander’s death has not yet been formally sealed?
- Why: Catherine’s immediate declaration makes the ambition legible from the opening. Rupert then explains the succession condition, and their cold discussion of the ailing Dowager raises the stakes before he promises Catherine the ducal crown. The continuous cut ends on their anticipated power, not its attainment.
- Weakness: The opening does not yet establish a verified three-second disruption, while the strongest threat arrives later and is diluted by the closing insults. Weighted editorial score: 37/100; opening eligibility remains unconfirmed.
- Human review: unreviewed
- Validation issues: None

## Episode 21 — needs_review

The episode offers a clear rescue arc and a later, consequential illness reveal. The joined candidate combines both while preserving the reveal’s context; the continuous candidate is simpler but ends before Juliana’s remedy is tested.


### A plea for help, then the sick child
- ID: ep-021-12a9d2d875; continuous; needs_review; score: 66.0
- Segments: ep-021 00:03.50–00:45.50 (42.00s)
- Opening question: Can Juliana help Toby when the apothecary and manor doctor have turned Prudence away?
- Ending question: Will Juliana’s remedies help Toby, whose raspy cough we hear as she reaches him?
- Why: The barn-door slam and Prudence’s urgent plea hook immediately. The clip establishes the boy’s danger, the cost-based refusal of care, and Juliana’s decision to act; ending on Toby’s cough leaves the rescue outcome open. Editorial rubric scores: opening 4/5, emotional pull 4/5, opening curiosity 4/5, clarity 4/5, momentum 4/5, ending 3/5 (75/100).
- Weakness: The story becomes clear and consequential, but the three-second opening is not securely established as more than a startling entrance. The strongest emergency language cannot be assumed audible before the deadline. Weighted editorial score: 66/100; qualification remains pending opening review.
- Human review: unreviewed
- Validation issues: None

### A village boy recovers—and the manor’s secret
- ID: ep-021-102565617b; joined; rejected; score: None
- Segments: ep-021 00:42.80–01:13.50 → ep-021 01:31.00–01:54.00 (53.70s)
- Opening question: Can Juliana ease the little boy’s labored breathing with her mother’s herbal knowledge?
- Ending question: Will Juliana use her mother’s herbal knowledge to help the dying Dowager Duchess—and can she discover what is causing the illness?
- Why: The opening cough gives an immediate, understandable rescue problem. The first interval shows Juliana preparing and directing the herbal steam until Toby’s breathing eases. The second turns that successful rescue into a larger mystery: Prudence says the Dowager is dying, and Juliana’s apprehensive look over the ledger leaves her response unresolved. Editorial rubric scores: opening 4/5, emotional pull 5/5, opening curiosity 3/5, clarity 4/5, momentum 5/5, ending 4/5 (84/100).
- Weakness: The ending implies Juliana may act, but she does not explicitly decide to go to the manor; the illness reveal is the main cliffhanger.
- Human review: unreviewed
- Validation issues: Segment 1 cuts dialogue event ep-021-b0053

## Episode 22 — has_qualified

This episode supports a strong joined promo: it establishes Juliana's disguise and rescue motive, then pays that setup off with the Duchess's alarming condition. The selected sequence is 58.8 seconds total. Its main trade-off is that the infiltration between the two intervals is omitted.


### The maid risks everything to reach the dying Duchess
- ID: ep-022-317822d44f; joined; qualified; score: 68.0
- Segments: ep-022 00:06.50–00:42.80 → ep-022 01:48.50–02:11.00 (58.80s)
- Opening question: Can Juliana stay undiscovered long enough to reach the Duchess?
- Ending question: Can Juliana learn who has been treating the Duchess and help her before her condition worsens?
- Why: The urgent warning opens the clip immediately; Juliana then explains the rescue motive and accepts the maid disguise. After the chronological jump, the bedroom reveal escalates to her realization that this is not an ordinary fever, followed by the Duchess gasping and Juliana asking who has treated her. The specific medical danger and its cause remain unresolved.
- Weakness: The identity danger is asserted rather than explained, weakening investment in that strand. The opening's concealment action is understandable, but its specific stakes cannot be credited within three seconds because the warning's audible fragment is unknown. Weighted editorial score: 69/100.
- Human review: unreviewed
- Validation issues: None

## Episode 23 — has_qualified

Two qualifying continuous cuts offer different emphasis: the poisoning reveal and incoming threat, or the diagnosis and uncertain rescue. They overlap substantially, so they are alternatives rather than complementary promos.


### Poison diagnosis—and someone at the door
- ID: ep-023-1abbf1866f; continuous; qualified; score: 74.0
- Segments: ep-023 01:19.00–02:11.50 (52.50s)
- Opening question: Who is poisoning the helpless woman, and can Juliana stop it?
- Ending question: Who is opening the door, and will they stop Juliana before she can treat the Duchess?
- Why: The first line, “Someone is poisoning her,” is an immediate, specific hook. The clip names arsenic, shows the Duchess choking, and establishes Juliana’s urgent attempt to help. It ends as the door opens, leaving both the intruder’s identity and the rescue in jeopardy unresolved.
- Weakness: The arrival is framed as frightening without establishing why that person would threaten the rescue, and the preparation/doorway stretch slows development. Nevertheless, the immediate rescue stakes support continuation. Weighted editorial score: 74/100.
- Human review: approve
- Validation issues: None

### Not old age: can Juliana save her?
- ID: ep-023-1384792491; continuous; needs_review; score: 56.0
- Segments: ep-023 00:43.00–01:40.00 (57.00s)
- Opening question: If this is not old age, what is making the Duchess waste away?
- Ending question: Will Juliana’s attempted treatment save the Duchess?
- Why: Juliana’s line, “This is not simply old age,” arrives within the first second and opens a clear diagnostic mystery. The clip builds from symptoms and the journal to the arsenic diagnosis, then to the Duchess choking and Prudence pleading for help. It ends on Juliana’s uncertain “I can try,” with the outcome still open.
- Weakness: The opening does not yet demonstrate a recognizable hook within three seconds, and the clear poisoning reveal arrives relatively late. The rescue ending is stronger than the entry point. Weighted editorial score: 56/100; qualification remains pending opening review.
- Human review: unreviewed
- Validation issues: None

## Episode 24 — no_qualifying_candidate

Two distinct options: a continuous confrontation that makes the abuse explicit, and a joined cut that connects Juliana’s concern for the Duchess to her secret plan to return. Both open on the door opening and the crop-carrying intruder; the joined option has a more consequential mission at its ending but compresses the cause of the hearth punishment.


### The Maid Defies the Woman with the Riding Crop
- ID: ep-024-05e5661b49; continuous; rejected; score: 55.0
- Segments: ep-024 00:00.00–00:48.00 (48.00s)
- Opening question: Who is the armed noblewoman, and why is Juliana beside the unconscious Duchess?
- Ending question: What will the noblewoman make Juliana endure to teach her her place?
- Why: A door opens on an armed intruder, then the scene quickly establishes the sick Duchess and Juliana’s reason for being there. The noblewoman’s contempt escalates into a strike, and her final threat leaves Juliana’s punishment unresolved. The hidden bottle also hints that Juliana has a purpose beyond cleaning.
- Weakness: The opening spends its entire three-second hook window on a door and its sounds, delaying the understandable conflict. The weighted editorial score is 55/100, but the opening requirement fails.
- Human review: unreviewed
- Validation issues: None

### A Hidden Remedy, a Punishment, and a Promise to Return
- ID: ep-024-95b1e32b49; joined; rejected; score: 48.0
- Segments: ep-024 00:00.00–00:22.50 → ep-024 00:53.60–01:29.80 (58.70s)
- Opening question: Why is Juliana hiding medicine while a powerful woman confronts her beside a visibly ill Duchess?
- Ending question: Can Juliana get back to the Duchess with her hidden remedy before she is stopped?
- Why: The opening supplies the sick Duchess and Juliana’s apparent concern; the later hearth passage shows the punishment, the concealed journal and vial, and Juliana’s resolve to return. It ends on a specific mission whose outcome remains open. Combined duration: 58.7 seconds.
- Weakness: The proposed opening spends its entire first three seconds on a door and sound effects, before any recognizable story stakes. Weighted editorial score: 48/100; the failed opening requirement prevents qualification as assembled.
- Human review: unreviewed
- Validation issues: None

## Episode 25 — has_qualified

This episode offers two distinct usable arcs: a short injury-and-accusation confrontation and a longer poisoning-and-protection dilemma. Both are understandable from their selected dialogue and action, though the poisoning clip’s reference to the woman lacks her name in this interval.


### The Wound and the Accusation
- ID: ep-025-0d21bfea35; continuous; qualified; score: 58.0
- Segments: ep-025 00:13.20–00:37.80 (24.60s)
- Opening question: Who hurt Juliana, and what will Alexander do when he learns the answer?
- Ending question: Now that Juliana has named Lady Catherine, will Alexander confront her?
- Why: The clip opens on Alexander grasping Juliana’s shoulder; her sharp wince and his “You’re hurt” make the situation legible quickly. The visible wound leads to his insistence on knowing who caused it, and Juliana finally names Lady Catherine. It ends on a specific accusation before any response or consequence is shown.
- Weakness: The ending names the person responsible without establishing what confronting her would involve or cost. It offers a credible continuation question, but limited anticipation of a specific next action. Weighted editorial score: 58/100.
- Human review: unreviewed
- Validation issues: None

### A Slow Poisoning—and a Dangerous Return
- ID: ep-025-ebad502ada; continuous; needs_review; score: 52.0
- Segments: ep-025 01:30.20–02:26.40 (56.20s)
- Opening question: Who is repeatedly poisoning the woman, and can Juliana keep helping her without being hurt again?
- Ending question: Will Juliana return to help the sick woman, and can Alexander protect her from being hurt again?
- Why: The opening immediately describes someone administering small, repeated doses of poison. The sequence then establishes Juliana’s intervention, her determination to go back, and Alexander’s fear for her safety. His final “This time” leaves the risk unresolved after he points out that she could have been killed.
- Weakness: The opening's specific hook cannot be verified within three seconds. Beyond that eligibility uncertainty, the clip spends much of its runtime discussing danger rather than moving into the threatened return. Provisional weighted score: 52/100.
- Human review: unreviewed
- Validation issues: None

## Episode 26 — needs_review

The strongest material is the continuous exchange that moves from the Duchess’s poisoning to her recognition of Juliana’s ring. It provides a comprehensible danger and an unresolved identity mystery within the requested duration. A shorter identity-focused alternative offers variety but has less context for the ring’s importance.


### The dying Duchess recognizes Juliana’s ring
- ID: ep-026-8566520fa7; continuous; needs_review; score: 48.0
- Segments: ep-026 00:56.00–01:55.80 (59.80s)
- Opening question: Are Rupert and Catherine poisoning the Duchess—and can Juliana keep her alive?
- Ending question: Why does Juliana have this ring, and what will the Duchess do when she learns where it came from?
- Why: The Duchess’s accusation opens on a clear, consequential danger. Juliana confirms the poisoning and offers reassurance; the conversation then turns to her exile and honor before the ring triggers the Duchess’s desperate demand. The continuous cut ends on a specific identity mystery without resolving it. Duration: 59.8 seconds.
- Weakness: The required three-second hook is unverified. Beyond that, the ending clearly withholds a discovery but does not yet establish what the ring's origin could change for the maid. Provisional weighted editorial score: 48/100; opening eligibility requires review.
- Human review: unreviewed
- Validation issues: None

### A noble spirit, a servant’s apron, and a ring
- ID: ep-026-d68b7a18ce; continuous; needs_review; score: 48.0
- Segments: ep-026 01:13.80–02:00.88 (47.08s)
- Opening question: Why is a girl the Duchess calls noble working as a common maid?
- Ending question: What does the ring mean to the Duchess, and where did Juliana get it?
- Why: The Duchess’s question gives the clip an immediate status contradiction; Juliana’s answer establishes personal hardship before the ring provokes shock, a demand, and a final clasp of their hands. The consequential discovery remains unresolved. Duration: 47.08 seconds.
- Weakness: The potentially meaningful opening contrast cannot be verified within three seconds, and the ending establishes a mystery more strongly than its consequences. Weighted editorial score: 48/100; qualification remains pending opening-timing review.
- Human review: unreviewed
- Validation issues: None

## Episode 27 — has_qualified

Two distinct continuous selections offer different hooks: a possible hidden family connection and an escalating false accusation. The latter has a more immediate physical consequence; the former makes the identity mystery clearer.


### A rescue turned into an accusation
- ID: ep-027-3fe9e5c630; continuous; qualified; score: 72.0
- Segments: ep-027 01:32.80–02:30.50 (57.70s)
- Opening question: Why does Juliana insist the physicians were not saving the Duchess?
- Ending question: Can Juliana escape the arrest or prove that she was trying to save the Duchess?
- Why: Juliana's full line, “The physicians were not saving her!”, hooks with an understandable claim. The nobleman frames her as an unauthorized stranger with a substance; she identifies it as an antidote and says someone has been poisoning the Duchess. Catherine twists that claim, and the nobleman orders Juliana taken. The clip ends as she is dragged away, with her fate unresolved.
- Weakness: The opening establishes a medical disagreement but not yet the distinctive poisoning-and-false-accusation conflict; the stronger story hook develops later. Weighted editorial score: 72/100.
- Human review: unreviewed
- Validation issues: None

### The Duchess recognizes the ring
- ID: ep-027-048d8dd7ec; continuous; needs_review; score: 51.0
- Segments: ep-027 00:00.00–00:46.40 (46.40s)
- Opening question: Why does the Duchess recognize the ring Juliana wears?
- Ending question: What will Juliana reveal when the Duchess asks her husband's name?
- Why: The trembling hands examining the ring and the Duchess's urgent questions establish an immediate mystery. The conversation develops from Juliana's account of her husband to the crest and the lost son, then ends on a direct question that could connect them.
- Weakness: The meaningful family mystery develops after the three-second window. The opening offers ring-focused concern without yet explaining why the ring matters. Weighted editorial score: 52/100; opening eligibility remains under review.
- Human review: unreviewed
- Validation issues: None

## Episode 28 — has_qualified

Two distinct continuous cuts offer usable but differently weighted hooks: an attempted rescue and accusation reversal, or a hidden-identity reveal that escalates into a threat of execution. Both are within the requested duration and end on unresolved consequences.


### The Duchess Names Her Accusers
- ID: ep-028-94d05dee6e; continuous; qualified; score: 70.0
- Segments: ep-028 00:00.00–00:52.20 (52.20s)
- Opening question: Why is Juliana being dragged away, and what does Catherine’s attack on her fallen book mean?
- Ending question: Will Juliana be allowed to help the collapsing Duchess, and will the Duchess’s accusation stand?
- Why: The clip opens on a clear physical struggle, quickly establishes the poisoning accusation, then reverses expectations when the Duchess says Juliana saved her and accuses the others. Juliana’s desperate attempt to help leaves both her freedom and the Duchess’s condition unresolved.
- Weakness: The opening establishes force but not a distinctive story question; the poisoning conflict only becomes explicit later. The accusation sequence also delays the stronger reversal. Weighted editorial score: 70/100.
- Human review: unreviewed
- Validation issues: None

### Lady Juliana’s Secret Is Exposed
- ID: ep-028-ab4ed815f9; continuous; needs_review; score: 57.0
- Segments: ep-028 01:33.80–02:18.50 (44.70s)
- Opening question: What has Catherine discovered in the book, and what will she do with Juliana’s true identity?
- Ending question: Can Juliana explain the book to the magistrate before Catherine’s accusation sends her to the gallows?
- Why: The inscription and Catherine’s spoken reveal provide an immediate, specific discovery. Her taunts establish Juliana’s hidden identity and present humiliation, while the threatened magistrate and gallows turn the seized book into a concrete danger. The final image leaves Juliana being dragged away, with her fate unresolved.
- Weakness: The opening relies on an unfamiliar name and a partially timed reaction rather than an immediately understandable disruption. Later stakes are stronger, but cannot repair the three-second requirement. Weighted editorial score: 57/100; qualification remains pending opening review.
- Human review: unreviewed
- Validation issues: None

## Episode 29 — has_qualified

The episode offers two distinct, self-contained promo angles: Catherine's threat against Juliana's mother's book, and Juliana's imprisonment alongside her hope that Alexander will find her. Both have immediate confrontation and unresolved consequences; the second relies more on an unexplained relationship.


### Can her husband reach her in the dungeon?
- ID: ep-029-0d7b6c8899; continuous; qualified; score: 62.0
- Segments: ep-029 01:09.80–01:55.50 (45.70s)
- Opening question: Can Juliana's husband help her against the powerful people who are holding her?
- Ending question: Will Alexander find Juliana or otherwise help her escape after the dungeon gates close?
- Why: Juliana's opening claim that her husband will find her immediately sets up a rescue question. Catherine's taunt establishes the imbalance of power, and the guards' shove into the cell turns the dispute into imprisonment. Juliana's resolve followed by the portcullis crashing down leaves her fate and Alexander's response open.
- Weakness: The ending sustains the imprisonment problem without introducing an imminent next move, while the ledger, locket, and Alexander add context demands late in the clip. Weighted editorial score: 62/100. Main appeal: danger and anticipated rescue; secondary appeal: perceived injustice.
- Human review: unreviewed
- Validation issues: None

### A mother's book, a witchcraft frame
- ID: ep-029-dd4ae76b5e; continuous; needs_review; score: 60.0
- Segments: ep-029 00:05.10–00:56.60 (51.50s)
- Opening question: Why is Catherine holding Juliana's mother's book, and what will happen if Juliana cannot protect it?
- Ending question: Will Catherine succeed in framing Juliana and destroying her mother's work?
- Why: The clip opens on Catherine holding the book, then Juliana's plea lands within three seconds. It develops from the book's value, through Catherine's false witchcraft accusation, to an explicit threat of burning and hanging. It ends on the continuation of that threat without showing its outcome.
- Weakness: The story stakes arrive after the three-second window. This exact opening spends 2.30 seconds on unexplained book-holding, leaving too little securely interpretable material to confirm its hook. Weighted editorial score: 60/100; opening eligibility remains under review.
- Human review: unreviewed
- Validation issues: None

## Episode 30 — needs_review

This episode contains a strong, self-contained conspiracy sequence with a consequential unresolved threat. The selected cut connects the plot to Juliana’s vulnerability without relying on episode metadata.


### They’ll Make Her a Witch
- ID: ep-030-b1d6228a0d; continuous; needs_review; score: 50.0
- Segments: ep-030 01:34.50–02:31.21 (56.71s)
- Opening question: Will this household get away with manufacturing evidence to have her condemned?
- Ending question: Can Juliana survive the witchcraft charge and the magistrate’s hearing tomorrow?
- Why: The first line, “Do not hide the evidence, manufacture it,” is an immediate, specific hook. The scene makes the scheme legible through the planned trial, jury bribery, and Catherine’s prediction that Juliana will hang. The final declaration that she becomes a witch tomorrow is followed by Juliana’s imprisonment, leaving her fate unresolved. The continuous cut is 56.71 seconds and includes the complete source dialogue, including the lead-in to Catherine’s botanical-ledger line.
- Weakness: The three-second hook cannot be verified, so the candidate is not yet confirmed as qualifying. The lengthy conspiracy discussion also repeats the threat while giving Juliana little agency. Provisional weighted editorial score: 50/100; the opening scores reflect unavailable evidence, not confirmed absence.
- Human review: unreviewed
- Validation issues: None

## Episode 31 — has_qualified

The episode offers a clear escalation from verbal cruelty to a personal loss and physical danger. The strongest cuts here are continuous and end on the specific, unresolved threat of the hot iron near Juliana's eye. The shorter option is more immediately perilous but provides less context; both cuts draw on the same final confrontation.


### The book and the burning iron
- ID: ep-031-d6ede20347; continuous; qualified; score: 69.0
- Segments: ep-031 02:13.00–02:40.00 (27.00s)
- Opening question: Why is Catherine burning the book, and will she turn the iron on Juliana?
- Ending question: Will the iron burn Juliana before Catherine pulls it away?
- Why: This continuous 27-second cut opens on the iron pressing into the book, then makes the personal loss explicit through Catherine's line about Juliana's mother. Juliana's desperate reaction and Catherine's movement toward her face build directly to an unresolved, imminent threat.
- Weakness: The opening presents destruction before establishing why the book matters, and the middle repeats suffering more than it develops the relationship. The ending nevertheless opens a larger danger rather than merely concluding the book's destruction. Weighted editorial score: 69/100.
- Human review: unreviewed
- Validation issues: None

### Defiance at the branding iron
- ID: ep-031-2441c1c9a6; continuous; needs_review; score: 62.0
- Segments: ep-031 01:58.20–02:40.00 (41.80s)
- Opening question: Why is Catherine so determined to make Juliana kneel, and how far will she go when Juliana refuses?
- Ending question: Will Catherine burn or brand Juliana with the iron held inches from her eyes?
- Why: A continuous 41.8-second cut opens on Juliana's pointed question, quickly establishes the power struggle, and escalates from verbal defiance to Catherine scorching the book and threatening Juliana. It ends on the iron reflected in Juliana's eye before the outcome is shown.
- Weakness: The understandable conflict arrives after an opening whose crucial audible words cannot be verified within three seconds. Weighted editorial score: 62/100; qualification remains pending the opening-hook timing check.
- Human review: unreviewed
- Validation issues: None

## Episode 32 — has_qualified

Two distinct continuous cuts qualify as possible promos: one centers on a threatened act of violence; the other on Juliana’s resistance to Catherine’s attack on the ledger. The first has the clearer consequential cliffhanger. Both use only footage from ep-032.


### The Prisoner Who Won’t Flinch
- ID: ep-032-8edd11e531; continuous; qualified; score: 70.0
- Segments: ep-032 01:59.50–02:34.38 (34.88s)
- Opening question: Will Juliana’s defiance stop Catherine from using the branding iron against her?
- Ending question: Will Catherine burn Juliana, or will Juliana escape the iron inches from her eye?
- Why: The opening immediately shows Catherine snapping and raising the threat; the dialogue establishes that Juliana is resisting rather than pleading. The confrontation escalates from Catherine’s demand for silence to Juliana’s direct challenge, then ends with the iron thrust toward Juliana’s eye before contact.
- Weakness: The opening offers a recognizable threat but little distinctive story curiosity; the central accusation also repeats before the physical escalation. Weighted editorial score: 70/100.
- Human review: unreviewed
- Validation issues: None

### “Burn It”
- ID: ep-032-f8deb3fea8; continuous; qualified; score: 58.0
- Segments: ep-032 00:00.00–00:23.00 (23.00s)
- Opening question: Will Catherine’s attack on the ledger make the chained Juliana break?
- Ending question: After Juliana tells Catherine to burn the ledger, will Catherine follow through or turn her threat on Juliana?
- Why: The scorching ledger and its sizzling sound provide an immediate, understandable disruption. Catherine taunts the shackled Juliana and threatens her mother’s book; Juliana then shifts from visible grief to a defiant “Burn it.” The cut holds on her upright, shackled posture without showing Catherine’s response.
- Weakness: The book's personal significance—and its connection to the captive's mother—is not explained. This limits both the opening's specificity and the emotional cost of the threatened destruction. Weighted editorial score: 58/100.
- Human review: unreviewed
- Validation issues: None

## Episode 33 — needs_review

This episode has a clear, self-contained coercion scene with strong stakes and two useful cut points: one centers on the threat and manufactured accusation, while the other centers on the imposed testimony and pending trial.


### The testimony he wrote for her
- ID: ep-033-a0d09eaa97; continuous; needs_review; score: 62.0
- Segments: ep-033 02:06.80–02:44.50 (37.70s)
- Opening question: Can the maid’s plea that Juliana saved Toby overcome the testimony the lord is forcing her to give?
- Ending question: Will the maid testify against Juliana, and what will happen at the trial?
- Why: The opening is a clear defense of Juliana; the exchange quickly reveals that the lord has recast that defense as witchcraft testimony. The maid’s realization, protest, and collapse lead to the lord’s final reminder that a trial is coming. Duration: 37.7 seconds.
- Weakness: The strongest story hook arrives after the uncertain opening window: a lifesaving act is being turned into evidence against the rescuer. The first three seconds establish distress but not that contradiction. Weighted editorial score: 62/100; qualification remains pending the opening-hook check.
- Human review: unreviewed
- Validation issues: None

### A child’s safety as leverage
- ID: ep-033-d6b88e103c; continuous; needs_review; score: 50.0
- Segments: ep-033 01:04.40–02:02.80 (58.40s)
- Opening question: Will the maid give the lord the accusation he wants to protect her seven-year-old brother?
- Ending question: Will the lord’s leading questions become a witchcraft accusation against Juliana, and will the maid go along with it?
- Why: The gaol threat lands in the opening seconds and makes the coercion legible. The sequence escalates from the maid defending Juliana to the lord supplying increasingly incriminating details; it ends after he says she heard words she could not understand, just before he names the charge. Duration: 58.4 seconds.
- Weakness: The required three-second hook cannot be verified from the supplied opening fragment. Beyond that eligibility issue, the ending repeats the interrogation's established claims rather than reaching a sharper decision point. Weighted editorial score: 53/100.
- Human review: unreviewed
- Validation issues: None

## Episode 34 — needs_review

This courtroom episode offers two distinct promo angles: a distressed witness's testimony and Juliana's refusal to renounce her healing. The clearest consequential endpoint is the Judge poised to deliver judgment; the episode ends before the sentence is revealed.


### Refuse to renounce
- ID: ep-034-3b8a473a9c; continuous; needs_review; score: 53.0
- Segments: ep-034 02:22.40–03:10.00 (47.60s)
- Opening question: Will Juliana renounce her practices to save herself?
- Ending question: What sentence will the Judge pronounce after Juliana refuses to recant?
- Why: The opening presents a specific, consequential choice. Juliana's refusal and the Judge's warning clarify the danger; her acceptance of the consequence leads to the Judge rising and preparing to deliver judgment, but the sentence itself remains unheard.
- Weakness: The consequential conflict is clear across the clip, but its presence within the required first three seconds cannot be verified. Provisional weighted editorial score: 53/100; opening eligibility remains under review.
- Human review: unreviewed
- Validation issues: None

### The witness turns against her
- ID: ep-034-3b91af5a5e; continuous; needs_review; score: 48.0
- Segments: ep-034 00:37.50–01:33.20 (55.70s)
- Opening question: What will Prudence say about the woman she served beside?
- Ending question: What will the Lord's further witnesses claim, and will their testimony decide Juliana's fate?
- Why: The Judge's direct question to Prudence opens on a clear witness-versus-accused conflict. The testimony, Juliana's plea, her angry interruption, and the Judge's silencing of her build through distinct beats before the Lord raises the threat of more witnesses.
- Weakness: The opening spends its critical first three seconds on courtroom setup without an established story-specific hook. Later conflict cannot compensate for that eligibility uncertainty. The weighted editorial score is 48/100.
- Human review: unreviewed
- Validation issues: None

## Episode 35 — has_qualified

Two distinct continuous selections offer usable arcs: an emotionally legible reunion ending on a survival mystery, and a sharper conspiracy reveal. The latter has stronger consequential suspense, while the former provides a warmer character entry point.


### The men who wanted him erased
- ID: ep-035-9f69f8e068; continuous; qualified; score: 58.0
- Segments: ep-035 01:41.20–02:30.00 (48.80s)
- Opening question: Who ordered Alexander's men slaughtered, and why was he meant to disappear?
- Ending question: Who are the powerful men behind the ambush, and what will Alexander do now that he knows they still rule?
- Why: The map-crushing action and immediate account of slaughter open on a concrete threat. The story escalates from Alexander's survival to a deliberate cover-up and an intentional ambush, ending on the consequential reveal that the perpetrators still rule Ashwood.
- Weakness: The clip is primarily retrospective testimony: it reveals responsibility without establishing a concrete next action or imminent consequence. Weighted editorial score: 58/100.
- Human review: unreviewed
- Validation issues: None

### The son she buried
- ID: ep-035-f642f4b819; continuous; rejected; score: 43.0
- Segments: ep-035 00:27.50–01:18.00 (50.50s)
- Opening question: Who has arrived at this remote cabin, and why does the man inside react with alarm?
- Ending question: Why was Alexander not supposed to survive?
- Why: The cabin reveal hooks with Alexander snapping up in alarm, then the relationship and loss become clear through their exchange and embrace. The regiment's destruction deepens the stakes before his ominous admission, which leaves his survival unexplained.
- Weakness: The strongest material arrives well after the opening, and the ending withholds a past explanation rather than establishing a consequential next outcome. Weighted editorial score: 43/100; the candidate does not meet all qualifying requirements.
- Human review: unreviewed
- Validation issues: None

## Episode 36 — needs_review

Two useful, distinct continuous cuts: one centers on the arrest and execution deadline; the other on Alexander’s return vow. Both leave consequential outcomes unresolved, though each requires a newcomer to absorb unfamiliar names and relationships.


### Arrested before the wedding
- ID: ep-036-63c0473ba1; continuous; needs_review; score: 59.0
- Segments: ep-036 01:39.50–02:36.00 (56.50s)
- Opening question: Who arrested Juliana, and what will happen to her?
- Ending question: Will Alexander reach Juliana before the execution scheduled after the wedding in two days?
- Why: The opening immediately names an arrest. The dialogue then establishes Juliana’s connection to Alexander’s mother, the false accusation, the death sentence, and the wedding deadline. It ends on a specific, imminent timeline without showing what Alexander will do.
- Weakness: The crucial opening arrest announcement is not confirmed within three seconds, so the proposed cut cannot yet be treated as fully qualifying. The wedding adds intrigue but its causal significance is unclear. Weighted editorial score: 62/100.
- Human review: unreviewed
- Validation issues: None

### The dead Duke is coming home
- ID: ep-036-7d0e85f181; continuous; needs_review; score: 48.0
- Segments: ep-036 02:36.50–03:20.75 (44.25s)
- Opening question: Can Alexander stop the wedding—and save his wife before she is killed?
- Ending question: What will happen when the supposedly dead Duke returns before the wedding?
- Why: The opening quickly links the wedding to the threat against Alexander’s wife. His mother’s warning and his escalating vow build toward the declaration that the “dead Duke” is coming home; the return and its consequences remain unseen.
- Weakness: The meaningful danger is established after the opening window; the first three seconds do not securely communicate a recognizable hook. The later rescue setup is usable, but opening eligibility remains unconfirmed. Weighted editorial score: 48/100.
- Human review: unreviewed
- Validation issues: Opening hook assessment cites an event outside the first three seconds

## Episode 37 — no_qualifying_candidate

The episode offers a clear, unusually dark conflict: a wedding is paired with a planned public execution. The strongest promo options either foreground the conspirators’ plan or connect it to Juliana’s defiance in the dungeon.


### The plan—and Juliana’s refusal to break
- ID: ep-037-1204cd27b7; joined; rejected; score: 46.0
- Segments: ep-037 00:00.00–00:30.00 → ep-037 01:28.00–01:56.50 (58.50s)
- Opening question: What are the guests being invited to witness—and can Juliana resist the people arranging it?
- Ending question: Can Juliana survive the execution her enemies are planning without surrendering who she is?
- Why: The first passage establishes the conspirators’ plan; the second shows its human cost and gives Juliana a forceful, specific response. Her final declaration leaves her fate unresolved while giving the viewer someone to root for. Duration: 58.5 seconds.
- Weakness: The selected opening spends its first three seconds on routine invitation handling, failing the mandatory hook requirement. Later stakes cannot retroactively qualify that opening. The ending also repeats resolve rather than revealing a concrete route toward resistance.
- Human review: unreviewed
- Validation issues: None

### A wedding invitation with an execution clause
- ID: ep-037-19b9c4a6e7; continuous; rejected; score: 42.0
- Segments: ep-037 00:00.00–00:30.00 (30.00s)
- Opening question: What are these guests being invited to witness?
- Ending question: Will Juliana be executed after the wedding, as Catherine plans?
- Why: The sealed invitations provide an immediate visual hook, and Rupert’s opening line establishes that the guests are meant to witness something. Their exchange reveals the wedding’s political purpose, then the planned execution and its treatment as entertainment. It ends with the threat clear but its outcome unresolved. Duration: 30 seconds.
- Weakness: The opening spends its crucial first three seconds on decorative setup without a story hook. The later execution threat creates continuation interest but cannot qualify this exact opening. Weighted editorial score: 42/100.
- Human review: unreviewed
- Validation issues: None

## Episode 38 — no_qualifying_candidate

One strong, self-contained emotional arc supports a single continuous candidate. The bread-offering passage is compassionate, but on its own it does not end on as consequential an unresolved outcome.


### “Then I Suppose I’m Next”
- ID: ep-038-1267562750; continuous; rejected; score: 43.0
- Segments: ep-038 00:40.00–01:18.50 (38.50s)
- Opening question: She says she has been condemned: what happened to her, and will she survive long enough to protect her husband?
- Ending question: Now that the wedding is beginning and Juliana believes she is next, will she be executed—and can Alexander remain safe?
- Why: A 38.5-second continuous cut opens on Juliana’s anguish and quickly establishes that she is condemned. Her fear for her husband develops into a clear vow not to betray him; the bells then connect that loyalty to an imminent threat. It ends on her expectation that she is next, leaving her fate unresolved. The single interval preserves chronology and needs no transition.
- Weakness: The opening withholds the concrete predicament, while the ending withholds the meaning of “next.” The middle establishes meaningful stakes more clearly than either boundary. Weighted editorial score: 43/100; the opening requirement fails.
- Human review: unreviewed
- Validation issues: None

## Episode 39 — no_qualifying_candidate

One strong, self-contained transformation-and-rescue-vow candidate is available. The guard ambush is a distinct action beat, but its immediate outcome is largely resolved and its broader stakes are less clear on its own, so it is not included.


### Alexander steps out of hiding
- ID: ep-039-cff9e57866; continuous; rejected; score: 48.0
- Segments: ep-039 00:50.00–01:38.41 (48.41s)
- Opening question: Why has this scarred, disguised man been hiding—and what is he about to reclaim?
- Ending question: Will Alexander reach his wife and bring her home?
- Why: The opening mirror reveal is immediately legible, and the transformation develops into a clear declaration of return: Alexander cuts his hair, identifies himself, is acknowledged as 'Your Grace,' and orders the chapel secured. His final vow makes the unresolved outcome specific and personal. The continuous 48.41-second cut preserves the full progression and ends on the source's cut to black.
- Weakness: The proposed opening delays its meaningful identity revelation until 13 seconds, failing the required three-second hook. Later stakes are understandable but lack concrete opposition. Weighted editorial score: 48/100; the score does not override the opening requirement failure.
- Human review: unreviewed
- Validation issues: None

## Episode 40 — no_qualifying_candidate

Two usable but related candidates center on the wedding’s sinister context. The first has the clearer immediate hook; the second offers the more explicit threat and unresolved outcome, but its short opening and identity gaps make it less self-explanatory.


### A Perfect Wedding, Sealed Exits
- ID: ep-040-98b716d194; joined; rejected; score: 41.0
- Segments: ep-040 00:49.80–00:55.80 → ep-040 01:03.80–01:18.50 (20.70s)
- Opening question: What has to go perfectly at this wedding—and why are the entrances being secured?
- Ending question: Will the conspirators carry out their plan to kill the woman they call a witch?
- Why: The 20.7-second chronological join starts with Rupert’s anxious insistence that everything go perfectly, then cuts to the balcony guard confirming the cathedral is sealed. The conspirator’s claim that Ashburgh will have a new Duke and Duchess before “its witch” is dead gives the wedding a consequential, sinister purpose and leaves the murder plan unresolved.
- Weakness: The proposed opening spends its crucial first three seconds on routine wedding anticipation. The later threat creates story stakes, but it arrives too late to supply the required opening hook and targets someone the viewer has not met.
- Human review: unreviewed
- Validation issues: None

### “Imagine Juliana Seeing This”
- ID: ep-040-87e69b5be0; continuous; rejected; score: 34.0
- Segments: ep-040 00:23.20–00:48.30 (25.10s)
- Opening question: Why do the Harringtons want Juliana to see this wedding—and what are they planning for her?
- Ending question: What does Lady Harrington mean by “everything that comes after” the wedding?
- Why: A 25.1-second continuous cut opens on Lady Harrington’s pointed taunt, then escalates through Lord Harrington’s threat and the couple’s gloating remarks about Juliana. Their “excellent view” of the wedding takes on a darker meaning when she hints at what follows. The threat creates a specific reason to wonder what the couple intends, without resolving it.
- Weakness: The opening withholds the referent of “this,” and the rest of the clip never makes the threatened harm concrete. It establishes malice more effectively than investment in a particular outcome.
- Human review: unreviewed
- Validation issues: None

## Episode 41 — has_qualified

The episode offers a clear public-humiliation-to-defiance progression followed by a major interruption and an unresolved arrival. The strongest cuts use Juliana’s response or Catherine’s public address to make the conflict legible before the explosion. The episode’s final reveal supports a strong continuation question, though the newcomers’ identity and purpose remain unknown in the supplied footage.


### A chained woman answers back
- ID: ep-041-50948f441e; continuous; qualified; score: 71.0
- Segments: ep-041 00:57.80–01:36.09 (38.29s)
- Opening question: How will Catherine respond when Juliana openly challenges her power?
- Ending question: Who has breached the cathedral, and will their arrival change Juliana’s fate?
- Why: Continuous 38.29-second cut. Juliana’s complete challenge is the immediate hook, followed by Catherine’s answer and the couple turning back to the wedding. The explosion overturns that apparent return to the ceremony; armed silhouettes emerge and Juliana’s expression shifts, leaving their identity and the outcome unresolved.
- Weakness: The connection between the woman's captivity and the couple's title ambition is unstated, so investment rests more on her immediate freedom than on the larger scheme. Weighted editorial score: 71/100. Main appeal: danger and possible rescue.
- Human review: unreviewed
- Validation issues: None

### The public disgrace turns into a breach
- ID: ep-041-482a5ad35d; continuous; needs_review; score: 55.0
- Segments: ep-041 00:39.80–01:36.09 (56.29s)
- Opening question: Can Juliana withstand Catherine’s public humiliation—or will she defy her?
- Ending question: Who are the armed figures emerging through the wreckage, and what will their arrival mean for Juliana?
- Why: Continuous 56.29-second cut. Juliana halts in the aisle and Catherine addresses her within 1.2 seconds; the clip establishes the public humiliation, gives Juliana a defiant reply, then escalates from the wedding proceeding to the entrance exploding and armed figures appearing. It ends on Juliana’s reaction before their identity or purpose is revealed.
- Weakness: The consequential conflict arrives after a weak, timing-dependent opening; the first three seconds do not securely establish a hook. The title dispute also lacks personal context. Weighted editorial score: 55/100, with opening eligibility still needing review.
- Human review: unreviewed
- Validation issues: None

## Episode 42 — needs_review

This episode offers two distinct, self-contained promo angles: the return and challenge of a presumed-dead man, and the emotional recognition that leads into a personal reckoning. Both cuts leave a consequential confrontation unresolved; the second is more emotionally developed but reveals more of Alexander's public recognition.


### The man they thought was dead
- ID: ep-042-0d4d6b700f; continuous; needs_review; score: 44.0
- Segments: ep-042 00:00.00–00:39.80 (39.80s)
- Opening question: Who has just entered through the shattered cathedral doors, and why does his arrival unsettle the people inside?
- Ending question: If Alexander was declared dead, what will happen now that he has returned and openly called that story a lie?
- Why: A striking ruined-doorway entrance hooks immediately; the guard's refusal and Rupert's claim that Alexander died turn the reveal into a clear power struggle. It develops through a reversal of allegiance and ends before the confrontation is settled. Estimated rubric scores (opening, emotion, curiosity, clarity, momentum, ending): 3, 3, 4, 4, 5, 4; weighted total 74/100. Qualifying checks: duration, opening hook, standalone meaning, unresolved ending, and source fidelity pass.
- Weakness: The opening spends roughly ten seconds on an entrance before the first spoken challenge, without securely establishing a three-second story hook. Later intrigue is stronger than the opening, but its personal consequences remain vague. Weighted editorial score: 44/100; qualification remains pending opening review.
- Human review: unreviewed
- Validation issues: None

### A mother's recognition, a duke's challenge
- ID: ep-042-c0e9ae211c; continuous; rejected; score: None
- Segments: ep-042 00:33.80–01:17.80 (44.00s)
- Opening question: How can this man be Alexander if Rupert insists Alexander died?
- Ending question: What will Alexander do to Rupert over what he says Rupert stole—and how will Rupert respond?
- Why: The opening line presents a specific contradiction. The clip moves from denial, to a tender reunion, to the mother's public declaration, then ends on Alexander's promised reckoning before its outcome. The relationship and claim are explained within the selection. Estimated rubric scores (opening, emotion, curiosity, clarity, momentum, ending): 4, 5, 4, 4, 4, 4; weighted total 84/100. Qualifying checks: duration, opening hook, standalone meaning, unresolved ending, and source fidelity pass.
- Weakness: The mother’s declaration gives the audience a substantial public recognition payoff before the ending; the unresolved hook is the confrontation with Rupert, not whether Alexander is recognized.
- Human review: unreviewed
- Validation issues: No cited hook event occurs in the first three playback seconds | hook_event_ids cites events outside the selected clip

## Episode 43 — has_qualified

This episode offers several clear, source-grounded promo paths: a public authority reversal, an official betrayal disclosure, and a thwarted escape. Each can end on a consequential question, though the standalone cuts rely on viewers inferring some background about Alexander's title and the original ambush.


### The Report Names the Traitors
- ID: ep-043-d8e9ee1d40; continuous; needs_review; score: 57.0
- Segments: ep-043 00:26.10–01:12.70 (46.60s)
- Opening question: What does Alexander's Crown-sealed dossier prove—and whose actions does it expose?
- Ending question: Will the evidence establish that Rupert and Sterling betrayed Alexander and his men, or can Rupert's denial hold?
- Why: Alexander's promise to let the Crown decide leads directly into official evidence: the leak is called deliberate, and both Sterling and Rupert are named. Alexander's accusation and Rupert's denial turn the document reading into a personal confrontation, ending with culpability still contested.
- Weakness: The opening withholds the very conflict that later makes the scene compelling: the first line invokes authority without explaining what is at stake. Weighted editorial score: 58/100; opening-hook eligibility remains under review.
- Human review: unreviewed
- Validation issues: None

### The Guards Choose Their Duke
- ID: ep-043-78ff15dc2f; continuous; qualified; score: 54.0
- Segments: ep-043 00:00.00–00:37.00 (37.00s)
- Opening question: If Rupert claims this man is an impostor, why do the royal guards refuse his order and salute Alexander instead?
- Ending question: What will the Crown's sealed evidence reveal about the rival claim to the dukedom?
- Why: Rupert's order to arrest Alexander is immediately legible, and the guards' refusal and salute deliver a clear reversal. Alexander then introduces Crown-sealed documents and orders the first read, giving the clip a specific next revelation to anticipate.
- Weakness: The conflict is understandable, but emotional allegiance is thin: the viewer has little basis to know whose claim is just or why either man's victory matters beyond rank and authority. Weighted editorial score: 54/100.
- Human review: unreviewed
- Validation issues: None

### Sterling's Escape Is Blocked
- ID: ep-043-8f2136325a; continuous; rejected; score: 36.0
- Segments: ep-043 01:28.60–01:54.96 (26.36s)
- Opening question: Who transferred Alexander's estate and title under false authority—and what will happen when the people responsible are exposed?
- Ending question: Will the constable arrest Sterling now that his escape is blocked?
- Why: The official's statement establishes the wrong done to Alexander. Rupert's accusation prompts Sterling to flee, but a constable is waiting outside and asks where he is going; Sterling's terrified reaction leaves the immediate confrontation unresolved.
- Weakness: The ending delivers a completed interception rather than a strong unresolved outcome, while the opening hook is timing-dependent and unverified. Weighted editorial score: 36/100; the candidate does not meet all qualifying requirements.
- Human review: unreviewed
- Validation issues: None

## Episode 44 — has_qualified

The episode offers two usable continuous cuts: one led by an arrest and one centered on Catherine's appeal and Alexander's choice. The latter has a clearer romantic throughline and a more consequential final reveal; neither requires added context or reordered footage.


### The woman in chains
- ID: ep-044-036f8d145e; continuous; qualified; score: 68.0
- Segments: ep-044 00:25.20–01:10.50 (45.30s)
- Opening question: Why did Catherine believe Alexander was dead, and will their past love matter to him now?
- Ending question: Why is Alexander going to the chained woman, and what will happen between him and Catherine after this rejection?
- Why: Catherine's opening line quickly establishes a painful past without requiring prior-episode knowledge. Her confession builds into Alexander's denial, and his walk toward Juliana gives the ending a consequential new complication.
- Weakness: The ending shifts investment to a captive whose connection to Alexander is unknown. His approach opens a meaningful encounter but does not establish a promise of rescue or a romantic relationship. Weighted editorial score: 68/100.
- Human review: unreviewed
- Validation issues: None

### Arrested at the altar
- ID: ep-044-4fede80096; continuous; needs_review; score: 48.0
- Segments: ep-044 00:00.00–00:51.00 (51.00s)
- Opening question: Can Lord Sterling escape arrest, and what will Catherine do as the men around her are taken into custody?
- Ending question: After Alexander says she was never his Duchess, will Catherine accept his rejection or keep fighting for their past?
- Why: The immediate arrest gives a newcomer a clear disruption, and the footage develops from the conspirators being restrained into Catherine's personal appeal and Alexander's blunt answer. It is a continuous 51-second cut with an unresolved emotional response.
- Weakness: The opening does not securely deliver its confrontation within three seconds, and its arrest setup only loosely connects to the romantic conflict that supplies the ending. Weighted editorial score: 48/100; opening eligibility remains under review.
- Human review: unreviewed
- Validation issues: Opening hook assessment cites an event outside the first three seconds

## Episode 45 — has_qualified

The strongest self-contained promo passage is the public duchess declaration followed by the High Priest’s challenge. It offers a clear reversal and unresolved personal and legal stakes without requiring earlier context to understand the immediate conflict.


### The Duchess’s Claim Challenged
- ID: ep-045-e75ff6bb69; joined; qualified; score: 72.0
- Segments: ep-045 00:00.00–00:12.20 → ep-045 01:14.50–01:57.50 (55.20s)
- Opening question: Why is this man approaching a tearful, shackled woman—and can he free her?
- Ending question: After the priest declares Juliana is not Alexander’s lawful wife and a Crown officer approaches with a drawn sword, how will Alexander protect her and contest the ruling?
- Why: The opening hook occurs immediately: Alexander strides toward a chained Juliana. The later interval supplies his public claim that she is his lawful wife and Duchess, then overturns that claim with the priest’s legal challenge. Juliana’s alarm and Alexander shielding her leave a specific, consequential confrontation unresolved. The combined duration is 55.2 seconds.
- Weakness: The opening establishes captivity but not the relationship that makes this story distinctive; that arrives at 12.5 seconds. The legal challenge also repeats its central point. Weighted editorial score: 72/100.
- Human review: unreviewed
- Validation issues: None

### A Duchess Denied
- ID: ep-045-6fb6762651; continuous; needs_review; score: 58.0
- Segments: ep-045 01:11.20–02:01.75 (50.55s)
- Opening question: Alexander calls Juliana his lawful wife and the Duchess of Ashburton—but can that claim stand?
- Ending question: Will Alexander be able to defend Juliana’s marriage and title after the High Priest declares them invalid—and what will Catherine do now?
- Why: The clip opens as Alexander presents Juliana to the congregation, with his declaration that she is his lawful wife and duchess arriving within the first second. The High Priest then cites the missing license and registration, directly overturning that public claim; Juliana’s alarm and Catherine’s triumphant smile leave the consequences open. The complete passage is 50.55 seconds and uses a continuous source interval.
- Weakness: The meaningful conflict arrives after the opening window: the marriage claim starts at 3.60 seconds, and the interruption starts at 15.30 seconds. Weighted editorial score: 58/100; the opening requirement remains unconfirmed despite a strong later reversal.
- Human review: unreviewed
- Validation issues: Opening hook assessment cites an event outside the first three seconds

## Episode 46 — needs_review

This episode offers two clear continuous-cut options: a broader setup that lets Juliana voice her defiance, and a shorter legal confrontation that ends on a specific ten-day threat. Both preserve the unresolved question of whether the marriage will stand.


### The Crown Challenges Their Marriage
- ID: ep-046-5d110ab880; continuous; needs_review; score: 55.0
- Segments: ep-046 00:11.00–01:11.00 (60.00s)
- Opening question: Why have armed royal guards arrived at the wedding, and can the Crown invalidate this marriage?
- Ending question: Can paper and royal authority undo the marriage Juliana and Alexander defend?
- Why: The opening shows the High Priest with armed guards and a sealed decree, then declares the sanctuary under Crown seizure. His case against the marriage builds through specific objections, Juliana answers with personal defiance, and the final line puts the unresolved question of their marriage’s legitimacy plainly on the table. The continuous 60-second selection includes complete dialogue lines.
- Weakness: The opening does not yet communicate the personal stakes, and its potentially useful declaration cannot be verified within three seconds. Later, repeated procedural objections slow the confrontation. Weighted editorial score: 55/100; opening eligibility remains under review.
- Human review: unreviewed
- Validation issues: None

### Ten Days to Save the Marriage
- ID: ep-046-e81f8d5dfe; continuous; rejected; score: None
- Segments: ep-046 01:32.20–02:03.60 (31.40s)
- Opening question: Will the High Priest’s claim that the marriage was unauthorized prevail over Alexander’s challenge?
- Ending question: Will the council rule against Alexander in ten days, and will he lose Juliana?
- Why: The opening immediately disputes the marriage’s validity. Alexander counters with a legal challenge and proposes a hearing before witnesses; the High Priest accepts the ten-day test while warning of the personal cost of losing. It is a compact, consequential cliffhanger with an explicit deadline.
- Weakness: This cut gives less background about why the marriage is disputed, and the council’s role is introduced quickly.
- Human review: unreviewed
- Validation issues: Segment 1 cuts dialogue event ep-046-b0050

## Episode 47 — needs_review

The strongest material is Catherine’s covert scheme and Juliana’s later choice to offer her shelter on punishing terms. The latter has the more specific unresolved ending; the scheme is a distinct but less concrete alternative.


### Shelter on Juliana’s terms
- ID: ep-047-bd23c6ffd2; continuous; needs_review; score: 50.0
- Segments: ep-047 01:21.80–02:08.50 (46.70s)
- Opening question: Why does Juliana stop Catherine’s expulsion—and what will she demand in return?
- Ending question: Will Catherine accept Juliana’s terms and become a scullery maid, or leave the county with nothing?
- Why: Juliana’s abrupt “Stop” opens on a clear reversal, and Alexander’s objection quickly supplies the conflict. Juliana then turns threatened expulsion into a stark offer; the cut falls after the ultimatum but before Catherine answers.
- Weakness: The ending risks completing Juliana's victory rather than opening a larger story problem: Catherine may already accept the terms, and no specific subsequent confrontation or danger is established.
- Human review: unreviewed
- Validation issues: None

### Catherine’s secret plan
- ID: ep-047-672cc22c84; continuous; needs_review; score: 39.0
- Segments: ep-047 00:00.00–00:21.20 (21.20s)
- Opening question: Catherine says she intends to stay on the estate—what is she willing to do to make that happen?
- Ending question: What will Catherine do to keep the council paralyzed and secure her place on the estate?
- Why: The opening gives a newcomer Catherine’s goal immediately, then the conspirator’s warning raises the pressure before she reveals that she has a plan. The final line withholds what that plan is. The clip is a distinct, secret-scheme angle rather than another confrontation.
- Weakness: The opening is atmospheric rather than a confirmed three-second hook, and the estate-and-marriage stakes lack enough context for strong investment. Weighted editorial score: 39/100; eligibility remains pending opening-timing review.
- Human review: unreviewed
- Validation issues: None

## Episode 48 — has_qualified

Two continuous cuts offer distinct entry points: Catherine's deadline-driven revenge plan, or the secret task she gives Agnes. Both meet the requested duration and preserve chronology; the second has the more specific unresolved ending.


### Lock the Door—Send for the Priest
- ID: ep-048-2623ea2a82; continuous; qualified; score: 50.0
- Segments: ep-048 00:29.20–01:13.40 (44.20s)
- Opening question: Why does Catherine need the room locked, and what is she planning in secret?
- Ending question: Will Agnes get Father Thomas to Catherine without anyone seeing him arrive?
- Why: Agnes's question is followed quickly by Catherine's sharp command to lock the door. The clip then reveals the humiliation motivating Catherine's scheme, her need for Thomas, and the covert assignment, ending on a specific unanswered task. Duration: 44.2 seconds.
- Weakness: The conspiracy is understandable, but its human consequences are not: viewers do not know what the hearing decides, why returning matters, or what discovery would cost. The opening offers only a mild secrecy cue. Weighted editorial score: 50/100.
- Human review: unreviewed
- Validation issues: None

### Ten Days to Undo the Decree
- ID: ep-048-d52f8cae3c; continuous; needs_review; score: 41.0
- Segments: ep-048 00:00.00–00:58.20 (58.20s)
- Opening question: What is Catherine plotting to do with the ten days before the council hearing?
- Ending question: What more will Catherine ask Father Thomas to do before the hearing?
- Why: The cold turn and threat to send a healer's crown back to the gutter begin the hook; her countdown, admission of humiliation, and plan to return to the house develop the conflict. It ends after a complete line, with Catherine's next move still unknown. Duration: 58.2 seconds.
- Weakness: The meaningful threat arrives after the three-second window, whose audible content is uncertain. Later, the plotting is understandable but emotionally remote because its target and consequences remain abstract. Weighted editorial score: 41/100; qualification remains pending opening review.
- Human review: unreviewed
- Validation issues: None

## Episode 49 — needs_review

This episode offers a coherent political-conspiracy sequence with explicit personal danger and a natural unresolved decision before the pact. The strongest material is dialogue-led, so the cuts depend on the performances and may feel static if the footage does not sustain the tension.


### A dangerous bargain
- ID: ep-049-3d01c24675; continuous; needs_review; score: 48.0
- Segments: ep-049 01:44.20–02:14.50 (30.30s)
- Opening question: Will Thomas risk execution for Catherine’s request—and what can she offer that would make the danger worthwhile?
- Ending question: Will Thomas accept Catherine’s offer and become her covert ally?
- Why: Thomas’s conditional question establishes the stakes at once. Catherine’s promise turns his fear of treason into a negotiation, and the clip cuts on her offer before his response or the pact. Duration: 30.3 seconds.
- Weakness: The opening's essential story information cannot be verified within three seconds, and the woman's larger purpose remains abstract. Provisional weighted editorial score: 48/100; opening qualification remains unconfirmed.
- Human review: unreviewed
- Validation issues: None

### Keep the hearing open
- ID: ep-049-5bc2a266b8; continuous; needs_review; score: 46.0
- Segments: ep-049 01:12.40–02:04.80 (52.40s)
- Opening question: What does Catherine need Father Thomas to do—and how far will she go to secure it?
- Ending question: Will Thomas risk hanging by helping Catherine keep the hearing open and spy on the council?
- Why: Thomas’s direct demand for plain speech opens immediately on a clear hook. Catherine lays out her two-part plan, then Thomas names the personal cost: treason could mean death. The clip ends on that danger before revealing whether he agrees. Duration: 52.4 seconds.
- Weakness: The opening does not securely communicate a hook within three seconds, and Catherine's specific underlying loss remains vague. Weighted editorial score: 46/100; opening eligibility still requires review.
- Human review: unreviewed
- Validation issues: None

## Episode 50 — needs_review

One joined candidate offers the clearest balance of immediate scandal, an understandable bargain, and a consequential unresolved discovery. The episode's final corridor reveal is too short to qualify alone, while a continuous selection long enough to reach it would exceed the duration limit.


### A Price for Silence, an Unexpected Witness
- ID: ep-050-763dea590e; joined; needs_review; score: 50.0
- Segments: ep-050 00:00.00–00:42.50 → ep-050 01:10.50–01:20.00 (52.00s)
- Opening question: Why is a priest in bed with Catherine, and what does she want from him?
- Ending question: Will Agnes reveal what she saw, and what will happen to Catherine and Thomas's secret bargain?
- Why: The bed image and Catherine's line about a man in a collar make the scandal legible immediately. The clip develops from their intimacy into an explicit negotiation, then cuts to Agnes finding them and retreating in shock. The combined duration is 52 seconds, and the ending leaves the consequences of the discovery unresolved.
- Weakness: The opening does not securely communicate its distinctive forbidden-affair hook within three seconds; ordinary bed intimacy precedes dialogue whose crucial early words cannot be timed from the supplied fragment.
- Human review: approve
- Validation issues: None

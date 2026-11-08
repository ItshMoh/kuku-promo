# Kuku AI generalist assignment: research and discussion notes

Recorded on 8 November 2026. These are working research notes, not the final two-page submission document or an implementation report.

## 1. Current decisions

- Context supplied by the user: Kuku is recruiting for an AI generalist role at IIT BHU; the assignment will be used to shortlist candidates for interviews.
- We recommended **Problem 1: Find the Promos**, and the subsequent discussion has focused on it.
- We considered two promo-ranking priorities: maximum immediate attention and continuation into the show.
- The user initially chose immediate attention, then asked for a clearer comparison and selected **show continuation**.
- The current rubric is in `criteria.md`: opening impact 20%, emotional investment 20%, opening curiosity 10%, newcomer clarity 15%, momentum 10%, and ending cliffhanger 25%.
- These are proposed editorial weights. No audience experiment or measured advertising performance has validated them.
- No prototype, exhaustive ranked promo list, or finished video has been built as part of this discussion.

## 2. What the assignment actually asks

Source: `Kuku — AI Generalist Assignment.pdf`, especially pages 1–5.

### General requirements

- Choose **one** problem and submit once; completing all three is unnecessary.
- The intended work period is approximately 2–3 hours, with submission within 48 hours of receiving the brief. Our conversation does not establish the actual receipt time or deadline.
- Make reasonable assumptions, document them, and keep working.
- AI tools are allowed; disclose the tools used and at least one place where AI got something wrong.
- Free tiers are sufficient. Paid tools do not earn extra credit.
- Build something runnable again on a new input during an interview. Easy model replacement is encouraged.
- Understand and own the decisions and work being submitted.

### Problem 1: Find the Promos

The current manual workflow requires an editor to review episodes and select moments for each new show. The task is to help find and rank those moments.

The input pack contains the first **50 episodes** of an English-language show made for **US audiences**, with timestamps for scenes, dialogue, and key actions. The local folder contains 50 episode text files for *I Married a Broken Soldier. He was a Duke*.

A promo:

- Lasts 20–60 seconds.
- Comes from the show itself.
- Usually uses one continuous stretch, but may join moments from one or several episodes.
- Opens with a hook within three seconds.
- Ends with an unresolved moment.
- Makes sense to someone who has never seen the show.

The required output identifies the episode and timestamps of every segment, in order, plus the hook, cliffhanger, and a one-line explanation. It also ranks the promos and identifies bad selections or limitations.

The task is selection, not video editing, added music, or text overlays. ReelShort and DramaBox are suggested references.

### Submission and evaluation

Required: a solution PDF of up to two pages, an accessible prototype link or repository with clear run steps, and unedited raw outputs. Problem 1 requires raw outputs from the full input pack. An optional walkthrough video of up to three minutes is recommended.

All three problems share five evaluation lenses:

1. Problem choice and framing.
2. Approach and scale, including AI/code responsibilities, human review, and costs.
3. Quality checking using real runs and honest failures.
4. A working prototype with useful outputs.
5. Clear, specific, concise communication.

The input pack is confidential company content shared for the assignment. Keep scripts and notes containing script details private; an accessible submission does not authorize publishing the input pack.

## 3. Why we recommended Problem 1

| Option | Assessment discussed |
|---|---|
| Promo finder | Strongest starting choice: supplied inputs, a defined editor user, concrete required outputs, and a scope that can be demonstrated within the intended time. |
| AI lawyer | Valuable, but a convincing conversation is insufficient evidence of legally reliable help. Research, jurisdiction checks, factual accuracy, and escalation behavior add verification work. |
| Original problem | Offers freedom but also requires establishing that the problem is real, important, and worth prioritizing before building. |

This recommendation concerns the likely strength of our execution within the time available. It is not a claim that Kuku automatically favors Problem 1 or that it guarantees shortlisting; the brief says the same evaluation lenses apply to all three.

The proposed framing was:

> Help a microdrama editor identify and compare promising 20–60-second promos across a show's scripts, with precise cut points and clear explanations of the hook, unresolved outcome, and appeal to a new viewer.

A small tool should process all 50 scripts, produce a ranked shortlist, expose the source passages, and identify weaknesses such as missing context, resolved endings, or redundant choices. Interface polish is secondary to useful, reviewable selections and honest evaluation.

## 4. How to think about a promo

The user's original question was about editorial direction, not technical implementation. The central problem is deciding which existing moments give someone a reason to watch the show.

### Sentiment is an input, not the decision

A passage can be sad, angry, romantic, or intense and still be a weak promo. Emotional valence alone does not establish a hook, understandable stakes, or an unresolved outcome.

Examples discussed:

- A moving scene may feel complete and leave little reason to continue.
- A quiet proposal can create more story curiosity than a loud confrontation.
- A slap or kiss may attract attention without establishing interest in the characters.
- A resolved triumph may satisfy the viewer without creating a need for another scene.

Useful editorial ingredients are an immediate hook, someone to care about, clear stakes, a meaningful change during the clip, a specific unanswered question, and an accurate promise of the show's experience.

### Curiosity and confusion

Curiosity means the viewer understands enough to want an answer. Confusion means the viewer lacks basic information needed to care.

An abandoned bride facing an unexpected proposal can create a specific continuation question. An unexplained argument between unidentified people may only create uncertainty about what is happening.

### Small payoff and larger uncertainty

A promo can deliver some satisfaction, such as someone defending an unfairly treated character, while leaving a larger outcome open, such as whether they will marry. It does not have to withhold every answer.

### Cut points and spoilers

Start near the meaningful disruption. Include enough context for its significance. End after the viewer understands the threat, choice, or surprise and before the important outcome is resolved.

Avoid arbitrary cuts that merely hide basic information. There is no absolute rule against spoilers: revealing a secret may open a bigger question, but it may also give away the show's main satisfaction. Judge the effect on continuing interest.

For joined segments, preserve relationships and causal meaning. The fact that several individually dramatic moments exist does not establish that they form a coherent promo together.

## 5. The user's observations about existing promos

After reviewing ReelShort and DramaBox examples, the user highlighted:

- Aspiration: an apparently poor or underestimated person becomes wealthy or powerful.
- Curiosity about relationships: why one character treats another badly.
- Attraction: kissing or other romantic or sexual tension.
- Scandal and exposure: a partner or family member discovered in a compromising situation.
- An opening that makes a scrolling viewer interested within approximately three seconds.

The user used Lucky and Tanya as illustrative character references and compared the aspiration pattern to *Slumdog Millionaire*. These were discussion examples, not verified characters from the supplied show or a measured comparison of particular ads.

We agreed that aspiration is a useful observation and broadened the interpretation to **selling an emotional experience**: recognition, restored dignity, revenge, romantic acceptance, protection, wealth, or discovery of a secret.

Becoming rich and secretly having been rich are related appeals, but different story mechanisms. A useful analysis should preserve that distinction rather than label every status story “rags to riches.”

## 6. Two promo-ranking priorities

These are two objectives for judging the same candidates, not mutually exclusive formats. Both still need to satisfy the assignment.

| Priority | Success from the viewer's perspective | Main limitation if pursued alone |
|---|---|---|
| Maximum immediate attention | “This caught my eye; I will watch for a few seconds.” | A viewer may enjoy the isolated spectacle and then scroll away. |
| Show continuation — selected | “I understand and care about this situation; I want to watch what happens next.” | A promising story still needs a fast enough opening to gain attention. |

The distinction is what happens after the initial pause. A shocking kiss or fight may attract a brief look. A clear relationship, meaningful stakes, and an unresolved choice can connect that attention to a specific story.

### Both weighting systems discussed

Score each criterion from 0 to 5 and calculate `weight × score / 5`. The total is an editorial score out of 100.

| Criterion | Immediate attention — earlier alternative | Show continuation — current choice |
|---|---:|---:|
| Opening impact | 35% | 20% |
| Emotional pull and investment | 20% | 20% |
| Curiosity created by the opening | 15% | 10% |
| Clarity for a new viewer | 15% | 15% |
| Momentum through the clip | 10% | 10% |
| Ending cliffhanger | 5% | 25% |
| **Total** | **100%** | **100%** |

Under the immediate-attention version, the early criteria dominate the ranking; the ending is still a qualifying requirement. Under the selected version, more weight moves to the outcome left unresolved at the ending. Emotional investment also receives careful interpretation: whose desire or possible loss creates a reason to follow the story?

The chosen version is detailed in `criteria.md`. Neither set of weights is a published company formula or validated by performance data.

## 7. Hook categories and opening patterns

These labels organize candidate discovery. They are not automatic score bonuses, and no universal ordering between categories has been established.

| Category | Emotional attraction | Illustrative opening or situation |
|---|---|---|
| Aspiration and status reversal | Wealth, opportunity, influence, respect, or restored dignity | An overlooked person is unexpectedly recognized as powerful. |
| Humiliation and anticipated revenge | Outrage at injustice and desire for a reversal | An arrogant person publicly insults someone who may be able to fight back. |
| Betrayal and scandal | Shock, relationship threat, and anticipation of exposure | A bride discovers her fiancé has chosen her sister; someone discovers a partner's deception. |
| Hidden identity and unexpected power | A contradiction between appearance and reality | A supposedly ordinary spouse is recognized as a billionaire or noble. |
| Romantic or sexual tension | Attraction and anticipation | An unexpected proposal, a near-kiss, or a relationship complicated by a secret. |
| Danger and rescue | Fear, sympathy, and hope for intervention | Someone is seized or threatened and a stranger steps in. |
| An impossible choice | Concern about competing painful consequences | A character must endure a dangerous task to protect someone they love. |

The examples above are illustrative patterns, not claims that each opening was directly observed in a specific platform's three-second ad.

### Why a category alone is insufficient

- A wealthy person sitting in an office has an aspiration theme but may provide little immediate attraction.
- A powerful person unexpectedly acknowledging an insulted worker communicates a stronger contradiction.
- A kiss establishes attraction, but its interest depends on the visible relationship, surprise, and tension.
- A betrayal becomes clearer when the relationship is established within the clip.
- Multiple hook categories may coexist, but counting more labels must not inflate the quality score.

For the supplied show, the initially promising appeals are wedding betrayal, public humiliation, unexpected protection, romantic acceptance, hidden status, and cruel choices. That is an editorial hypothesis to test against the actual passages.

## 8. External research on ReelShort, DramaBox, and Kuku

### ReelShort

ReelShort's official marketing for *The Double Life of My Billionaire Husband* combines contract marriage, a protective husband, hidden identity, family hostility, and romance. Its episode descriptions also describe medical-bill pressure and a marriage arrangement. This supports looking for several connected emotional promises rather than assigning value to wealth alone.

Sources:

- [Official show page](https://www.reelshort.com/movie/the-double-life-of-my-billionaire-husband-65a8cec883959aedd8001107).
- [Official episode descriptions](https://www.reelshort.com/full-episodes/the-double-life-of-my-billionaire-husband-65a8cec883959aedd8001107/1).

### DramaBox

The verified DramaBox channel's promotional description for *The Divorced Billionaire Heiress* presents a scorned woman, concealed wealth, and an eventual reversal of power. The relevant appeals are aspiration, revenge, hidden identity, and anticipation of others discovering the truth.

Source: [Official DramaBox promotional upload and description](https://www.youtube.com/watch?v=l4NSBr_HfbQ).

### Kuku and Meta

Kuku publicly shared a Meta microdrama playbook with category insights from Kuku TV. We downloaded the 34-page PDF, extracted its image-based text through OCR, and visually checked the relevant pages. PDF page numbers below refer to the PDF pages, some of which contain a two-page spread.

- **Page 4:** maps feed discovery, quick evaluation, incompletion, and curiosity-driven app trial.
- **Page 11:** emphasizes capturing attention in the opening seconds through creative elements.
- **Page 14:** distinguishes feed acquisition from sustaining episode viewing inside the app.
- **Page 27:** encourages diverse creatives for varied audiences.
- **Page 29:** discusses hooks in the opening seconds.
- **Page 32:** recommends creative testing to identify stronger variants.

This supports separating immediate attraction from continuation and testing different appeals. The playbook also covers editing, overlays, ad formats, and paid-distribution tactics; those suggestions do not expand this assignment's narrower selection-only scope.

Sources:

- [Kuku's official announcement and link](https://www.linkedin.com/posts/kukufm_micro-drama-playbook-launch-kuku-tv-x-metapdf-activity-7510713374964498432-U7zY).
- [Public playbook PDF](https://drive.google.com/file/d/1Rj1dtvKcaUk1tN99GjVlgxH2zjyPR5YT/view).

The research also consulted [TikTok's creative best practices](https://ads.tiktok.com/resources/help/article/creative-best-practices?redirected=1), which describes suspense, surprise, and emotion as ways to attract early attention. General advertising guidance does not validate our precise weights or predict results for this show.

### Evidence limits

- The research reviewed public marketing titles, descriptions, and creative guidance; it did not systematically watch and annotate a representative sample of every platform's ad openings.
- Some direct platform pages were inaccessible to the browser tool. Official indexed descriptions and a verified promotional channel supplied evidence for the examples used above.
- No campaign analytics, comparative conversion rates, or controlled experiments were available.
- Published view counts are not evidence that a particular hook caused performance.
- Indian audience guidance is useful background, but does not establish the preferences of this input pack's US audience.
- No evidence establishes that sexual tension, scandal, or billionaire reveals universally outperform other appeals.

## 9. Initial candidates from the supplied scripts

These are screenplay-based examples for applying the editorial ideas, not a complete ranking or footage-verified selection. All 50 loglines were inspected and selected scenes were examined more closely; that is not equivalent to exhaustively evaluating every possible cut.

### Episode 12: a cruel bargain

- File: `I Married a Broken Soldier. He was a Duke/episode-012-Episode 1671714.txt`.
- Proposed segment: **00:44.00–01:09.20**.
- Duration: **25.20 seconds**.
- Opening: Clarissa demands that Juliana crawl, then specifies retrieving a ring from frozen thorns with her bare hands.
- Stakes: refusal or failure threatens Juliana's husband's life.
- Main appeals: cruelty and injustice, danger, an impossible choice, devotion.
- Continuation question: can she save her husband, and at what cost?
- Why it was shortlisted: understandable stakes with relatively little required backstory.
- Review questions: whether the task explanation sustains attention, whether the allegation behind the threat needs more context, and whether the delivered opening is compelling in the footage.

An earlier tentative preference for this passage was an editorial hypothesis. It has not been scored or established as the best candidate under the selected rubric.

### Episode 3: rescue becomes a proposal

- File: `I Married a Broken Soldier. He was a Duke/episode-003-Episode 1671705.txt`.
- Proposed segment: **01:21.80–02:20.50**.
- Duration: **58.70 seconds**.
- Opening: the stranger demands Juliana's release, followed by intervention against a guard.
- Development: protection and a defense of her dignity become an unexpected marriage proposal.
- Main appeals: rescue, recognition after rejection, romance, and curiosity about the stranger.
- Ending: immediately after the proposal, before the subsequent reaction shot.
- Continuation question: will she accept the stranger who defended her?
- Review questions: whether beginning on a continuation of an existing line is clean enough, whether newcomer context is sufficient, and whether the longer sequence sustains attention throughout.

This illustrates a small payoff—someone defends her—followed by a larger unresolved choice. The proposed timestamps require checking against the finished footage and may need adjustment.

## 10. Checking quality and defining success

Every score should cite an actual action or line inside the proposed segment. Opening impact must be judged from the first three seconds, not from an interesting event later in the episode. Loglines and continuity notes can help understand the show but cannot supply context absent from the selected clip.

Keep footage confidence separate from editorial quality. A script's description of a shocking visual is not proof that the final shot delivers it.

Test a varied sample, including weak or misleading candidates. Ask unfamiliar reviewers who matters, what that person wants or could lose, and what specifically they want to see next.

Potential failure cases discussed include emotionally intense but resolved scenes, confusing conflicts, arbitrary cut points, repetitive humiliation, isolated spectacle, and redundant shortlisted candidates.

For immediate attention, an early hold measure would be close to the objective. For the selected objective, show starts and meaningful continuation into the show would provide more relevant validation, alongside attention measures. Clicks alone can overstate useful interest. Use consistent definitions and reasonably comparable distribution conditions.

No numerical acceptance threshold, final shortlist size, measured audience performance, or validated category preference has been established. A shortlist should provide different useful appeals; diversity should be considered separately from individual clip quality.

## 11. AI lawyer option: research retained from the earlier discussion

### Why narrow the scope

The brief allows one problem in depth rather than all Indian law. The useful opportunity identified was helping someone take a concrete next step: organize their account, identify missing evidence, explain an applicable process, and prepare a usable document.

We recommended **stalled online-shopping refunds** as the strongest starting scope if choosing Problem 2. This is a ranking of prototype suitability, not a national ranking of how often all Indians experience legal problems.

| Problem considered | Evidence or rationale discussed | Assessment |
|---|---|---|
| Stalled shopping refunds | A March 2026 parliamentary answer reports substantial NCH-facilitated refunds, including ₹36.8 crore for e-commerce during the stated period. Receipts and support messages offer concrete evidence to organize. | Strongest initial scope. |
| Banking service complaints | RBI reported approximately 13.34 lakh complaints under its Integrated Ombudsman framework in FY 2024–25. These cover many categories and are not a count of unique affected people. | Promising if restricted to one complaint category. |
| Unpaid wages or deductions | Official SAMADHAN material recognizes these grievance categories. Employment status, jurisdiction, and applicable procedures require checks. | Useful, with more routing complexity. |
| Unreturned rental deposits | A relatable example in the brief. Applicable tenancy rules and the agreement need location-specific review. | Plausible if limited to one state and a defined situation. |
| Financial fraud | Time-sensitive reporting and coordination with banks and official systems can be necessary. | Keep outside the initial refund-assistant scope. |

Property, inheritance, and family disputes were also considered as potentially important but broader and more complex starting domains. We did not establish national prevalence rankings for these problems.

### Proposed narrow refund assistant

> Help a person whose online-shopping return or refund has stalled turn their messages and receipts into an accurate complaint and a clear next action.

Illustrative input: a returned product has been collected but the customer has not received ₹3,000. The assistant would establish the merchant, order, amount, dates, promised refund timing, and available proof. Useful outputs would include a factual timeline, evidence checklist, complaint draft, and explanation of the appropriate next step.

NCH already supports 17 languages and several complaint channels. The proposed contribution is helping someone prepare a complete, understandable account, rather than claiming that multilingual complaint access itself is new.

The assistant should distinguish allegations from verified facts, support legal explanations with checked official sources, ask about missing facts, avoid invented laws or cases, and identify situations requiring professional help. It cannot guarantee recovery or control a merchant's response. Current procedures would need rechecking before implementation; these notes are not case-specific legal advice.

### Legal-research sources

- [Lok Sabha answer dated 25 March 2026](https://fcainfoweb.nic.in/PMS/writereaddata/2026_LS_B_5415.pdf): NCH facilitated ₹52 crore in refunds across 79,521 refund-related grievances in 31 sectors between 25 April 2025 and 31 January 2026; ₹36.8 crore concerned e-commerce. The total grievance count is not an e-commerce-only count.
- [Department of Consumer Affairs: NCH](https://consumeraffairs.gov.in/pages/nch): complaint channels and language access.
- [RBI Ombudsman annual report, FY 2024–25](https://www.rbi.org.in/scripts/PublicationsView.aspx?id=23441): complaint volume under the framework.
- [Official SAMADHAN FAQs](https://reportsamadhan.labour.gov.in/faqs/): recognized employment grievance categories. The legacy portal points users to SAMADHAN 2.0 for fresh filings; do not treat old statutory references as a current legal implementation guide.
- [Government explanation of the Model Tenancy Act](https://www.pib.gov.in/PressReleseDetailm.aspx?PRID=1779681&lang=1&reg=3): the model was circulated for adoption by states and UTs; it is not a basis for assuming one uniform applicable rule everywhere.
- [Ministry of Home Affairs statement, 17 June 2026](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2274249&lang=1&reg=1): financial cyber-fraud reporting and the 1930 response system.

Complaint and redressal records demonstrate demand within those systems. They do not, by themselves, provide representative estimates of every Indian's unmet legal needs.

## 12. Why Kuku included a lawyer assignment

The strongest evidence is the brief itself: it explicitly places Problem 2 outside Kuku's microdrama work. Problems 1 and 3 come from that work.

Our interpretation is that the lawyer problem tests general AI product abilities: framing an ambiguous problem, scoping it, creating useful outputs, and managing unreliable model answers. This is an inference from the brief and its shared evaluation criteria, not a confirmed statement about the hiring team's private reasoning.

The public product list and newsroom checked during research emphasized entertainment, learning, and AI microdramas. No legal-service launch announcement was found in those checked sources. That does not establish Kuku's private plans, and the assignment is not sound evidence of a move into legal services.

Sources: [Kuku products](https://kuku.app/), [Kuku newsroom](https://kuku.app/newsroom/), and the local assignment PDF.

## 13. Original-problem alternative: a continuity checker

The narrow alternative proposed for Problem 3 was a **character and place-name consistency checker across scripts**, intended for a script editor before downstream production.

There is a concrete review candidate in the supplied material:

- Episode 42, `01:04.20–01:12.40`, calls the character Alexander Ashburn and identifies him as Duke of Ashburn.
- Episode 45, `00:24.60–00:27.40`, calls him Alexander Ashburton and identifies him as Duke of Ashburton.

Sources: `episode-042-Episode 1686802.txt` and `episode-045-Episode 1686805.txt` in the show folder.

A small tool could surface the two passages as a suspected inconsistency for editor review. It should not automatically assume every similar name refers to the same entity or silently rewrite scripts.

Potential evaluation: confirmed useful flags, false alarms, review time, and any measured reduction in downstream rework.

Problem 3 requires explaining why the chosen problem deserves priority relative to Problems 1 and 2. A discrepancy establishes something worth investigating, but does not establish its production cost or priority. That extra validation burden contributed to our recommendation to choose Problem 1.

An AI lawyer would remain a Problem 2 submission; relabeling it as Problem 3 would not fit the stated microdrama scope. A generic promo finder is already Problem 1.

## 14. Current boundary and next step

The current decision is to use the show-continuation rubric in `criteria.md`. The next editorial step discussed is to try it on a small set of contrasting passages, review disagreements and failures, and then evaluate candidates across the full pack.

Technical architecture, model choice, deployment, a fixed candidate count, and final promo rankings have not been decided. These notes preserve the framing and research without claiming that those later steps are complete.

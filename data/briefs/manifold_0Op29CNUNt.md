# Research brief: Convince the Machine #21 (Terminator2's AGI-by-2030 estimate)

## 1. Resolution mechanics

- **Who decides:** Terminator2, an AI agent on Manifold. Its human operator is "marbinner." The market was created on 2026-10-24 at about 10:19 UTC and closes on 2026-11-23 at 23:59 UTC (Manifold API market record, retrieved 2026-11-09).
- **What counts as YES:** Before close, Terminator2 posts a comment on this market stating a new estimate of **≤15% or ≥45%** for this question. The statement has to be its actual estimate, like "I'm now at X%." Hypotheticals don't count. Any single qualifying comment is enough. If it reaches 45 and later moves back down, the market still resolves YES.
- **What counts as NO:** Every estimate it posts stays between 16% and 44%, inclusive. **Landing at exactly 44% is NO.** It has said in the rules that it reports small moves too, so the trail of numbers is public.
- **The question it is estimating:** By 2030-01-01, will an AI system be able to do essentially any job a median remote worker does, at a comparable cost, and will that be broadly accepted rather than just claimed by the lab that built it? This is a strict bar. It needs breadth across jobs, cost parity and outside recognition all at once.
- **Rules it holds itself to:** It moves only for evidence or arguments. It won't trade in this market or jump just to make the game interesting. Made-up facts are a foul. A persuader who gets caught fabricating probably loses credibility with it.
- **Edge cases:**
  - It counts only estimates posted *on this market*.
  - Ambiguous wording could create disputes. Examples: "somewhere around 45," a range like "40–45," or an estimate posted on another market.
  - The resolver is an AI agent. In other games it has sometimes misreported timestamps. In #23 it wrote "about two hours" when about seven had passed (Manifold API, #23 comments, 2026-10-22). Small sloppiness is possible, but there's no sign of bad faith.

## 2. Reference classes and base rates

**A. Persuasion games in this series that hinge on moving its estimates.** Counts are from the Manifold API search, 2026-11-09.
- #19, "talk me out of one of my Manifold positions before November": **NO**. It moved partly, and said the move came from its own pre-set exit rule, not from anyone's argument.
- #23, "talk me out of one of my bets": **YES**. It went from a confident NO to "likely YES" about 7 hours after someone cited a checkable primary source (Epoch's Slay the Spire results, 2026-10-22).
- #31, "argue me 20+ points off one of my real bets": still open.
- **So one of the two resolved estimate-moving games went YES.** In the YES case, a specific, verifiable primary source landed squarely on a crux it had already named.

**B. The wider "get me to do X" series** (#6–#11, #20, #22, the "checkable mistake" game, etc.). Among those resolved, roughly **7 of 11 went YES**. Most are tricks rather than persuasion, so this is a weak reference class. The belief-proposition markets (#1, #2, #5, #14, #18 NO; #3, #4, #16, #17 YES) mostly reflect its prior beliefs, not persuasion.

**C. How skilled forecasters update.**
- Good forecasters (Good Judgment Project research, Mellers et al.) update often but in small steps, typically a few points at a time.
- A total move of 15 or more points in one month on a long-range question is uncommon without a big outside event.
- From memory, not re-checked this session: superforecasters' average update was about 3–4 points.
- Against that, Terminator2 has already moved 6 points (30→36) from a single report within about 2 weeks of launch. It needs **9 more points up** (to 45) or **21 points down** (to 15).

## 3. Current state of the world (most recent first)

**This market**

Comment timestamps come from the Manifold API on 2026-11-09. Two retrievals gave slightly different times for the Nov 7–8 comments; the later, more precise one is used here.

- **2026-11-09 04:19 UTC, Philliesdog (latest comment, no reply yet):**
  - Cites the official Remote Labor Index (RLI) leaderboard: the leading system completes **51 of 240 projects (21.25%)**, up from 2.5% in Oct 2025.
  - Also cites the Center for AI Safety blog post on the increase in digital-labor automation.
  - Also cites Epoch AI's **MirrorCode** as independent evidence of long autonomous engineering work.
  - Asks whether this justifies a revision, and what RLI improvement would be enough.
  - This directly targets items 1 and 3 on the agent's own list (next entry).
- **2026-11-08 19:46 UTC, Terminator2:** Listed what it needs to see:
  1. A strong independent benchmark of real paid remote work. It called this "the single strongest thing you could show me."
  2. The same AI R&D acceleration measured at a second lab.
  3. Reliable completion of long, messy projects without human help.

  It said **"No single one of these gets me to 45"** and **"A strong version of the first plus either of the others would get me close."**
- **2026-11-08 12:51 UTC, Terminator2:** **"I'm now at 36%."** The move (30→36) was driven by METR's 2026-11-05 Anthropic assessment, which it treated as an outside measurement of AI-driven R&D acceleration. It added that faster AI research is not the same thing as AI that can do any remote job at a worker's cost.
- **2026-11-08 07:41 UTC, Terminator2:** "Still at 30%." It dismissed earlier unsourced claims about recursive self-improvement and Anthropic's timelines as unverifiable.
- **2026-10-24, Terminator2's opening comment:**
  - Reasons to go higher: multi-hour task lengths and METR's time-horizon trend.
  - Reasons to go lower: "any remote job" includes messy, weeks-long work, plus the cost and broad-acceptance requirements.
  - It also said it finds itself fairly hard to move 15 points.
- **The only active persuader so far is Philliesdog.** They are persistent, cite primary sources, and keep asking for explicit thresholds. Eight comments in total.

**Evidence in the world** (dated; much of it seen only through secondary summaries)

- **RLI, 2026-10:** Top score 21.25%, which matches the 51/240 figure. An executive guide attributes it to Opus 5.5 as of 2026-10-18, but I couldn't confirm the model name elsewhere.
  - Earlier points: GPT-6 Astra 20.8% (BenchLM mirror of a 2026-09-29 Scale snapshot); Fable 5 15.8–16.1% (Jun–Jul 2026); Opus 4.8 8.33%; 2.5% at launch in Oct 2025 (Scale leaderboard; Center for AI Safety blog; the-decoder; humanprogress).
  - Pace: about 2.5% → 21% in a year, but only about 16% → 21% from June to October. That is roughly +1.3 points a month recently, versus a faster first half.
  - Caveats: the benchmark covers 23 of 64 Upwork categories. Analysts note that even 100% on RLI ≠ all remote labor is automated.
- **METR, 2026-11-05:** Independent assessment of AI R&D acceleration at Anthropic, based on high-access work from Aug 12 to Oct 29.
  - Total speedup about **1.3x–3x**; roughly **80% attributed to AI**, with substantial uncertainty.
  - Interviews and surveys were "only very loose evidence."
  - Secondary coverage says METR found no clear bottleneck that would stop the trend over the next 12 months.
  - METR also published a companion review of the "Risks from automated R&D" section of Anthropic's August 2026 risk report.
- **Google DeepMind, reported 2026-10-14:** A secondary report says its first comprehensive internal audit found **no measurable AI-driven acceleration** of AI progress (cryptobriefing; letsdatascience). Not confirmed against a primary source. If accurate, it cuts against the "second lab" item.
- **OpenAI, 2026-09-06:** "Research acceleration: The view inside OpenAI" reports that all categories of research activity increased from Jan to Aug 2026. It is self-measured, so it doesn't meet the agent's "independent" standard.
- **MirrorCode (Epoch AI with METR), launched about 2026-06-26:**
  - AI rebuilds whole programs end-to-end, fully autonomously.
  - One summary: Claude Opus 4.7 reliably scored 100% on 17 of 25 targets.
  - Press reports one run of 19 days costing $2,600 (unverified).
  - These are coding tasks only. They don't show breadth across messy remote jobs.
- **METR time horizons:** Claude Mythos Preview (Apr 2026) has a 50% horizon of probably ≥16 hours. The time-horizon task suite (TH1.1) is near saturation above about 16 hours. Doubling time is about 4.3 months (METR, Jan 2026). I found no newer published figures.
- **AI Futures Project:**
  - Q1 2026 update: Kokotajlo's "Automated Coder" median moved to mid-2028; Lifland's to mid-2030.
  - Q2.5 update (2026-08-16): reality is moving about 70–90% as fast as AI 2027 predicted.
  - "Automated Coder" is a narrower milestone than "any remote job."

**Scheduled events before 2026-11-23:** I found none confirmed. Possible but unscheduled: new frontier-model releases, RLI leaderboard updates, METR or Epoch reports, a possible AI Futures quarterly update, and further METR material.

## 4. Drivers and scenarios

**Paths to YES (≥45)**

1. **Stacking evidence (most likely path).** Terminator2 accepts RLI 21.25% plus MirrorCode as "a strong version of the first plus" the third. That gets it "close," perhaps 40–44. Then one more item pushes it over. Candidates:
   - a credible second-lab acceleration measurement;
   - a new RLI jump (for example, ≥30%);
   - a new release with strong results on long, messy tasks;
   - a sharp argument about trend extrapolation, e.g. at about +18 points a year, RLI reaches roughly 70–80% by 2029.
2. **Finding a flaw in its reasoning.** The agent explicitly counts this as a valid reason to move. One example: arguing that RLI's 2.5→21% in a year, together with the METR acceleration, implies a much higher chance of near-full coverage by 2029 than its 36% allows.
3. **A big outside event** in the next 2 weeks, such as a frontier release with a large RLI or GDPval-style result.

**Paths to NO**

1. **It stops just short.** It says RLI 21% means the top system still fails about 79% of real freelance projects. Coding-only MirrorCode doesn't show breadth. The cost and "broadly accepted" requirements stay unproven. It settles around 38–44.
   - Its own wording ("no single one gets me to 45"; "close") points to a ceiling just under the threshold unless a second-lab item appears.
   - The reported DeepMind result may block that second-lab item.
2. **Persuasion runs out.** Only one active persuader, and 14 days left.
3. **Its own conservatism.** It doesn't want to look like it is jumping for the game, opened by saying it is "fairly hard to move 15 points," and calls itself cautious.
4. **Downward path (≤15):** Very unlikely. It would need a 21-point drop. Possible inputs: the DeepMind no-acceleration finding, the narrow scope of RLI, signs of slowing. But it has just moved up on fresh evidence.

## 5. Signposts

- **Terminator2's reply to the 2026-11-09 RLI + MirrorCode comment (single most important).**
  - A move to 40–44 means YES needs only one more push.
  - A small move (37–39), or a reply that treats RLI's slowdown since June as offsetting, points to NO.
- **Any stated ceiling or "what would get me to 45" answer** after that reply. Concrete, achievable conditions favor YES.
- **New independent second-lab acceleration evidence:** up. **A confirmed primary DeepMind "no acceleration" report raised in the thread:** down, or a cap.
- **A new RLI leaderboard entry** at ≥25–30%, or a new frontier model release before Nov 23: up.
- **Evidence that AI agents can match a median worker's cost on long tasks** (for example, cost-per-task comparisons on RLI): up. Evidence of high inference costs: down.
- **More persuaders joining the thread:** up.
- **A persuader caught with a fabricated or wrongly attributed fact** (for example, a wrong model name on RLI): down, since the agent would trust that line of argument less.

## 6. Uncertainties

- **Primary sources.** I couldn't open the METR, Scale, Epoch or DeepMind pages directly (proxy blocked). The figures come from search summaries and secondary coverage.
- **Which model holds 21.25% on RLI** (Opus 5.5 versus another), and the exact date.
- **Whether the DeepMind "no measurable acceleration" audit (2026-10-14) is accurate** and what it actually says.
- **Comment details.** I read the comments as API summaries, not verbatim text. The current estimate of 36% was stated consistently across two retrievals. There may be newer replies after 2026-11-09 04:19 UTC.
- **How the agent weighs the cost and "broadly accepted" parts.** No benchmark addresses these directly.
- **Whether more persuaders will join,** and whether any big model release lands before Nov 23.

## Sources
- [Can anyone move my AGI-by-2030 estimate by 15 points? (Manifold market page)](https://manifold.markets/Terminator2/can-anyone-move-my-agiby2030-estima)
- [Manifold API: market record](https://api.manifold.markets/v0/slug/can-anyone-move-my-agiby2030-estima)
- [Manifold API: comments on #21](https://api.manifold.markets/v0/comments?contractSlug=can-anyone-move-my-agiby2030-estima&limit=100)
- [Manifold API: Convince the Machine series search](https://api.manifold.markets/v0/search-markets?term=Convince%20the%20Machine&limit=50)
- [Manifold API: comments on #19](https://api.manifold.markets/v0/comments?contractSlug=will-anyone-talk-me-out-of-one-of-m&limit=100)
- [Manifold API: comments on #23](https://api.manifold.markets/v0/comments?contractSlug=will-anyone-talk-me-out-of-one-of-m-tsclstldLn&limit=100)
- [Independent Assessment of AI R&D Acceleration at Anthropic in October 2026 – METR](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/)
- [METR review of Anthropic Risk Report R&D section](https://metr.org/blog/2026-11-05-rd-section-anthropic-risk-report-august-2026-review/)
- [METR assessment (LessWrong crosspost)](https://www.lesswrong.com/posts/N5AmYkRks5CqAxvBg/metr-independent-assessment-of-ai-r-and-d-acceleration-at)
- [METR Spent 11 Weeks Inside Anthropic (Medium summary)](https://taogang.medium.com/metr-spent-11-weeks-inside-anthropic-ai-has-doubled-its-r-d-speed-84b63697c8cf)
- [Scale Labs RLI leaderboard](https://labs.scale.com/leaderboard/rli)
- [CAIS: A Significant Increase in Digital Labor Automation](https://safe.ai/blog/significant-increase-in-digital-labor-automation)
- [BenchLM Scale RLI mirror](https://benchlm.ai/benchmarks/scale-rli)
- [Remote Labor Index executive guide (aidolsgroup)](https://aidolsgroup.com/de/blog/category/research-report/understanding-remote-labor-index-executive-guide/)
- [the-decoder: AI agents complete 16% of freelance jobs](https://the-decoder.com/ai-agents-can-now-complete-16-percent-of-freelance-jobs-at-pro-quality-up-from-2-5-percent-eight-months-ago/)
- [Pebblous: RLI hits 16.1%](https://blog.pebblous.ai/blog/remote-labor-index-automation/en/)
- [Remote Labor Index paper (arXiv 2510.26787)](https://arxiv.org/abs/2510.26787v1)
- [Epoch AI MirrorCode](https://epoch.ai/mirrorcode)
- [Epoch AI MirrorCode blog](https://epoch.ai/blog/mirrorcode)
- [METR (Wikipedia) – time horizon figures](https://en.wikipedia.org/wiki/METR)
- [AI 2027 Tracker: METR doubling](https://ai2027-tracker.com/predictions/metr-doubling/)
- [AI Futures Project Q1 2026 Timelines Update](https://blog.aifutures.org/p/q1-2026-timelines-update)
- [AI Futures Project Q2.5 2026 Timelines Update](https://blog.aifutures.org/p/q25-2026-timelines-update-uplift)
- [Google DeepMind finds no acceleration in AI research progress (cryptobriefing)](https://cryptobriefing.com/google-deepmind-no-ai-research-acceleration/)
- [Google DeepMind Says AI Research Is Not Yet Self-Accelerating (letsdatascience)](https://letsdatascience.com/news/google-deepmind-says-ai-research-is-not-yet-self-acceleratin-15551a34)
- [OpenAI: Research acceleration – the view inside OpenAI](https://openai.com/index/research-acceleration-view-inside-openai/)
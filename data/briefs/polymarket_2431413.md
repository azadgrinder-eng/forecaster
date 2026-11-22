# Research brief: Will Anthropic have the #1 model on the LMArena text leaderboard (style control off) on Dec 31, 2026, 12:00 PM ET?

**Source caveat:** I could not open any page directly. Every fetch, including arena.ai, was refused by the network proxy, so everything below comes from search-result snippets. Many of them are third-party aggregators that disagree with each other. Treat individual scores as approximate, give ±3–5 points of slack, and have someone check the live board.

## 1. Resolution mechanics

- **What counts as YES:** a model owned by Anthropic sits at #1 on lmarena.ai/leaderboard/text with style control turned off, checked on Dec 31, 2026 at 12:00 PM ET (17:00 UTC). That is about 39 days from today.
- **Tie-breaks:** rank decides first. If ranks are tied, the higher Arena score wins, using unrounded values. If scores are still tied, the company name that comes first alphabetically wins, which puts "Anthropic" ahead of "Google".
- **The default view is not the resolution view.** Style control has been the default on the text arena since May 16, 2025 (lmarena-ai leaderboard-dataset card, 2025). The market uses the non-default view, which arena.ai publishes as /leaderboard/text/overall-no-style-control. Many news reports and aggregators quote the default view, so make sure any number you use is from the style-off view.
- **Edge cases:**
  - Arena's "Rank" uses confidence intervals, so several models can share rank 1. In that case the higher raw score wins.
  - Preliminary models, i.e. new entries with few votes and wide CIs (Gemini 4 Carbon was still flagged preliminary as of ~Nov 9), appear to count if they are shown on the table.
  - Models with limited availability can also appear. Gemini 4 Carbon was reportedly limited to partners and cyber defenders at announcement.
  - Lmarena.ai now redirects to arena.ai. The "Leaderboard tab" wording may not match the current site layout, which could matter if the style-off view moves or is renamed.
  - If the site is down at check time, the market stays open until the first check after it comes back.
  - "Company that owns the model": Meta's Muse models count as Meta.

## 2. Reference classes and base rates

**A. Who held #1 on the style-off board at month-end, 2023–2026 (rough count from my knowledge plus the snippets).**
- 2023 to mid-2024: OpenAI held #1 nearly every month. Claude 3 Opus was #1 or tied briefly around March–April 2024.
- Late 2024 to 2025: mostly Google (Gemini Exp, then 2.5 Pro, then Gemini 3 Pro from November 2025), with OpenAI in spells.
- 2026: Anthropic led at times. Opus 4.6 around February 2026, and Claude Fable 5 reportedly around August. Opus 5.5 led the style-off view on Sep 25 at 1518 (versusapp, Sep 2026). Google's Gemini 4 Argon then led style-off on Oct 8 at 1534 vs Opus 5.5 at 1515 (arena.ai overall-no-style-control, Oct 8 2026), and again on Oct 20 at 1532 (versusapps, Oct 2026).
- **Rough base rate: Anthropic held #1 in about 10–15% of month-ends since 2023, and maybe 30–40% in 2026.**

**B. Does the current leader survive ~6 weeks?** When a lab led by more than 10 points on the style-off board, it usually still led 5–6 weeks later. The exceptions were a rival flagship launching inside the window. Frontier labs have each been releasing about every 1–3 months in 2026, so the chance that some lab ships a new top model in any given 6-week window is substantial, perhaps 30–50%.

**C. Effect of style control on Claude.** Since the feature was introduced in 2024, Claude has historically ranked better with style control on than off. Lengthy, heavily formatted answers are rewarded when style control is off, and Gemini and GPT benefited. Recent data:
- Opus 5.5 scored 1509 with style control on and 1518 with it off (Sep 25).
- Meta's Muse Wonder was #2 in the default view but #6 with style control off (Oct 20).

Overall, the style-off view does not clearly favour Anthropic and has recently favoured Google.

## 3. Current state of the world (most recent first)

- **~Nov 18–20, 2026 (default view):**
  - Gemini 4 Carbon (High) is #1 at 1526–1528.
  - Gemini 4 Argon (High) is about 1520–1522.
  - Muse Wonder (Max, Meta) is 1511.
  - Claude Opus 5.5 (High) is 1507–1509, around #3–#4.
  - Claude Fable 5.2 (Max) is 1503, tied for #7.
  - Sources: arena.ai model-page snippets, Nov 18; BenchLeader, Nov 2026; Developers Digest, Nov 2026.
  - A social post noted that Google held the top 3 spots: Carbon, Argon and Neon (X @hqmank, Nov 2026).
  - Outlier aggregators claim "Claude Mythos 5" is #1 at 1531 (swfte) or Opus 4.6 at 1497 (tokenando). Both look unreliable or stale. Mythos is reportedly not on the public board (airanks.app).
- **Style-off view in November:** I found no figures. The last style-off data point I have is Argon leading on Oct 20. If Carbon is about 5 points above Argon in the default view, Google very likely leads style-off as well.
- **Nov 13:** Instruction-following category: Gemini 4 Argon 1528, Carbon 1525 (BenchLeader).
- **Nov 9, 2026:**
  - Anthropic released Claude Fable 5.2 to the public, with Mythos 5.2 limited to approved organisations (tessgroup; airanks).
  - Fable 5.2 is #1 on Arena's Agent Index at 1448, 112 points ahead of Opus 5.5 (fourweekmba), and #1 in Creative Writing at 1529 (arena.ai).
  - Overall text default view: only 1503.
  - Gemini 4 Carbon was #1 on text at 1526 ±10, flagged preliminary (infosdivers).
- **~Nov 10:** Gemini 4 Carbon was reportedly released, after being announced Oct 28 with limited access (projedefteri; Kanerika). Its general availability is disputed.
- **Oct 26:** OpenAI released GPT-6.1 Terra (Design Arena). The GPT-6 line (Astra Sep 3, Sol Sep 22) does not appear near the top of the text board.
- **Oct 13:** Gemini 4 Argon reached broad release (Kanerika).
- **Sep 22:** Claude Opus 5.5 was released. It debuted #1 on text at 1509 ±12, and Anthropic reportedly held the top six spots (cryptobriefing; KuCoin).

**Scheduled or rumoured before Dec 31 (unconfirmed; one release-cadence estimate page):**
- Claude Opus 5.6, ~Dec 21
- GPT-6.1 Astra and GPT-6.2 Sol, ~Dec 10
- Gemini 4 Flash, ~Dec 10
- Grok 4.8, ~Dec 10

Other points:
- Grok 5 looks unlikely to ship by year-end (geotoolbox).
- Anthropic has not announced an Opus 6. Mythos-class general availability is speculated for "late 2026" but not confirmed.
- Gemini 4 Argon's price rises Dec 1. This doesn't affect the arena directly.

## 4. Drivers and scenarios

**Paths to YES:**
1. **Anthropic ships a new flagship between ~Dec 1 and 20** (Opus 5.6, Fable 5.3, or a public Mythos/Fable 6) that beats Gemini 4 Carbon on the style-off board by enough to hold #1. That means roughly 1530+ in style-off terms. Anthropic's release cadence in 2026 makes a December launch plausible but not confirmed. Holiday timing makes Dec 21–31 launches less likely, and a model launched very late may not be scored in time.
2. **Gemini 4 Carbon's preliminary score drops** as votes accumulate, or Carbon is withdrawn. Even then, Argon led Opus 5.5 by about 19 points style-off in October, so this path alone probably isn't enough.
3. **Arena changes its methodology or the style-off view** (e.g. drops the view or re-baselines scores) in a way that favours Claude. Low probability.

**Paths to NO:**
1. **Status quo.** Google's Carbon or Argon stays #1. This is the dominant path.
2. **Another lab takes #1 in December**, e.g. an OpenAI GPT-6.x release or a Meta Muse model.
3. **Anthropic launches something that ranks #1 in the default view but not style-off**, given Claude's historical style-control advantage.

## 5. Signposts

- **Strongly toward YES:**
  - An official Anthropic flagship launch before ~Dec 15, plus Arena confirming that it debuts #1 on the text board. Check the style-off view specifically.
  - The current style-off board showing an Anthropic model within about 5 points of #1.
- **Toward YES:** Carbon's preliminary rating falling below about 1515.
- **Toward NO:**
  - A live check showing Google ≥15 points ahead in the style-off view.
  - No Anthropic release by mid-December.
  - A new Google or OpenAI model in December.
- **Most valuable single check:** the current arena.ai/leaderboard/text/overall-no-style-control top 10, with scores and CIs.

## 6. Uncertainties

- **Current style-off standings:** no November data point. This is the biggest gap.
- **Reliability of scores:** they come from aggregators with conflicting numbers (Carbon 1526 vs 1528; contradictory outliers).
- **Gemini 4 Carbon:** whether it is generally available, whether it will lose its preliminary flag, and where its score settles.
- **Anthropic's December plans:** the Opus 5.6 date is a model-based guess, not an announcement.
- **Leaderboard structure:** whether arena.ai's layout or naming changes before Dec 31 could complicate resolution.
- **Unannounced launches:** whether OpenAI, Meta or xAI release something that jumps to #1.

## Sources
- [LMArena Text Leaderboard (Nov 2026) – BenchLeader](https://www.benchleader.com/benchmarks/lmarena_text)
- [LMArena Leaderboard (November 2026) – Developers Digest](https://www.developersdigest.tech/benchmarks/lmarena)
- [LMArena (Now Arena): Leaderboard and How It Works – infosdivers](https://infosdivers.com/en/lmarena/)
- [Arena Text: overall, no style control](https://arena.ai/leaderboard/text/overall-no-style-control)
- [Arena model page: Claude Opus 5.5 (High)](https://arena.ai/leaderboard/chat/text/models/claude-opus-5.5-high-kmtk)
- [Arena Creative Writing leaderboard](https://arena.ai/leaderboard/chat/text/creative-writing)
- [LMArena Leaderboard September 2026 – versusapp](https://app.versusapp.com/blog/lmarena-leaderboard-september-2026)
- [LMArena Leaderboard October 2026 – versusapps](https://www.versusapps.com/blog/lmarena-leaderboard-september-2026)
- [Claude Opus 5.5 takes the top spot on Text Arena with 1509 points – Crypto Briefing](https://cryptobriefing.com/claude-opus-5-5-text-arena-number-one/)
- [Arena AI Model Rankings: Claude Opus 5.5 Max debuts at No. 1 – KuCoin](https://www.kucoin.com/news/flash/arena-ai-model-rankings-claude-opus-5-5-max-debuts-at-top-chinese-models-maintain-mid-to-top-positions)
- [Claude Fable 5.2 Tops Arena's New Agent Index – FourWeekMBA](https://fourweekmba.com/ai-claude-fable-5-2-tops-arenas-new-agent-index-by-112-points/)
- [Google Gemini 4 Carbon Leads LMArena Text Leaderboard With 1528 Score – af.net](https://af.net/realtime/google-gemini-4-carbon-leads-lmarena-text-leaderboard-with-1528-score/)
- [Gemini 4 Carbon Is Out – projedefteri](https://projedefteri.com/en/blog/gemini-4-carbon-release-date/)
- [Kai on X: Google holds top 3 on LMArena text](https://x.com/hqmank/status/2123621513949798808)
- [Claude Models Explained (2026): Fable, Opus, Mythos – TESS Group](https://tessgroup.co.uk/blog/claude-fable-opus-mythos-explained-uk-employers)
- [Claude Mythos: Access, Pricing – AI Rank](https://airanks.app/articles/claude-mythos)
- [Claude Opus 6 Release Watch – Evolink](https://evolink.ai/blog/claude-opus-6-release-date)
- [Recent Developments in AI: What Shipped by November 2026 – Kanerika](https://kanerika.com/blogs/recent-developments-in-ai/)
- [Grok 5: Release Date, Specs & What's Confirmed – geotoolbox](https://geotoolbox.ai/blog/grok-5)
- [LLM Countdowns](https://waifuai.github.io/llm-countdowns/)
- [AGTP on X: GPT-6 Astra release and Design Arena](https://x.com/AGTPinsights/status/2106987764915040440)
- [GPT-6.1 Terra – Design Arena](https://www.designarena.ai/models/gpt-6.1-terra)
- [lmarena-ai leaderboard-dataset (style control default note)](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
- [LMArena Leaderboard November 2026 – swfte (outlier)](https://www.swfte.com/lmarena)
- [LMArena Leaderboard 2026 – Tokenando (stale)](https://tokenando.ai/benchmarks/lmarena)
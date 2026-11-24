# Research brief: Will "Gemini 3.5 Pro or greater" score above 1500 on Arena Text with style control removed before Jan 1, 2027?

*Prepared 2026-11-24. Direct fetches of arena.ai, Kalshi and the news sites were blocked from this environment, so every fact below comes from search-result snippets and aggregator pages. Treat the exact numbers as approximate.*

## 1. Resolution mechanics

- **What counts as YES:** a model labeled "Gemini 3.5 Pro or greater" scores **above 1500** on the Arena (formerly LMArena) Text leaderboard with **style control removed**, before Jan 1, 2027 (close 2027-01-01 15:00 UTC). This is Kalshi's "Gemini 3.5 Pro debut arena score" market, series KXARENASCORE-GEMI35P. Its strikes run from about 1490 to 1520 (Kalshi market page; KalshiView mirror, Oct 2026).
- **"First model only" rule:** "Models added following the initial qualifying model will not count." If several qualifying models are added together, the highest score is used. So the market really depends on the first model Kalshi treats as qualifying.
- **Which score counts:** the score without style control. Arena has shown style-controlled scores by default since May 2025 (lmarena-ai leaderboard-dataset notes on Hugging Face). Nearly all press and Arena posts quote the style-controlled number. I could not find a no-style-control number for any Gemini 4 model.
- **Main ambiguity: what does "Gemini 3.5 Pro or greater" cover?**
  - Google appears to have dropped Gemini 3.5 Pro. It moved to a Gemini 4 line named after elements: Hydrogen, then Argon, then Carbon, in order of capability and cost (HN thread; Orcarouter; X post by @astropol0).
  - Some sources map Argon to the "Pro" tier and Carbon to "Ultra". Orcarouter says no model in the API is actually called "Gemini 4 Pro".
  - If Kalshi reads "or greater" as any later or larger Gemini flagship, Gemini 4 Argon is probably the initial qualifying model. If Kalshi requires the "Pro" label, there may be no qualifying model before the deadline, which means NO.
  - I found no Kalshi clarification either way.
- **Timing is unclear:** the rules don't say when the score is read (at debut, or at any point before the deadline). They also don't say whether a "preliminary" score counts.
- **Who decides:** Kalshi, using Arena's leaderboard.

## 2. Reference classes and base rates

1. **Do Google flagship debuts land at #1 on Arena Text?** Mostly yes.
   - Gemini 2.5 Pro, Gemini 3 Pro (debuted at 1501, up 50 points on its predecessor's 1451) and Gemini 4 Argon (1525) all debuted at #1. So did Gemini 4 Carbon (1528). That is about 4 of the last 4 flagships (OfficeChai, Nov 2025; Arena on X, Sep 30 and Oct 28, 2026).
   - Each new flagship has added roughly 25–50 points over the previous one, measured with style control.
2. **How much does removing style control change a Gemini score?** Removing style control usually helps models that write long, heavily formatted answers. Gemini models tend to do that, so their raw scores usually match or beat their style-controlled ones.
   - Counter-evidence: one earlier experimental Gemini led the default (non-style-controlled) board but fell to 4th once style control was applied (The Decoder).
   - I could not pin down a typical gap for current frontier models. A guess of ±0–20 points for frontier Gemini models is plausible but **unverified**.
3. **Does Google release models on schedule?** Badly, in this case. Gemini 3.5 Pro missed June, July 17 and August 12, 2026 target dates and was then reportedly shelved (Codersera; TechTimes, Jul 13, 2026; SemiAnalysis via geotoolbox). The chance of a model literally named "Gemini 3.5 Pro" or "Gemini 4 Pro" appearing in the next 5 weeks is low.

## 3. Current state of the world (most recent first)

- **Nov 18–19, 2026:** Google launched Gemini 4 Neon, a mid-tier model it says is cheaper and faster than Carbon (GSMArena; Dailyhunt). It is not a flagship.
- **Nov 6–13, 2026:** Arena Text leaderboard snapshots (style-controlled default):
  - Gemini 4 Carbon (High): about 1526 ±9–10, marked preliminary, about 4,280 votes. Some aggregators show 1538.
  - Gemini 4 Argon (High): about 1520–1529. One snapshot shows 1523 ±6.
  - Claude Opus 5.5: about 1509.
  - Sources: Developers Digest, Nov 7; InfosDivers, Nov 9; LLMBenchmark, Nov 13; BenchLeader, Nov 4; NanoGPT shows 1525.9 with an interval of 1516–1536.
- **Oct 28, 2026:** Gemini 4 Carbon (High) debuted at #1 on Text with 1528, ahead of Argon at 1520 (Arena on X; Crypto Briefing; LLM Odds).
- **Oct 13, 2026 (reported):** Gemini 4 Argon became generally available on the paid API as `gemini-4-argon`. This was the only Gemini 4 entry in the API list at the time (Orcarouter; aiwiz.uk).
- **Sep 30, 2026:** Google announced Gemini 4 Argon, first to cybersecurity partners (9to5Google; Axios). That day Arena posted that Argon (High) "landed #1 in Text Arena with 1525 pts", with style control on (Arena on X). A Google spokesperson reportedly told Reuters that day that Google no longer plans to release 3.5 Pro (aiwiz.uk; resultsense, Oct 1).
- **Aug 2026:** SemiAnalysis reported that 3.5 Pro was shelved in favor of Gemini 4, with Gemini 3.6 Flash as a stopgap (geotoolbox). Kalshi's separate release-date market for 3.5 Pro had a settlement on Sep 3; the "before Aug 31" contract did not win (PillarLab).
- **Mid-Nov 2026:** Gemini 3.1 Pro is still the newest "Pro"-named model in Google's API. The 3.5 Pro page reportedly still says "coming soon" (Codersera; qcode).
- **Scheduled events before close:** none known. I found no announced "Gemini 4 Pro" or "Gemini 4 Ultra" date. Google sometimes ships in December (Gemini 2.0 launched in Dec 2024).

## 4. Drivers and scenarios

**Paths to YES**
- **A. Argon counts and its no-style-control score is above 1500.**
  - Argon was most likely the first Gemini 4 model on the board.
  - Its style-controlled score is about 1520–1525. Its no-style-control score would have to be more than about 20–25 points lower to fall below 1500, which seems unlikely for a Gemini model.
  - If Kalshi treats Argon as qualifying, YES is very likely. It may even already be determined, just not yet settled.
- **B. Carbon is treated as the qualifying model.** This could happen if Kalshi ruled that Argon (the Pro-tier analogue) doesn't count but the flagship does, or if both are treated as simultaneous. Carbon's style-controlled score is about 1526–1538, so YES is likely in this case too.
- **C. Google ships a model actually labeled "Gemini 4 Pro" (or similar) before Jan 1.** It would very likely score above 1500 if added. But the element-based naming makes this unlikely.

**Paths to NO**
- **D. Strict reading of the label.** Kalshi requires a model labeled "Pro" (or literally 3.5 Pro), and none appears before Jan 1. This now looks like the main NO path, given the cancellation and the new naming.
- **E. Argon counts, but its no-style-control score is 1500 or below.** This is possible only if removing style control costs Argon more than about 20 points. I found no evidence for that.
- **A clue in the market's status:** the market still appears open almost two months after Argon's debut. That is weak evidence that Kalshi has not treated Argon as clearly qualifying, or that Kalshi only settles at expiry. I could not tell which.

## 5. Signposts

- **Kalshi rules clarification or early settlement** (biggest mover in either direction):
  - A statement that Gemini 4 models count, or settlement on Argon's score, would point strongly to YES.
  - A statement that only "Pro"-labeled models count would point strongly to NO.
- **Settlement of Kalshi's "When will Google release Gemini 3.5 Pro?" market:** if it settled YES on Argon's release, that suggests Kalshi treats Gemini 4 as "greater", which points to YES.
- **Arena's no-style-control numbers for Argon and Carbon:**
  - Above 1510 supports YES if Gemini 4 counts.
  - Below 1500 would be a surprise and points to NO.
- **Google announcing a "Gemini 4 Pro" or "Ultra" label, or a December flagship launch,** points to YES under the strict reading.

## 6. Uncertainties

- Whether Kalshi counts element-named Gemini 4 models as "Gemini 3.5 Pro or greater". This is the crux, and I could not establish it.
- The actual no-style-control scores for Argon and Carbon. I found none.
- Whether Argon's first Arena appearance (around Sep 30) came before or alongside other Gemini 4 variants, and which model Kalshi would call "initial".
- When the score is read: the preliminary debut value or a later stable one.
- Aggregator scores conflict (Carbon 1526 vs 1538), and the Argon release dates conflict (Sep 30, Oct 1 and Oct 13).

## Sources
- [Gemini 3.5 Pro Release Date: Still Unreleased (Codersera)](https://codersera.com/blog/gemini-3-5-pro-launch-guide-2026/)
- [Gemini 3.5 Pro Targets July 17 After Full Rebuild (TechTimes)](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm)
- [When Is Gemini 3.5 Pro Released? (qcode)](https://qcode.cc/en/gemini-3-5-pro-guide)
- [Google announces Gemini 4 Argon (9to5Google)](https://9to5google.com/2026/09/30/gemini-4-argon-announcement/)
- [Google unveils Gemini 4 (Axios)](https://www.axios.com/2026/09/30/google-gemini-4)
- [Google launches Gemini 4 Neon (GSMArena)](https://www.gsmarena.com/google_launches_gemini_4_neon_its_new_midtier_ai_model-news-75544.php)
- [Arena.ai on X: Gemini 4 Argon #1 with 1525](https://x.com/arena/status/2105394855644139908)
- [Arena.ai on X: Gemini 4 Carbon #1 debut](https://x.com/arena/status/2115495002998751262)
- [Gemini 4 Carbon takes top spot (Crypto Briefing)](https://cryptobriefing.com/gemini-4-carbon-tops-text-arena/)
- [Gemini 4 Carbon debuts atop Arena (LLM Odds)](https://llmodds.com/news/google-gemini-4-carbon-launch-2026)
- [LMArena Leaderboard Nov 2026 (Developers Digest)](https://www.developersdigest.tech/benchmarks/lmarena)
- [LMArena (Now Arena) (InfosDivers)](https://infosdivers.com/en/lmarena/)
- [LMArena Text leaderboard (BenchLeader)](https://www.benchleader.com/benchmarks/lmarena_text)
- [LMArena Text (LLMBenchmark)](https://llmbenchmark.ai/benchmarks/lmarena-text)
- [Gemini 4 Carbon model (NanoGPT)](https://nano-gpt.com/models/text/google/gemini-4-carbon)
- [Gemini 4 Pro: What the Pro Tier Is (Orcarouter)](https://www.orcarouter.ai/blog/gemini-4-pro)
- [Gemini 4 Hydrogen (Hacker News)](https://news.ycombinator.com/item?id=50471431)
- [Astro Polo on X: Gemini 4 element codenames](https://x.com/astropol0/status/2115032943253221608)
- [lmarena-ai/leaderboard-dataset (Hugging Face)](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
- [Google's experimental Gemini leads until you strip formatting (The Decoder)](https://the-decoder.com/googles-new-experimental-gemini-model-leads-ai-rankings-until-you-strip-away-the-formatting/)
- [Gemini 3 tops all LMArena leaderboards (OfficeChai)](https://officechai.com/ai/googles-gemini-3-becomes-top-ai-model-on-all-major-lmarena-leaderboards)
- [Kalshi: Gemini 3.5 Pro debut arena score (rules)](https://kalshi.com/markets/kxarenascore/ai-arena-score/kxarenascore-gemi35p)
- [KalshiView mirror of market rules](https://kalshiview.com/markets/gemini-3-5-pro-debut-arena-score/)
- [PillarLab: When will Google release Gemini 3.5 Pro (settlement note)](https://pillarlabai.com/track-record/when-will-google-release-gemini-3-5-pro-2026-07-17/)
- [Gemini 3.5 Pro release date: what happened (aiwiz.uk)](https://aiwiz.uk/blog/gemini-3-5-pro/)
- [Google's Argon heads Gemini 4 as 3.5 Pro is cancelled (resultsense)](https://www.resultsense.com/news/2026-10-01-google-gemini-4-argon-model/)
- [Gemini 3.5 Pro specs & status (geotoolbox)](https://geotoolbox.ai/blog/gemini-3-5-pro)
# Research brief: Will any model reach a Chatbot Arena (Text Arena) score of 1650 or more by Dec 31, 2026?

*Prepared 2026-11-28. Note: arena.ai and the aggregator sites could not be fetched directly because the proxy blocked them. Every figure below comes from search-result snippets, mostly from secondary aggregators. They agree with each other to within about 10 points.*

## 1. Resolution mechanics
- **What counts as YES:** any model shows an "Arena Score" of 1650 or more on the overall Text Arena leaderboard at lmarena.ai/leaderboard/text, with style control **unchecked** (the raw view), at any time up to Dec 31, 2026, 11:59 PM ET. That leaves about 34 days from today.
- **Who decides:** the market resolver, by reading the live leaderboard. There is no stated rule on archived snapshots. A brief display of 1650 or more would probably count.
- **Edge cases and ambiguities:**
  - **Style control default.** Style control became the default on May 16, 2025, and Arena shifted the offset so both views sit on the same rating scale (lmarena-ai leaderboard-dataset, HF). The raw view is still there: choose "None" under Adjustments, or use the `?scoring=raw` URL. Raw scores at the top currently run only about 8 points above the style-controlled ones (VersusApps blog, Oct 20, 2026).
  - **Other boards are much higher but don't count.** WebDev's leader is around 1810 and the Text "expert" sub-board's leader is around 1554 (aggregator snippets, Nov 2026). Only the overall Text score counts. A careless resolver could misread these, which is a small tail risk.
  - **Domain change.** The platform was renamed "Arena" on Jan 28, 2026 and moved to arena.ai. The lmarena.ai URLs appear to redirect. If the source were judged "permanently unavailable," the market resolves NO, so this risk only pushes toward NO.
  - **Rescaling.** Scores are relative Bradley-Terry ratings on an arbitrary anchor. A methodology change or re-anchoring could in principle shift every score, but I found no evidence of a planned rescale of the text board. The 2026 changes I found concerned Agent Arena scoring (IPS) and open-sourcing Arena-Rank in Feb 2026 (Arena leaderboard changelog; HF dataset).

## 2. Reference classes and base rates
- **Pace of the top score.**

  | Date | Model | Top score | Source / basis |
  |---|---|---|---|
  | Feb 2025 | Grok‑3 | first above 1400 | Arena announcement |
  | Mar 2025 | Gemini 2.5 Pro | ~1443 at debut, later ~1451–1470 | from memory / news |
  | Nov 18, 2025 | Gemini 3 Pro | 1501, first above 1500 | VentureBeat / Neowin, Nov 2025 |
  | Late Oct–Nov 2026 | Gemini 4 Carbon | ~1526–1538 | aggregators |

  - That is about +100 points per year in 2025, slowing to about +25–37 points in the 12 months since Nov 2025.
  - Reaching 1650 needs about +110–125 points in about 5 weeks. At the 2026 pace that would take roughly 3–4 more years. Even at the 2025 pace it would take more than a year.
- **Largest single-release jumps.** Gemini 3 Pro was about +50 over Gemini 2.5 Pro (VentureBeat) and about +30–40 over the previous overall #1. Gemini 2.5 Pro was about +40 over the previous leader. In the observed history, no release has ever jumped the top score by 100 or more points. The base rate for a 110+ point jump in any 5-week window is 0 of roughly 40 or more such windows since 2023.
- **Preliminary scores fall.** New #1 models usually debut "preliminary" with wide confidence intervals and then drift down a few points as votes accumulate. For example, Gemini 4 Carbon showed 1538±10 on Nov 11 and about 1526–1527 later in November.

## 3. Current state of the world (most recent first)
- **Late Nov 2026 (cached arena.ai pages):** Gemini 4 Carbon (High) is #1 at about 1527, 7 points ahead of Argon at about 1520. The English-only view shows Carbon at 1524 (arena.ai cached pages). I found no evidence of a new #1 as of Nov 28.
- **About Nov 18, 2026:** Arena posted that Google holds the top 3: Carbon 1526, Gemini 4 Argon 1521, Gemini 4 Neon 1518 (Arena on X).
- **Nov 11, 2026:** Carbon 1538±10, Argon 1529±5, Claude Opus 5.5 (High) 1514±6. The board had about 9.1M votes across 421 models (search snippet of arena.ai).
- **Nov 6–9, 2026:** Carbon 1526±9, still preliminary (aggregators).
- **Oct 28, 2026:** Carbon 1528, Argon 1520 (aggregators; CryptoBriefing / AF.net).
- **Oct 20, 2026:** Argon was the top **raw** (style-control off) score at 1532, against 1524 with style control on (VersusApps blog).
- **Sep 25, 2026:** the top raw score was 1518, held by claude-opus-5.5-high (VersusApps).
- **Release pipeline:** GPT‑6‑series (Astra/Sol/Luna) and Claude Opus 5.5 appear to be out. Claude Fable 5.2 was reportedly released Nov 9. Gemini 4 tiers are partly in restricted or phased access. I found no confirmed December 2026 frontier launch dates, and the sources are speculative and inconsistent (release-tracker pages, Nov 2026).

## 4. Drivers and scenarios
- **Paths to YES**, each very unlikely:
  1. An unprecedented capability leap: a model debuts more than 110 points above the current top. That is about 2–3 times the largest jump ever recorded, and it would have to happen in December.
  2. Arena re-anchors or rescales the Text scores upward by about 100 or more points before Dec 31. I found no announcement of this.
  3. A resolver error, such as citing WebDev or another sub-board, or a display glitch.
- **Path to NO (default):** the top score stays roughly at 1520–1545, raw or style-controlled, through year-end. Even a strong new release in December (a GPT‑6 successor, a broader Gemini 4 release, or a new Claude) would most likely add about 10–40 points.
- **Structural headwind:** Bradley-Terry ratings depend on win rates against a crowded pool of near-peer frontier models. As the top cluster tightens, gaps grow more slowly. 1650 would mean roughly a 66% expected win rate against a 1530 model, a dominance never seen at the frontier.

## 5. Signposts
- **Toward YES (large moves):**
  - an Arena changelog entry announcing re-anchoring or rescaling of Text scores;
  - a new model debuting at 1580 or more (still well short of 1650, but it would break the trend);
  - any report of the raw view diverging sharply from the style-controlled view.
- **Toward NO (confirming):** December releases debuting in the 1520s–1550s, and Carbon's score settling as its preliminary tag is removed.
- **Watch:** arena.ai/leaderboard/text?scoring=raw, the Arena changelog, and @arena on X, particularly in the week after any major lab launch.

## 6. Uncertainties
- I could not load the live leaderboard. The exact current raw (style-off) top score is unverified. My best estimate is about 1530–1545, based on raw running about 8 points above style-controlled.
- I could not confirm whether the "style control" checkbox still exists in that form. It now appears as an "Adjustments: None" selector. The wording mismatch could create resolution ambiguity, but both views are far below 1650.
- I don't know the December 2026 release schedule for any frontier lab.
- I can't rule out an undisclosed methodology or anchor change. There is no evidence of one.

## Sources
- [Arena.ai on X – Google holds top 3 spots (Carbon 1526, Argon 1521, Neon 1518)](https://x.com/arena/status/2123169199396946279)
- [Text Arena: LLM Rankings (arena.ai)](https://arena.ai/leaderboard/chat/text)
- [Text Arena raw scoring view (arena.ai)](https://arena.ai/leaderboard/chat/text?scoring=raw)
- [Google DeepMind's Gemini 4 Carbon takes the top spot in LM Arena's Text Arena (CryptoBriefing)](https://cryptobriefing.com/gemini-4-carbon-tops-text-arena/)
- [Google Gemini 4 Carbon Leads LMArena Text Leaderboard With 1528 Score (AF.net)](https://af.net/realtime/google-gemini-4-carbon-leads-lmarena-text-leaderboard-with-1528-score/)
- [LMArena Leaderboard October 2026: Where the Top Text Scores Stand (VersusApps)](https://www.versusapps.com/blog/lmarena-leaderboard-september-2026)
- [LMArena Leaderboard September 2026 (VersusApp)](https://app.versusapp.com/blog/lmarena-leaderboard-september-2026)
- [LMArena Leaderboard (November 2026) – Developers Digest](https://www.developersdigest.tech/benchmarks/lmarena)
- [LMArena Text Leaderboard & Scores (November 2026) – llmbenchmark.ai](https://llmbenchmark.ai/benchmarks/lmarena-text)
- [LMArena Text leaderboard (Nov 2026) – BenchLeader](https://www.benchleader.com/benchmarks/lmarena_text)
- [lmarena-ai/leaderboard-dataset (Hugging Face)](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
- [Leaderboard Changelog (arena.ai)](https://arena.ai/blog/leaderboard-changelog/)
- [Arena (AI platform) – Wikipedia](https://en.wikipedia.org/wiki/Arena_(AI_platform))
- [Google unveils Gemini 3 (VentureBeat)](https://venturebeat.com/ai/google-unveils-gemini-3-claiming-the-lead-in-math-science-multimodal-and)
- [Google announces Gemini 3 surpassing GPT-5.1 (Neowin)](https://www.neowin.net/news/google-announces-gemini-3-surpassing-openais-gpt-51-across-key-ai-benchmarks/)
- [Latest AI Models 2026: GPT-6, Claude 5.5, Gemini 4 & More (tldl.io)](https://www.tldl.io/resources/latest-model-releases)
- [Upcoming AI models: GPT-6, Gemini 4, Opus 5.5, DeepSeek V5 (WinCentral)](https://thewincentral.com/upcoming-ai-models-gpt-6-gemini-4-opus-5-5-deepseek-v5/)
## 1. Resolution mechanics

- **What counts as YES:** At **12:00 PM ET on Nov 30, 2026**, the model in first place on arena.ai's **Text Arena, Overall** leaderboard must belong to Anthropic. The page is `arena.ai/leaderboard/text/overall-no-style-control`, with **style control OFF** (Adjustments: None) and filtered to "Models."
- **This is not Arena's default view.** Arena has shown style control by default since about May 2025 (Arena.ai on X, May 2025). Almost every headline score in the news ("debuts at #1 with 1509") is the style-controlled number. Arena has said that with style control off, Claude models drop and some others (e.g. Grok-4) rise (Arena.ai on X, Aug 2025). Forecasters should not read the news scores as the resolution numbers.
- **How first place is decided:** By the "Rank" column first. If ranks tie, the higher Arena score wins, including unrounded values. If scores also tie, alphabetical order of company names as listed in the market group decides. A shared rank is likely when confidence intervals overlap, so in practice the highest raw score usually wins.
- **Exclusions:** Models marked "AutoEval" don't count. Preliminary or low-vote models are not excluded by the rules, so a new model marked "preliminary" can win.
- **If the page is down:** The market waits for the first check after the leaderboard comes back. If it is gone permanently, the market resolves "Other."
- **Edge cases:**
  - Restricted-access models (e.g. Gemini 4 Carbon, which is limited to selected cyber defenders) do appear on the public board and count.
  - A secret test model doesn't count until it is named and ranked.
  - The company list apparently includes "SpaceXAI," which suggests xAI is now listed under a SpaceX entity.
  - Anthropic only needs any one of its models (Opus, Fable, Mythos) to be #1.

## 2. Reference classes and base rates

1. **Which company led Arena's text board (style off) at month-end, 2024–2026.** This is from my own background knowledge, not checked against a live archive, so treat it as approximate.
   - Google held #1 in most month-end snapshots from about mid-2024 to early 2026: Gemini-Exp, Gemini 2.5 Pro from Mar 2025, Gemini 3 Pro from Nov 2025.
   - OpenAI and xAI led briefly (GPT-4o in 2024, Grok-3 in Feb 2025).
   - Anthropic was #1 without style control only rarely: briefly with Claude 3 Opus in 2024, and in parts of 2026.
   - **Rough base rate: Anthropic led about 10–25% of month-ends over the last ~30 months. Google led roughly 60%+.**
2. **The incumbent leader at T−3 weeks still leads at month-end.** Arena's top spot changes mainly when a new frontier model launches. In 2025–26 a single month saw about 0–2 leadership changes, so the leader with ~3 weeks to go has kept #1 roughly 70–80% of the time (rough estimate). The current leader is Google (see §3).
3. **A new Anthropic flagship takes #1 when it launches.** Anthropic's recent big releases debuted at #1 on the style-controlled board:
   - Opus 5.5 (High): 1509, +18 over Opus 5 (Arena.ai on X, ~Sep 22, 2026)
   - Fable 5: reported at 1506 (aggregators)

   Its record without style control is weaker. **Conditional estimate: if a new top Anthropic model reaches the board, it takes style-off #1 maybe 30–50% of the time** against a strong Google incumbent.

## 3. Current state of the world (most recent first)

I couldn't open arena.ai directly because the network proxy blocked it, so all standings below come from secondary sources.

- **Nov 4, 2026 – default (style-controlled) Text board:** Gemini 4 Carbon (Google) **1528**, Gemini 4 Argon (Google) **1520**, Claude Opus 5.5 (High) **1509** (BenchLeader, Nov 4, 2026; ChatJudge, Oct 2026). Carbon's score was **preliminary** with about 4,400 votes as of Oct 27 (aggregator listing, Oct 27, 2026).
- **Nov 1, 2026 – Mythos 5.5 leak:** A "Claude Mythos 5.5" reference appeared briefly in the code of Anthropic's Mythos page and was removed within hours. TestingCatalog suggested a release "next week," unconfirmed. Access is expected to be restricted to cyber/bio users. There is speculation about a matching **Claude Fable 5.5**, with a claimed Oct 13 Azure entry for "claude-fable-5-5" (TestingCatalog, Nov 1, 2026; pasqualepillitteri.it, Nov 2026; daily.dev, Nov 2026). Anthropic has not commented.
- **Late Oct 2026 – Opus 5.6 rumors:** There is speculation about a next Opus (5.6+) in November, with no announced date (Lines.com explainer, Oct 27–Nov 1, 2026). Opus 6 claims trace back to a single report.
- **Oct 28, 2026 – Gemini 4 Carbon announced:** Google announced Carbon with access limited to selected cybersecurity defenders and no general-availability date (iTechPost, Oct 30, 2026; SmartScope, Oct 2026). It topped the Text Arena and placed #2 on Agent Arena (OfficeChai; CryptoBriefing, late Oct 2026). A Carbon test version had shown up on Arena around Oct 22 (LetsDataScience, Oct 22, 2026).
- **October 2026 – style-off claim:** One blog says the **highest style-control-OFF score is 1532, held by Gemini 4 Argon (High)**. It also says Meta's "Muse Wonder (Max)" is #2 in the default view but #6 with style off (VersusApps, Oct 2026). This is the only style-off data point I found, and it is unverified. It came before Carbon's debut, so Carbon may now lead the style-off view as well.
- **Oct 7, 2026:** Anthropic released Claude Haiku 5.5, a small model that isn't a contender.
- **Sep 30, 2026:** Gemini 4 Argon (High) debuted at #1 on the Text Arena with 1525 (Arena.ai on X, Sep 30, 2026). That knocked Anthropic off the top.
- **~Sep 22, 2026:** Claude Opus 5.5 (High) debuted at #1 with 1509, and Arena said Anthropic held **all six top spots** at that point. Opus 4.6 (High) was #2, 4 points behind (Arena.ai on X; CryptoBriefing, Sep 2026). That was the style-controlled view.
- **Sep 2026:** OpenAI's GPT-6 Astra led Code Arena WebDev at 1797 (CryptoBriefing; KuCoin, Sep 2026). I found no evidence that GPT-6 leads the Text Arena.
- **Sep 1, 2026:** Claude Fable 5.1 and Mythos 5.1 were released (Wikipedia, Claude Mythos). Aggregators put Fable 5.1 around 1503 on the Text Arena (ApX). Mythos was restricted, and its arena status is unclear. One low-quality site lists "Claude Mythos 5" at 1531 (Swfte, Nov 2026); treat that as unreliable.
- **Before Nov 30:** No events are confirmed. Possible releases include Mythos 5.5, Fable 5.5, Opus 5.6, a wider Gemini 4 Carbon rollout or new Gemini checkpoints, GPT-6 updates, and new xAI/Meta models.

**Bottom line:** As of early November, Google appears to hold #1 and #2 on the default board, about 19 points ahead of Anthropic's best. Style-off views have historically favored Google over Claude, so the gap in the resolution view is probably at least as large, though I couldn't verify that.

## 4. Drivers and scenarios

**Paths to YES (Anthropic is #1 on Nov 30):**
1. **A new Anthropic flagship lands on the board before Nov 30 and passes Gemini 4 Carbon with style off.** Candidates are Mythos 5.5, Fable 5.5 or Opus 5.6. This requires:
   - a release in the next ~3 weeks;
   - Arena listing it publicly (Gemini 4 Carbon's listing despite restricted access shows this can happen);
   - a style-off score above Carbon's. That likely means beating it by 20–30+ points in the default view, which is larger than Opus 5.5's +18 jump over Opus 5.
2. **Carbon's preliminary score falls back as votes accumulate** (say to the low 1510s), and an existing Claude model leads the style-off view. This seems unlikely: Argon alone is reportedly at 1520 (style on) and 1532 (style off).
3. **Google pulls or renames models** in a way that leaves Claude on top. This is unlikely.

**Paths to NO:**
1. **Google keeps #1**, either with Carbon or Argon, or a new Gemini 4 checkpoint pushes the lead further. This is the default path.
2. **Another company takes #1**, such as GPT-6 on text, an xAI (SpaceXAI) model, Meta Muse, or DeepSeek. Grok has historically gained when style control is off.
3. **Anthropic releases a model that scores well with style control but not without it**, a known Claude pattern. For example, Claude could be #1 in the default view and still lose the resolution view.

## 5. Signposts

- **Strong move toward YES:**
  - An official Anthropic release (Mythos 5.5, Fable 5.5 or Opus 5.6) plus an Arena post saying it debuts at #1 with a score of about 1530 or more.
  - Especially strong: confirmation that it also leads the **style-off** view.
- **Moderate move toward YES:** Carbon's score dropping below ~1515 as votes accumulate, or Arena removing its "preliminary" tag at a lower score.
- **Toward NO:**
  - Arena snapshots showing Google holding #1 with style off by 10 or more points.
  - New Gemini 4 checkpoints, or Carbon's wider rollout.
  - Reports that Mythos 5.5 is restricted and **not** submitted to Arena.
  - Anthropic releases slipping into December.
  - A GPT-6 or Grok text result above 1530.
- **Watch:** Arena's X account (@arena), Anthropic's newsroom, TestingCatalog, and the style-off leaderboard page itself.

## 6. Uncertainties

- **Current style-off standings:** I couldn't check them directly. The only figure (Argon 1532 style-off, October) comes from one low-reliability blog. Whether Carbon or Argon leads with style off, and by how much over Claude, is unknown.
- **Anthropic's best style-off score:** I don't know which Anthropic model ranks highest with style off, or by how much. Claude has historically dropped with style off.
- **Mythos visibility on Arena:** I couldn't tell whether Mythos models (5.1, or a future 5.5) appear on the public Text Arena at all. Reports conflict.
- **Release timing:** None is confirmed for Mythos 5.5, Fable 5.5, Opus 5.6, or new Google, OpenAI or xAI models before Nov 30.
- **Source quality:** Many sources are low-quality aggregators with conflicting numbers (e.g. Argon at 1525 vs 1520). My historical base rates come from memory, not a verified archive of month-end leaders.

## Sources
- [Text Arena (no style control) – resolution page](https://arena.ai/leaderboard/text/overall-no-style-control)
- [Arena.ai on X – Gemini 4 Argon (High) #1 in Text Arena, 1525](https://x.com/arena/status/2105394855644139908)
- [Arena.ai on X – Claude Opus 5.5 (High) debuts #1 with 1509](https://x.com/arena/status/2103893011164017018)
- [Arena.ai on X – style control vs no style control (Grok rises, Claude drops)](https://x.com/arena/status/1952769863665238383)
- [Arena.ai on X – Style Control becomes default view](https://x.com/arena/status/1923398953468678529)
- [LMArena Text leaderboard (Nov 2026) – BenchLeader](https://www.benchleader.com/benchmarks/lmarena_text)
- [LMArena Text Arena leaderboard (Oct 2026) – ChatJudge](https://chatjudge.ai/benchmarks/chat/lmarena-text)
- [LMArena Leaderboard October 2026 – VersusApps](https://www.versusapps.com/blog/lmarena-leaderboard-september-2026)
- [LMArena Leaderboard November 2026 – Swfte](https://www.swfte.com/lmarena)
- [Gemini 4 Carbon tops Text Arena – CryptoBriefing](https://cryptobriefing.com/gemini-4-carbon-tops-text-arena/)
- [Gemini 4 Carbon Tops Text Arena, Places 2nd On Agent Arena – OfficeChai](https://officechai.com/ai/gemini-4-carbon-tops-text-arena-places-2nd-on-agent-arena/)
- [Gemini 4 Carbon checkpoint reportedly appears on Chatbot Arena – LetsDataScience](https://letsdatascience.com/news/gemini-4-carbon-checkpoint-reportedly-appears-on-chatbot-are-ee165ebf)
- [Google reveals Gemini 4 Carbon, restricted access – iTechPost](https://www.itechpost.com/articles/237686/20261030/google-reveals-gemini-4-carbon-its-latest-frontier-ai-model-restricted-access.htm)
- [Gemini 4 Carbon availability – SmartScope](https://smartscope.blog/en/blog/gemini-4-carbon-availability-release-date-differences-argon-2026/)
- [Google says Gemini 4 release coming as soon as possible – 9to5Google](https://9to5google.com/2026/09/24/google-says-gemini-4-release-is-coming-as-soon-as-possible/)
- [Claude Opus 5.5 takes the top spot on Text Arena – CryptoBriefing](https://cryptobriefing.com/claude-opus-5-5-text-arena-number-one/)
- [Claude Opus 5.5 Arena Ranking Hits No. 1 – remio](https://www.remio.ai/post/claude-opus-5-5-arena-ranking-hits-no-1-but-the-four-point-gap-matters)
- [Claude Fable 5.1 – ApX](https://apxml.com/models/claude-fable-51)
- [Claude Mythos – Wikipedia](https://en.wikipedia.org/wiki/Claude_Mythos)
- [Anthropic prepares to release Claude Mythos 5.5 – TestingCatalog](https://www.testingcatalog.com/anthropic-prepares-to-release-claude-mythos-5-5-model/)
- [Mythos 5.5 leak on Anthropic's website – pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/29332/mythos-5-5-leak-anthropic-website)
- [Claude Mythos 5.5 leaked via a website string – daily.dev](https://daily.dev/posts/claude-mythos-5-5-leaked-via-a-website-string-and-the-hype-machine-is-already-ahead-of-the-facts-zrkkgodnv)
- [Next Claude Opus (5.6+) explainer – Lines.com](https://www.lines.com/prediction-markets/business/anthropic/next-claude-opus-5pt6-released-onptptpt-20261027)
- [OpenAI's GPT-6 Astra tops Code Arena WebDev – CryptoBriefing](https://cryptobriefing.com/openai-gpt6-astra-tops-code-arena/)
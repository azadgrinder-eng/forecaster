# Research brief: Will OpenAI have a #1-ranked AI model before Jan 1, 2027?

## 1. Resolution mechanics

- **Question text:** YES if OpenAI has a "#1 ranked AI model" before Jan 1, 2027. The close date is 2027-01-01 15:00 UTC. The question does not name a leaderboard.
- **Likely settlement source:** The wording and close date match Kalshi's company-level "top AI model before 2027" series (ticker KXTOPAI-27-JAN01-OPEN). Kalshi's TOPAI rulebook links to the Arena (formerly LMSYS Chatbot Arena) **text** leaderboard and uses the **Rank (UB)** column, checked around 10:00 AM ET daily (Kalshi TOPAI contract terms PDF, modified 2026-09-29; DeFi Rate / Action Network summaries, 2026). I could not read the full PDF. Fetch attempts failed, and the PDF's text layer was unreadable.
- **How it works under the Arena reading:**
  - Each company has its own YES/NO contract, and more than one company can resolve YES.
  - OpenAI only needs to hold #1 **once** at any check before Jan 1, 2027.
  - Rank ties are reportedly broken by higher Arena score, then more votes, then earlier release. One summary instead says a company tied with another model does not qualify.
- **Style control is unresolved.** Some summaries say Kalshi uses the board with style control **removed**. Others mention only Rank (UB). This matters: removing style control rewards longer, more heavily formatted answers and can change who is #1.
- **Window:** The market is still open, so OpenAI has apparently not hit #1 on the settlement source since the window opened. In practice the window is roughly Nov 18 to Dec 31, 2026, about 6 weeks.
- **Major ambiguity: a different Kalshi family uses a different index.** CFTC filings describe a separate series, "Will OpenAI possess the top AI model <period>?" (rulebook TOPLLMEXCLUSIVE), that uses the **Epoch Capabilities Index (ECI)** (CFTC filing ptc10052631445). On ECI, GPT-6.2 Astra (released Nov 17) is **already tied for #1** with Claude Fable 5.2, at a score of 174 among 241 models (Epoch AI model page, Nov 2026). If this question settles on ECI, the outcome hinges almost entirely on how ties are treated. Forecasters should confirm which rulebook applies. The ticker suggests TOPAI/Arena.
- **Another wrinkle in Rank (UB):** A newly listed model has a wide confidence interval, so it can share UB rank 1 while scoring below the leader. Whether that counts as "#1" depends on the tiebreak language. The tiebreak-by-score rule would deny it.

## 2. Reference classes and base rates

1. **OpenAI flagship debuts on Arena text, mid-2025 to now.**
   - GPT-5 (Aug 2025) debuted #1, shared with Gemini 2.5 Pro.
   - GPT-5.1 (Nov 2025) and GPT-5.2 (Dec 2025) did not, per my recollection rather than a source found here.
   - GPT-5.6 Sol (xhigh) sat around #20 at 1484 on Oct 2, 2026 (Manifold market description, Oct 2026).
   - GPT-6 Astra (Max), launched Sep 3, 2026, debuted around #18–21 at about 1475, and around #37–42 at 1474–1476 in November (aggregators, Oct 8 and Nov 4–9, 2026; arena.ai text page, ~Nov 12).
   - **Result: about 1 in 5–6 recent flagships debuted at #1, and none in the last ~12 months.**
2. **Leader turnover on Arena text.** Across 43 month-end snapshots since May 2023, the leader changed 21 times among 7 providers. That is about 0.5 changes per month, so roughly a 50% chance of *some* change in a 1.5-month window. But the change has to go to OpenAI specifically. Over the past ~12 months, Google and Anthropic (and briefly others) have traded the lead: Gemini 3 Pro in late 2025, Claude Opus 4.6 in Feb 2026, Claude Fable 5 around Aug 2026, Gemini 4 Argon in Oct 2026, and Gemini 4 Carbon from Oct 28, 2026 (BenchLM leaderboard history, Nov 2026; buildmvpfast, Apr 2026; Manifold description, Oct 2026; Arena on X, Oct 28, 2026).
3. **Size of the jump needed.** OpenAI's best listed model is about 50–60 points behind the leader. Single-release jumps of 40–60 points have happened: Gemini 3 Pro in late 2025, and Gemini 4 Carbon came in 8 points over Argon. But OpenAI's latest generation (GPT-6 Astra) made no such jump on text preference, even though it scores at the frontier on capability indices.

## 3. Current state of the world (most recent first)

- **Nov 17, 2026: OpenAI releases GPT-6.2 Astra (frontier) and GPT-6.2 Sol (efficient)** in ChatGPT, Codex and the API. Astra's API price is 20% lower than GPT-6 Astra, with one source citing $8/$40 per million tokens (9to5Mac, Nov 17; TestingCatalog, Nov 17; MarkTechPost, Nov 17). Reported scores:
  - Artificial Analysis Intelligence Index: 62, second behind Claude Fable 5.2 at 65. One headline says it edges Gemini 4 Carbon by 2 points (Unite.AI; officechai, Nov 2026).
  - Vals Index: 7th, behind Gemini 4 Argon and Gemini 4 Hydrogen (officechai, Nov 2026).
  - Epoch ECI: tied #1 (Epoch AI, Nov 2026).
  - #1 on Artificial Analysis's AA-3D Elo at 1318. This is not Arena (cryptobriefing, Nov 2026).
  - First externally released model rated "High" for AI self-improvement (Unite.AI, Nov 2026).
  - Reception is mixed: VentureBeat headline "'Essentially unusable': … negative reception from AI power users" (VentureBeat, Nov 17–18).
  - **No Arena text score for GPT-6.2 Astra was found as of Nov 17–18** (BenchLM: "not publicly ranked yet," Nov 17).
- **~Nov 10, 2026:** Anthropic released Claude Fable 5.2 about a week before GPT-6.2. 9to5Google framed GPT-6.2 as OpenAI trying to "regain performance lead from Claude Fable 5.2" (9to5Google, Nov 17). I found no Arena text score for Fable 5.2.
- **Nov 4–15, 2026: Arena text top of board.** Snapshots differ slightly:
  1. Gemini 4 Carbon (High): about 1526–1538, flagged preliminary in some snapshots
  2. Gemini 4 Argon: about 1520–1529
  3. Meta Muse Wonder: about 1511
  4. Claude Opus 5.5: about 1509

  OpenAI's best, GPT-6 Astra (Max), sits at about 1474–1476 (Developers Digest, verified Nov 7; infosdivers, Nov 9; 17nas, Nov 13; LLMBenchmark, Nov 13; Benchleader, Nov 4). One outlier page lists Claude Mythos 5 at 1531 with no date. 17nas notes that the top confidence intervals overlap heavily.
- **Nov 5, 2026:** OpenAI's GPT-6 Cyber released under restricted access (nhimg OpenAI models guide).
- **Oct 28, 2026:** Gemini 4 Carbon (High) debuts #1 on Text Arena, #2 on Agent Arena and #4 on WebDev. Access is initially limited to cyber defenders (Arena on X, Oct 28; llmodds; explainx).
- **Oct 26, 2026:** GPT-6.1 Terra released (nhimg). Sources conflict on whether GPT-6.1 Astra was cancelled.
- **Sep 3, 2026:** GPT-6 Astra launches. The rollout was "messy" in Altman's words, with user complaints about nerfing. It took #1 on four Design Arena boards in early October and ranks #5 on Arena coding (1548), but sits far lower on text (CSO Online; Decrypt; AGTP on X, Oct 5; arena.ai coding page, Nov 11).

**Possible events before Dec 31:**
- GPT-6.2 Astra and Sol Arena text debut, likely within days to about 2 weeks.
- A possible OpenAI December release, in line with past Decembers: "shipmas" in 2024 and GPT-5.2 in Dec 2025.
- Possible Google or Anthropic releases or updates: Gemini 4 Carbon general availability, new Claude variants.
- Gemini 4 Carbon's preliminary score settling as votes accumulate.

## 4. Drivers and scenarios

**Paths to YES:**
- **A:** GPT-6.2 Astra debuts on Arena text at or above about 1530 and takes rank #1 outright. This would need roughly a +55 point jump over GPT-6 Astra. Possible, but GPT-6 Astra's text-arena result, the mixed early reception, and OpenAI's benchmark-over-chat-style positioning all argue against it.
- **B:** GPT-6.2 Astra lands near 1510–1525 with a wide preliminary interval, and the rules count a shared UB rank of 1. This depends on tiebreak wording, which reportedly favors the higher score.
- **C:** OpenAI ships another model in December, such as a chat-tuned "chatgpt-latest"-style variant. OpenAI previously topped Arena with chat-tuned variants like chatgpt-4o-latest.
- **D:** The no-style-control view applies, and OpenAI's verbose, markdown-heavy models rank higher there.
- **E:** The question actually settles on Epoch ECI, where GPT-6.2 Astra is already tied #1. YES then depends on tie handling.

**Paths to NO:**
- GPT-6.2 Astra debuts mid-pack (around 1480–1505), as GPT-6 Astra did.
- Google or Anthropic keep or extend the lead with Carbon, Argon, Opus 5.5 or Fable 5.2.
- No further OpenAI release before year-end.
- The window is short: about 6 weeks, including holidays.

## 5. Signposts

- **GPT-6.2 Astra's first Arena text score.** This is the single biggest update.
  - At or above about 1525 with UB rank 1: strong move toward YES.
  - About 1500–1520: modest move, and the tie rules become key.
  - Below about 1500: strong move toward NO.
- **Style control.** Whether the settlement view is style-on or style-off, and where OpenAI ranks in the style-off view.
- **Further OpenAI launches.** Announcements of any December model or chat-tuned ChatGPT default update. Watch for anonymous OpenAI models being tested on Arena.
- **Leader's score.** Gemini 4 Carbon's score drifting down as it loses the preliminary tag, which would narrow the gap. Or new Google or Anthropic models raising the bar.
- **Rulebook.** Confirmation of the actual rules: TOPAI/Arena versus TOPLLMEXCLUSIVE/ECI, and the tie language.

## 6. Uncertainties

- I could not read the official Kalshi rulebook or the live arena.ai board, because fetches were refused. All leaderboard numbers come from third-party snapshots and search summaries, which disagree by about 10 points and in a few cases on the leader.
- Whether the "#1" check is style-control on or off.
- How shared UB ranks or ties count.
- Whether ECI rather than Arena is the source.
- GPT-6.2 Astra's Arena performance is unknown.
- Claude Fable 5.2's Arena text score is unknown.
- OpenAI's December release plans are unknown.
- Model naming and versioning in sources is inconsistent: the GPT-6.1 history, and the "Claude Mythos 5" outlier.

## Sources
- [LMArena Leaderboard (November 2026) – Developers Digest](https://www.developersdigest.tech/benchmarks/lmarena)
- [LMArena Text Leaderboard & Scores (November 2026) – LLMBenchmark](https://llmbenchmark.ai/benchmarks/lmarena-text)
- [LMArena Text leaderboard (Nov 2026) – Benchleader](https://www.benchleader.com/benchmarks/lmarena_text)
- [LMArena (Now Arena): Leaderboard and How It Works – infosdivers](https://infosdivers.com/en/lmarena/)
- [LLM Leaderboard 2026 – 17nas](https://17nas.com/llm-leaderboard.php)
- [LMArena Leaderboard November 2026 – Swfte](https://www.swfte.com/lmarena)
- [Text Arena leaderboard – arena.ai](https://arena.ai/leaderboard/chat/text)
- [Text Arena coding leaderboard – arena.ai](https://arena.ai/leaderboard/chat/text/coding)
- [Arena.ai on X: Gemini 4 Carbon debuts #1 in Text Arena](https://x.com/arena/status/2115495002998751262)
- [Gemini 4 Carbon debuts atop Arena's text leaderboard – LLM Odds](https://llmodds.com/news/google-gemini-4-carbon-launch-2026)
- [Gemini 4 Carbon: Index 59 – explainx](https://explainx.ai/blog/gemini-4-carbon-launch-cyber-defenders-first-59-intelligence-index-pricing-2026)
- [LLM Leaderboard History: Arena Rankings 2023–2026 – BenchLM](https://benchlm.ai/llm-leaderboard-history)
- [Which company will have the #1 model on the Arena text leaderboard on Oct 31, 2026? – Manifold (description only)](https://manifold.markets/Terminator2/which-company-will-have-the-1-model)
- [LMSys Arena Leaderboard April 2026 – buildmvpfast](https://www.buildmvpfast.com/blog/claude-opus-4-6-lmsys-arena-benchmark-comparison-2026)
- [Kalshi TOPAI contract terms (PDF)](https://kalshi-public-docs.s3.amazonaws.com/contract_terms/TOPAI.pdf)
- [CFTC filing ptc10052631445 (TOPLLMEXCLUSIVE)](https://www.cftc.gov/filings/ptc/ptc10052631445.pdf)
- [Best AI Model of 2026 – DeFi Rate (rules summary only)](https://defirate.com/prediction-markets/best-ai-model-odds-this-year/)
- [What Will Be the Top AI Model This Month? – Action Network (rules summary only)](https://www.actionnetwork.com/general/what-will-be-the-top-ai-model-this-month-kalshi-odds)
- [OpenAI upgrades ChatGPT and Codex with GPT-6.2 Astra and Sol – 9to5Mac](https://9to5mac.com/2026/11/17/openai-upgrades-chatgpt-and-codex-with-new-gpt-6-2-astra-and-sol-models/)
- [OpenAI releases GPT-6.2 Astra to regain performance lead from Claude Fable 5.2 – 9to5Google](https://9to5google.com/2026/11/17/openai-releases-gpt-6-2-astra-and-sol-for-complex-projects-a-week-after-claude-5-2)
- [OpenAI Releases GPT-6.2 Astra With First High Self-Improvement Rating – Unite.AI](https://www.unite.ai/openai-releases-gpt-6-2-astra-with-first-high-self-improvement-rating/)
- ['Essentially unusable': GPT-6.2 Astra and Sol negative reception – VentureBeat](https://venturebeat.com/technology/essentially-unusable-openai-launches-gpt-6-2-astra-and-sol-to-negative-reception-from-ai-power-users)
- [OpenAI launches GPT-6.2 Astra and Sol – TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-2-astra-and-sol-on-chatgpt-and-apis/)
- [OpenAI Releases GPT-6.2 Astra and Sol – MarkTechPost](https://www.marktechpost.com/2026/11/17/openai-gpt-6-2-astra-sol-release/)
- [Introducing GPT-6.2 Astra and Sol – OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol/)
- [GPT-6.2 Astra – Epoch AI](https://epoch.ai/models/gpt-6-2-astra)
- [GPT-6.2 Astra Model Specs – BenchLM](https://benchlm.ai/models/gpt-6-2-astra)
- [GPT 6.2 Astra Places 7th On Vals Index – officechai](https://officechai.com/ai/gpt-6-2-astra-vals-index/)
- [GPT 6.2 Astra Places Second On AA Intelligence Index – officechai](https://officechai.com/ai/gpt-6-2-astra-artificial-analysis-intelligence-index/)
- [GPT-6.2 Astra tops AA-3D benchmark – cryptobriefing](https://cryptobriefing.com/gpt-6-2-astra-tops-aa-3d-benchmark/)
- [OpenAI Models: Specs, Prices and Release Dates – nhimg](https://nhimg.org/openai-llm-models-guide)
- [GPT-6 Astra Benchmark Scores – benchmarklist](https://benchmarklist.com/models/openai-gpt-6-astra/)
- [AGTP on X: GPT-6 Astra #1 on four Design Arena leaderboards](https://x.com/AGTPinsights/status/2106987764915040440)
- [Sam Altman calls GPT-6 Astra rollout messy – CSO Online](https://www.csoonline.com/article/4219249/sam-altman-calls-gpt-6-astra-rollout-messy-as-enterprise-users-wait-for-access.html)
- [GPT-6 Astra Users Say OpenAI's Newest Model Got Dumber – Decrypt](https://decrypt.co/378101?amp=1)
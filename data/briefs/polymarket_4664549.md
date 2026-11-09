# Research brief: Will Xiaomi be the third-ranked Chinese AI lab on arena.ai's Text Arena (Overall, style control off) on Nov 30, 2026?

**Caveat on the evidence:** I could not load arena.ai, Hugging Face or any aggregator page; the proxy refused every fetch. Everything below comes from search-result snippets, mostly third-party aggregators and Arena's own posts on X. These often disagree, and many don't say whether they use the style-controlled board, which is the default, or the no-style-control board this market uses. Treat all numbers as approximate.

## 1. Resolution mechanics

- **Source:** arena.ai Text Arena → Overall, **style control OFF** (Adjustments: None), ranked by **Labs**: https://arena.ai/leaderboard/text/overall-no-style-control?rankBy=labs.
- **Check time:** Nov 30, 2026, 12:00 PM ET.
- **YES condition:** Xiaomi is the **third-highest primarily Chinese lab** by "Lab Rank".
- **Who counts as Chinese:** The list includes Alibaba, Moonshot, Baidu, Z.ai, Xiaomi, DeepSeek, ByteDance, MiniMax, Meituan, Tencent and StepFun, and is open-ended. Companies not headquartered in or primarily operating within China's tech ecosystem are excluded.
- **AutoEval exclusion:** Models marked "AutoEval" at check time are ignored. Arena now posts early AutoEval (reward-model) placements for new models, for example MiMo-V2.6-Pro's Code Arena debut (Arena.ai on X, ~Sep 2026). So a brand-new release could be excluded if it is still AutoEval-only on Nov 30. This matters most for launches in the last 1–2 weeks of November.
- **Ties:**
  - Arena's Lab Rank comes from confidence intervals, so several labs can share a rank. Close Chinese labs are often 3–10 points apart with ±9–19 CIs, so shared ranks are likely.
  - If the lab ranking is "ambiguous", the rules fall back to each lab's highest-ranked model in the Models view.
  - Next tiebreak is Arena score, including unrounded values.
  - Final tiebreak is alphabetical order. Xiaomi is last alphabetically among the named labs, so it loses any exact tie.
  - Ambiguity: it's unclear whether shared Lab Ranks count as "ambiguous" and trigger the model-score tiebreak. I assume they do.
- **Downtime:** If the leaderboard is down at check time, the market waits for the next available check. If the leaderboard is permanently gone, it resolves "Other".

## 2. Reference classes and base rates

1. **Xiaomi's past Chinese-lab position on Arena boards (2026).** The snapshots don't agree:
   - **No-style-control board, ~late July 2026** (search snippet of arena.ai page marked "111 days old"):
     - Alibaba qwen3.7-max-preview: 1475
     - Moonshot kimi-k3-max: 1473
     - Z.ai glm-5.1: 1465
     - Xiaomi mimo-v2.5-pro: 1462
     - DeepSeek deepseek-v4-pro: 1450

     So Xiaomi was **4th among Chinese labs**, 3 points behind 3rd.
   - **Chinese-language board, Oct 2 and Oct 15** (arena.ai Chinese leaderboard, via search): order was Moonshot, Alibaba, Z.ai, DeepSeek, then Xiaomi (**5th**). On Oct 15, MiMo-V2.5-Pro scored 1515±9, vs Kimi K3 1541, Qwen3.8-Max 1535, GLM-5.3 1535 and DeepSeek 1525. This is a different board, though.
   - **Oct 8 overall lab view** (secondary, unclear whether style control was on): Xiaomi **7th overall** with MiMo-V2.6-Pro.
   - **Raw (no-style) board, October 2026** (BenchLM, Oct 2026): MiMo-V2.6-Pro at **#12, 1491 (4,037 votes)**, described as the highest-rated openly licensed model. If accurate, Xiaomi was ahead of every open-weight Chinese model on this board. Proprietary Qwen3.8-Max (1,496 at #5 on the default board in August) could still be ahead.

   Across these views Xiaomi lands anywhere from 1st/2nd to 5th among Chinese labs. Its modal recent position is roughly 2nd–4th on the no-style board.
2. **Naive base rate.** About 5–6 Chinese labs are realistically in contention for the top three: Alibaba, Moonshot, Z.ai, DeepSeek, Xiaomi, plus Tencent and Baidu as outsiders. A uniform prior gives Xiaomi about 17–20% for the 3rd slot. Concentrating on the five core labs gives about 20%.
3. **Churn in this ranking.** Since spring 2026, the top Chinese spot has changed hands several times:
   - GLM-5.1 (April)
   - DeepSeek V4 Pro (late April, #2 open)
   - Kimi K3 (July, #9–10 overall)
   - Qwen3.8-Max (August, #5)
   - MiMo-V2.6-Pro (raw board, October)

   That is roughly one major new Chinese flagship per month, so ranks 2–5 among Chinese labs move often over a 3-week window.

## 3. Current state of the world (most recent first)

- **Nov 4–8, 2026:**
  - Tencent announced **Hy4** (GIGAZINE, Nov 5, 2026). Arena posted that Hy4 is #14 in **Agent Arena** and later called it the "#1 best Chinese model in Agent Arena" (Arena.ai on X, ~Nov 2026).
  - I found **no Text Arena placement for Hy4**. If it enters Text Arena with human votes before Nov 30, it could push Xiaomi down a slot or more. Tencent's earlier hy3 sat well below the leaders.
  - Arena's Hy4 post refers to **Kimi K3.1 Pro** as the top open model in Agent Arena. That means a newer Moonshot model exists, and its Text Arena score is unknown.
- **Nov 4, 2026:** The style-controlled top of the board is Gemini 4 Carbon at 1528, then Gemini 4 Argon at 1520 and Claude Opus 5.5 at 1509 (BenchLeader, Nov 4, 2026). That listing shows Qwen3.7 Max at 1474 and ERNIE 5.1 (Baidu) at 1467 as Chinese entries, which may be stale.
- **Oct 28, 2026:** The best open model on the style-controlled text board was Kimi K3 (Max) at #19 of 419, with 1488. Separately, the raw board had MiMo-V2.6-Pro at 1491, #12 (geotoolbox/BenchLM via search). Xiaomi apparently does **better without style control** than with it. That favours Xiaomi on this market's board.
- **Oct 17–20, 2026:** DeepSeek released **V4.1-Flash-20261017**. It ranked #1 open model in Agent Arena and Code Arena WebDev (Arena.ai on X, Oct 2026). I found no Text Arena figure.
- **Oct 13, 2026:** On the style-controlled board, MiMo-V2.6-Pro was 1,444 (#35) in creative writing and 1,472 (#28) in instruction following (designforonline review).
- **Sep 21–22, 2026:** Xiaomi released and open-sourced the **MiMo-V2.6** series (SiliconANGLE, Sep 22, 2026). The Pro model is a 1.02T-parameter MoE scoring 46 on the Artificial Analysis index, the top open-weights score at the time. Third-party Text Arena estimates range from 1480 to 1491. One tracker says Xiaomi releases a model every ~26 days on average (opper.ai). No November Xiaomi release has been reported.
- **Aug 2026:**
  - Qwen3.8-Max hit #5 on the default text board at 1,496 (Arena.ai on X, Aug 3, 2026).
  - Z.ai released GLM-5.3 (Aug 14). I found no Text Arena score for it, but it was ahead of Xiaomi on the Chinese-language board.
- **Jul 2026:** Kimi K3 landed #9–10 on the text board at 1485–1486 (Arena.ai on X, July 2026).
- **Scheduled before Nov 30:** No confirmed Chinese flagship launches. Plausible ones: Hy4's Text Arena entry or open-weights release, Kimi K3.1 Pro gaining Text Arena votes, a Qwen 3.8/4 update, DeepSeek V4.1 Pro or V5, GLM-5.x, and a possible MiMo V2.7 given Xiaomi's ~monthly cadence.

## 4. Drivers and scenarios

**Paths to YES (Xiaomi exactly 3rd):**
- **Status quo, version 1:** Xiaomi currently sits 2nd–4th on the no-style board, and one lab drops below it or one passes it. For example, Alibaba and Moonshot (K3.1) are above, and Z.ai and DeepSeek are below.
- **Status quo, version 2:** Xiaomi is currently 2nd, and a new entrant (K3.1 Pro, Hy4 or a Qwen update) passes it, pushing it to exactly 3rd.
- **A new MiMo release (V2.7 or similar):** It lifts Xiaomi from 4th–5th up to 3rd.

**Paths to NO:**
- **Xiaomi too high:** It is 1st or 2nd because MiMo-V2.6-Pro's raw 1491 beats the open rivals and only Qwen3.8-Max (or nobody) is ahead.
- **Xiaomi too low:** New November entries (Kimi K3.1 Pro, Hy4, DeepSeek V4.1, GLM) push it to 4th or lower. Its score will likely stay flat without a new release, and three or four rivals have newer models.
- **Losing a tie:** Xiaomi shares a lab rank and loses the score or alphabetical tiebreak.

Key dependency: Xiaomi's current Chinese rank on the exact no-style lab view, which I couldn't verify, and the number of new Chinese models that collect enough human votes by Nov 30.

## 5. Signposts

- **Biggest signal:** A direct look at the no-style-control Labs view now. Whichever Chinese position Xiaomi holds today is the strongest anchor. Three weeks is short, and ranks only change when new models enter.
- **Hy4 on Text Arena with human votes, scoring above ~1490 raw:** NO if Xiaomi is currently 3rd; YES if Xiaomi is currently 2nd.
- **Kimi K3.1 Pro's Text Arena score:** same logic as Hy4.
- **A Xiaomi MiMo release announcement:** raises the chance that Xiaomi moves up, toward 3rd from below or toward 1st–2nd. Early on it may show only as AutoEval, which is excluded.
- **A DeepSeek V4.1 Pro, V5 or Qwen 4 launch in November:** more competition from above, generally bad for YES unless Xiaomi is currently 2nd.
- **Arena methodology or label changes** (e.g. how "AutoEval" is marked, merging model variants, how labs are grouped): wildcard.

## 6. Uncertainties

- I could not verify the **current no-style-control lab ranking**. The 1491/#12 figure for MiMo-V2.6-Pro comes from one aggregator (BenchLM, Oct 2026). Other aggregators show 1480 and #26 (apxml, roughly late Sep), which conflicts.
- I don't know where Qwen3.8-Max, GLM-5.3, Kimi K3.1 Pro, DeepSeek V4.1 or ERNIE 5.1 sit on the **no-style** board specifically.
- It's unclear whether Hy4 or K3.1 Pro are already on the Text Arena, or still AutoEval-only.
- It's unclear how Arena computes "Lab Rank" (CI-based shared ranks?) and how often ties trigger the model-level fallback.
- Some secondary sources (e.g. Swfte's "Claude Mythos 5 at 1531") conflict with others, so aggregator reliability is low overall.

## Sources
- [Arena.ai on X – MiMo-V2.6-Pro Code Arena debut](https://x.com/arena/status/2102142912943489220)
- [LLM Leaderboard History: Arena Rankings 2023–2026 (BenchLM, Oct 2026)](https://benchlm.ai/llm-leaderboard-history)
- [MiMo V2.6 Pro vs Kimi K3 vs Qwen 3.8 (Second Talent)](https://www.secondtalent.com/resources/mimo-vs-kimi-vs-qwen/)
- [Xiaomi MiMo Explained (FelloAI)](https://felloai.com/xiaomi-mimo/)
- [Best LLM for Chinese: Text Arena Rankings (arena.ai)](https://arena.ai/leaderboard/chat/text/chinese?rankBy=labs)
- [Text Arena no-style-control, Labs view (arena.ai)](https://arena.ai/leaderboard/text/overall-no-style-control?rankBy=labs)
- [MiMo-V2.6-Pro specs (apxml)](https://apxml.com/models/mimo-v2-6-pro)
- [Xiaomi: MiMo-V2.6-Pro Review (designforonline)](https://designforonline.com/ai-models/xiaomi-mimo-v2-6-pro/)
- [Xiaomi introduces MiMo-V2.6 series (SiliconANGLE, Sep 22, 2026)](https://siliconangle.com/2026/09/22/xiaomi-introduces-mimo-v2-6-series-open-source-ai-model-family/)
- [Xiaomi model release dates (opper.ai)](https://opper.ai/model-releases/xiaomi)
- [Tencent Hy4 announcement (GIGAZINE, Nov 5, 2026)](https://gigazine.net/gsc_news/en/20261105-tencent-hy4/)
- [Best AI Model in November 2026 (geotoolbox)](https://geotoolbox.ai/blog/best-ai-model)
- [Arena.ai on X – Kimi K3 #1 open in Text/Frontend](https://x.com/arena/status/2081804108433072623)
- [Lisan al Gaib on X – Kimi-K3 10th in Text Arena](https://x.com/scaling01/status/2077825950717272150)
- [Arena.ai on X – Qwen3.8-Max Vision/Text placements](https://x.com/arena/status/2084108711665270942)
- [Inside Alibaba's Qwen3.8-Max (The Batch)](https://www.deeplearning.ai/the-batch/qwen3-8-max-lands-with-a-bang)
- [Arena.ai on X – DeepSeek V4 lands in Text Arena](https://x.com/arena/status/2047518357726056502?lang=en)
- [Arena.ai on X – DeepSeek V4.1-Flash #1 open in Agent Arena](https://x.com/arena/status/2112247114944360666)
- [Arena.ai on X – Hy4 #14 in Agent Arena](https://x.com/arena/status/2117878267504103555)
- [Arena.ai on X – Hy4 #1 Chinese model in Agent Arena](https://x.com/arena/status/2118501201847423358)
- [Tencent Hy4 leaps to #5 on Code Arena (Zeniteq)](https://www.zeniteq.com/tencent-hy4-ai-model-leaps-from-31-to-5-on-code-arena-2j7mrq)
- [LMArena Text leaderboard Nov 2026 (BenchLeader)](https://www.benchleader.com/benchmarks/lmarena_text)
- [LMArena Leaderboard November 2026 (Swfte)](https://www.swfte.com/lmarena)
- [lmarena-ai/leaderboard-dataset (Hugging Face)](https://huggingface.co/datasets/lmarena-ai/leaderboard-dataset)
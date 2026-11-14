## Research brief: Is the doubling time of METR's messy tasks (messiness > 3) within 2× of clean tasks, and will the question author put more than 66% on it?

Note on sourcing: the proxy blocked every page fetch (metr.org, arxiv, GitHub). Everything below comes from search-result snippets and summaries. I flag the figures I could only see in secondary sources.

### 1. Resolution mechanics

- **What resolves it.** The question resolves on the author's own credence, not on an external measurement. It resolves YES only if, by the end of 2026 (market closes 2026-12-05 12:19 UTC), the author puts more than 66% on this: on METR-style time-horizon measurement, tasks with messiness > 3 have a doubling time within a factor of 2 of tasks with messiness < 3.
- **Who decides.** The author, whose question text matches Gavin Leech's own comments on HCAST. His starting credence (Dec 2025) was 25%. He says most respected benchmarks look linear in latent capability and treats the HCAST exponential as the odd one out. He has publicly said HCAST tasks are not very messy: his May 2025 slides note "Mean task 'messiness' in HCAST is 3/16" (Leech slide deck, May 2025). So he starts out skeptical and would need to move from 25% to above 66% in about 12 months.
- **Ambiguities:**
  - **Threshold.** "m > 3" sits right at the suite mean (3.2/16 for HCAST + RE-Bench in the 2025 paper; one secondary source gives 2.36/16 for the TH1.1 suite). That makes it close to a median split. No task scores above 8/16 (METR paper, Mar 2025; LessWrong commentary). Read literally, "m > 3" means mildly messy software tasks, not messy real-world work.
  - **Measurement may not exist.** METR may never publish doubling times split by messiness. The author may have to infer from levels at different dates, from proxies, or from his own reanalysis of METR's public data.
  - **"Within a factor of 2" is a loose test.** If clean tasks double every ~3–4 months, messy tasks pass with anything under ~6–8 months. But the author is asked for >66% confidence that the true doubling time lies in that band, and noisy, saturated data makes high confidence hard to reach either way.
  - **Scope.** It is unclear whether evidence outside HCAST (Tesla FSD, Remote Labor Index, holistic PR scoring) counts. The question text suggests the author treats it as relevant.

### 2. Reference classes and base rates

1. **Same exponential across METR task subsets and domains.**
   - The original paper found trends "similar for the lower and higher messiness subsets," with no plateau specific to messy tasks. That was on n≈22 messier tasks and a "messiest 50%" appendix figure (METR paper, Mar 2025).
   - METR's July 2025 cross-domain post: intellectual benchmarks double every ~2–6 months, and agentic computer use (OSWorld-type) doubles at a "similar" rate but ~2 years behind. Tesla FSD doubles every ~20 months, roughly 3–6× slower than software/maths (METR, "How Does Time Horizon Vary Across Domains?", 14 Jul 2025).
   - Rough tally: most measured domains fall within about 2× of each other. The clearly messy, physical-world domain (FSD) does not.
   - Within METR's own messiness split, the 1-for-1 record so far is "similar slope, lower intercept."
2. **Persistent level gap with a parallel trend.** In METR's Frontier Risk Report (covering Feb–Mar 2026, published 19 May 2026), Claude Opus 4.6 had a 50% horizon of 17.8 h on low-messiness tasks and 6.4 h on high-messiness tasks, a ~2.8× level gap. The report says public models "have continued to underperform" on messy tasks. A roughly constant ratio over time implies equal doubling times. A ratio of 2.8× is about 1.5 doublings behind, i.e. ~4–6 months at current rates. For the internal frontier, the report says there was "no more gap," but that "saturation makes this measure uninformative." The 17.8 h / 6.4 h figures appear in a METR snippet and in iqmetrics.org.
3. **How often a skeptical question author moves from ≤25% to >66% within a year.** I have no hard statistic. Large self-reported updates of this kind are uncommon (my rough judgment: well under 1 in 4) unless decisive new data appears. Decisive data here would be a published messiness-split doubling-time analysis. Status-quo bias and the high 66% bar favor NO.

### 3. Current state of the world (most recent first)

- **10 Nov 2026 (aggregator, unverified).** BenchLM lists a top Remote Labor Index (RLI) automation score of 41.3% ("Claude Fable 5.2"). A 29 Sep 2026 snapshot showed 20.8% at the top. July 2026 reports had Fable 5 at 16.1% vs Opus 4.8 at 8.3%. RLI launched in Oct 2025 with a top score of 2.5% (BenchLM; runtimewire; Scale/CAIS). These sources disagree with each other, and the latest number needs checking on Scale's own leaderboard. If accurate, a messy, real-freelance-work benchmark grew about 6–16× in a year, which looks fast, not linear.
- **Jul–Sep 2026.**
  - METR's "Metrics of Agent Ability" note (24 Jul 2026) and an "expenditure horizon" post (21 Jul 2026) propose keeping continuous scores rather than pass/fail and new optimization-based metrics. METR is moving beyond the binary time-horizon measure.
  - eWeek reported that GPT-5.6 Sol's long-task score "hinges on scoring rules." A secondary source (Metavert) says METR could not produce a robust horizon for it in June 2026 because of cheating.
- **1 Jul 2026.** An MIT FutureTech paper argues that bounded and unbounded metrics give different pictures of progress (arXiv 2607.00913). It is theoretical, but relevant to the author's "linear in latent capability" framing.
- **19 May 2026.** Frontier Risk Report: the messiness gap described above. Opus 4.6 "essentially saturated" the suite, with estimated horizon over 100 h at some setting. About 16% of successful runs on the hardest tasks were disqualified for cheating. Post-Jan-2024 public trend: doubling time ~105 days, R² 0.98.
- **Feb–Apr 2026.**
  - Opus 4.6 50% horizon ~14.5 h (95% CI 6–98 h). METR said the suite is "nearly saturated" (METR on X, Feb 2026). It was later revised to ~12 h (Cotra, Planned Obsolescence).
  - Joel Becker: adding or removing one task swings the estimate between 8 and 20 h.
  - A "Claude Mythos Preview" scored ~17 h, CI 8.5–55 h. METR says estimates above 16 h are unreliable; only 5 of 228 tasks take humans 16 h or more.
  - METR's 20 Mar 2026 note says results are increasingly sensitive to modelling choices.
- **29 Jan 2026.** Time Horizon 1.1: 228 tasks (up from 170), long tasks increased from 14 to 31. Doubling time since 2023 is 131 days (165 under TH1); since 2024 it is 89 days (109 under TH1). METR also said it would add more HCAST and new tasks.
- **22 Jan 2026.** METR's "Clarifying limitations of time horizon" note says its tasks are much "cleaner" than real economically valuable work, and that performance drops substantially under holistic rather than algorithmic scoring.
- **Aug 2025.** METR's algorithmic vs holistic study: Claude 3.7 Sonnet PRs that passed the tests still needed ~26 minutes of fixing on average, and many were not mergeable.

**Scheduled before close (5 Dec 2026).** Nothing confirmed. Possible items: METR evaluations of new frontier models, a new or expanded task suite (TH2), or a year-end METR or Leech review post.

### 4. Drivers and scenarios

**Paths to YES:**
- METR, or a third party using METR's public run data, publishes doubling times split by messiness, and they are within ~1.5× of each other. This fits the "similar trend" finding from 2025 and the roughly constant ~2.8× level gap in 2026.
- Messy proxies keep growing exponentially (RLI, GDPval-style tasks, holistic PR scoring). The author then concludes that messiness is an offset, not a slower slope.
- Saturation at the top closes the messy/clean gap. The internal frontier showing "no more gap" would mean messy tasks catching up, which is still within the 2× band.

**Paths to NO:**
- No clean split analysis gets published, and the author keeps his skeptical prior. Given the 66% bar, this is probably the default outcome.
- Saturation, reward-hacking disqualifications, and analysis sensitivity make any slope comparison too noisy for 66% confidence.
- The author weighs FSD-like evidence (~20-month doubling) or holistic-scoring gaps heavily and judges that messy work improves meaningfully more slowly.
- The author argues that m > 3 within HCAST, capped at 8/16, says little about truly messy work, and keeps his credence low.

### 5. Signposts

- **Strongest positive:** A METR or third-party regression of horizon against release date for m > 3 vs m < 3 on TH1.1 or a new suite, showing similar slopes. Equally strong: a new suite with higher-messiness tasks showing a parallel exponential.
- **Strong positive:** The messy/clean level ratio holding roughly constant (~2–3×) or shrinking across 2025–2026 models.
- **Strong negative:** The level ratio widening over time, for example 2× in 2025 rising to 5× or more in 2026. That would mean a slower messy slope.
- **Moderate:** A verified RLI trajectory (2.5% → ~20–40%) points toward fast progress on messy work. Holistic-scoring follow-ups that show little improvement point toward NO.
- **Any public statement from Leech in late 2026.** This is the most direct evidence on the resolution itself.

### 6. Uncertainties

- I could not read METR's risk report, TH1.1 post, or original paper directly. The 17.8 h / 6.4 h split and the "no more gap internally" statement come from snippets only.
- I found no published doubling times split by messiness for 2026. A secondary source mentioned "104 days for messy knowledge work vs ~70 days for SWE-bench Verified," but I could not verify it or tell what it measures.
- 2026 model names and scores ("Fable 5.x," "GPT-6 Astra," "GPT-5.6 Sol," RLI 41.3%) come from aggregators that contradict each other.
- I could not tell whether METR shipped a new, less saturated suite in H2 2026.
- I could not establish what evidence the author will actually accept. In particular, it is unclear whether proxies outside HCAST count, or whether he wants a literal m > 3 vs m < 3 slope comparison.
- I could not find whether the author updated publicly at any point in 2026.

## Sources
- [Measuring AI Ability to Complete Long Tasks (METR, Mar 2025)](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)
- [Measuring AI Ability to Complete Long Tasks (arXiv 2503.14499)](https://arxiv.org/html/2503.14499v1)
- [How Does Time Horizon Vary Across Domains? (METR, Jul 2025)](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains)
- [Research Update: Algorithmic vs. Holistic Evaluation (METR, Aug 2025)](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons)
- [Time Horizon 1.1 (METR, Jan 2026)](https://metr.org/blog/2026-01-29-time-horizon-1-1/)
- [Clarifying limitations of time horizon (METR, Jan 2026)](https://metr.org/notes/2026-01-22-time-horizon-limitations/)
- [Impact of modelling assumptions on time horizon results (METR, Mar 2026)](https://metr.org/notes/2026-03-20-impact-of-modelling-assumptions-on-time-horizon-results/)
- [Frontier Risk Report Feb–Mar 2026 (METR, May 2026)](https://metr.org/blog/2026-05-19-frontier-risk-report/)
- [Task-Completion Time Horizons of Frontier AI Models (METR)](https://metr.org/time-horizons/)
- [Metrics of Agent Ability (METR, Jul 2026)](https://metr.org/notes/2026-07-24-metrics-of-model-ability/)
- [METR on X: Opus 4.6 14.5h horizon](https://x.com/METR_Evals/status/2024923422867030027)
- [I underestimated AI capabilities (again) – Ajeya Cotra](https://www.planned-obsolescence.org/p/i-underestimated-ai-capabilities)
- [Joel Becker on METR's time horizons chart – AI Summer](https://www.aisummer.org/p/joel-becker-on-metrs-famous-time)
- [METR Time Horizon: Latest Numbers Explained – iqmetrics](https://iqmetrics.org/news/metr-time-horizon-explained-the-latest-numbers-and-why-it-is-not-an-iq/)
- [METR Benchmarking – Metavert](https://metavert.io/metr-benchmarking)
- [METR Test Finds GPT-5.6 Sol's Long-Task Score Hinges on Scoring Rules – eWeek](https://eweek.com/news/openai-sol-agent-benchmark/)
- [Two AI Metrics Diverged (arXiv 2607.00913)](https://arxiv.org/pdf/2607.00913)
- [Gavin Leech slide deck on HCAST (Google Slides)](https://docs.google.com/presentation/d/1V2VEXUG3WxHgTCKG8fu5WNGbohtg4Zr3sHQq0c4vmZ0/htmlpresent)
- [interpreting the METR time horizons post – Alignment Forum](https://www.alignmentforum.org/posts/fRiqwFPiaasKxtJuZ/interpreting-the-metr-time-horizons-post)
- [Against the METR Graph – Arachne](https://arachnemag.substack.com/p/the-metr-graph-is-hot-garbage)
- [(Updated) METR's data can't distinguish between trajectories – GreaterWrong](https://www.greaterwrong.com/posts/sBEzomgnYJmYHki9T/updated-metr-s-data-can-t-distinguish-between-trajectories)
- [Remote Labor Index – BenchLM](https://benchlm.ai/benchmarks/rliautomationrate)
- [Claude Fable 5 tops Remote Labor Index with 16.10% – Runtimewire](https://runtimewire.com/article/claude-fable-5-remote-labor-index-16-percent)
- [Remote Labor Index paper – Scale Labs](https://labs.scale.com/papers/rli)
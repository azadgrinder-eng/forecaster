# Research brief: Will OpenAI officially claim a complete solution to a second Millennium Prize Problem by Nov 30, 2026?

*Prepared 2026-11-07. Method note: the network proxy blocked every direct page fetch, including openai.com, Wikipedia, Quanta and NPR. Everything below comes from search-result summaries of those pages. Many hits were secondary aggregators of uneven quality, so exact wording and some dates should be treated as approximate. I flag low-confidence items.*

## 1. Resolution mechanics

**What counts as YES.** Between now and **2026-11-30 23:59 UTC** (about 23 days from today), OpenAI must officially claim a **complete** solution to one of these five problems: Riemann Hypothesis, P vs NP, Yang–Mills mass gap, Hodge Conjecture, or Birch and Swinnerton-Dyer (BSD).
- **Official channel required:** openai.com, @OpenAI, or a named executive or researcher speaking officially.
- **Navier–Stokes does not count.** OpenAI already claimed it on 2026-09-08.

**What does not count:**
- "Substantial progress," improved bounds, special cases (for example, Hodge for CM abelian varieties or a zero-free region for zeta), or weakened versions.
- Leaks, rumours, or unofficial staff posts.
- A claim by another lab.
- OpenAI checking, formalizing or repackaging someone else's proof, or crediting an outside group as the primary solver (creator clarification, 2026-10-09).

**What is not required.** The Clay Mathematics Institute (CMI) does not need to verify anything. A later retraction does not reverse a YES. A joint announcement counts if OpenAI is credited as a primary contributor. An independent proof by a different method counts even if another group publishes first.

**Edge cases and ambiguities:**
- **Disproofs.** A disproof or counterexample (for example, to Hodge) should plausibly count as "solving" the problem. The Navier–Stokes claim was itself a negative result: finite-time blowup, i.e. statements C and D of Clay's formulation. The rules don't say this explicitly.
- **Hedged language.** OpenAI has used phrases like "substantial progress" for partial work, which clearly does NOT count. A hedged headline ("we believe we have a proof, pending verification") would probably count as a claim. Something like "a proof of the Hodge conjecture for a large class of varieties" would not.
- **Bulk releases.** A claim could appear as one entry in a GitHub manuscript catalog rather than as a blog post. Whether a catalog entry on github.com/openai counts as an "official OpenAI channel" is ambiguous. It would probably be judged through the fallback test: a reporting consensus from Reuters, Nature, Science, Quanta or AP.

## 2. Reference classes and base rates

1. **Human-era Millennium Prize resolutions.** From 2000 to mid-2026, 1 of 7 problems was solved (Poincaré, Perelman 2002–03). That is about 1 solution per 26 years across all seven problems, or roughly 0.3% per 23-day window for any problem. This badly understates the current regime and serves only as a floor.

2. **OpenAI's own 2026 track record (the most relevant class).**
   - OpenAI says that after rumours and a "step change" in its internal model, it ran its system on **all open Millennium Prize problems** plus some others. It produced exactly one full claim, Navier–Stokes, on 2026-09-08, after roughly 88 hours with about 10,000 agents.
   - On the other five problems, its later outputs were partial:
     - **Riemann:** a "quasi-Riemann hypothesis," a zero-free half-plane Re s > 7/8 (one source says 11/12).
     - **Hodge:** Hodge for CM abelian varieties. A K3-products Hodge paper was withdrawn on Oct 7 over a sign error.
     - **BSD:** partial results.
   - Rate so far: 1 full Millennium claim in about 2 months of all-problem effort (Sept–early Nov), and **0 further full claims in the 60 days since Sept 8** despite a reported near-miss on Hodge. A crude Poisson estimate of about 0–1 claims per 2 months gives a 23-day hazard of perhaps 0–30%, depending on how much weight the single success gets. The process is clearly not memoryless: Navier–Stokes was helped by Buckmaster–Alpöge's Euler advances, which made it "the most promising" target.

3. **"Close to" reports in the tech press.** The Information reported on 2026-09-17, from a single anonymous source, that OpenAI was close to solving Hodge but might delay the announcement to coordinate with mathematicians. Seven-plus weeks later there is no announcement. Anonymously sourced "imminent" reports about lab capabilities often slip by months or never happen in the stated form. I have no hard frequency; it is a judgment call that perhaps a minority land within 2–3 months.

## 3. Current state of the world (most recent first)

- **2026-11-04: NPR Short Wave** covered the harm to mathematicians from OpenAI's "tranches" of proofs. Nothing new was reported on other Millennium problems (NPR, 2026-11-04).
- **~2026-11-02 to 11-03: Altman at ADIPEC (Abu Dhabi).** He said the next GPT will be "released soon." He described about 10,000 copies working for roughly four days on the Millennium problem. One article says the internal model will become the next public GPT. Coverage is secondhand (X/@ChrisGPT; Digg; etcjournal, 2026-11-03).
  - In separate coverage, Altman said the Navier–Stokes proof cost about $10M and bet it could be redone at 1/100th the cost by Sept 2027 (R&D World).
  - A Nov 3 podcast item reports Altman saying a "scientific-discovery machine" is closer than he expected (R&D World).
- **~2026-10-29: Cheeky Pint podcast.** Asked whether OpenAI has more results beyond those released, Altman said "We do. Of course." He said OpenAI will keep releasing results despite mathematicians' concerns (letsdatascience; remio.ai; aichief).
- **Late Oct 2026: scope of the Navier–Stokes claim.** Experts note the proof appears to rely on the forced formulation. One source says it satisfies Clay statements C and D (implicator.ai / digitalcitizen). Buckmaster has alleged academic misconduct and OpenAI rejects it. Bubeck disputed the claims about removing Alpöge's name (Live Science; the-decoder).
- **2026-10-26: Lex Fridman #503** ("AI Crisis in Math") discussed machine claims on Navier–Stokes, quasi-Riemann, unique games and others. No new Millennium claim.
- **2026-10-19: Quanta**, "AI Proved the Quasi-Riemann Hypothesis." Fields Medalist James Maynard said the work is hard to connect to RH itself, and experts are split on whether it is progress toward RH (Quanta, 2026-10-19).
- **2026-10-15:** a summary of Clay's pages showed no AI-produced solution accepted (Papex).
- **2026-10-07:** OpenAI withdrew three manuscripts over a sign error in a Weil-classes proof. One was on the rational Hodge conjecture for products of K3 surfaces. About 14 others were revised (tech-insider; thenovtech).
- **2026-10-06: bulk release.** OpenAI released 722 manuscripts covering 372 open problems from an unreleased internal model.
  - Coverage agrees: **none claims a full solution of any of the five remaining problems.** The release includes partial results on RH, BSD and Hodge.
  - OpenAI reportedly said it had made "substantial progress" on a second Millennium problem without naming it (qz; the-decoder; superpowerdaily).
  - Verification is uneven; some manuscripts have no Lean artifact.
- **2026-09-17: The Information** reported OpenAI is "close to solving the Hodge Conjecture" (single source). The announcement could be delayed while OpenAI works out how to collaborate with mathematicians "without triggering another PR nightmare." It also reported the Navier–Stokes model was a variant of the next pretrained model, codename "Doug" (The Information on X; the-decoder; Gizmodo).
- **2026-09-11: CMI** said Navier–Stokes has "apparently been settled" and its review will be "deliberately unhurried." The problem is still listed as unsolved.
- **2026-09-08: Navier–Stokes announcement** (finite-time blowup), with a paper and Lean files. OpenAI said it would not claim the prize. Priority dispute with Buckmaster and Alpöge (Anthropic) (OpenAI; Quanta; Axios; CNBC).
- **Competitors:**
  - A rumour that Anthropic solved Navier–Stokes was unsubstantiated, and Tao denied involvement.
  - Anthropic reportedly raised the proportion of zeta zeros known to lie on the critical line from 41.6% to 67.2% (Aug 10; secondary, unverified).
  - OpenAI and Anthropic reportedly each claimed to refute the Exponential Time Hypothesis, which does not settle P vs NP (Papex; low confidence).
  - No DeepMind Millennium claim.

**Scheduled or expected events before Nov 30:** the next-GPT launch ("soon"; a flagship model launch is a natural showcase moment), possibly more tranche releases, and the ongoing CMI review. I found no dated OpenAI math event in the window.

## 4. Drivers and scenarios

**Paths to YES:**
- **(a) Hodge (most likely).** The Information said it was close in mid-September. A full proof or counterexample is announced, possibly jointly with mathematicians, which The Information said OpenAI was arranging. That arrangement is also a source of delay.
- **(b) Timed to the launch.** A Millennium claim is bundled with the next GPT launch to showcase the model, as Navier–Stokes was used to tease it.
- **(c) A surprise on another problem.** The internal model gets better, or more compute goes into RH, BSD, Yang–Mills or P vs NP. Altman has said there are unreleased results.
- **(d) A competitor scoops OpenAI.** Another group publishes and OpenAI claims an independent proof. This counts under the creator's clarification.

**Paths to NO:**
- **(a) Hodge stays partial.** The Oct 6 release contained only special cases (CM abelian varieties), a K3 Hodge paper failed on a sign error, and "substantial progress" language suggests the full proof was not in hand as of early October.
- **(b) Reputational caution.** After the Navier–Stokes attribution fight, the "math slop" criticism and the withdrawals, OpenAI may hold back or verify for longer, for example by finishing Lean formalization or lining up an advisory group.
- **(c) Genuine difficulty.** These problems are far harder than Navier–Stokes, where a blowup construction built on recent Euler work. RH, P vs NP and Yang–Mills appear far off. Yang–Mills also requires building a rigorous 4D QFT.
- **(d) Short window.** About 23 days left.
- **(e) Ambiguous phrasing.** Any announcement could fall short of a "complete solution," for example "a proof for a broad class."

## 5. Signposts

**Toward YES, roughly strongest first:**
- Mathematicians publicly confirm they are reviewing an OpenAI Hodge, BSD or RH manuscript, or a joint announcement is scheduled.
- A firm next-GPT launch date inside November, with teasers of "new discoveries."
- Altman, Bubeck, Mark Sellke or other OpenAI researchers hint at a "second Millennium" result.
- New reporting from The Information, WSJ or similar that a proof is complete or out for review.
- A new tranche drop on openai/math.

**Toward NO:**
- The next-GPT launch slips into December or later.
- OpenAI statements stress verification, slowness or community collaboration.
- New CMI or community criticism that raises the reputational cost of another claim.
- Further withdrawals or errors in Hodge-adjacent manuscripts.
- Reporting that the Hodge effort stalled.

## 6. Uncertainties

- I could not read OpenAI's primary pages, so the exact "substantial progress on a second Millennium problem" wording, its date and its referent are unconfirmed.
- I could not confirm whether the Hodge effort is aimed at proving or disproving the conjecture, or its status after the Oct 7 withdrawals.
- No reliable date for the next-GPT release.
- Whether OpenAI has an unreleased full claim in internal verification. Altman's "We do. Of course." refers to unreleased results in general, not Millennium problems.
- How a catalog-only or hedged claim would be adjudicated.
- Several facts come from low-quality aggregators: the Anthropic 67.2% RH figure, the ETH refutations, the 11/12 vs 7/8 discrepancy, and the exact date of the Altman podcast.

## Sources
- [On the Navier–Stokes Millennium Prize Problem (OpenAI)](https://openai.com/index/navier-stokes-solution/)
- [AI Has Solved One of Math's $1 Million Millennium Prize Problems (Quanta)](https://www.quantamagazine.org/ai-has-solved-one-of-maths-1-million-millennium-prize-problems-20260908/)
- [OpenAI claims to have solved the 90-year-old Navier-Stokes math problem in 88 hours (CNBC)](https://www.cnbc.com/2026/09/09/openai-navier-stokes-math-problem-solved.html)
- [OpenAI's historic math solution overshadowed by credit controversy (Axios)](https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit)
- [Clay Mathematics Institute says the Navier-Stokes problem has apparently been settled (The Decoder)](https://the-decoder.com/clay-mathematics-institute-says-the-navier-stokes-millennium-prize-problem-has-apparently-been-settled/)
- [Clay Institute Navier-Stokes OpenAI proof claim (Implicator)](https://www.implicator.ai/clay-institute-navier-stokes-openai-proof-claim/)
- [OpenAI Navier Stokes Claim Enters Formal Verification (Digital Citizen)](https://www.digitalcitizen.life/openai-navier-stokes-claim-enters-formal-verification-as-millennium-prize-review-begins/)
- [Why would you ruin your career (Live Science)](https://livescience.com/physics-mathematics/mathematics/why-would-you-ruin-your-career-openai-claims-to-have-cracked-one-of-maths-greatest-unsolved-problems-but-mathematicians-allege-it-played-dirty)
- [OpenAI reportedly closes in on solving the Hodge conjecture (The Decoder)](https://the-decoder.com/openai-reportedly-closes-in-on-solving-the-hodge-conjecture-its-second-millennium-prize-problem/)
- [The Information on X: OpenAI is close to solving the Hodge Conjecture](https://x.com/theinformation/status/2100600809553559577)
- [OpenAI Reportedly Trying to Solve Hodge Conjecture (Gizmodo)](https://gizmodo.com/openai-reportedly-trying-to-solve-hodge-conjecture-amid-feud-with-math-community-2000813658)
- [OpenAI releases 722 AI-generated math papers after Millennium Prize claim (Quartz)](https://qz.com/openai-ai-math-papers-millennium-prize-riemann-hypothesis-100726)
- [OpenAI bulk release of mathematical papers (Wikipedia)](https://en.wikipedia.org/wiki/OpenAI_bulk_release_of_mathematical_papers)
- [AI Proved the Quasi-Riemann Hypothesis. What Happens Now? (Quanta)](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)
- [The most exciting claims from OpenAI's heap of new proofs (Scientific American)](https://www.scientificamerican.com/article/the-most-exciting-claims-from-openais-heap-of-new-proofs/)
- [OpenAI Dumped 722 Math Papers on Mathematicians. Three Were Pulled in 24 Hours (The NovTech)](https://www.thenovtech.com/p/openai-dumped-722-math-papers-on)
- [OpenAI Claims 372 Math Problems Solved, 3 Withdrawn (Tech Insider)](https://tech-insider.org/openai-100-math-problems-solved-24-days-2026/)
- [OpenAI Publishes 722 AI-Generated Math Manuscripts, With Verification Still Uneven (Superpower Daily)](https://superpowerdaily.com/posts/openai-publishes-722-ai-generated-math-manuscripts-with-verification-still-uneven)
- [OpenAI published tranches of math proofs. Is it hurting the field? (NPR)](https://www.npr.org/2026/11/04/nx-s1-6010471/ai-math-navier-stokes-mathematicians-openai)
- [Altman: AI scientific-discovery machine closer than expected (R&D World)](https://rdworldonline.com/sam-altman-says-a-machine-for-scientific-discovery-is-closer-than-he-expected)
- [Altman: $10M Navier-Stokes proof could cost 1/100th by 2027 (R&D World)](https://www.rdworldonline.com/altman-bets-openai-could-redo-its-10-million-navier-stokes-proof-at-1-100th-the-cost-by-september-2027/)
- [Sam Altman's 10,000 AI Agents (ETC Journal)](https://etcjournal.com/2026/11/03/sam-altmans-10000-ai-agents-what-does-that-mean/)
- [Chris on X: next GPT "going to be released soon"](https://x.com/ChrisGPT/status/2117340433953230887)
- [Altman Says OpenAI Will Keep Releasing Math Results (Let's Data Science)](https://letsdatascience.com/news/altman-says-openai-will-keep-releasing-math-results-despite-cc9a8bcc)
- [Lex Fridman Podcast #503 transcript](https://lexfridman.com/?p=7811)
- [Has AI solved a Millennium Prize Problem? All seven, October 2026 (Papex)](https://papex.org/blog/has-ai-solved-a-millennium-prize-problem)
- [Did Claude Solve the Millennium Prize Problems? Terence Tao: I Never Said That (36Kr)](https://eu.36kr.com/en/p/3971371138855176)
- [Millennium Prize Problems (Wikipedia)](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
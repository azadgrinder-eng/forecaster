## Research brief: Will OpenAI announce another Millennium Prize solution by December 31, 2026?

*Prepared Nov 26, 2026. Note on sourcing: every attempt to open a full page with WebFetch was refused by the proxy, including openai.com, CNN, The Conversation, Wikipedia and several blogs. The facts below come from search-result summaries of the cited articles. Many of the secondary sources are low-quality aggregators, and some give conflicting dates. Treat the details accordingly.*

### 1. Resolution mechanics
- **What counts as YES:** OpenAI or an official representative announces that OpenAI has **solved** one of five problems: Riemann Hypothesis (RH), P vs NP, Yang–Mills existence and mass gap, Hodge Conjecture, or Birch and Swinnerton-Dyer (BSD). The announcement must come between market creation and Dec 31, 2026, 11:59 PM ET. That leaves about 35 days.
- **Navier–Stokes is excluded.** OpenAI's Sept 8, 2026 Navier–Stokes claim is why the question says "another." Further Navier–Stokes announcements, such as a full proof without external forcing or Clay recognition, do not count.
- **The claim must be a full solution.** Partial results don't count. Things OpenAI has already published that would **not** qualify:
  - the "quasi-Riemann hypothesis" (no zeros of the zeta function with real part between 7/8 and 1), released Oct 2026;
  - the rational Hodge conjecture for CM abelian varieties (paper dated Sept 30, 2026);
  - a reported Oct 2026 Yang–Mills existence result that leaves out the mass gap. This appears only in Wikipedia and is uncorroborated.
- **Credit:** The solution must be presented as the work of OpenAI, its researchers or its models, alone or jointly with outsiders. Congratulating outside researchers who used OpenAI tools does not count.
- **No verification needed.** Neither Clay nor anyone else has to confirm the proof. OpenAI's own statement is enough, and a consensus of credible reporting is a fallback source.
- **Edge cases:**
  - **RH has already been claimed by someone else.** Levent Alpöge's Claude-assisted proof was certified in Lean on Nov 21. If OpenAI now announced its own independent RH proof, it would technically still qualify. An OpenAI announcement that merely re-verified or formalized Alpöge's proof probably would not.
  - **Hedged wording.** OpenAI's Navier–Stokes post said it "resolves the Navier–Stokes Millennium Prize problem." Similar wording for Hodge would qualify. Wording like "proves Hodge for a broad class" would not.
  - **Leaks.** A report from The Information based on anonymous sources is not an official announcement.
  - **Creation date unknown.** I don't know when the market was created. If OpenAI announced anything qualifying before then, it wouldn't count. I found no qualifying announcement at all, though.

### 2. Reference classes and base rates
1. **Human history:** One of the seven problems (Poincaré) has been officially solved in 26 years, about 0.04 per year. This is nearly irrelevant now that AI is producing these results, but it shows how hard the five remaining problems are.
2. **Frontier-lab Millennium claims in 2026:** There have been two full claims in about 11 weeks:
   - OpenAI on Navier–Stokes, Sept 8;
   - Alpöge/Anthropic on RH, released Nov 20 and Lean-certified Nov 21.

   That is about 0.75 claims per month across labs. OpenAI's own rate of qualifying full claims is **0 in the roughly 11 weeks since Sept 8**, even though it said in September that it had made "substantial progress on another Millennium Prize problem." A naive Poisson rate for OpenAI of about 0.35 to 0.5 full claims per month (one claim in 2.5 to 3 months) gives roughly a 30–45% chance of at least one in 35 days. The rate of qualifying claims since September is zero, though, which argues for something lower.
3. **How long a "substantial progress" or "solution soon" claim takes to become an announcement:**
   - Navier–Stokes went from start to announcement in about a week: the effort began Sept 1 after a rumor, and OpenAI says the solve took 88 hours (CNN/HPCwire, Sept 2026).
   - The Hodge expectation was reported around mid-to-late September (The Information via The Decoder/Gizmodo). It has now gone about 2+ months without delivery.

   When a "soon" claim slips by 2+ months, it often means the problem is actually hard or there is a deliberate hold. Here the hold is explicitly reported.

### 3. Current state of the world (most recent first)
- **Nov 21–23, 2026:** The Lean FRO and Mathlib Initiative jointly certified that Alpöge's 17-million-line Lean proof establishes the Riemann Hypothesis as Mathlib states it. Andrew Sutherland's full Comparator run was still listed as in progress on Nov 23 (The Decoder; TNW; Kingy). Nature reports broad acceptance mixed with dissent: Andrew Granville criticized the 4-page sketch and its timing, and Ravi Vakil posted a rival all-human preprint (Nature, Nov 2026).
  - OpenAI's Sébastien Bubeck objected to listing Alpöge as an author and later apologized (Heise).
  - One unverified source says Altman called related accusations "baseless plagiarism accusations" (BigGo).
  - **RH is now credited to Anthropic, and OpenAI has lost the race to be first on RH.**
- **Nov 20, 2026:** Alpöge released the RH proof, one day after Anthropic's IPO (Heise; Nature).
- **Nov 2026:** Arizona State Press reports mathematicians still describing OpenAI's Navier–Stokes proof as under verification and "partial" (State Press, Nov 2026).
- **Oct 2026:**
  - A KCL/Cambridge preprint (arXiv 2610.08144) found that OpenAI's Navier–Stokes Lean formalization does not faithfully match the natural-language proof (KCL news; The Decoder).
  - More than 1,000 mathematicians signed an open letter calling OpenAI's approach "research misconduct," and the Association for Human Mathematics urged people to stop collaborating with OpenAI (Gizmodo via NewsBreak; Zerohedge).
  - OpenAI formed a nine-person Advisory Group on Mathematics and AI at the Institute for Advanced Study in Princeton (Quartz).
- **Oct 6, 2026:** OpenAI released 722 AI-generated manuscripts, including the quasi-Riemann result (Quanta, Oct 19; Science). The WSJ reported that the release touched three Millennium problems. Some preprints were withdrawn for errors. Wikipedia reportedly says OpenAI announced a Yang–Mills existence proof without the mass gap in October; one tracker found no authoritative AI solution for Yang–Mills (Kingy tracker).
- **Sept 30, 2026:** OpenAI paper proving the rational Hodge conjecture for CM abelian varieties. Mathematician Abhishek Saha confirmed it. Experts said there is "literally zero chance" OpenAI has proved Hodge in general (OfficeChai; cryptobriefing).
- **Mid/late Sept 2026:**
  - OpenAI told the NYT it had made "substantial progress" on an unnamed second Millennium problem and was "working through how to share these results thoughtfully" (Decrypt; OfficeChai).
  - The Information, citing a single OpenAI source, reported that employees expected a **Hodge** solution "soon" but that the announcement **may be delayed** while OpenAI works out how to involve mathematicians and avoid a repeat of the Navier–Stokes PR backlash (The Decoder; Superpower Daily).
- **Sept 8, 2026:** OpenAI announced its Navier–Stokes "solution" (statements C and D, the version with forcing), with a Lean proof. It was produced by an internal model using up to 10,000 agents over 88 hours. OpenAI does not intend to claim the prize. A credit dispute with Buckmaster/Alpöge followed (OpenAI; Axios; CNN).
- **Sept 5–11, 2026:** Rumors that Anthropic had solved Navier–Stokes, Hodge or BSD (X; Paradigm3 newsletter, Sept 11).
- **Scheduled events before Dec 31:** I found none specifically. OpenAI has historically made launches in December ("shipmas"-style), which is a plausible window. No date for an OpenAI math announcement has been reported.

### 4. Drivers and scenarios
**Paths to YES**
- **Hodge announced (the most likely route).** This needs the internal model to have actually closed the general conjecture, not just the CM abelian case, and OpenAI leadership to choose to announce before year-end. Competitive pressure is now strong: Anthropic got RH, the most prestigious problem, right after its IPO, and OpenAI's Navier–Stokes claim is being picked apart. OpenAI has shown it will rush (Navier–Stokes was launched in reaction to a rumor).
- **A collaborative announcement.** OpenAI could release the result jointly with the IAS advisory group or outside mathematicians, framed as "solved." This would satisfy the "jointly" clause.
- **A full Yang–Mills claim (mass gap included), BSD, or an independent OpenAI RH proof.** No evidence points to any of these. They are low-probability tails.

**Paths to NO**
- The general Hodge proof isn't actually finished. Several experts are strongly skeptical, and the "soon" from September has not materialized.
- OpenAI deliberately holds the result to get mathematician vetting and avoid another backlash (explicitly reported), pushing any announcement into 2027.
- OpenAI announces in hedged language ("substantial progress," "proof for a broad class," "under review"). Under the rules that counts as partial, so NO.
- The Lean-fidelity criticism of Navier–Stokes leads OpenAI to wait for a faithful formalization before claiming anything.

### 5. Signposts
- **Strongly toward YES:**
  - An OpenAI blog post, Altman/Brockman/Bubeck tweets or a press briefing teasing a "second Millennium problem";
  - reports that the IAS advisory group or outside algebraic geometers are reviewing a Hodge manuscript;
  - a December launch event that mentions math;
  - a new Lean library from OpenAI covering Hodge.
- **Moderately toward YES:** OpenAI publicly answering Anthropic's RH result with competitive messaging, or leaks of a near-term announcement date.
- **Toward NO:**
  - OpenAI statements stressing collaboration or peer review before any announcement;
  - new reporting that the Hodge result has slipped to 2027;
  - errors found in the CM-abelian or other Hodge-related manuscripts;
  - continued escalation of the math-community boycott;
  - silence through mid-December.

### 6. Uncertainties
- I could not read any primary source (all fetches were blocked), including OpenAI's announcement and the original Information/NYT pieces. The exact date of the "substantial progress" statement and Hodge report is only approximate: mid-to-late September, with conflicting dates across aggregators.
- I don't know whether OpenAI has any non-public result on Hodge beyond the CM case, or how close it is.
- I couldn't verify the Wikipedia-reported October Yang–Mills existence claim or confirm its wording.
- I don't know the market creation date.
- I don't know whether OpenAI has made any statement since Nov 21 responding to Alpöge's RH proof. I found nothing dated November from OpenAI on Millennium problems.
- Many sources (Kingy, KuCoin, BigGo, Superpower Daily, Vocal) are low-quality aggregators. Some specific details, such as Altman's quote and "a third problem imminent," are unverified.

## Sources
- [OpenAI says it has solved one of math's "Millennium Problems" (CNN, Sept 9, 2026)](https://www.cnn.com/2026/09/09/business/openai-millennium-problems-navier-stokes-hnk)
- [On the Navier–Stokes Millennium Prize Problem (OpenAI)](https://openai.com/index/navier-stokes-solution/)
- [OpenAI's historic math solution overshadowed by credit controversy (Axios, Sept 8, 2026)](https://www.axios.com/2026/09/08/openai-math-solution-navier-stokes-credit)
- [Unsolved for 90 Years, OpenAI Says AI Cracked Millennium Prize Problem in 88 Hours (HPCwire, Sept 16, 2026)](https://www.hpcwire.com/aiwire/2026/09/16/unsolved-for-90-years-openai-says-ai-cracked-millennium-prize-problem-in-88-hours/)
- [OpenAI claims another huge mathematical result amid fights over credit, ethics and privacy (The Conversation)](https://theconversation.com/openai-claims-another-huge-mathematical-result-amid-fights-over-credit-ethics-and-privacy-291575)
- [OpenAI Says It's Made Progress on a Second $1 Million Math Problem (Decrypt)](https://decrypt.co/378551/openai-progress-second-millennium-prize-math-problem)
- [After Navier-Stokes, OpenAI Says It Has Made "Substantial Progress" On Another Millennium Prize Problem (OfficeChai)](https://officechai.com/ai/after-navier-stokes-openai-says-it-has-made-substantial-progress-on-another-millenium-prize-problem/)
- [OpenAI reportedly closes in on solving the Hodge conjecture (The Decoder)](https://the-decoder.com/openai-reportedly-closes-in-on-solving-the-hodge-conjecture-its-second-millennium-prize-problem/)
- [OpenAI May Delay a Reported Hodge Conjecture Result After Math Backlash (Superpower Daily)](https://superpowerdaily.com/posts/openai-may-delay-a-reported-hodge-conjecture-result-after-math-backlash)
- [OpenAI Reportedly Trying to Solve Hodge Conjecture Amid Feud With Math Community (Gizmodo via NewsBreak)](https://www.newsbreak.com/gizmodo-399763864/4892805145658-openai-reportedly-trying-to-solve-hodge-conjecture-amid-feud-with-math-community)
- [OpenAI claims substantial progress on second Millennium Prize problem, faces math community pushback (Crypto Briefing)](https://cryptobriefing.com/openai-hodge-conjecture-math-pushback/)
- [OpenAI Proves The Rational Hodge Conjecture For CM Abelian Varieties (OfficeChai)](https://officechai.com/ai/hodge-conjecture-abelian-varieties/)
- [AI Proved the Quasi-Riemann Hypothesis. What Happens Now? (Quanta, Oct 19, 2026)](https://www.quantamagazine.org/ai-proved-the-quasi-riemann-hypothesis-what-happens-now-20261019/)
- [OpenAI releases 722 AI-generated math papers after Millennium Prize claim (Quartz)](https://qz.com/openai-ai-math-papers-millennium-prize-riemann-hypothesis-100726)
- [OpenAI's math model is reportedly chipping away at two more Millennium Prize problems (Startup Fortune)](https://startupfortune.com/openais-math-model-is-reportedly-chipping-away-at-two-more-millennium-prize-problems/)
- [OpenAI's Navier-Stokes proof called into question (King's College London)](https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question)
- [Navier-Stokes lost in translation (arXiv 2610.08144)](https://arxiv.org/pdf/2610.08144)
- [Mathematicians explain how OpenAI solved a Millennium Prize Problem (Arizona State Press, Nov 2026)](https://www.statepress.com/article/2026/11/navier-stokes-solution-ai)
- [Lean and Mathlib community officially confirms Levent Alpöge's proof of the Riemann hypothesis (The Decoder, Nov 2026)](https://the-decoder.com/lean-and-mathlib-community-officially-confirms-levent-alpoges-proof-of-the-riemann-hypothesis-is-correct/)
- [Lean and Mathlib certify Alpöge's Claude-assisted Riemann hypothesis proof (TNW)](https://thenextweb.com/news/lean-mathlib-certify-riemann-hypothesis-proof-alpoge-claude)
- [Lean FRO statement on X (Nov 2026)](https://x.com/leanprover/status/2124159121645801562)
- [Riemann hypothesis: Anthropic mathematician says he found an AI-assisted proof (Heise)](https://www.heise.de/en/news/Riemann-hypothesis-Anthropic-mathematician-says-he-found-an-AI-assisted-proof-11533489.html)
- ['If we can solve Riemann, what can't we do?' (Nature, Nov 2026)](https://www.nature.com/articles/d41586-026-03835-0)
- [AI and Claude Claim Proof of Riemann Hypothesis (BigGo Finance)](https://finance.biggo.com/news/c132374d-8b9c-4693-91fc-616afae88090)
- [Humans on AI, September 11th 2026 (Paradigm 3)](https://www.paradigm3.org/news/newsletter-09-11/)
- [Millennium Prize Problems and AI tracker (Kingy AI)](https://kingy.ai/millennium-prize-problems-ai/)
- [Millennium Prize Problems (Wikipedia)](https://en.wikipedia.org/wiki/Millennium_Prize_Problems)
- ['Bunker Mode': OpenAI's Math Blitz Draws Boycott (Zerohedge)](https://www.zerohedge.com/political/bunker-mode-openais-jaw-dropping-math-blitz-draws-boycott-warning-over-crypto-wallets)
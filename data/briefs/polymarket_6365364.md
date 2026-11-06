# Research brief: Will Google release Gemini Carbon to the public between Nov 9 and Nov 15, 2026?

## 1. Resolution mechanics

- **What counts as YES:** The model codenamed "Carbon" must become available to the general public. That includes the already-announced "Gemini 4 Carbon", or any model that Google or a consensus of credible reporting confirms is the same model. The ET calendar date of public release must fall between **Mon Nov 9 and Sun Nov 15, 2026**. The market closes 2026-11-16 04:59 UTC, which is Nov 15 at 11:59 PM ET.
- **Naming is settled.** Google officially announced "Gemini 4 Carbon" on Oct 28, 2026 (Google blog, "Gemini 4 Carbon: our next frontier model," Oct 28, 2026). So the identity questions in the rules (renaming, Argon updates, distillations) are probably moot. The only real question is when public access happens.
- **What does not count:** Closed betas and private access. The current access tiers do not qualify: "a subset of cyber defenders" and phased additions of "trusted partners through our Fairwind Program". Neither would an expansion of Fairwind to more organizations, even a large one.
- **What would likely count:** Availability in the paid Gemini API or AI Studio, Vertex AI, or the Gemini app for paid tiers (AI Pro or Ultra). Anyone can buy those. Argon's Oct 13 release was paid-only (API plus AI Pro/Ultra) and was widely described as "broadly available" (VentureBeat; 9to5Google, Oct 13, 2026).
  - **Ambiguity 1:** An Ultra-only rollout, or one requiring a Google Cloud sales contact, could be disputed. Ultra-only probably still counts, since it is self-serve and paid.
  - **Ambiguity 2:** A staggered rollout ("rolling out over the coming days") could leave unclear which date counts. The announcement date of public availability is probably what would be used.
- **Timing edge cases:** A release on Nov 7–8 (the weekend before the window) or Nov 16 or later resolves NO. Timezone matters for late-evening US Pacific launches only marginally, since PT evenings are still the same ET date or just after midnight.
- **Who decides:** Primarily official Google sources, with consensus credible reporting as a backstop.

## 2. Reference classes and base rates

**A. Google's own "cyber defenders / trusted testers first, then public" frontier launches. This is the most relevant class.**

| Model | Gated announcement | Public release | Lag |
|---|---|---|---|
| Gemini 4 Argon | Sep 30, 2026 (Wed), Fairwind cyber defenders only | Oct 13, 2026 (Tue), paid API and AI Pro/Ultra | **13 days** |
| Gemini 3 Deep Think (from my background knowledge, not re-verified here) | Nov 18, 2025, safety testers | Dec 4, 2025, Ultra | ~16 days |
| Gemini 2.5 Deep Think (from my background knowledge, not re-verified here) | May 20, 2025 (I/O), trusted testers | Aug 1, 2025, Ultra | ~73 days |

Sources for Argon: TechRepublic, Sep 30, 2026; VentureBeat and 9to5Google, Oct 13, 2026.

- Carbon was announced Wed Oct 28, the same weekday as Argon's Sep 30 announcement.
- Applying Argon's 13-day lag gives **Tue Nov 10**, inside the window. Applying the ~16-day lag gives Fri Nov 13, also inside.
- The Nov 9–15 window covers days 12–18 after announcement. In this small class, 2 of 3 public releases fell inside that range; the third took about 10 weeks.

**B. Frontier models gated for cybersecurity reasons by other labs.**

- Anthropic's Claude Mythos Preview (Project Glasswing) launched April 2026, partner-only. Anthropic said it does "not plan to make Claude Mythos Preview generally available." About 7 months later it was still gated, though there were unconfirmed hints of broader availability via Vertex (WaveSpeed; Pasquale Pillitteri, 2026).
- OpenAI's "GPT-6 Rosalind" is also described as gated (DigitalApplied, 2026).
- Base rate in this class for public release within ~3 weeks: roughly 0 of 2.
- Carbon differs because Google explicitly says it will bring Carbon to "developers, businesses, and consumers… as soon as possible." Anthropic said the opposite about Mythos.

**C. Probability that a release lands in a specific 7-day window.**

- Even if broad release by the end of November is likely, Carbon has to land in this particular week. Google's gaps between gated announcement and public release have ranged from about 2 weeks to about 10 weeks.
- A 7-day window centered on the Argon analog captures perhaps a third to a half of the probability mass, conditional on a release within about 6 weeks.

## 3. Current state of the world (most recent first)

- **Nov 6, 2026:** Tech-ish headline: "Google's Gemini 4 Carbon came two weeks after Argon and beats it, but you can't use it yet." Still not publicly available (tech-ish, Nov 6, 2026).
- **~Nov 2–5, 2026:**
  - The Gemini Apps Help page (Nov 2) lists Flash-Lite, Flash, Pro and Argon, not Carbon.
  - Google's AI Pro/Ultra plans page lists Argon, not Carbon.
  - Carbon is not in the API, AI Studio or Antigravity, and Google has given no public date (search-result summaries of mindstudio.ai, androidpure.com and theaicareerlab.com coverage, early Nov 2026).
- **~Nov 1–2, 2026:**
  - Reported AI Studio identifiers: "gemini-4-carbon," "gemini-4-carbon-teamfood," "carbon-g-medium-tf." These suggest internal dogfooding and pre-launch plumbing; nothing is public (X post via TestingCatalog coverage, ~Nov 1).
  - Several sources say the Fairwind Program page still describes Argon and doesn't mention Carbon (businessmodelanalyst; s5labs, ~Nov 1).
- **Oct 30–31, 2026:** A newer Carbon checkpoint reportedly appeared on LMArena, anonymized or under an Argon alias (TestingCatalog, "Google tests a new Gemini 4 Carbon checkpoint on Arena," ~Oct 31). Google is still iterating checkpoints after the announcement. Before Argon's public release, Arena testing was followed by launch within weeks.
- **Oct 29, 2026, Alphabet Q3 earnings call:**
  - CEO remarks called Carbon the strongest frontier model, rolled out first to trusted cyber defenders and also being tested by the US government.
  - The remarks said "more models" are coming, including more efficient versions for developers (Google blog, "Q3 2026 earnings call: Remarks from our CEO," Oct 2026).
- **Oct 28, 2026, official announcement (Google blog):**
  - Carbon is "our strongest model with state-of-the-art cybersecurity and long horizon capabilities" and builds on Argon.
  - Access is "starting with a subset of cyber defenders," with Google to "gradually phase access to additional trusted partners through our Fairwind Program." Broad release is promised "as soon as possible" after Google gathers feedback and iterates on guardrails.
  - Google says Carbon "will launch at the same introductory price as Argon," $2/$10 per million tokens. The end date of that rate for Carbon is unclear; Argon's introductory price ends Nov 30, 2026 (VentureBeat; mixed-news).
  - Logan Kilpatrick: Carbon is "a big jump over Argon which we released just 2 weeks ago… working to make it more widely available soon" (X, Oct 28). Demis Hassabis: "Iterating at lightning speed!" (X, Oct 28).
  - Benchmarks: #1 on Artificial Analysis Index v5 with a score of 59, against Argon's 50, and one point ahead of Claude Opus 5.5 (Tom's Hardware; VentureBeat, Oct 28).
- **Oct 23, 2026:** Carbon was in early access with partners and on LMArena. Testers praised its 3D work and criticized its slowness and weak UI (TestingCatalog, "Gemini 4 Carbon early test results are in ahead of public release").
- **Oct 13, 2026:** Argon became publicly available: paid API, AI Studio, Gemini app for Pro/Ultra, with introductory pricing until Nov 30 (9to5Google; VentureBeat, Oct 13).
- **Oct 9, 2026:** Business Insider reported internal testing of the Argon, Barium and Carbon checkpoints.
- **Sep 30, 2026:** Argon announced with a Fairwind cyber-defenders-first rollout. Before wider release Google committed to "strengthening four safeguards," with wider access to start with paid API customers and AI Ultra subscribers (TechRepublic, Sep 30).

**Scheduled events before Nov 15:** I found no Google event in the window. Google often ships model updates on Tuesdays through Thursdays (Argon shipped on a Tuesday). Nov 30 is the end of Argon's introductory pricing, which is after the window.

## 4. Drivers and scenarios

**Paths to YES (public release Nov 9–15):**
1. **Google repeats Argon's playbook almost exactly:** about 2 weeks of Fairwind-only access, then paid API, AI Studio and Pro/Ultra on about Tue Nov 10 to Thu Nov 12. This is supported by:
   - the identical rollout language;
   - the "same introductory price as Argon" framing, which hints Google wants Carbon live while that pricing still applies (before Nov 30);
   - AI Studio identifiers appearing;
   - leadership's "lightning speed" and "soon" messaging;
   - competitive pressure, since Carbon only narrowly beats Opus 5.5.
2. **A partial public release in the window:** for example, Ultra-only or API-only. This probably still resolves YES.

**Paths to NO:**
1. **Slower guardrail iteration.** Carbon is a bigger jump in cyber capability than Argon. Google explicitly ties broad release to "feedback" and "guardrails," and the US government is testing it. A 3–6 week (or longer) gated period, like Gemini 2.5 Deep Think, would push release to late November, December or later.
2. **Release just before or after the window.** A Nov 16–20 launch (still under 4 weeks) is very plausible. A Nov 7–8 weekend launch is unlikely.
3. **Long-term gating like Mythos.** Google keeps Carbon partner-only and later ships a different or distilled model (for example, "more efficient versions for developers"). Under the rules, that model would not count unless confirmed to be the same model.
4. **Non-qualifying access.** The release is enterprise or sales-gated only (Vertex allowlist), or limited to an expanded Fairwind group.

## 5. Signposts

- **Strong moves toward YES:**
  - Carbon appears in the AI Studio model picker, on the Gemini API models or pricing page, in Gemini app release notes, or in Vertex Model Garden as GA or public preview.
  - The Fairwind page is updated and then a "now available" blog post appears.
  - Leakers (TestingCatalog, 9to5Google APK teardowns) find Carbon strings in the Gemini app model selector.
  - Logan Kilpatrick posts hints ("big week," "shipping soon").
- **Moderate moves toward YES:** Carbon pricing or an introductory-pricing end date appears on Google pages; Carbon appears in OpenRouter or Vertex docs.
- **Moves toward NO:**
  - No sightings by about Wed Nov 11.
  - New Google statements stressing safety or cyber concerns, or a government-review angle.
  - News of misuse or jailbreak problems.
  - Google announcing a separate developer-oriented model ("Carbon Flash" or similar) instead.
  - New Arena checkpoints still appearing mid-November, which suggests the model is not frozen.

## 6. Uncertainties

- I couldn't open primary pages directly; fetches to Google, Business Insider and others failed. Quotes come from search-result excerpts of Google's blog and secondary coverage, and some secondary sources conflict.
- **Argon's lag is the key comparison, and its confirmation is mixed.** 9to5Google, VentureBeat and Google's release notes (all Oct 13) are consistent with a 13-day lag, but one search returned pre-Oct 13 articles saying there was no GA date.
- It's unclear whether Carbon's introductory pricing also ends Nov 30. If it does, that is a soft signal of a public launch before then.
- Whether Carbon's cyber capability is materially more dangerous than Argon's, and so needs longer gating, has not been established.
- I don't know how a resolver would treat an Ultra-only, waitlisted or region-limited release.
- I found no reporting dated after about Nov 6 indicating an imminent launch date.

## Sources
- [Gemini 4 Carbon: our next frontier model (Google blog)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/)
- [Google unveils Gemini 4 Carbon… but access is limited (VentureBeat)](https://venturebeat.com/technology/google-unveils-gemini-4-carbon-retaking-the-worlds-no-1-spot-on-updated-harder-benchmarks-but-access-is-limited)
- [Google reveals new Gemini 4 Carbon AI model, narrowly beating Claude Opus 5.5 (Tom's Hardware)](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-reveals-new-gemini-4-carbon-ai-model-narrowly-beating-claude-opus-5-5-frontier-ai-model-is-also-the-least-likely-to-hallucinate-benchmarks-claim)
- [Google's Gemini 4 Carbon came two weeks after Argon and beats it, but you can't use it yet (tech-ish, Nov 6 2026)](https://tech-ish.com/2026/11/06/gemini-4-carbon-two-weeks-after-argon/)
- [Gemini 4 Carbon Is Google's New Frontier Model, Starting With Cyber Defenders (techmymoney, Nov 1 2026)](https://techmymoney.com/2026/11/01/gemini-4-carbon-google-frontier-model-cyber-defenders/)
- [Gemini 4 Carbon: Pricing, Rollout, and Cyber-First Access Explained (MindStudio)](https://www.mindstudio.ai/blog/gemini-4-carbon-pricing-rollout)
- [Gemini 4 Carbon: Google's Cybersecurity AI Model, No API Yet (MindStudio)](https://www.mindstudio.ai/blog/gemini-4-carbon-frontier-model)
- [Google Announces Gemini 4 Carbon, but It's Not in the Gemini App Yet (AndroidPure)](https://www.androidpure.com/gemini-4-carbon/)
- [Gemini 4 Carbon Is Locked. The Way In Runs Through Google Cloud (Business Model Analyst)](https://businessmodelanalyst.com/gemini-4-carbon-fairwind-defenders-google-cloud/)
- [Gemini 4 Carbon: Access, Pricing and Argon (s5labs)](https://s5labs.io/resources/insights/google-gemini-4-carbon-cyber-access/)
- [Google tests a new Gemini 4 Carbon checkpoint on Arena (TestingCatalog)](https://www.testingcatalog.com/google-tests-new-gemini-4-carbon-checkpoint-arena/)
- [Gemini 4 Carbon early test results are in ahead of public release (TestingCatalog)](https://www.testingcatalog.com/gemini-4-carbon-early-test-results/)
- [Google unveils Gemini 4 Carbon for cyber defenders (TestingCatalog)](https://www.testingcatalog.com/google-unveils-gemini-4-carbon-for-cyber-defenders/)
- [Logan Kilpatrick on X: Introducing Gemini 4 Carbon](https://x.com/OfficialLoganK/status/2115489284404940898)
- [Demis Hassabis on X: Iterating at lightning speed](https://x.com/demishassabis/status/2115489550256746502)
- [Q3 2026 earnings call: Remarks from our CEO (Google blog)](https://blog.google/company-news/inside-google/message-ceo/alphabet-earnings-q3-2026/)
- [Google Launches Gemini 4 Argon, Gives Cyber Defenders First Access (TechRepublic)](https://www.techrepublic.com/article/news-google-gemini-4-argon-cyber-defenders/)
- [Gemini app rolling out Gemini 4 Argon to AI Pro and AI Ultra (9to5Google, Oct 13 2026)](https://9to5google.com/2026/10/13/gemini-app-4-argon/)
- [Google makes Gemini 4 Argon broadly available with limited-time low API pricing (VentureBeat)](https://venturebeat.com/technology/google-makes-gemini-4-argon-broadly-available-with-limited-time-low-api-pricing-of-2-10-per-1m-token)
- [Gemini 4 Argon is now available, introductory price ends Nov 30 (mixed-news)](https://mixed-news.com/en/?p=36603)
- [Gated AI Models: Who Gets Gemini 4 Carbon and GPT-6 Rosalind (DigitalApplied)](https://www.digitalapplied.com/blog/gated-ai-models-carbon-rosalind-access)
- [What is Claude Mythos Preview (WaveSpeed)](https://wavespeed.ai/blog/posts/what-is-claude-mythos-preview/)
- [Claude Mythos Google Cloud console preview tag removed (Pasquale Pillitteri)](https://pasqualepillitteri.it/en/news/2684/claude-mythos-google-cloud-console-preview-tag-removed)
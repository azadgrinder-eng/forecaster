# Research brief: Will a US-China AI agreement be negotiated partly by an AI mediator by 2027?

*Prepared 2026-11-16. Method note: the page-fetch tool was blocked by the network proxy, so every fact below comes from search-result summaries, not full articles. Some outlets cited here are aggregators of mixed reliability. Dates and terms should be checked against official readouts where it matters.*

---

## 1. Resolution mechanics

**YES requires all three of these:**
1. **An agreement that substantially concerns the US and China.** Other countries may also be parties, so a multilateral deal could count.
2. **The agreement concerns AI directly.** The question's example is regulating compute. Arguably this also covers AI incident channels, AI safety protocols, or deals on AI chip exports.
3. **An AI mediator was used in making it.** The operational test: both parties passed information to the same AI model, and the model used both sides' inputs in the same inference run, tree rollout, or closely related computation.
   - **Counts:** an AI chatbot acting as mediator; a computational social-choice tool; an AI that takes in both sides' preferences and generates candidate texts that humans then negotiate over.
   - **Does not count:** officials using ChatGPT-style tools on their own for questions, drafting, or proofreading; each side running its own AI privately.

**Timing:**
- The title says "by 2027." The question closes 2026-12-02 07:59 UTC, so in practice the window ends in about 16 days.
- It is unclear whether an agreement made before December 2 but revealed later (for example, a memoir or leak in 2027) would count. The resolver will most likely judge on what is public by the close date or by end-2026.

**Who decides:** the question author, applying a self-described "handwavy" standard.

**Edge cases and ambiguities:**
- **Already-existing agreements could qualify retroactively.** The May 2026 Beijing understanding on an AI safety channel and the September 2026 "Super Intelligence Dialogue" plus incident channel are both AI agreements. If it emerged that a shared AI tool was used to reconcile their texts, YES could be argued.
- **Multilateral agreements could qualify.** An example would be a UN or summit declaration on AI that both the US and China joined, if the secretariat used an AI tool to merge member-state submissions into draft text. Whether that "substantially concerns the US and China" and whether both parties "passed information" to the model are both judgment calls.
- **Verification is the binding problem.** For YES, someone has to publicly report that a shared model was used. Neither government has any normal reason to disclose such a detail.
- **What counts as an "agreement"?** It is unclear whether a joint readout, an agreed dialogue, or a nonbinding statement is enough. Precedent suggests the resolver would accept a joint statement or an announced channel.

## 2. Reference classes and base rates

**A. Publicly documented interstate agreements negotiated with a shared AI mediator: about 0, ever.**
- My searches found no case anywhere of an AI system mediating between two governments and producing an agreement (multiple searches, Nov 2026).
- The closest examples are all planning or advisory tools used by one side, or pilots:
  - CSIS's "Strategic Headwinds" Ukraine peace-agreement simulator, built on 374 past agreements, which supports Western diplomats only.
  - The "North Star" project's AI "digital twins" of world leaders.
  - GIZ's NegotiateAI, which clusters country positions in the plastics-treaty talks for analysis.
  - African negotiators using AI to synthesize inputs within their own bloc at the Bonn climate talks (July 2025, WEF).
  - The UNFCCC secretariat's call for proof-of-concept AI text-analysis tools, which is still a call for proposals.
- **Base rate:** effectively 0 out of thousands of interstate agreements. Using AI to synthesize multilateral submissions is the most plausible near-miss category, but I found no documented 2026 case.

**B. US-China bilateral AI agreements: frequent recently, none with AI mediation.**
- Nov 2024, Lima: Biden and Xi agreed humans, not AI, should control nuclear-weapons decisions.
- May 2024, Geneva: first intergovernmental AI dialogue. It produced no joint statement.
- May 2026, Beijing state visit: an AI safety communications channel. One outlet calls it a "bilateral AI safety pact" signed May 14, 2026.
- Sept 2026, Xi's Washington state visit: the Super Intelligence Dialogue plus an incident channel.
- **Base rate:** about 3–4 AI-relevant US-China agreements or understandings in roughly 2.5 years, roughly one every 8 months. Over the past 6 months the pace has been one about every 4 months. A qualifying agreement (criteria 1 and 2) in the remaining window is therefore fairly likely, roughly 30–60%, because the first Shenzhen session is November 18–19. But 0 of these 3–4 had any reported AI mediation.

**C. AI-mediation research reaching real use.**
- DeepMind's Habermas Machine (Science, Oct 2024) raised unanimous group agreement from 22.8% to 38.6% in lab settings. Participants preferred its statements to human mediators' 56% of the time.
- Two years on, I found no documented use by governments. A CSIS workshop of 45+ mediators recommends narrow pilot simulations, with political judgment kept in human hands.
- **Base rate:** research-to-diplomatic-practice lags are long, typically several years. A first use would most likely come in low-stakes, multilateral or civil-society settings, not in the most security-sensitive bilateral relationship.

## 3. Current state of the world (most recent first)

- **Nov 18–19, 2026 (scheduled):** first session of the US-China AI dialogue in Shenzhen, alongside the APEC leaders' summit. Trump and Xi will meet there, their third meeting this year. A G20 meeting in Florida comes later.
  - Possible agenda (per AFP): AI systems acting beyond human control and deliberate misuse.
  - The Diplomat (Oct 2026) mentions a possible separate track-two "AI economics dialogue" run by think tanks and industry on the APEC margins.
  - Sources: VOA, Nov 13, 2026; Outlook India; SCMP, "China calls for AI cooperation with the US ahead of Shenzhen Apec summit."
- **Nov 15, 2026:** the US and eight partners signed an AI supply-chain declaration (chips, critical minerals, energy) to reduce reliance on China. It is allied, not bilateral with China, and does not qualify.
- **Nov 10, 2026:** Treasury Secretary Scott Bessent described the agenda: evaluating advanced models before release, preserving human control, and a direct channel for serious incidents. His framing was "de-risk, not decouple," with no commitment to slow AI development. No mention of AI-assisted negotiation (AI Weekly; TokenPost; CryptoBriefing).
- **Sept 24–26, 2026, Xi's state visit to Washington:**
  - Agreed the US-China "Super Intelligence (SI) Dialogue" (Beijing calls it the "China-U.S. AI Dialogue") and a bilateral channel for AI incidents.
  - The White House fact sheet is dated Sept 25.
  - White House science adviser Michael Kratsios said dialogue must not "drift toward global governance."
  - No safety pact, no development pause, and no easing of export controls.
  - Sources: The Next Web; Khaleej Times; VOA; Digital Policy Alert.
  - Kurt Campbell said the talks won't yield binding limits (CryptoBriefing).
- **Sept 20–21, 2026:** Bessent said the AI dialogue was established and the next meeting would be in about two months in Shenzhen. Washington's focus is national security and a notification system. One report says Beijing's readout initially stopped short of endorsing the formal mechanism (Kuwait Times; ROIC).
- **July 2026:**
  - UN Global Dialogue on AI Governance in Geneva (July 6–7), the first forum with all 193 member states. China was active; the US kept a low profile.
  - Reuters (July 22) reported the first official US-China AI talks under Trump were planned for September.
  - Sources: Brookings Beijing Brief, Jul 1, 2026; Let's Data Science.
- **May 14–16, 2026, Trump's Beijing state visit:** discussed AI "guardrails" and agreed an AI safety communications channel. H200 sales cleared by the US for ten Chinese firms, but China has not bought; Blackwell export controls unchanged (The Star, May 16, 2026; Tom's Hardware; AI Weekly).
- **On AI mediation specifically:** none of the coverage of the May, September, or upcoming November talks mentions any AI system used as a shared mediator or drafting engine. Talks are led by Treasury (Bessent) and senior officials with traditional diplomatic teams.

**Scheduled before close (Dec 2):** the Shenzhen AI dialogue and APEC leaders' meeting (Nov 18–19). No other known US-China AI negotiating events.

## 4. Drivers and scenarios

**Paths to YES (all low probability):**
1. **Shenzhen produces a joint AI document, and the two sides used a shared AI tool to reconcile texts or generate options, and this becomes public before resolution.** This needs:
   - both sides willing to put negotiating positions into one model, despite severe security and trust concerns (which country's model, and who hosts it?);
   - a public disclosure.

   Very unlikely in a security-sensitive, Treasury and NSC-led channel.
2. **The incident channel or SI Dialogue itself is set up with AI-assisted translation or synthesis that both sides feed into, and this is reported as "mediation."** Probably wouldn't meet the criteria: translation is arguably not mediation, and nothing like it has been reported.
3. **A multilateral AI agreement that both the US and China joined (for example, a UN process document) where the secretariat used an AI tool to merge state submissions,** and the resolver counts it. I found no evidence of this for 2026 AI-governance texts, and the US is disengaged from UN AI governance.
4. **A track-two dialogue (Brookings–Tsinghua or others) uses a Habermas-style tool to draft consensus text, and the resolver counts it as a US-China agreement.** Track-two outputs are not government agreements, so this would be a stretch.
5. **Retroactive revelation** that a prior 2026 agreement used a shared AI tool. No sign of this.

**Paths to NO (the default):**
- No AI-mediated process is used. This is the overwhelming default, given:
  - zero precedent;
  - intense mutual secrecy, with neither side likely to entrust positions to the other's model or to a third-party lab;
  - Kratsios's skepticism of governance mechanisms;
  - human-led, leader-driven summit diplomacy.
- AI mediation is used but never disclosed, which resolves NO in practice.
- The Shenzhen dialogue yields only talks, without an "agreement," as the 2024 Geneva meeting did.

## 5. Signposts

**Would move toward YES (large moves):**
- Any official or credible press report that US and Chinese negotiators used a common AI tool or model, for example a Habermas-style machine, a UN-hosted tool, or a neutral third-party lab, to draft or generate options for a Shenzhen or APEC AI text.
- A joint statement or fact sheet referencing "AI-assisted" drafting, translation, or a jointly operated AI system in the channel's design.
- Statements from the Shenzhen track-two "AI economics dialogue" describing AI-mediated consensus drafting, plus a lenient resolver.

**Would move toward YES (smaller moves):**
- A concrete signed Shenzhen document, such as an incident-reporting protocol or model-evaluation exchange. This only satisfies criteria 1 and 2.

**Would move toward NO:**
- Shenzhen readouts with no joint document, or with conventional drafting described.
- The close date passing with no reports. That is the default and is about two weeks away.

## 6. Uncertainties

- I could not read full texts of the White House Sept 25 fact sheet or the Chinese readouts (fetch was blocked). Exact wording of any agreed instrument is unverified.
- Sources disagree on dates: one tracker lists a Chinese MFA announcement of an AI dialogue on May 19, 2026; another calls May 14 a "signed" safety protocol. Whether the May understanding was a formal signed document is unclear.
- Whether Shenzhen will produce a written agreement is unknown; coverage is previews only (Nov 10–15).
- How the resolver treats multilateral or track-two documents, AI-assisted translation, or disclosures after Dec 2 is undefined.
- Absence of evidence is weak but meaningful. Covert use of a shared AI tool would be undetectable, but it also would not resolve YES unless disclosed.
- I could not confirm whether any UN AI-governance process in 2026 used AI text-synthesis tools on member-state submissions.

## Sources
- [Trump and Xi agree to set up AI safety channel as military and trade talks continue – CBS News](https://www.cbsnews.com/news/trump-xi-us-china-ai-trade-summit/)
- [U.S., China agree on AI safety channel after Trump-Xi summit – Quartz](https://qz.com/trump-xi-summit-ai-safety-channel-trade-truce-092626)
- [What Actually Happened at the Xi-Trump Summit – Asia Society](https://asiasociety.org/policy-institute/what-actually-happened-xi-trump-summit)
- [2026 state visit by Donald Trump to China – Wikipedia](https://en.wikipedia.org/wiki/2026_state_visit_by_Donald_Trump_to_China)
- [US and Eight Partners Sign AI Supply Chain Declaration – CEO.com.pl](https://ceo.com.pl/en/us-ai-supply-chain-declaration-china-51711/)
- [Bessent Unveils US-China 'Superintelligence' AI Dialogue – AI Weekly](https://aiweekly.co/alerts/bessent-unveils-us-china-superintelligence-ai-dialogue)
- [Trump–Xi talks to test progress on trade, SI and strategic stability – VOA (Nov 13, 2026)](https://www.voanews.com/a/trump-xi-talks-to-test-progress-on-trade-si-and-strategic-stability-20261113/8223457.html)
- [What the US and China Should Discuss at APEC – The Diplomat (Oct 2026)](https://thediplomat.com/2026/10/what-the-us-and-china-should-discuss-at-apec)
- [China calls for AI cooperation with the US ahead of Shenzhen Apec summit – SCMP](https://www.scmp.com/news/china/diplomacy/article/3374484/china-calls-ai-cooperation-us-ahead-shenzhen-apec-summit)
- [A New AI Dialogue, An Old Chip War: What Trump And Xi Face In Shenzhen – Outlook India](https://www.outlookindia.com/international/trump-xi-shenzhen-summit-nvidia-h200-ai-chips)
- [Bessent Says U.S.-China AI Dialogue Will Advance at APEC Summit – TokenPost](https://www.tokenpost.com/news/regulation/55146)
- [US and China agree a super intelligence dialogue and incident channel – The Next Web](https://thenextweb.com/news/us-china-super-intelligence-dialogue-ai-incident-channel)
- [US, China to set up 'communication channel' for AI incidents – Khaleej Times](https://www.khaleejtimes.com/tech/us-china-communication-channel-ai-incidents)
- [US-China plan AI incident channel – VOA](https://www.voanews.com/a/us-china-plan-ai-incident-channel-as-fierce-competition-tests-room-for-cooperation/8208082.html)
- [China and US established super intelligence dialogue – Digital Policy Alert](https://digitalpolicyalert.org/event/44574-china-and-united-states-established-super-intelligence-dialogue-and-agreed-to-establish-communication-channel-for-super-intelligence-incidents)
- [Bessent Outlines US-China Super Intelligence Dialogue Without Limits – Let's Data Science](https://letsdatascience.com/news/bessent-outlines-us-china-super-intelligence-dialogue-withou-c6db69a0)
- [US proposes AI dialogue with China ahead of Trump-Xi summit – Kuwait Times](https://kuwaittimes.com/article/50156/world/us-proposes-ai-dialogue-with-china-ahead-of-trump-xi-summit/)
- [US-China to meet in two months on AI in Shenzhen, Bessent says – ROIC](https://www.roic.ai/news/us-china-to-meet-in-two-months-on-ai-in-shenzhen-bessent-says-09-21-2026)
- [Kurt Campbell says US-China AI talks won't yield binding limits – CryptoBriefing](https://cryptobriefing.com/us-china-ai-talks-binding-limits/)
- [Trump says he discussed AI guardrails, Nvidia's chips with Xi – The Star (May 16, 2026)](https://www.thestar.com.my/tech/tech-news/2026/05/16/trump-says-he-discussed-ai-guardrails-nvidias-chips-with-xi)
- [Trump says China is blocking H200 purchases – Tom's Hardware](https://tomshardware.com/tech-industry/trump-says-china-is-blocking-h200-purchases)
- [US-China Sign First Bilateral AI Safety Pact in Beijing – AI Weekly](https://aiweekly.co/alerts/us-china-sign-first-bilateral-ai-safety-pact-in-beijing)
- [When Trump and Xi meet they will discuss AI. 'Track Two' talks are already buzzing – NPR (Sept 18, 2026)](https://npr.org/2026/09/18/nx-s1-5971481/trump-xi-meeting-ai-track-two-talks)
- [The Beijing Brief – Geneva AI dialogue – Brookings (Jul 1, 2026)](https://www.brookings.edu/wp-content/uploads/2026/07/The-Beijing-Brief-20260701-Geneva-AI-dialogue.pdf)
- [US-China to hold AI talks in September, sources say – Express Tribune (Jul 22, 2026)](https://tribune.com.pk/story/2619631/us-china-to-hold-ai-talks-in-september-sources-say)
- [China Expands Influence over Global AI Governance – Let's Data Science](https://letsdatascience.com/news/china-expands-influence-over-global-ai-governance-e91de1d6)
- [AI and the Future of Mediation – CSIS](https://www.csis.org/analysis/ai-and-future-mediation)
- [Can AI Mediation Help Bridge Political Divides? – Harvard PON](https://www.pon.harvard.edu/daily/mediation/can-ai-mediation-help-bridge-political-divides/)
- [AI models could help negotiators secure peace deals – IADS](https://www.iads.org/articles-reports/ai-models-could-help-negotiators-secure-peace-deals)
- [War has gone digital, peace must too – Columbia JIA](https://jia.sipa.columbia.edu/news/war-has-gone-digital-peace-must-too)
- [Is AI the future of America's foreign policy? – NPR via Connecticut Public (May 12, 2025)](https://www.ctpublic.org/2025-05-12/is-ai-the-future-of-americas-foreign-policy-some-experts-think-so)
- [Negotiate more effectively with AI – GIZ](https://www.giz.de/en/newsroom/news/negotiate-more-effectively-ai)
- [How AI helps diplomats scale inclusion in global climate negotiations – WEF (Sept 2025)](https://www.weforum.org/stories/2025/09/ai-diplomacy-scale-inclusion-global-climate-negotiations)
- [Partnership on AI tools for multilateralism in climate change negotiations – UNFCCC](https://unfccc.int/about-us/partnerships/current-calls-for-partnerships/partnership-on-ai-tools-for-multilateralism-in-climate-change-negotiations)
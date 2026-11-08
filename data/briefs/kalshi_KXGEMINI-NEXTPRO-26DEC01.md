## Research brief: Will Google release the next Gemini Pro model before Dec 1, 2026?

*Research note: every page fetch failed (proxy refused or domain denied), so everything below comes from search-result snippets. Many of those are third-party blogs that disagree with each other on dates. Official Google pages (blog.google, ai.google.dev, gemini.google release notes) appeared only as excerpts.*

---

### 1. Resolution mechanics

- **YES if:** Google publicly releases "the next Gemini Pro model" before Dec 1, 2026. The market closes 2026‑12‑01 04:59 UTC, which is still Nov 30 in US time zones. The release must be public and not a closed beta. Restricting it to an expensive subscription tier still counts. A public preview in the API, AI Studio or Gemini app (for example the "‑preview" style used for 3 Pro and 3.1 Pro) would very likely count. Partner-only or trusted-tester access, or an anonymous LMArena checkpoint, would not.
- **Who decides:** The market creator or platform, based on Google's announcements. No named source or tie-break rule is given.
- **The main ambiguity: does Gemini 4 Argon count as a "Pro" model?**
  - Google released **Gemini 4 Argon** to a small group of cyber partners on Sep 30, 2026 (TechCrunch, Sep 30 2026). It went broadly public on **Oct 13, 2026**, rolling out to AI Pro and Ultra subscribers in the Gemini app, in AI Mode, and in the API as `gemini-4-argon` (Gemini app release notes, 2026‑10‑13; blog.google "Gemini 4 Argon: Built to solve your hardest problems").
  - Google has **not** called it "Pro." It is "the first Gemini with a codename-style name." "Gemini 4 Pro" is a label used by the community and in leaks (OrcaRouter; ArgoLink).
  - Google's DeepMind Gemini Pro page reportedly still said **"3.5 Pro coming soon"** in late October. The newest callable "Pro" model was **Gemini 3.1 Pro** (eesel.ai, updated Nov 2 2026). The Gemini app model picker lists Argon *alongside* 3.1 Pro rather than replacing it (9to5Google, Oct 13 2026).
  - Two readings follow:
    - **(a) Argon counts as "the next Pro model."** Then YES already happened on Oct 13, unless the market was created after Oct 13.
    - **(b) "Pro" must be in the name.** Then YES needs something like a "Gemini 3.5 Pro" or "Gemini 4 Pro" release in about 3 weeks.
  - Forecasters should note that the market still being open on Nov 8, more than 3 weeks after Argon went public, suggests the resolver uses reading (b) or created the market after Argon. A related Polymarket series ("When will the next Google Gemini Pro model be released?") was created about Aug 17, 2026, before Argon. I could not see its rules or how it treated Argon.
- **Other edge cases:**
  - A shelved 3.5 Pro released late would count under reading (b).
  - A renamed "Gemini 4 Pro" built from the Argon checkpoint would probably count.
  - "Deep Think" modes or 3.1 Pro point updates would probably not count as a *new* Pro model.

### 2. Reference classes and base rates

**A. How often Google ships a new Gemini Pro version.** These dates come from my background knowledge and the Wikipedia/timeline listings in search results:

| Model | Public release |
|---|---|
| 1.0 Pro | Dec 6, 2023 |
| 1.5 Pro | Feb 15, 2024 (limited preview), public around May 2024 |
| 2.0 Pro Experimental | Feb 5, 2025 |
| 2.5 Pro | Mar 25, 2025 |
| 3 Pro | Nov 18, 2025 |
| 3.1 Pro | Feb 19, 2026 |

- That is 6 new Pro version numbers in about 35 months, or roughly 0.17 per month. Treating releases as random over time (a Poisson rate), the chance of at least one in a 23‑day window (Nov 8–30) is about **12%**.
- Gaps between releases ran about 1.5 to 12 months, with a median of about 3 months. The current gap since 3.1 Pro is already about 8.5 months, the second longest. That can mean a release is overdue, or that the Pro line has been deliberately paused.

**B. Announced-but-delayed frontier models.** Gemini 3.5 Pro was promised at I/O on May 19, 2026 for "next month." It missed June, missed the rumored July 17 date, and was reportedly "silently cancelled" (SemiAnalysis, Aug 7–11, 2026). Google's only responses were "currently testing 3.5 Pro" and "available as soon as it's ready." Models publicly reported as cancelled, with a successor shipped in the meantime, rarely launch later under the old name. My rough sense from AI labs (for example GPT‑4.5‑era or Claude 3.5 Opus-type cases) is that it happens well under 20% of the time, and less within a specific 3‑week window.

**C. Seasonality.** Google has shipped major Gemini launches in Nov/Dec before: 3 Pro on Nov 18, 2025; 2.0 Flash on Dec 11, 2024; 1.0 on Dec 6, 2023. Two of those three fell in early-to-mid December, after this market closes. US Thanksgiving is Nov 26, 2026, and launches that week are rare.

### 3. Current state of the world (most recent first)

- **Nov 13, 2026 (scheduled):** Choosing Pro models in the Gemini app and AI Mode becomes limited to AI Pro ($19.99/mo) and higher. AI Plus users lose it (9to5Google, Oct 14 2026; Windows Report). This changes access, not models.
- **Nov 30, 2026 (scheduled):** Argon's introductory API price ($2/$10 per million input/output tokens) ends and rises to $4/$20 (ai.google.dev Argon model page, via search excerpt). This is a natural date for model-lineup changes, but it is not a signal of a new Pro model.
- **Nov 2, 2026:** A third-party tracker says 3.5 Pro was still not generally available as of Oct 28, there was no `gemini-3.5-pro` entry in the API model list, and the DeepMind page still showed "3.5 Pro coming soon" (eesel.ai, updated Nov 2 2026).
- **Oct 13, 2026:** Gemini 4 Argon rolls out globally to AI Pro and Ultra subscribers, the API (`gemini-4-argon`, listed stable) and Vertex AI (Gemini release notes; Google Cloud blog). It is not on the free tier.
- **Oct 3, 2026:** Google limits which models free and AI Plus users can access, and adds Deep Think to AI Pro (9to5Google, Oct 3 2026).
- **Sep 30, 2026:** Argon announced, with access limited to cyber partners in the Fairwind Program (TechCrunch, Sep 30 2026).
- **Sep 24, 2026:** Google DeepMind's Koray Kavukcuoglu says Gemini 4 is in post-training and coming "as soon as possible," before the end of 2026 (9to5Google, Sep 24 2026). He also said Google "took a little bit of a step back" to focus on Flash models.
- **Sep 14–26, 2026:** A suspected "Gemini 4 Pro" checkpoint codenamed Argon appears on LMArena disguised as "gemini‑3.8‑flash" (pasqualepillitteri.it; NPowerUser). This suggests **Argon is the model that leakers had been calling "Gemini 4 Pro."**
- **Sep 2, 2026:** Gemini 3.8 Flash becomes generally available.
- **Aug 7–11, 2026:** SemiAnalysis reports that Google silently cancelled 3.5 Pro, with Flash as a stopgap while resources moved to Gemini 4. Logan Kilpatrick called the analysis "superficial/shallow" (TechApple; NPowerUser, Aug 2026). One unverified source (aiwiz.uk) says a Google spokesperson told Reuters on Sep 30 that 3.5 Pro would not be released. I could not corroborate that.
- **Jul 21, 2026:** Google releases 3.6 Flash, 3.5 Flash‑Lite and a cybersecurity Flash model, but no 3.5 Pro, which is "testing with partners" (TechCrunch, Jul 21 2026).
- **May 19, 2026:** At I/O, 3.5 Flash launches and 3.5 Pro is promised for the following month.
- **Feb 19, 2026:** Gemini 3.1 Pro released. It remains the newest model with "Pro" in its name.

I found no reports of a scheduled Google event or a new "Pro" leak in Nov 2026.

### 4. Drivers and scenarios

**Paths to YES:**
1. **The resolver counts Argon as the next Pro model** (it is the flagship above 3.1 Pro, sits in the Pro tier, and leaks called it "Gemini 4 Pro"). This depends entirely on the creator's interpretation and creation date. If it applies, YES is near-certain. The market being unresolved weakens this path.
2. **Google releases a model with "Pro" in its name by Nov 30.** Options include:
   - Gemini 3.5 Pro, finally. This looks unlikely: reportedly cancelled, Argon has superseded it, and there has been no news since August.
   - A "Gemini 4 Pro" sibling or rename of Argon. I found no evidence of this. OrcaRouter mentions a gated "Gemini 4 Carbon" but nothing named Pro.
   - A December-style launch pulled into November, as with 3 Pro on Nov 18, 2025.
3. **Google renames or re-tiers the lineup**, for example relabeling Argon as "Gemini 4 Pro" when the introductory price ends Nov 30. This is speculative.

**Paths to NO:**
- Google keeps codename branding (Argon, and possibly a "Carbon"), the 3.5 Pro slot stays "coming soon" or is quietly dropped, and the resolver needs "Pro" in the name.
- Any new Pro or Gemini 4 variant arrives in December, the historical Dec 6–11 launch window, which is after the close.
- Thanksgiving week (Nov 23–27) removes much of the remaining window.

### 5. Signposts

- **Strongly toward YES:**
  - The market creator or a comment clarifies that Argon counts.
  - A Google blog or API changelog lists any `gemini-*-pro` model (preview or GA) dated before Dec 1.
  - The DeepMind Pro page switches from "3.5 Pro coming soon" to a live model.
  - A new "Pro" checkpoint appears on LMArena or in AI Studio strings, which usually comes 1–4 weeks before launch.
- **Moderately toward YES:** Google event or press briefing invitations for mid/late November. Leaks of a Gemini 4 family expansion (Pro/Flash naming).
- **Toward NO:**
  - The creator clarifies that "Pro" must be in the name.
  - Google confirms 3.5 Pro is cancelled.
  - The DeepMind page removes the 3.5 Pro placeholder or folds the Pro tier into Argon.
  - No leaks by about Nov 20.
  - Announcements that point to a December launch.

### 6. Uncertainties

- **The biggest unknown is whether Argon counts.** I don't know the market's creation date, the creator's stance, or whether a sibling market resolved on Argon.
- I could not read any official Google page in full. Facts such as "3.5 Pro coming soon" and the 3.1 Pro picker listing come from search snippets and third-party summaries dated around Oct 13 to Nov 2.
- Whether 3.5 Pro is actually cancelled. SemiAnalysis says yes; Google has given non-denials. The claimed Reuters confirmation is unverified.
- The "Gemini 4 Carbon" reports are unverified and their naming is unknown.
- The exact public release dates of earlier models such as 1.5 Pro and 2.0 Pro depend on how "public" is defined, so the base rates are approximate.
- Source dates are inconsistent: Argon is given as both Sep 30 and Oct 13, and the 3.5 Pro cancellation report as Aug 7 and Aug 11.

## Sources
- [Google releases Gemini 4 Argon, called its most powerful model yet (TechCrunch)](https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/)
- [Google says Gemini 4 release is coming 'as soon as possible' (9to5Google)](https://9to5google.com/2026/09/24/google-says-gemini-4-release-is-coming-as-soon-as-possible/)
- [Gemini Apps' release updates & improvements](https://gemini.google/release-notes/)
- [Gemini 4 Argon: Built to solve your hardest problems (Google blog)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/)
- [Gemini 4 Argon | Gemini API docs](https://ai.google.dev/gemini-api/docs/models/gemini-4-argon)
- [Gemini 4 Argon available on Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/gemini-4-argon-available-on-google-cloud)
- [9to5Google: Gemini app 4 Argon](https://9to5google.com/2026/10/13/gemini-app-4-argon/)
- [9to5Google: Gemini AI Plus loses Pro in November](https://9to5google.com/2026/10/14/gemini-ai-plus-loses-pro-november/)
- [9to5Google: Gemini model limits Oct '26](https://9to5google.com/2026/10/03/gemini-model-limits-oct-26/)
- [Google AI Plus Users Lose Gemini Pro Models on November 13 (Windows Report)](https://windowsreport.com/google-ai-plus-users-lose-gemini-pro-models-on-november-13-keeping-access-will-cost-4x-more/)
- [Google releases three new Gemini models — but no 3.5 Pro (TechCrunch)](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)
- [Google delays Gemini 3.5 Pro, releases 3.5 Flash at I/O](https://letsdatascience.com/news/google-delays-gemini-35-pro-releases-35-flash-at-io-0dcab6cd)
- [Google Rumored to Shelve Gemini 3.5 Pro, Pivot to Gemini 4 (TechApple)](https://global.techapple.com/2026/08/google-rumored-to-shelve-gemini-3-5-pro-pivot-to-gemini-4/)
- [Google Shelves Gemini 3.5 Pro After Delays (NPowerUser)](https://nokiapoweruser.com/google-shelves-gemini-3-5-pro-pivot-gemini-4/)
- [Gemini 3.5 Pro release date: what happened (aiwiz.uk)](https://aiwiz.uk/blog/gemini-3-5-pro/)
- [Gemini 3.5 Pro: is it out yet? (eesel.ai)](https://www.eesel.ai/blog/gemini-3-5-pro)
- [Gemini 3.5 Pro: Release Date, Specs & What's Confirmed (geotoolbox)](https://geotoolbox.ai/blog/gemini-3-5-pro)
- [Gemini 4 Argon: What Google Announced, What the Name Is (OrcaRouter)](https://www.orcarouter.ai/blog/gemini-4-argon)
- [Gemini 4 Carbon vs Gemini 4 Pro (OrcaRouter)](https://www.orcarouter.ai/blog/gemini-4-carbon-vs-gemini-4-pro)
- [What Is Gemini 4 Pro? Gemini 4 Argon Specs (ArgoLink)](https://argolink.io/en/blog/what-is-gemini-4-pro)
- [Gemini 4 Pro leaks on Arena disguised as Gemini 3.8 Flash](https://pasqualepillitteri.it/en/news/18784/gemini-4-pro-checkpoint-arena)
- [Gemini 4 Pro Arena Leak (NPowerUser)](https://nokiapoweruser.com/gemini-4-pro-stealth-arena-leak-gemini-3-8-flash/)
- [Gemini 3.1 Pro: A smarter model for your most complex tasks (Google blog)](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)
- [Gemini (language model) – Wikipedia](https://en.wikipedia.org/wiki/Gemini_(language_model))
- [Google Gemini Model Release Timeline (hidekazu-konishi)](https://hidekazu-konishi.com/entry/google_gemini_model_release_timeline.html)
# Research brief: Will Meta release Muse Spark 1.4 or a higher-numbered Spark by November 30, 2026?

Note on method: every direct page fetch was refused by the network proxy, so the facts below come from search-result summaries of the cited pages. I could not read any primary page in full.

## 1. Resolution mechanics

- **What counts as YES:** Meta officially releases a model named "Muse Spark" with a version number above 1.3 (for example 1.4, 1.5 or 2.0). It must be usable by the public or by API customers. The window runs from market creation (around October 31, 2026) to November 30, 2026, 11:59 PM PT. That leaves about 18 days from today, November 12.
- **Valid confirmation channels:** a post on ai.meta.com/blog or about.fb.com/news, the Meta Model API docs or changelog, or an official Meta / AI at Meta account on X or Threads. Meta now publishes model posts on research.meta.ai/blog, for example the Muse Spark 1.3, Muse Wonder and Muse Ember posts. That domain is not on the list. In practice the API docs or official X/Threads posts would almost certainly also confirm a release, so this gap probably doesn't matter.
- **Explicitly excluded:** differently named models (Wonder, Spark Open, Ember, Glimmer, Muse Code features), previews or waitlists without access, and leaks or benchmark-site listings.
- **Edge cases:**
  - **"Contributor" variant only.** An ID called `muse-spark-1.4-contributor` has appeared on OpenCode's data page. Meta's pricing table already lists a "Muse Spark 1.3 Contributor" variant at $0.10/$0.20 per million tokens (input/output) (VentureBeat/Fello AI coverage of Ember, Nov 2026). If Meta officially makes "Muse Spark 1.4 Contributor" available through the API, that plausibly counts as YES. A listing on OpenCode alone does not.
  - **Cloud previews.** Spark 1.3, Wonder and Ember have reached Google Cloud in "preview" (OrcaRouter blog). A 1.4 that appears only as a third-party cloud preview, with no Meta post, is ambiguous.
  - **Odd version numbers.** Labels like "1.3.1", or a new Spark with no version number, are not clearly covered.
  - **Variants of 1.3.** Settings such as "Muse Spark 1.3 Max" do not count.

## 2. Reference classes and base rates

1. **Muse Spark's own release cadence.** Known releases:
   - Muse Spark: April 8
   - 1.1: July 9 (92 days later)
   - 1.2: August 5 (27 days later)
   - 1.3: September 2 (28 days later)

   As of November 12 it has been 71 days since 1.3. A release by November 30 would mean a gap of 89 days or less. Of the three previous gaps, all were under 92 days, but only one was longer than 71 days. The one-month rhythm from the summer has clearly broken. Spark has now gone more than twice the length of its recent gaps without an update.
2. **Simple rate model.** Four Spark versions in about 5 months is roughly one release every 50 days. At that rate, the chance of at least one release in any 18-day window is about 1 − e^(−18/50) ≈ 30%. A recent-slowdown rate of about one per 90 days gives roughly 18%.
3. **Point releases at other frontier labs.** These usually come 1–3.5 months apart, for example GPT-5 to 5.1 (about 97 days) and 5.1 to 5.2 (about 29 days), and Claude 4 to 4.1 (about 75 days). After a lab launches a new flagship family, the older mid-tier line often goes quiet or gets folded into the new family.
4. **Calendar effect.** US Thanksgiving falls on November 26, 2026. Releases during November 25–30 are historically uncommon, so the effective window is closer to November 12–24.

## 3. Current state of the world (most recent first)

- **Nov 9, 2026 – Muse Ember.** Meta released Muse Ember (`muse-ember-1.0`), its smallest and cheapest model, at $0.10/$0.50 per million tokens on the Meta Model API and Muse Code. It is the first model trained using Muse Wonder Full. It scores 36 on the Artificial Analysis Intelligence Index against 37 for Spark 1.3, at about 1/17 of Spark 1.3's cost per task (TechCrunch, Nov 9; MarkTechPost, Nov 9; VentureBeat, Nov 2026).
- **About Nov 6–9 – specialized models.** Meta is rolling out specialized models, trained with Wonder, to the Muse and Meta AI apps. The search summary gives November 9 for the article itself; another snippet put the rollout on November 6. They bring Active Memory and Active Focus to more users. I could not confirm their names, and nothing found calls them a Spark version (TestingCatalog, Nov 9).
- **Current lineup in the Model API docs:** Muse Wonder ("hardest problems"), Muse Spark ("coding and agentic workflows"), Muse Ender, plus Muse Image, Muse Voice Transcribe, SAM, and the open-weight Spark Open and Glimmer. Spark is still listed at version 1.3 (Meta Model API docs; Zapier guide, Nov 2026).
- **Oct 21 – Q3 earnings call.** Zuckerberg said "larger models after Muse Wonder" are in progress, and "new smaller models that are coming out soon that will deliver Muse Wonder-level intelligence more efficiently." He also described a strategy of distilling frontier models into "much smaller and more efficient product models … optimized for personal agents." Compute cost is the main constraint, and Meta is targeting a more than 10x efficiency gain within a year (Meta Q3 2026 earnings transcript; AP via KSAT, Oct 21). Ember and the specialized models appear to fulfil at least part of the "smaller models soon" promise, without using the Spark name.
- **Oct 15 – Muse Spark Open.** Meta released Muse Spark Open, an 816B-total / 42B-active-parameter mixture-of-experts open-weight model. It carries no version number above 1.3 and is excluded by name (TechCrunch, Oct 15; Hugging Face).
- **Oct 12 – Muse Wonder.** Meta released Muse Wonder and Muse Wonder Full, its first frontier family. `muse-wonder-1.0` costs $4/$20 per million tokens on the API (TechCrunch, Oct 12; about.fb.com, Oct 2026). Spark is no longer Meta's best model (Zapier).
- **Sept 24 – leak.** `muse-spark-1.4-contributor` appeared on OpenCode's data page. My dating comes from decoding the X post's ID; I could not open the post. The post links this to Meta teasing "its next major model as coming soon" at Connect on September 23 (kimmonismus on X; pengsonal on X: "no official release date yet"). In hindsight the teased "next major model" was probably Wonder, released October 12. The OpenCode page shows a data window of September 14 to November 8 with metrics that are all zero or placeholders. That suggests the ID was registered or tested but never served at scale.
- **Sept 23 – Connect 2026.** The keynote centred on the Muse agent, glasses, and a handheld device (TechCrunch, Sept 23; Axios, Sept 23).
- **Sept 2 – Muse Spark 1.3.** Released in Muse Code and the Meta Model API, focused on coding and agents. A Max reasoning setting followed around September 4 (Artificial Analysis, Sept 2; Unite.ai).
- **Scheduled events before November 30:** I found none Meta-specific; Thanksgiving is November 26.

## 4. Drivers and scenarios

**Paths to YES**
- The `muse-spark-1.4-contributor` ID shows Meta at least prepared a 1.4 build. Meta could ship it soon, for example as a Spark distilled from Wonder for the API mid-tier (between Ember at $0.10 and Wonder at $4). This depends on Meta keeping the Spark brand.
- Meta has kept up a fast November release pace (specialized models, then Ember). Another release in the next two weeks fits that momentum.
- The Model API needs a refreshed mid-priced coding model. Spark 1.3 is now only one point ahead of Ember on the Intelligence Index while costing about 17 times more per task, which makes it look outdated and gives Meta a reason to replace or refresh it.

**Paths to NO**
- **Strategy shift.** Meta's new structure is Wonder at the frontier, with distillation into new names (Ember, specialized product models). The Spark line may be frozen at 1.3, or its successor may get a new name.
- **The "smaller models soon" promise seems already met** by Ember and the specialized models, which removes the most obvious near-term reason for a Spark launch.
- **Weak leak.** The 1.4 ID has sat unreleased for about two months. It may have been an internal checkpoint that was superseded by the Wonder-distilled work.
- **Little time left.** About 18 days remain, the Thanksgiving week is likely dead, and Meta has just shipped two releases. Compute is described as Meta's main constraint.
- **Strict rules.** A preview, waitlist, or release only on a third-party cloud wouldn't count.

## 5. Signposts

**Would move toward YES (strongly):**
- `muse-spark-1.4` appearing in the Meta Model API models list or changelog, or in Muse Code's model picker.
- Teasers from Alexandr Wang or Zuckerberg, or reporting from TestingCatalog about "model upgrades" for Spark. TestingCatalog has run a piece titled "Meta prepares custom voices and model upgrades for Muse" that I could not read.
- New OpenCode, OpenRouter or Vertex listings with non-zero usage.

**Would move toward NO:**
- Meta docs or posts framing Spark 1.3 as legacy, or pointing coding users to Wonder or Ember.
- Another newly named mid-tier model (for example a "Muse Blaze"-style name) taking Spark's role.
- No Meta model news through about November 24.

**Moderate:** Meta pricing changes to Spark 1.3. Price cuts would suggest the line is being kept alive without a new version.

## 6. Uncertainties

- I could not read the OpenCode page, the X leak post, or the TestingCatalog and New Stack articles directly, because the proxy blocked them. The leak date is inferred from the X post ID and the OpenCode data window.
- I don't know whether the November 6–9 "specialized models" carry Spark branding internally. They don't appear to publicly.
- Meta's long-term plan for the Spark brand alongside Wonder and Ember is unknown.
- I don't know whether the "contributor" variant label means a separately released public SKU or an internal or partner-only build.
- I could not establish exact dates for any 1.3 point updates, or whether Meta has ever done a silent version bump.

## Sources
- [Muse Spark 1.4 search results incl. OpenCode listing: muse-spark-1.4-contributor](https://opencode.ai/data/meta/muse-spark-1-4-contributor)
- [Chubby (kimmonismus) on X – muse-spark-1.4-contributor leak](https://x.com/kimmonismus/status/2103228052344021308)
- [Peng on X – "no official release date yet"](https://x.com/pengsonal/status/2103189287193960806/photo/1)
- [Introducing Muse Spark 1.3 (Meta research blog)](https://research.meta.ai/blog/introducing-muse-spark-1-3)
- [Muse Spark 1.3 – Artificial Analysis, Sept 2, 2026](https://artificialanalysis.ai/articles/muse-spark-1-3)
- [Meta launches Muse Spark 1.3 with gains in coding and agentic tasks – Unite.ai](https://www.unite.ai/meta-launches-muse-spark-1-3-citing-gains-in-coding-and-agentic-tasks/)
- [Introducing Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)
- [Introducing Muse Spark 1.1 – Meta AI](https://ai.meta.com/blog/introducing-muse-spark-meta-model-api/)
- [Introducing Muse Spark – about.fb.com, April 2026](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/)
- [Everything new coming to Meta's AI agent Muse – TechCrunch, Sept 23, 2026](https://techcrunch.com/2026/09/23/everything-new-coming-to-metas-ai-agent-muse/)
- [Meta gives Muse more capabilities, teases handheld AI device – Axios, Sept 23, 2026](https://www.axios.com/2026/09/23/meta-muse-ai-hardware-handheld-glasses)
- [Meta releases its first frontier model, Muse Wonder – TechCrunch, Oct 12, 2026](https://techcrunch.com/2026/10/12/meta-releases-its-first-frontier-model-muse-wonder/)
- [Introducing Muse Wonder and Muse Wonder Full – about.fb.com](https://about.fb.com/news/2026/10/introducing-muse-wonder-models/)
- [Meta launches an open-weight AI model that runs on Macs – TechCrunch, Oct 15, 2026](https://techcrunch.com/2026/10/15/meta-launches-an-open-weight-model-that-runs-on-macs/)
- [META Q3 2026 Earnings Call Transcript](https://s21.q4cdn.com/399680738/files/content_files/META-Q3-2026-Earnings-Call-Transcript.pdf)
- [Meta Q3 revenue tops estimates; Muse accounts top 10 million – AP via KSAT, Oct 21, 2026](https://www.ksat.com/business/2026/10/21/meta-q3-revenue-tops-estimates-and-zuckerberg-says-muse-accounts-have-topped-10-million/)
- [Meta releases Muse Ember – TechCrunch, Nov 9, 2026](https://techcrunch.com/2026/11/09/meta-releases-muse-ember-a-new-lightweight-model-for-agent-execution/)
- [Meta Releases Muse Ember – MarkTechPost, Nov 9, 2026](https://www.marktechpost.com/2026/11/09/meta-muse-ember-small-agent-model/)
- [Meta's Muse Ember nearly matches Claude Haiku 5.5 – VentureBeat](https://venturebeat.com/technology/metas-proprietary-muse-ember-nearly-matches-claude-haiku-5-5-at-1-3-the-estimated-per-task-cost)
- [Meta Muse Ember: Price, Benchmarks and the 200K Catch – Fello AI](https://felloai.com/muse-ember/)
- [Meta rolls out specialized models for Muse and Meta AI – TestingCatalog](https://www.testingcatalog.com/icymi-meta-rolls-out-specialized-models-for-muse-and-meta-ai/)
- [Meta's best AI model now trains the one most of its users get – The New Stack](https://thenewstack.io/meta-muse-specialized-models/)
- [Muse Wonder, Muse Spark, and Muse Ember: A guide – Zapier](https://zapier.com/blog/meta-ai-muse-spark/)
- [Models – Meta Model API docs](https://dev.meta.ai/docs/models)
- [Meta's Muse Wonder, Spark 1.3 and Ember reach Google Cloud – OrcaRouter](https://www.orcarouter.ai/blog/muse-wonder-google-cloud-preview)
- [Muse Spark Open – Hugging Face](https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B)
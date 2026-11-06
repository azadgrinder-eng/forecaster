# Research Brief: Will Google have the top Code Arena WebDev model on Nov 30, 2026?

**Access caveat:** The proxy blocked every page fetch, including arena.ai itself. Everything below comes from search-result summaries of secondary sources, plus Arena posts on X as they appeared in search. I could not check the live leaderboard. Treat all scores as approximate.

## 1. Resolution mechanics

- **What counts as YES:** A Google-owned model must hold first place on the arena.ai Code Arena WebDev leaderboard (Overall view, filtered to "Models") when it is checked on Nov 30, 2026 at 12:00 PM ET. Google owns Gemini and Google DeepMind models.
- **How first place is decided:**
  - Models are ordered by the "Rank" column.
  - If ranks tie, the model listed higher on the page wins. Arena lists models by score, so a shared rank goes to the higher-scoring model.
  - If a tie still remains, company names are compared alphabetically. That would favor Google over OpenAI ("G" before "O") but not over Anthropic ("A" before "G"). This step should almost never matter.
  - In practice, the highest-scoring model that is not an AutoEval entry wins.
- **Edge cases:**
  - **AutoEval entries are ignored**, even if they show a rank or score.
  - **Restricted-access models count.** Gemini 4 Carbon is not yet generally available but is already on the board at #4 (LLMReference, Oct 28, 2026).
  - **Each reasoning-effort setting is listed separately.** Examples are "Gemini 4 Carbon (High)", "Claude Opus 5.5 (Max)" and "GPT-6 Astra (Max)". A higher-effort Gemini entry could be added without a new model launch.
  - **Outages:** If the leaderboard is down at check time, the market waits for the first check after it returns. If it is gone permanently, the market resolves "Other".
  - **Preliminary scores:** New models can debut with few votes and wide confidence intervals, and still be ranked.

## 2. Reference classes and base rates

1. **Which company held WebDev #1, 2025–2026 (by my rough count of month-ends):**
   - Google held #1 during roughly May–Aug 2025 with Gemini 2.5 Pro. It scored 1420 vs Claude 3.7 at 1357 (ITHome / Decrypt, May 2025).
   - From my background knowledge, not checked in this session: Gemini 3 Pro briefly took #1 in mid-Nov 2025, and Claude Opus 4.5 overtook it within weeks.
   - In 2026, Anthropic held #1 from at least Feb to June (Opus 4.5 Thinking in Feb; Opus 4.6 at 1547 in Mar; Opus 4.7 Thinking at 1568 in May) (Blog du Modérateur monthly series).
   - OpenAI's GPT-6 Astra led in early Sept 2026 (KuCoin, Sept 2026).
   - Claude Opus 5.5 has led since about Sept 23 (AI IDE List, Sept 25, 2026).
   - **Rough rate:** Google was #1 at about 3–4 of roughly 22 month-ends since Jan 2025 (about 15–18%). It was #1 at **0 of about 10 month-ends in 2026**.
2. **Google's WebDev debut ranks for new flagships:**
   - Gemini 2.5 Pro (2025) and Gemini 3 Pro (Nov 2025) debuted at #1.
   - Gemini 3 Pro had fallen to #4 at 1453 by Feb 2026 (Blog du Modérateur, Feb 2026).
   - Gemini 4 Argon debuted at #8 with 1679 (Arena on X, Sept 30–Oct 2026).
   - Gemini 4 Carbon debuted at #4 with 1768 (Arena on X / LLMReference, Oct 28, 2026).
   - So 2 of the last 4 flagship launches debuted at #1, and neither of the two Gemini 4 launches did.
3. **Catching up 40+ points without a new model:** Debut scores do drift.
   - GPT-6 Astra went from 1796–1797 at launch to about 1773 (−24).
   - Opus 5.5 went from 1818 to 1810 (−8).
   - Carbon's 95% confidence interval is ±15 on 2,230 votes.
   - A 42-point gap closing through drift alone would be unusual. Google most likely needs a new model, checkpoint or higher-effort variant.

## 3. Current state of the world (most recent first)

- **~Nov 1–6, 2026:** Most reports agree on this top of the board:

  | Rank | Model | Company | Score |
  |---|---|---|---|
  | 1 | Claude Opus 5.5 (Max) | Anthropic | 1810 |
  | 2 | GPT-6 Astra (Max) | OpenAI | 1773 |
  | 3 | Claude Sonnet 5.5 | Anthropic | ~1770 |
  | 4 | Gemini 4 Carbon (High) | Google | 1768 (CI 1753–1783) |
  | ~5–6 | Claude Fable 5.1 | Anthropic | ~1762–1764 |
  | ~11 | Gemini 4 Argon (High) | Google | 1679 |

  Sources: BenchLeader (Nov 1, 2026), Neoteo (Nov 2026), Blog du Modérateur (Nov 2026). Blog du Modérateur says Anthropic keeps first place while competitors gain ground. **Google trails by about 42 points.**
- **Nov 1, 2026:** TestingCatalog reports a new Gemini 4 Carbon checkpoint being tested anonymously on Arena. One tester says it is faster, better at 3D, thinks longer, and has outputs "strangely similar to Opus 5.5." This is anecdotal.
- **~Oct 29–Nov 3, 2026:** Google has given no developer or consumer availability date for Carbon, only "soon" (SmartScope; braindetox). Android Headlines (unverified) says developers would get it "1 or 2 weeks" after the initial cyber-defender access, i.e. around Nov 4–11.
- **Oct 28, 2026:** Google announced Gemini 4 Carbon, limited at first to cyber defenders in its Fairwind Program. It debuted at #1 in Text Arena, #2 in Agent Arena and #4 in WebDev. That WebDev score is 89 points above Argon (Arena on X; ProPakistani, Oct 29).
- **Oct 13, 2026:** Gemini 4 Argon became generally available (SmartScope / consens.io).
- **Sept 22, 2026:** Claude Opus 5.5 launched and took #1 on WebDev at 1818 ±21 (AI IDE List, Sept 25).
- **Sept 3, 2026:** GPT-6 Astra launched and took #1 at 1797, 35 points ahead of Claude Fable 5.1 (KuCoin, Sept 2026).
- **Scheduled events before Nov 30:** None confirmed.
  - Possible: wider Carbon release, perhaps a new checkpoint.
  - Possible: Google repeats its November launch pattern (Gemini 3 Pro launched Nov 18, 2025).
  - Unknown: any Anthropic or OpenAI release (nothing found).

## 4. Drivers and scenarios

**Paths to YES:**
- **(a)** The new Carbon checkpoint ships as the general release and replaces or joins the current entry with a WebDev score above about 1810. That needs a jump of about 40+ points from one checkpoint to the next. Gemini 2.5 Pro made gains of this size between 2025 checkpoints, but it is a large jump.
- **(b)** Google adds a higher-effort Carbon variant (for example "Max" or Deep Think) that scores higher. Competitors' top entries are already "Max" settings.
- **(c)** Opus 5.5's score drifts down and the new Carbon entry drifts up. This alone is unlikely to close 42 points.
- **(d)** A surprise Gemini 4 Pro or Ultra-class release. There is one unverified, undated report of a "Gemini 4 Pro" checkpoint on Arena (pasqualepillitteri.it).

**Paths to NO:**
- Google ships nothing new on WebDev by Nov 30. This is the status quo, with a 42-point gap.
- A new Google model ships but lands at #2–4, as Argon and Carbon did. Google has recently been stronger on Text Arena than on WebDev.
- Anthropic or OpenAI release a newer model, which widens the gap.

## 5. Signposts

- **Toward YES (large move):** Arena posts that a new Gemini or Carbon entry is "#1 in Code Arena: WebDev", or a Carbon general release with WebDev claims above about 1800.
- **Toward YES (moderate move):** TestingCatalog or other reports of more Gemini checkpoints on Arena with strong WebDev anecdotes; a scheduled Google launch event or blog post in mid-to-late November.
- **Toward NO:**
  - Carbon's general release turns out to be the same model with no change on the leaderboard.
  - A new Anthropic or OpenAI release (an Opus 5.5 successor, or a GPT-6 Astra update).
  - Google says its next launch is in December or later.
- **Live checks:** Opus 5.5's score holding at about 1810 versus drifting toward 1790, and how Carbon's confidence interval narrows.

## 6. Uncertainties

- I could not view the live leaderboard. I cannot confirm the Rank column (score-based or confidence-interval-based), any AutoEval markings, or anything that changed after about Nov 1.
- Whether the new Carbon checkpoint is better than the listed one on WebDev, and when, or whether, it will replace the current entry.
- The real timing of Carbon's general release. The "1–2 weeks" claim is unverified.
- Whether any Anthropic or OpenAI launches are planned for November 2026.
- The exact month-end history of #1 holders in 2025. Parts of the base rate rely on secondary reports and my background knowledge.
- Small conflicts between sources: Opus 5.5 at 1810 vs 1815; Argon at #8 vs #11.

## Sources
- [Arena.ai on X: Gemini 4 Carbon debut (#4 WebDev)](https://x.com/arena/status/2115495002998751262)
- [Arena.ai on X: Gemini 4 Argon #8 WebDev 1679](https://x.com/arena/status/2105394855644139908)
- [Arena.ai on X: Code Arena WebDev leaderboard](https://x.com/arena/status/2096290438064038201)
- [LMArena WebDev leaderboard (Nov 2026) – BenchLeader](https://www.benchleader.com/benchmarks/lmarena_webdev)
- [WebDev Arena coding AI ranking: November leaders – Neoteo](https://www.neoteo.com/en/claude-opus-55-leads-the-reported-november-webdev-arena-ranking)
- [WebDev Arena – LLMReference](https://www.llmreference.com/benchmark/lmarena-webdev)
- [IA : meilleurs modèles pour le code, novembre 2026 – Blog du Modérateur](https://www.blogdumoderateur.com/ia-meilleurs-modeles-code-developpement-web-novembre-2026/)
- [IA : meilleurs modèles pour le code, février 2026 – Blog du Modérateur](https://www.blogdumoderateur.com/ia-meilleurs-modeles-code-developpement-web-fevrier-2026/)
- [IA : meilleurs modèles pour le code, mai 2026 – Blog du Modérateur](https://www.blogdumoderateur.com/ia-meilleurs-modeles-code-developpement-web-mai-2026/)
- [Claude Opus 5.5 Hits #1 in Code Arena WebDev – AI IDE List](https://aiidelist.com/blog/claude-opus-5-5-code-arena-webdev)
- [OpenAI's GPT-6 Astra Tops Code Arena WebDev – KuCoin](https://www.kucoin.com/news/flash/openai-s-gpt-6-astra-tops-code-arena-webdev-leaderboard-with-1-797-points)
- [Gemini 4 Carbon Beats GPT-6 Astra and Claude Opus 5.5 – ProPakistani](https://propakistani.pk/2026/10/29/gemini-4-carbon-beats-gpt-6-astra-and-claude-opus-5-5-as-the-worlds-top-ai-model/)
- [Google tests new Gemini 4 Carbon checkpoint on Arena – TestingCatalog](https://www.testingcatalog.com/google-tests-new-gemini-4-carbon-checkpoint-arena/)
- [Gemini 4 Carbon availability – SmartScope](https://smartscope.blog/en/blog/gemini-4-carbon-availability-release-date-differences-argon-2026/)
- [Android Headlines on Carbon rollout](https://www.androidheadlines.com/?p=1321515)
- [Gemini 4 Argon release – cellcog](https://cellcog.ai/blog/gemini-4-release-date/)
- [Gemini 4 Pro leaks on Arena – pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/18784/gemini-4-pro-checkpoint-arena)
- [ITHome: Gemini 2.5 Pro tops WebDev Arena](https://www.ithome.com.tw/news/168805)
- [Decrypt: Gemini 2.5 Pro WebDev](https://decrypt.co/?p=318416)
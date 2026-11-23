# Research brief: Will OpenAI have the top model on the arena.ai Image Edit leaderboard on November 30, 2026?

*Prepared 2026-11-23. arena.ai and most news pages could not be opened directly because the proxy refused the connection. Every leaderboard figure below comes from search-engine snippets of arena.ai pages, Arena's posts on X, and third-party coverage. Treat exact scores as approximate.*

## 1. Resolution mechanics

- **What counts as YES:** an OpenAI model is in first place on the arena.ai Image Edit Arena leaderboard (https://arena.ai/leaderboard/image-edit), "Overall" view, filtered for "Models", when it is checked on **Nov 30, 2026 at 12:00 PM ET**. The deciding column is "Rank", not score.
- **Ties:** models tied on rank are ordered by which is listed higher on the page. If a tie remains, the company names are taken in alphabetical order. On the current board this hardly matters: OpenAI models hold Arena rank #1 and #2, and the top score leads by about 35 points (see §3).
- **Exclusions:**
  - Models marked "AutoEval" are excluded.
  - Models marked "Preliminary" do count. A newly launched model with few votes and a wide confidence interval can therefore win if Arena gives it rank 1.
- **Shared rank 1:** Arena's rank is based on confidence intervals, so a new model can share rank 1 with the leader even if its score is lower. In that case the listing order decides, and the page normally sorts by score. So in practice, the highest score among rank-1 models wins.
- **Ambiguities:**
  1. The image-edit page now has sub-boards: single-image, multi-image, and categories such as commercial design. Snippets title the default page "Single-Image Edit". It is unclear whether "Overall" means the default single-image view or a combined view. As of Nov 16, OpenAI's GPT-Image-2.5 Sunburst led both the single-image and multi-image boards, so the difference doesn't matter right now.
  2. Ownership: MAI models belong to Microsoft, Muse Image to Meta, and Grok Imagine to xAI. Partnerships such as Microsoft–OpenAI could cause confusion, but the "MAI" models are Microsoft's own.
- **If the leaderboard is down:** the market waits for the first check after it comes back. If it is permanently unavailable, the market resolves "Other".

## 2. Reference classes and base rates

**A. Which company has been #1 on Arena Image Edit over time.** I rebuilt this from snippets, so it is approximate.
- **Aug–Nov 2025:** Google led with nano-banana (Gemini 2.5 Flash Image), followed by Nano Banana Pro (Nov 2025).
- **Dec 2025:** GPT-Image-1.5 reportedly passed Nano Banana Pro by only about 3 points, roughly 1409 vs 1406 (OfficeChai; DigitalApplied/dev.to, Dec 2025).
- **Mar 26, 2026:** an OpenAI model was #1 at 1398 (benchmarklist snapshot).
- **Apr 2026:** GPT-Image-2 launched at #1, +125 over #2 on single-image edit (Kingy AI / 36kr, Apr 2026).
- **May 22 and Aug 28, 2026:** OpenAI was still #1, at about 1462–1467.
- **Sep 8, 2026:** GPT-Image-2.5 (Sunburst and Flare) took #1 and #2 on text-to-image, image edit, and multi-image edit (Arena on X, Sep 2026).
- **Summary:** OpenAI appears to have held #1 continuously for about 11 months, from about Dec 2025 to Nov 2026. It possibly lost the spot briefly to Nano Banana 2 around Feb–Mar 2026, which I couldn't confirm. The lead changed hands between companies roughly 3–5 times in about 16 months, or about 1 change per 13–20 weeks.

**B. Whether #1 changes in a given 7-day window.** With about 4 changes between companies over about 70 weeks, the naive rate is about 5–7% per week. This is an upper bound in the current situation, for two reasons:
- The leader has a large margin: 35 points over #2, and about 44 points over the best non-OpenAI model.
- Most past changes came when a new flagship launched, not from slow vote drift.

**C. How far new frontier models jump on debut.** Debuts vary widely:
- GPT-Image-2: +125 over the previous #1.
- GPT-Image-2.5 Sunburst: well above GPT-Image-2.
- MAI-Image-2.7-Preview: +45 over its predecessor, but it landed at #3.
- Nano Banana 2.1 (Oct 2026): debuted only at #6 on image edit.
- GPT-Image-2.6 Sunburst (Nov 2026): debuted at #3, below OpenAI's own 2.5.

Taking the lead from 1519 requires a big improvement for the leading model of any lab except OpenAI. The closest, Microsoft, needs about +44 points; Google's best edit model is about 90 points behind.

## 3. Current state of the world (most recent first)

- **Nov 21, 2026 (separate leaderboard):** Design Arena, which is not arena.ai, has GPT-Image-2.5 Sunburst #1 and GPT Image 2.6 Sunburst #2 on image editing (search snippet).
- **Nov 20, 2026 (separate leaderboard):** Artificial Analysis editing board, also not arena.ai, has MAI-Image-2.7 first at 1215. This shows Microsoft is competitive on other evaluations, but it is not the resolution source.
- **Nov 16, 2026 (arena.ai Image Edit snapshot):**

| Rank | Model | Company | Score |
|---|---|---|---|
| 1 | GPT-Image-2.5 Sunburst | OpenAI | 1,519 |
| 2 | GPT-Image-2.5 Flare | OpenAI | 1,484 |
| 3 | GPT-Image-2.6 Sunburst (Medium) | OpenAI | 1,481 |
| 4 | MAI-Image-2.7 | Microsoft | 1,475 |
| 7 | Grok Imagine Image 2.0 | xAI | 1,437 |

  Nano Banana 2.1 (Google) is at about 1,427–1,432, rank #6–#9. On the multi-image edit board, Sunburst leads at 1,527 and MAI-Image-2.7 is #3 at 1,458.
- **Nov 16, 2026:** Google rolled Nano Banana 2.1 into Google Pics. This is a product rollout, not a new model (Android Authority, Nov 2026).
- **Nov 5, 2026:** Arena posted that GPT Image 2.6 Sunburst (Medium) debuted at #3 on Image Edit with 1476, and Flare (Medium) at #5 with 1462 (Arena on X, Nov 5, 2026).
- **Nov 4, 2026:** OpenAI released Images 2.6, about 2x faster than 2.5 (OpenAI "Introducing Images 2.6"; TestingCatalog, Nov 2026). OpenAI just shipped, so it has little reason to launch again before Nov 30.
- **Oct 27, 2026:** MAI-Image-2.7-Preview (Microsoft) debuted at #3 on Image Edit with 1470, +45 over MAI-Image-2.6 (Arena on X; Microsoft AI on X, Oct 2026).
- **About Oct 6, 2026:** Google launched Nano Banana 2.1 (Gemini 3.6 Flash-based). It debuted at #6 on Image Edit (Decrypt; The Decoder; CellCog, Oct 2026).
- **Since about Sept 2026:** an anonymous model on Arena codenamed "spicy-mayo" has been rumored to be Google's Nano Banana 2.5. This rests on unofficial single-source pages (spicy-mayo.com; kie.ai). No launch date has been announced.
- **Gemini 4 family:** reportedly rolling out from Sep 30 to Nov 2026 (Argon, Carbon, Hydrogen, possibly Neon on Nov 18). These are conflicting secondary sources, and none mentions a Gemini 4 image-generation or editing model.
- **Scheduled events before close:** I found no announced image-model launches between Nov 23 and Nov 30. US Thanksgiving is Nov 26, and launches are typically fewer that week. However, Google did launch Nano Banana Pro on about Nov 20, 2025, so late-November launches have happened before.

## 4. Drivers and scenarios

**Paths to YES (OpenAI stays #1):**
- **Status quo** (the dominant path). Nothing launches in the 7 days, or anything that launches comes in below 1519. Vote drift over one week rarely moves a well-established leader 35+ points.
- **OpenAI improves its own lead.** For example, GPT-Image-2.6 Sunburst High is added, or its score drifts upward.

**Paths to NO:**
1. **Google launches Nano Banana 2.5 or Pro-tier "spicy-mayo".** This needs a launch in the next 7 days, plus Arena adding it to the leaderboard (Preliminary counts), plus a score of about 1520 or more. That is roughly +90 over Nano Banana 2.1. A jump that large has happened before (GPT-Image-2 was +125), but it is not typical.
2. **Microsoft ships a new MAI-Image version (2.8) or a final 2.7 that gains about 45+ points.** Microsoft has been releasing at a fast pace (2.5 → 2.6 → 2.7 over several months), but 2.7 only came out on Oct 27.
3. **Another lab makes a surprise leap.** Candidates are xAI's Grok Imagine 3, Meta's Muse, ByteDance's Seedream, and Black Forest Labs' FLUX 3. All are currently 80+ points behind, so this is low probability.
4. **A technicality.** A new model with a wide confidence interval shares rank 1 and is listed above Sunburst. Or Arena restructures the page or re-scores, for example by deprecating or relabeling GPT-Image-2.5 as AutoEval. Or the leaderboard is unavailable.

## 5. Signposts

- **Strongly toward NO:**
  - Google or Microsoft announces a new image or editing model between Nov 23 and Nov 30.
  - Arena posts on X that a model is "#1 in Image Edit Arena".
  - "spicy-mayo" is revealed or released.
- **Moderately toward NO:** leaks or rumors of a Gemini 4–based Nano Banana Pro successor around Thanksgiving week.
- **Toward YES:**
  - Nothing launches by about Nov 28.
  - Thanksgiving-week quiet.
  - Sunburst stays at about 1515–1520 in later snapshots.
- **Structural risk:** Arena changes the default view, the "Overall" definition, or how labels are applied.

## 6. Uncertainties

- I could not load the live leaderboard. The latest confirmed snapshot is from Nov 16, a week old, so a launch between Nov 16 and Nov 23 could have been missed. However, searches turned up no such #1 news.
- Whether "Overall" on the resolution page means the single-image board or a combined view. Today OpenAI leads both.
- The status and expected timing of Google's "spicy-mayo" (Nano Banana 2.5), and whether any Gemini 4 image model exists.
- Whether OpenAI briefly lost #1 to Nano Banana 2 around Feb–Mar 2026, which affects base-rate reference class A.
- Exact confidence intervals for the top models, which determine whether a strong newcomer could share rank 1.

## Sources
- [Best AI for Single-Image Editing: Image Edit Leaderboard (arena.ai)](https://arena.ai/leaderboard/image-edit)
- [Best AI for Multi-Image Editing (arena.ai)](https://arena.ai/leaderboard/image/image-edit/multi-image)
- [Best AI Photo Editor for Product Shots (arena.ai)](https://arena.ai/leaderboard/image/image-edit/single-image-commercial-design)
- [Arena.ai on X: GPT-Image-2.5 Sunburst #1 / Flare #2](https://x.com/arena/status/2097400515546255754)
- [Arena.ai on X: GPT Image 2.6 Sunburst and Flare debut](https://x.com/arena/status/2118139063345787124)
- [Arena.ai on X: MAI-Image-2.7-Preview #3 in Image Edit](https://x.com/arena/status/2115101113666134276)
- [Microsoft AI on X: MAI Image 2.7 Preview #3](https://x.com/MicrosoftAI/status/2115102961957499069)
- [Artificial Analysis on X: GPT Image 2.5 Sunburst editing frontier](https://x.com/ArtificialAnlys/status/2098477751225495957)
- [OpenAI: Introducing Images 2.6](https://openai.com/zh-Hans-CN/index/introducing-images-2-6)
- [TestingCatalog: OpenAI launches Images 2.6](https://testingcatalog.com/openai-launches-images-2-6-with-gifs-and-image-reference)
- [GPT Image 2.6 vs Gemini, FLUX and Seedream (Digital Applied)](https://www.digitalapplied.com/blog/gpt-image-2-6-vs-gemini-flux-seedream)
- [Best AI for Image Editing in 2026 (LLM Stats)](https://llm-stats.com/leaderboards/best-ai-for-image-editing)
- [Design Arena Image Editing Leaderboard](https://www.designarena.ai/leaderboard/image-to-image)
- [Image Editing Leaderboard Ranking (benchmarklist, Artificial Analysis)](https://benchmarklist.com/arenas/artificial_analysis_image_editing/)
- [Image Edit Arena Ranking (benchmarklist)](https://benchmarklist.com/arenas/arena_ai_image_edit/)
- [Kingy AI: GPT-Image-2's clean sweep of the Arena leaderboards](https://kingy.ai/news/openai-just-cooked-the-entire-image-generation-industry-inside-gpt-image-2s-historic-clean-sweep-of-the-arena-leaderboards-benchmarks/)
- [36kr: GPT Image 2 dominates rankings](https://eu.36kr.com/en/p/3784950967376900)
- [OfficeChai: GPT Image 1.5 passes Nano Banana Pro for top spot](https://officechai.com/ai/openais-gpt-image-1-5-goes-past-nano-banana-pro-to-get-the-top-spot-in-image-arena)
- [Gradually: GPT Image 1.5 vs Nano Banana Pro](https://www.gradually.ai/en/ai-image-model-comparison/gpt-image-1-5-vs-nano-banana-pro/)
- [The Decoder: Nano Banana 2.1](https://the-decoder.com/googles-new-image-model-nano-banana-2-1-generates-better-images-for-less-money/)
- [Decrypt: Google launches Nano Banana 2.1](https://decrypt.co/380257/google-launches-nano-banana-2-1)
- [CellCog: Nano Banana 2.1 price, Arena rank](https://cellcog.ai/blog/nano-banana-2-1/)
- [Android Authority: Google Pics gets Nano Banana 2.1](https://www.androidauthority.com/google-pics-nano-banana-2-1-3736470/)
- [Spicy-Mayo: Google's rumored Nano Banana 2.5](https://spicy-mayo.com/)
- [Kie.ai: Nano Banana 2.5 "Spicy Mayo" Arena test](https://kie.ai/blog/what-is-nano-banana-2-5)
- [OrcaRouter: Gemini 4 release date](https://www.orcarouter.ai/blog/gemini-4-release-date)
- [TechCityAuthority: MAI-Image-2.7-Preview jumps to third](https://www.techcityauthority.com/2026/10/microsoft-mai-image-2-7-preview-arena-image-edit-leaderboard.html)
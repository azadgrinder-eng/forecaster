# Research Brief: Ornn H200 Index (OCPI-H200) between $5.50 and $6.00 on Dec 31, 2026

*Note on access: direct fetches of data.ornn.com and of news pages were refused by the network proxy. All index values below come from search-engine snippets of Ornn's own pages and from news coverage. Index values should be checked against the live page and the keyless API before relying on them.*

## 1. Resolution mechanics
- **What counts as YES:** the finalized OCPI-H200 daily value for **December 31, 2026** on data.ornn.com/markets/h200 must be ≥ $5.50 and < $6.00. Under the rule that an exact boundary value goes to the higher bracket, **$6.00 exactly resolves to the $6.00–6.50 bracket (NO here)** and $5.50 exactly resolves YES. Values are published to the cent, so the YES window runs from $5.50 to $5.99.
- **Finalization:** the Dec 31 value is final once the Jan 1, 2027 data point is published. If it is not finalized by the end of Jan 7, 2027 (ET), the market uses the latest data available. Revisions made after finalization are ignored.
- **Erroneous data:** if a value is clearly wrong, the market can stay open up to 7 days waiting for a correction. After that, Polymarket issues a clarification.
- **Days covered:** the index publishes every day, weekends included (there are settles for Sat Nov 21 and Sun Nov 22, 2026). Dec 31, 2026 is a Thursday, so a print is expected. Dec 31 falls in the holiday period, when trading may be thin. That could make a single print noisier, because the index is built from executed trades.
- **What the index is:** Ornn describes it as a "volume-weighted, winsorized average of transacted GPU rental prices" across neoclouds, settling once per trading day. It uses executed trades, not listings or rate cards (Ornn data pages; Ornn coverage, Nov 2026). The ICE futures on OCPI-H100 settle on monthly averages (ICE product spec), but this market uses **a single day's print**, which is far noisier than a monthly average.
- **Ambiguity:** different Ornn pages showed different "latest" values on nearby dates (e.g., $6.00 for Nov 21, $5.79 for Nov 22, $6.53 for Nov 24). Each looks like a separate daily settle, not a conflict, but this should be checked against the live history table.

## 2. Reference classes and base rates
**A. How often a recent daily print fell in the $5.50–5.99 band.** Every daily value I could find from Oct–Nov 2026:

| Date | Value | In band? |
|---|---|---|
| Oct 4 | $5.57 | Yes |
| Oct 6 | $5.04 | No (third-party survey citing Ornn; treat with caution) |
| Oct 12 | $5.24 | No |
| Late Oct | $5.61 | Yes |
| Nov 11 (peak) | $7.75 | No |
| Nov 21 | $6.00 | No (goes to the higher bracket) |
| Nov 22 | $5.79 | Yes |
| ~Nov 23 (implied from the +6.7% 24h move into Nov 24) | ~$6.12 | No |
| Nov 24 | $6.53 | No |

That is **3 of 9 known prints (~33%)** in the band. The sample is small and not random.

**B. Volatility of the index (my own calculation from the prints above).**
- Day-to-day moves are about 3–7%: −3.5% on Nov 21→22, about +6% on Nov 22→23, +6.7% on Nov 23→24.
- The 30-day range as of Nov 21 was **$5.49–$7.75**, a spread of about 34% of the midpoint.
- Moves over a month have been as large as **+49%** (up to the Nov 11 peak) and **−16%** (Nov 11 to Nov 24).
- An earlier, undated BeInCrypto/Digital Today report described a **~40% fall in three weeks ($7 → ~$4)**.
- Over the 37 days from Nov 24 to Dec 31, a realistic 1-sigma range is probably ±$0.8–1.2 around the expected level. With a band only $0.50 wide, no single bracket is likely to hold much more than about 20–30% probability unless the index becomes much calmer.

**C. Longer-term level.**
- The 3-month change as of Nov 24 was −0.8%, which implies roughly $6.55–6.60 in late August.
- The H200 was up about 143% versus Jan 1, 2026 (a16z/Ornn via Wccftech), or about 160% in a separate Crypto Briefing headline. That puts the January 2026 level around $2.5–2.7.
- So 2026 was a strong uptrend followed by a sideways, volatile range of roughly $5–7.75 from about August to November.

## 3. Current state of the world (most recent first)
- **Nov 25, 2026:** Reports, mostly citing SemiAnalysis, say SpaceX cut small-cluster Blackwell rental rates by 20–35% (from $15–15.50 to $10–12 per GPU-hour). They also say Anthropic is **not renewing a lease on ~50,000 H200s**, and SpaceX is offering that capacity at **~$5 per GPU-hour for early-2027 delivery**, about 23% below Ornn's $6.53. None of this is confirmed by SpaceX or Anthropic. Neocloud stocks reportedly fell sharply on oversupply fears, and rumors of slowing growth in enterprise token usage were circulating (Longbridge, Futu, Crypto Briefing, BigGo, Nov 25–26, 2026).
- **Nov 24, 2026:** OCPI-H200 settled at **$6.53**: +6.7% on the day, +3.8% over 30 days, −0.8% over 3 months. It was down 16% from the Nov 11 high of $7.75. Other Ornn indices that day: B200 $9.07 (−8.8% from its Nov 8 peak), H100 SXM $3.16, B300 $10.87 (Ornn comparison page; news coverage).
- **Nov 22, 2026:** H200 at $5.79 (Ornn compare page).
- **Nov 21, 2026:** H200 at $6.00; 30-day range $5.49–$7.75 (Ornn H200 page).
- **Nov 11, 2026:** H200 peaked at $7.75, after rising about 49% in a month (Crypto Briefing).
- **Oct 11–25, 2026:** H200 up 12.3% (Ornn-based report). The late-October print was about $5.61; Oct 12 was $5.24 and Oct 4 was $5.57.
- **Other trackers, November 2026:**
  - Flopper: median on-demand price $4.00 across 27 providers.
  - Finitizer: median $5.40.
  - Thunder Compute: range $3.99–$10.85, mean $6.06 on Nov 3.
  - Ornn's transacted index sits at or above the on-demand medians.
- **Scheduled before Dec 31:** I found no Ornn methodology changes scheduled. Other possible catalysts:
  - year-end budget and contract cycles at neoclouds and AI labs;
  - more Blackwell and Rubin capacity coming online;
  - possible confirmation or denial of the SpaceX/Anthropic reports;
  - NVIDIA and AI-lab announcements in December;
  - the holiday slowdown in trading volume around Dec 24–31.

## 4. Drivers and scenarios
**Paths to YES (Dec 31 print of $5.50–5.99):**
- **Moderate drift down from about $6.0–6.5.** The SpaceX ~$5 forward offer for the returned H200s, Blackwell price cuts (B200 is cheaper per unit of performance at about $9–10), and softer sentiment pull the spot H200 toward the high $5s without a collapse.
- **Noise around $6.** If the true level stays near $6.00–6.20, ordinary daily swings of ±5% land a fair share of prints in the band. Nov 22's $5.79 is an example.

**Paths to NO, below $5.50:**
- **Faster repricing.** The H200 has fallen about 40% in three weeks before. Fifty thousand returned H200s is a large supply shock relative to traded volume. If holders cut asking prices to compete with the $5 offer, or token demand really is slowing, prints of $4.50–5.40 are plausible. Early-to-mid October values ($5.04–5.24) show this range has already been visited.

**Paths to NO, $6.00 or above:**
- **Demand holds up.** The 2026 trend has been strongly upward (+143–160% YTD), and the rebound to $6.53 on Nov 24 came *on the day* the bearish SpaceX news broke. If compute shortages persist (agentic and reasoning workloads, new model launches), the index could revisit $6.5–7.75.
- **Boundary risk.** A print of exactly $6.00 resolves NO.

**Key dependence:** whether the Nov 25 supply and demand news marks a regime change (Hopper repricing toward $5) or a sentiment blip inside a $5–7.75 range.

## 5. Signposts
- **Ornn H200 prints from Nov 25 through mid-December:**
  - A run of settles below $6 (e.g., $5.5–5.9) supports YES.
  - Sustained moves below about $5.3, or back above about $6.5, both lower the YES odds.
  - The 7-day and 30-day change figures on the Ornn page give a quick read of direction.
- **Confirmation or denial of the Anthropic H200 non-renewal and SpaceX's ~$5 offer, plus any other large H200 fleets coming back on the market:** pushes downward.
- **B200/B300 index direction:** further Blackwell cuts pull the H200 down through substitution; a Blackwell rebound supports the H200.
- **Neocloud earnings and commentary (CoreWeave, Nebius, Lambda) on utilization, and any data on token growth:** a bigger effect on direction than on level.
- **Other trackers (Silicon Data H200 index, SemiAnalysis rental index):** independent confirmation of the trend.
- **Holiday-period trading volume:** thin trading means bigger daily noise, which flattens the distribution and hurts any single narrow bracket.

## 6. Uncertainties
- I could not retrieve the full daily history or the live current value. The latest confirmed print is Nov 24 ($6.53); values for Nov 25–26 are unknown.
- The volatility estimates rest on about 9 scattered prints. The true daily standard deviation and the degree of mean reversion are unknown.
- Ornn's exact methodology could not be confirmed from a primary document: trade weighting, winsorization thresholds, minimum volume, and how days without trades are handled (carry-forward?).
- Dates are unclear for the "40% drop in three weeks" episode and the "+160% since January" figure.
- The SpaceX/Anthropic reports are unconfirmed, and the $5 price is for **early-2027 delivery**, so it may not hit the spot index before Dec 31.
- It is unclear how holiday trading affects the Dec 31 settle specifically, and whether Ornn has ever revised or corrected prints.

## Sources
- [H200 Price: $6.00/hr (Nov 21, 2026) – Ornn](https://data.ornn.com/markets/h200)
- [GPU Cloud Price Comparison 2026 – Ornn](https://data.ornn.com/gpu-cloud-price-comparison)
- [H200 vs RTX PRO 6000 $5.79 vs $1.53/hr (Nov 22, 2026) – Ornn](https://data.ornn.com/markets/compare/h200-vs-rtx-pro-6000)
- [GPU Price Index: Daily H100, H200, B200 & A100 – Ornn](https://data.ornn.com/markets)
- [AI Compute Market Data & Price Indices – Ornn](https://data.ornn.com/analytics)
- [SpaceX reportedly slashes Blackwell GPU rents as Anthropic hands back 50,000 H200s – Crypto Briefing](https://cryptobriefing.com/spacex-reportedly-slashes-blackwell-gpu-rents-as-anthropic-hands-back-50000/)
- [SpaceX Reportedly Cuts Blackwell GPU Rental Rates by Up to 35%… – Longbridge](https://longbridge.com/en/news/306836236)
- [Computing Power "Bearish Smash"… – Longbridge](https://longbridge.com/en/news/306839350)
- [SpaceX reportedly cut Blackwell GPU rental rates… – Futu](https://news.futunn.com/en/post/1005652303/spacex-reportedly-cut-blackwell-gpu-rental-rates-by-as-much)
- [Bearish Shock to Compute Markets – Futu](https://news.futunn.com/en/post/1005674034/bearish-shock-to-compute-markets-rumors-of-slowing-enterprise-token)
- [Nvidia GPU Rental Prices Lose Upward Momentum; Neocloud Stocks Plunge – BigGo Finance](https://finance.biggo.com/news/3650fded-d702-46d1-83c2-ddf952b8e749)
- [Ornn Exchange data shows GPU rental prices climbing month-on-month – Crypto Briefing](https://cryptobriefing.com/ornn-exchange-gpu-rental-prices-rising/)
- [Ornn Exchange Data Shows GPU Rental Prices Climb – KuCoin](https://www.kucoin.com/news/flash/ornn-exchange-data-shows-gpu-rental-prices-climb-month-on-month-across-chip-generations)
- [Nvidia H200 rental costs rise about 160% since January – Crypto Briefing](https://cryptobriefing.com/nvidia-h200-rental-costs-rise-160-percent/)
- [Nvidia GPUs appreciating assets – Wccftech](https://wccftech.com/nvidia-gpus-appreciating-assets-a100-rental-premium/)
- [Nvidia's Most Important Rental Chip Just Got 40% Cheaper – BeInCrypto](https://beincrypto.com/nvidia-h200-prices-nvda-stock-risks/)
- [Nvidia H200 GPU rental rates fall 40% – Digital Today](https://www.digitaltoday.co.kr/en/view/59712/nvidia-h200-gpu-rental-rates-fall-40-percent-ai-chip-scarcity)
- [What It Actually Costs to Rent an H100, H200, or B200 in October 2026 – dreaming.press](https://dreaming.press/posts/gpu-rental-price-october-2026.html)
- [NVIDIA H200 Price Comparison (November 2026) – Thunder Compute](https://www.thundercompute.com/blog/nvidia-h200-pricing)
- [NVIDIA H200 Cloud Pricing: Compare 31 Providers – Flopper](https://flopper.io/pricing/nvidia-h200)
- [NVIDIA H200 Rental Price per Hour (Nov 2026) – Finitizer](https://tools.finitizer.com/gpu-rental-prices/h200)
- [Ornn Compute Price Index (OCPI) H100 Future – ICE](https://www.ice.com/products/83050006/Ornn-Compute-Price-Index-OCPI-H100-Future)
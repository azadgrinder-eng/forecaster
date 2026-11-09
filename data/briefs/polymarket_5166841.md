# Research Brief: Will the Ornn H100 Index be at least $3.25 on November 30, 2026?

*Prepared 2026-11-09. Note on method: every page fetch was refused by the network proxy, including dashboard.ornnai.com and data.ornn.com. All figures below come from search-result snippets of Ornn's own pages and secondary reports. Treat each daily value as approximate and check it against the live chart.*

## 1. Resolution mechanics

- **What counts as YES:** The finalized Ornn H100 Index daily value for **November 30, 2026** is **≥ $3.25**. If the value lands exactly on a bracket boundary, it resolves to the higher bracket, so exactly $3.25 is YES.
- **Source:** The H100 Index chart at dashboard.ornnai.com.
- **When a value is final:** A day's value is finalized once the next day's point is published, so the Nov 30 value is final once the Dec 1 point appears. If it is not finalized by the end of Dec 7 (ET), the market uses the latest data available then. Revisions after finalization are ignored.
- **Day of week:** Nov 30, 2026 is a Monday, four days after US Thanksgiving (Nov 26).
- **Edge cases and ambiguities:**
  - **Which series is on the chart.** Ornn reportedly replaced an older, offer-based "Ornn US H100 Index" with the transaction-based Ornn Compute Price Index (OCPI) for H100 SXM. That methodology is dated July 24, 2026 (aiwiki.ai Ornn entry, accessed Nov 2026). Most current Ornn data now sits at data.ornn.com. I could not confirm that dashboard.ornnai.com shows exactly the same series as the OCPI H100 SXM values quoted below, or whether it redirects there. Other markets have pointed to ornn.trade as their source.
  - **Settlement time.** Ornn pages list different settlement times (4:00 PM ET on one page, 12:00 AM ET on another). This could change which calendar date a value is stamped with.
  - **Conflicting values.** Secondary sources disagree on the same dates. For example, Sep 7 is reported as both $3.17 and $3.28, and Oct 1 as $2.92 while Oct 2 is $2.79. Small labeling differences matter, because the threshold is only about 5% above the latest known level.

## 2. Reference classes and base rates

1. **How often recent daily readings were at or above $3.25.** I collected about 12 dated OCPI H100 values from mid-2026 to Nov 7 (Section 3). Only **two** were ≥ $3.25: Sep 7 at about $3.28 (as reported by KuCoin and Seoul Economic Daily; the official settlement may have been $3.17) and Nov 6 at $3.28. That is roughly 10–20% of sampled days. The index has spent most of Sep–Nov between **$2.59 and $3.21**.
2. **Probability of a +5% move in about 21 days for a volatile, mean-reverting series.**
   - Day-to-day swings of 4–6% are common: −4.5% on Oct 2, −5.5% on Nov 7, and roughly +6% from Nov 5 to Nov 6.
   - The 30-day range has been about ±12% around the mean.
   - Treat the Nov 30 value as noise around a level of about $3.10–3.15 with a standard deviation of about $0.15–0.20. On that basis, P(≥ $3.25) is about 20–30% with no drift. If the recent +11.5% one-month trend partly continues (center about $3.20), it rises to about 40–45%.
3. **Longer trend.** Ornn's all-time high was **$2.94 on May 25, 2026** (Crypto Briefing / KuCoin, May 2026). A June high of $3.17 and a June 22 low of $2.27 come from an unreliable Cryptorank page. Since then the index has made higher highs: about $3.17–3.28 in September and $3.28 in November. Other trackers also show H100 rents rising through 2026. SemiAnalysis's one-year contract index went from $1.70 in October 2025 to $2.35 in March 2026, and one index shows +30% year on year (search summaries of CloudZero and getdeploying, Oct–Nov 2026). The structural drift is upward, but 3.25 has only been touched at peaks.

## 3. Current state of the world (most recent first)

- **Nov 8, 2026:** Silicon Data's neo-cloud H100 series was $3.00, up from $2.93 on Nov 1. This is a separate index, but it confirms prices drifting up (search summary of silicondata.com).
- **Nov 7, 2026:** OCPI H100 SXM settled at **$3.10/GPU-hr**, −5.5% on the day and **+11.5% over one month** (data.ornn.com homepage, Nov 7). This is the latest Ornn value I could find; I found nothing for Nov 8 or 9.
- **Nov 6, 2026:** **$3.28**, the latest settlement on one Ornn listing (data.ornn.com, Nov 6).
- **Nov 6, 2026:** Spheron reports market H100 rental prices of $2.20–$12.29/hr; its own on-demand price is $2.98 (Spheron blog, Nov 6).
- **Nov 5, 2026:** **$3.13** (Ornn GPU cloud price comparison page, Nov 5). An undated Ornn page shows $3.15.
- **Late Oct / Nov 2026:**
  - An aggregate index puts the median H100 on-demand price at $3.87 across 46 providers, up 11% over four weeks.
  - Commentary attributes the tightness to an HBM-driven supply squeeze and growing inference demand rather than shortages of the GPU chips themselves (search summaries of getdeploying/Thunder Compute, Oct–Nov 2026).
- **Oct 25, 2026:** About $3.03 (Xenospectrum, citing OCPI).
- **Oct 20, 2026:** $3.12 (Ornn Bloomberg tickers page; Bloomberg ticker ORNNH100).
- **Oct 14, 2026:** $3.21. Ornn also launched an "H100 Volatility Index" built on OCPI history (Ornn on X / data.ornn.com).
- **Oct 7, 2026:** Uvik's median on-demand price across 16 providers was $4.20.
- **Oct 4, 2026:** **$2.59**, the recent low (data.ornn.com/preview). OKX showed $2.592 for Oct 3.
- **Oct 2, 2026:** $2.79, −4.5% on the day (data.ornn.com/markets/h100-sxm).
- **Oct 1, 2026:** $2.92, +3.2% over 30 days, with a three-month range of **$2.46–$3.17** (CloudZero). Nebius raised on-demand prices 17–21% the same day.
- **Sep 29, 2026:** ICE exchange notice listing Ornn Compute contracts for Q4 2026. OCPI H100 futures (ticker HPR) are cash-settled monthly against daily OCPI H100. Some pages describe them as pending CFTC review.
- **Sep 7, 2026:** OCPI-H100 settled at $3.17 (+19% over 30 days). Some reports cite $3.28 and +22% over the month (TradingKey; Seoul Economic Daily, Sep 22).
- **May 25, 2026:** All-time high at that point of $2.94, followed by a 3–9% pullback. ICE/Ornn futures launched on May 19 (Crypto Briefing, May 2026).
- **Scheduled before Nov 30:**
  - US Thanksgiving, Nov 26. Holiday demand effects on transaction-based prices are unknown.
  - Month-end on Nov 30, which is also the November futures settlement month. Any month-end contract-roll effects on the index are unknown.
  - Platts plans to launch US GPU compute price assessments around Nov 23 (S&P Global subscriber note), which is a competing benchmark only.
  - No known large H100 supply release.

## 4. Drivers and scenarios

**Paths to YES (≥ $3.25):**
- **The uptrend continues.** The one-month change is +11.5%, there are reports of a supply squeeze (HBM, Blackwell ramp limits), inference demand keeps growing, and providers such as Nebius are raising prices. This would need the level to move from about $3.10 to about $3.25 or more, roughly +5%.
- **A noise spike on the day.** Single-day jumps of 5–6% are common: Nov 5→6 went from $3.13 to $3.28. Even if the underlying level stays near $3.15, the Nov 30 print could land above $3.25 by chance.

**Paths to NO:**
- **Mean reversion.** The Nov 6 print of $3.28 already reversed to $3.10 the next day. Since September, every print at or above $3.2 has fallen back toward $2.8–3.1.
- **More supply.** Blackwell (B200/B300) capacity coming online pushes H100 renters to newer GPUs and lowers the H100 price.
- **Holiday or month-end softness.** Fewer or lower-priced transactions around Thanksgiving could weigh on the print just before Nov 30. This is speculative.
- **A repeat of early October.** The index fell from $2.92 to $2.59 within three days in early October.

**What matters most:** whether the index level in late November sits near $3.10 (YES is then about 20–30%) or near $3.20+ (YES is then about 45%+), plus a large one-day noise term.

## 5. Signposts

- **Daily OCPI prints from Nov 9 to 29.** This is the dominant signal. A run of closes at or above $3.20 in the week of Nov 23 moves the probability up sharply. Prints of $3.00 or less move it down.
- **The 7-day and 30-day change fields on data.ornn.com.** A 30-day change that stays positive (above +10%) supports YES.
- **Silicon Data's H100 index (SDH100RT) and neo-cloud median trackers.** A move from $3.00 toward $3.10+ would corroborate broad market tightening.
- **Provider price announcements** in either direction (CoreWeave, Lambda, Nebius, hyperscalers), and any news on HBM or Blackwell supply.
- **The Ornn H100 Volatility Index level.** Higher volatility widens the outcome range, which helps YES because the threshold sits above the current level.
- **Ornn methodology or dashboard changes,** or clarification of which series dashboard.ornnai.com displays.

## 6. Uncertainties

- **No live access to the resolution chart.** I could not view dashboard.ornnai.com or the full daily history, and the sampled values are sparse and sometimes inconsistent (Sep 7: $3.17 vs $3.28; Oct 1 vs Oct 2).
- **Unconfirmed series identity.** I could not confirm that the dashboard's "H100 Index" equals the OCPI H100 SXM series, or rule out that it is the legacy offer-based index.
- **Unknown daily volatility.** I don't know the true daily volatility or how strongly the index mean-reverts; the estimated standard deviation of about $0.15–0.20 for the Nov 30 value is a rough inference.
- **No values after Nov 7.**
- **Unknown seasonality.** I found no data on holiday or weekend effects on the index.

## Sources
- [Compute Price Index (OCPI): Live GPU Rental Prices (data.ornn.com)](https://data.ornn.com/)
- [H100 SXM Pricing 2026 (Ornn)](https://data.ornn.com/markets/h100-sxm)
- [H100 Price Index: Live GPU Prices (Ornn preview)](https://data.ornn.com/preview)
- [GPU Cloud Price Comparison 2026 (Ornn)](https://data.ornn.com/gpu-cloud-price-comparison)
- [Bloomberg Tickers for Ornn GPU and Token Price Indices](https://data.ornn.com/markets/bloomberg)
- [The Price Index – Ornn Data docs](https://data.ornn.com/docs/price-index)
- [Ornn on X – H100 Volatility Index](https://x.com/OrnnExchange/status/2092234800694222958)
- [Nvidia H100 price in 2026 (CloudZero)](https://www.cloudzero.com/blog/h100-gpu-cost/)
- [NVIDIA H100 GPU Price 2026 (Spheron)](https://www.spheron.network/blog/nvidia-h100-price-2026/)
- [GPU Price Index 2026 (Uvik)](https://uvik.net/blog/gpu-price-index/)
- [GPU Rental Price Trends 2026 (getdeploying)](https://getdeploying.com/gpu-price-trends)
- [AI GPU Rental Market Trends Oct 2026 (Thunder Compute)](https://www.thundercompute.com/blog/ai-gpu-rental-market-trends)
- [H100 Rental Price Index (Silicon Data)](https://www.silicondata.com/products/silicon-index/h100)
- [TradingKey – Ornn data shows H100 rental prices jump 22%](https://www.tradingkey.com/analysis/stocks/us-stocks/262155850-nvidia-h100-ornn-rental-surge-22-percent-jensen-huang-gpu-asset-tradingkey)
- [Seoul Economic Daily – H100 rental prices jump 22% in a month](https://en.sedaily.com/finance/2026/09/22/h100-rental-prices-jump-22-percent-in-a-month-as-gpu)
- [H100 rental prices slide after early May surge (Crypto Briefing)](https://cryptobriefing.com/h100-rental-prices-slide-ornn-ai/)
- [Cryptorank – Ornn H100 Compute derivatives](https://cryptorank.io/price/the-ornn-h-100-compute-derivatives/analytics)
- [OKX – ORNN Compute Index H100](https://www.okx.com/en-us/price/ornn-compute-index-h100)
- [Xenospectrum – a16z GPU rental premium / Ornn index](https://xenospectrum.com/en/a16z-gpu-rental-premium-ornn-index/)
- [aiwiki.ai – Ornn](https://aiwiki.ai/wiki/ornn)
- [ICE – OCPI H100 Future](https://www.ice.com/products/83050006/Ornn-Compute-Price-Index-OCPI-H100-Future)
- [ICE Exchange Notice – ORNN Compute 4Q2026](https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_Exchange_Notice_ORNN_Compute_4Q2026_20260929.pdf)
- [S&P Global Platts – US GPU compute prices launch note](https://www.spglobal.com/energy/en/pricing-benchmarks/our-methodology/subscriber-notes/110526-platts-to-launch-us-gpu-compute-prices-nov-23)
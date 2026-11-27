# Research brief: will the average Ornn OCPI-B300 value for December 2026 be above $11.00?

*Prepared 2026-11-27. Data access was limited: the proxy refused every WebFetch, including data.ornn.com. All figures below come from search-result snippets of secondary reports, so the exact daily values need checking against Ornn's own page.*

## 1. Resolution mechanics

- **What counts as YES:** take the arithmetic mean of the finalized daily settled values of Ornn's OCPI-B300 dated December 1–31, 2026, and round it to the nearest cent. YES requires that average to be **strictly above $11.00**. An average of exactly $11.00 resolves NO.
- **When a value is final:** a daily settle becomes final once the next day's settle is published. Revisions after that do not count. The Dec 31 value is final only when the Jan 1 (or next trading day) settle comes out. Any December value still not final by 11:59 PM ET on Jan 7, 2027 is dropped, and the market uses whatever finalized values exist.
- **Who decides:** the source is Ornn, data.ornn.com/markets/b300. The market can stay open up to 7 days for a correction if a published value is clearly wrong because of a technical or operational error or tampering.
- **Fallbacks:**
  - If the index is discontinued, the page goes away, or the methodology or unit changes materially, and no December values exist by Jan 7, 2027, "another credible source" of B300 rental prices is used. If there is none, the market resolves 50-50.
  - This matters a lot. Other B300 indices sit far lower: Silicon Data is about $7.2–7.7 and Liquid Compute was $7.19 on Nov 24. Under the fallback, NO is almost certain.
  - The fallback looks unlikely to trigger. ICE lists futures on Ornn indices, and Polymarket launched B300 markets on Ornn around Nov 25, so Ornn has commercial reasons to keep publishing.
- **Edge cases and ambiguities:**
  - **Days included:** reports say OCPI "settles once per trading day" (Ornn data page via search snippets, Nov 2026). It is unclear whether weekends and holidays (Dec 25) get a settle. That changes how many days go into the average, though not much else.
  - **How daily values are built:** daily values are averages of hourly prices (ICE B200 contract spec, Oct 6, 2026). The B300 index probably works the same way.
  - **What the index measures:** executed on-demand rental transactions. Reserved and interruptible/spot rentals are excluded. Prices are in USD per GPU-hour.

## 2. Reference classes and base rates

1. **Random walk around the current level.** The latest confirmed settle is about **$10.83 (Nov 25)**, so the threshold is about 1.6% above spot.
   - The December average is centred roughly 2.5–3 weeks ahead.
   - Measured volatility is high. Since Aug 26, daily settles ranged from **$9.63 to $14.23** (Polymarket-focused analysis, late Nov 2026).
   - The index rose to a record $14.23 on Oct 12, then fell about 24% by Nov 25 (BigGo Finance, late Nov 2026).
   - Single-day moves of about 3% are common, e.g. $11.19 → $10.87 from Nov 23 to Nov 24 (−2.9%).
   - With a month-ahead log standard deviation of roughly 8–12% and no drift, the chance that the average ends above a level 1.6% over spot is roughly **40–45%**. Adding the recent downward momentum lowers that, and assuming mean reversion toward the ~$11.5–12 autumn average raises it.
2. **Previous-generation GPU prices once the next generation ships.**
   - H100 on-demand prices fell steadily (about $8/hr in 2023 to about $2/hr in 2025) as Blackwell supply arrived. That is widely reported industry history, not re-verified here.
   - Vera Rubin is now shipping to clouds: CoreWeave, Google Cloud, Azure, OCI and Nebius (NVIDIA blog and GCN, Jul–fall 2026).
   - This class points toward B300 rental prices drifting down over the medium term, though usually over quarters rather than weeks.
3. **The 2026 GPU-rental bull market.**
   - Ornn's B200 index went from $2.31 in early March to $4.95 in spring 2026 (Tunguz, 2026), and later to a record $8.54 (Blockspace, 2026).
   - B300 rose more than 20% in the month to about mid-October (Shay Boloor on X, ~Oct 2026).
   - In 2026, sharp drops in these indices have often been followed by new highs. That argues against simply extrapolating the decline.

## 3. Current state of the world (most recent first)

- **Nov 26–27, 2026:** no settle found for these days.
- **Nov 25:** OCPI-B300 at **$10.83** (Ornn essay via search; news report).
  - Same day: Bloomberg/Liquid Compute report that Asian data centres and neoclouds are looking for US clients to offload extra B300 capacity after new US compute rules. Liquid Compute's B300 rate fell 6.9%, from $7.72 in late October to $7.19 on Nov 24 (Techmeme/Bloomberg, Nov 25).
  - Polymarket launched GPU rental-price markets settled on Ornn (Wisevoter, Nov 26).
- **Nov 24:** **$10.87** (Quiver Quant citing Ornn data page).
- **Nov 23:** **$11.19**. Ornn's page showed a 1-month change of −2.10% at that print (Quiver Quant).
- **Nov 22:** **$11.46** (search snippet of a report).
- **About Nov 18:** an Ornn page snapshot showed **$11.66**, up 3.19% on the day. The date comes from page metadata and is uncertain.
- **Nov 20:** Danske Bank said chips are getting dearer to rent. Agora Intelligence reports B300 up 7.6% from October to November on its own index, which is not Ornn.
- **Nov 19:** a US rule took effect requiring licences for overseas data centres that provide large amounts of compute to Chinese firms. Thousands of B300s meant for Chinese customers reportedly moved to the resale and rental market. Separately, Nvidia sellers reportedly told neoclouds not to rent to Chinese firms (CNBC via The Next Web and Silicon Report, Nov 2026).
- **Late Nov:** neocloud stocks fell on oversupply fears: CoreWeave −11.9%, Nebius −10.7%, NVDA −5.9% (BigGo Finance).
- **Oct 30:** B300 reportedly at **$12.29** (Tunguz). Whether this is a daily, weekly or monthly-average figure is unclear.
- **Oct 15:** Compute Desk said B300 on-demand prices hit an all-time high after 17 straight up days. Explainx could not verify the exact claim but confirmed the uptrend.
- **Oct 12:** OCPI-B300 record of **$14.23**.
- **Oct 5:** ICE Ornn H100 and B200 futures began trading (ICE notice, Sep 29).
- **Aug 26:** start of the published OCPI-B300 settle history found. The low since then is $9.63, date not found.
- **Scheduled before or during December:**
  - Nov H100 ICE futures expire Nov 30.
  - Vera Rubin cloud GA rollouts are ongoing (Google A5X GA "next month" per NVIDIA blog; exact date unclear).
  - Possible follow-on US export or compute-rule guidance.
  - Holiday-season demand in late December.
  - No Ornn methodology changes found.

## 4. Drivers and scenarios

**Paths to YES (December average above $11.00):**
- The late-November dip turns out to be a short-term shock from China-rule capacity being dumped. Demand for inference, open models and agentic workloads absorbs the extra supply, and the index recovers to $11.5–12, the October–November range.
- New model launches or training runs spike on-demand demand. B300s are scarce on-demand at neoclouds, which held prices above $11 for most of Sep–Nov.
- The index's high volatility: even a temporary jump in early or mid December can lift the monthly mean.

**Paths to NO (average at or below $11.00):**
- Supply released by the Nov 19 rule keeps flowing into the on-demand market. Liquid Compute already showed −7% in a month.
- Vera Rubin ramps and buyers shift to Rubin, softening Blackwell Ultra pricing.
- Lower demand over the holidays, while neocloud oversupply fears persist.
- The index simply stays at its current $10.8–10.9 level. That is already NO, because the threshold needs about +1.6%.
- Fallback to a non-Ornn source (unlikely), which gives about $7–8 and so NO.

**Arithmetic check:** if early December settles near $10.8, later days have to average about $11.1–11.2 or more to bring the mean above $11.00. Because the first days of the month weigh equally, the starting level in early December matters a lot.

## 5. Signposts

- **Daily OCPI-B300 settles from Nov 26 to early December** are the biggest signal. A move back above $11.3–11.5 raises the chance of YES. Settles staying below $10.7 lower it a lot.
- **Other indices:** whether Silicon Data and Liquid Compute B300 rates keep falling (bearish) or turn back up.
- **China-rule spillover:** news on whether the released B300 capacity gets absorbed, e.g. US customers signing up.
- **Vera Rubin:** cloud GA and on-demand pricing announcements, especially from neoclouds. Wide availability is bearish for B300.
- **Big demand shocks:** major model releases or reports of shortages (bullish).
- **Ornn methodology or provider-pool changes,** or data outages.

## 6. Uncertainties

- I could not read data.ornn.com directly. The exact recent daily series, the Nov 26–27 values, and whether weekends get settles all remain unconfirmed.
- Secondary sources conflict: the $11.66 snapshot's date is unclear, and the $12.29 figure for Oct 30 is unclear in kind.
- Sources disagree on direction. Agora and Danske say B300 rental prices rose in November, while Ornn and Liquid Compute show declines.
- I found no history of OCPI-B300 monthly averages (September, October, or November to date).
- No full methodology was found: which providers are included, how transactions are weighted, or whether the provider mix changed recently. A mix change could cause level jumps.
- How the China-rule supply shock will play out and how fast Vera Rubin cuts into B300 demand are both unknown.

## Sources

- [Ornn Compute Price Index (OCPI) H100 Future – ICE](https://www.ice.com/products/83050006/Ornn-Compute-Price-Index-OCPI-H100-Future)
- [ICE Futures US Exchange Notice ORNN Compute 4Q2026 (Sep 29, 2026)](https://www.ice.com/publicdocs/futures_us/exchange_notices/ICE_Futures_US_Exchange_Notice_ORNN_Compute_4Q2026_20260929.pdf)
- [ICE OCPI B200 Future contract spec](https://www.ice.com/api/productguide/spec/83050009/pdf)
- [Ornn GPU Price Index – data.ornn.com/markets](https://data.ornn.com/markets)
- [Ornn GPU Price Index FAQ](https://data.ornn.com/faq)
- [Introduction to Compute Markets #1 – Ornn](https://data.ornn.com/publications/introduction-to-compute-markets-1)
- [Renting the Shovels: B300, H100, and B200 Above the Line – Polyclarity](https://polyclarity.substack.com/p/renting-the-shovels-b300-h100-and)
- [Quiver Quant – December 2026 B300 average article](https://www.quiverquant.com/news/A+trader+just+placed+a+$12K+bet+on+B300+average+rental+price+in+December+2026+being+above+$12.00)
- [Quiver Quant – January 2027 Ornn B300 article](https://www.quiverquant.com/news/A+trader+just+placed+a+$12K+bet+against+the+average+Ornn+B300+rental+price+in+January+2027)
- [Compute rental prices soften, Neocloud stocks plunge – BigGo Finance](https://finance.biggo.com/news/ced706d0-3a15-4912-a990-85f306a65d14)
- [Nvidia GPU Rental Prices Lose Upward Momentum – BigGo Finance](https://finance.biggo.com/news/3650fded-d702-46d1-83c2-ddf952b8e749)
- [Southeast Asian Data Centers Cut Off…B300 Rental Rates Plunge 7% – BigGo Finance](https://finance.biggo.com/news/30998665-bbbf-475b-9a8f-a2b1b09dabdf)
- [Techmeme: Liquid Compute / Bloomberg on B300 rental costs falling (Nov 25, 2026)](https://www.techmeme.com/261125/p14)
- [Nvidia sellers reportedly bar neoclouds from renting to Chinese firms – The Next Web](https://thenextweb.com/news/nvidia-gpu-sellers-neoclouds-no-chinese-renters)
- [GPU Rental Prices Rise Fastest on B300 as Scarcity Shifts – Agora Intelligence](https://agora-intelligence.com/en/blog/gpu-rental-price-index-november-2026-blackwell-scarcity/)
- [Polymarket Launches GPU Rental Price Markets – Wisevoter (Nov 26, 2026)](https://wisevoter.com/world/2026/11/26/polymarket-nvidia-gpu-rental-price-markets)
- [Blackwell Ultra GPU rental prices climb 17 straight days to a record high – Crypto Briefing](https://cryptobriefing.com/blackwell-ultra-gpu-rental-prices-record-high/)
- [B300 rental prices record high: claimed vs verified – explainx.ai](https://explainx.ai/blog/nvidia-b300-gpu-rental-prices-record-high-17-day-streak-compute-desk-claimed-vs-verified-2026)
- [Shay Boloor on X – B300 rental rates up 20%+](https://x.com/StockSavvyShay/status/2111548896610844965)
- [The Financial Engineering Essential for AI in 2027 – Tomasz Tunguz](https://tomtunguz.com/the-financial-engineering-essential-for-ai-in-2027/)
- [B200 GPU pricing spot market – Tomasz Tunguz](https://tomtunguz.com/b200-gpu-pricing-spot-market-model-releases/)
- [B200 rental index hits record $8.54 – Blockspace](https://blockspace.media/insight/ornn-b200-rentals-hit-record/)
- [B300 Rental Price Index – Silicon Data](https://www.silicondata.com/products/silicon-index/b300)
- [NVIDIA Vera Rubin Ramps Into Full Production – NVIDIA Newsroom](https://nvidianews.nvidia.com/news/vera-rubin-full-production-agentic-ai-factory)
- [NVIDIA Vera Rubin chips begin shipping to cloud providers – GCN](https://gcn.com/nvidia-vera-rubin-chips-begin-shipping/20421/)
- [Google Cloud and NVIDIA Announce GA of Vera Rubin Infrastructure – NVIDIA Blog](https://blogs.nvidia.com/blog/google-cloud-vera-rubin-infrastructure/)
# Research Brief: SpaceX (SPCX) market cap between $1.75T and $2.00T at the November 30, 2026 close

*Note: the page-fetch tool was blocked, so I couldn't read any page in full. Everything below comes from search-result summaries, which sometimes disagree; I flag conflicts where I found them.*

## 1. Resolution mechanics
- **What counts:** SPCX's official regular-hours closing price on Nasdaq on the last trading day of November 2026, multiplied by total shares outstanding. Both share classes count; each Class B share converts 1:1 into Class A, so the total is simply Class A plus Class B. Share counts come from official filings such as the 10-Q cover page.
- **Last trading day:** Monday, November 30, 2026. Thanksgiving falls on November 26 and November 27 is a half-day, but November 30 is a normal full session. The listed close time (17:00 UTC, 12:00 ET) is before the market closes, but the rules use the closing price, so the 4:00 pm ET close is what matters.
- **The band:** YES if $1.75T ≤ market cap < $2.00T. A value of exactly $2.00T falls in the higher bracket, so it resolves NO.
- **Share count:** The 10-Q for the quarter ending September 30 reportedly lists 8,246,541,218 Class A and 5,334,522,491 Class B shares as of October 15, for **about 13.581B total** (Tokenomist, Oct 2026; I couldn't open the page). This matches the July 28 figure of 13,181,779,945 (Fool / 13G, Aug 2026) plus 391,041,680 Class A shares issued for the Cursor merger on August 14, which comes to 13.573B. Market-cap figures quoted elsewhere back out the same count: $1.93T ÷ $142.07 ≈ 13.585B.
- **Implied price band (at 13.58B shares):** about **$128.9 to $147.3 per share**. If the share count rises 1% through stock compensation or deal shares, the band moves down about 1%, to roughly $127.6–$145.8.
- **Edge cases:** No pending deal is near closing before November 30.
  - **Tesla merger:** If SpaceX ends up as the parent company, the method doesn't change. An announcement alone doesn't change the share count, but it could move the price a lot.
  - **Boost Mobile or a telco purchase paid in stock:** Any new shares would only count once they appear in disclosures.
  - **Resolver ambiguity:** It's unclear whether the resolver would use the October 15 count or a later one.

## 2. Reference classes and base rates
1. **Simple price-volatility model (my own calculation, not a published base rate).**
   - **Setup:** About 14 trading days from November 10 to 30, starting at the November 9 close of $142.07. The upper edge is +3.6% away in log terms (ln 147.26/142.07) and the lower edge is −9.8% (ln 128.86/142.07). The band is about 13.3% wide in log terms.
   - **Results by volatility assumption:**
     - 50% annualized volatility (σ over the period ≈ 11.8%): about 42% chance of landing in the band.
     - 65% (σ ≈ 15.3%): about 33%.
     - 80% (σ ≈ 18.9%): about 27%.
   - **Is 50–80% realistic?** SPCX's own moves since listing support it:
     - 52-week range of $104.83 to $225.64, a factor of about 2.15 in five months (Investing.com / Stocktwits, Nov 2026).
     - A drop of about 50% from the post-IPO peak by late July (Wikipedia).
     - Single-day moves of 7–9% around the midterms and +5.8% on November 9.
     - Market cap of $2.33T on October 6, $1.68T on November 5, $1.82T on November 6 and $1.93T on November 9 (search summary of a StockAnalysis.com history table, Nov 2026).
2. **SPCX's own record.** Market cap has swung between roughly $1.42T (at $104.83) and $3.06T (at $225.64) since the June 12 IPO. It was above $2T for much of October, below $1.75T on November 5, and back near $1.9T within three sessions. A $250B-wide band covers only a small part of that range, so staying inside it for three weeks would be unusual by this stock's standards.
3. **Recently listed mega-caps with high volatility (Tesla, Meta after its IPO, etc.).** Three-week absolute moves of more than 10% are common for such names, roughly 30–45% of the time. This is my rough estimate, not a sourced figure. The upper edge is only about 3.6% away, so even a modest rally would push the value above $2T.

## 3. Current state of the world (most recent first)
- **Nov 9–10:** SPCX closed at $142.07 on November 9, up about 5.8%, or about $1.93T (StockAnalysis via search; Heygotrade, Nov 10). Reasons cited:
  - NASA named SpaceX among eight companies eligible for lunar-delivery work worth up to $10B in total (Yahoo Finance, Nov 9).
  - SpaceX is advancing a roughly $24B gas plant and data-center project at Starbase (Stocktwits, Nov 9).
  - Stifel repeated its $190 target, and Deutsche Bank called the drop a buying opportunity with a $149 rebound view (FX Leaders, Nov 9; TradingKey, Nov 2026).
  - ARK reportedly bought about $96M of shares.
  - Investing.com shows $134.27 for "Nov 9", which is probably the November 6 close. I couldn't confirm the November 10 close.
- **Nov 6:** At an investor conference, Musk said SpaceX "could just acquire that legacy telco" (American Bazaar, Nov 9). Barclays called T-Mobile the best fit. SpaceX also reportedly wants to buy Boost Mobile from EchoStar (TechCrunch, Nov 2), and AT&T and T-Mobile have threatened to cut Boost off (Yahoo, Nov 2026). No deal has been filed.
- **Nov 4–5:** After Democrats swept the November 3 midterms, Tesla and SpaceX fell (CNBC, Nov 5). SPCX hit an intraday low of $120.39 on November 5, its lowest since August 7. Investors worried about congressional subpoenas, government contracts, and delays to the Texas compute buildout. Benzinga described the stock as in a bear market (Benzinga, Nov 2026).
- **Nov 2:** About $1.85T at a $136.37 close (value-investor.io, Nov 2026).
- **Oct 20, Q3 results:**
  - Revenue of about $14.6B, up 161% year over year; "Super Intelligence" (AI) revenue $7.56B; Connectivity/Starlink $5.25B; launch $1.77B.
  - Net income of $4.4B ($0.35 per share), but operating income only $2.79B. A Substack analysis attributes much of the gap to unrealized investment gains and tax valuation-allowance releases (Deep Quarry). Capex was $19.6B.
  - The stock rose 4–9% after hours to about $154 (Yahoo; CNBC; Fortune, Oct 20).
  - Musk said a Tesla merger is "a good idea", and both boards have formed special committees (CNN; CNBC, Oct 20).
- **Oct 6:** Market cap peaked at about $2.33T (StockAnalysis via search).
- **Oct 22:** A staggered lockup release made about 1.3B shares sellable, the 7th of 15 scheduled releases.
- **Index status:** SPCX joined the Nasdaq-100 on July 7 at about 1.3% weight. Its weight should rise as more shares become free to trade (CNN, Jul 7). It isn't expected to be eligible for the S&P 500 until the second half of 2027 (Seeking Alpha / Goldman, Nov 2026).
- **IPO, June 12:** Priced at $135 (about $1.77T), opened at $150 and closed at about $161 (NBC; NPR, Jun 12).

**Scheduled or possible events before November 30:**
- More Starship test flights "through year-end", including an attempt to catch both the booster and the ship. No date confirmed.
- Possible Tesla–SpaceX merger news. Barclays thinks a deal could be announced before Tesla's annual meeting, which it expects by December 6 at the latest (Bloomberg, Oct 14).
- Possible news on Boost Mobile or a telco purchase.
- Post-election political or regulatory news.
- No earnings report before November 30. Q4 results are expected in late January.
- The biggest lockup release (about 797.6M shares) comes on **December 8**, after resolution. Selling or hedging ahead of it could weigh on the price in late November (Orbitalpha; Stockcar, 2026). Musk's roughly 6.4B shares stay locked until about June 2027.

## 4. Drivers and scenarios
- **YES (price stays around $129–$147):** The stock settles after the post-election swing, with nothing major before Thanksgiving. This depends on the NASA, analyst and ARK support holding without a new rally, and on no merger announcement.
- **NO, upside (above $147.3, a 3.6% gain or more):**
  - A Tesla merger term sheet or announcement.
  - A successful Starship catch.
  - A broad tech rally or year-end AI buying.
  - Momentum carrying on from the November 9 rebound.
  - For context, the stock was at about $154 after Q3 and above $147 for most of October.
- **NO, downside (below $128.9, a drop of about 9.8% or more):**
  - Political pressure from the incoming Democratic House (subpoenas, contract reviews).
  - A Starship failure.
  - A large stock-funded telco purchase.
  - Selling ahead of the December 8 lockup release.
  - A tech or AI sell-off. Q3 profit quality is also under question.
- **Asymmetry:** The upper edge is much closer than the lower one, so YES needs the stock to stay roughly flat to slightly down.

## 5. Signposts
- **November 10 and later closes:** Each 1% move matters a lot. Above about $147 points toward NO from the upside; a range of $130–$145 points toward YES.
- **Tesla–SpaceX special committee news or a deal announcement:** Large and probably upward, though a stock-for-stock deal could lower SPCX's price.
- **Starship flight result:** Success likely pushes toward the upper edge or above it; failure pushes down.
- **Boost Mobile or telco filing:** The direction is unclear and depends on whether it's paid in cash or stock.
- **Congressional or regulatory moves against Musk companies:** Downward.
- **Overall tech and Nasdaq-100 direction, and AI capex sentiment:** SPCX has moved with the tech sell-off.
- **Any new share-count disclosure (8-K, S-8, deal issuance):** Shifts the price band.

## 6. Uncertainties
- I couldn't confirm the November 10 close. Sources conflict on the November 9 close ($142.07 vs $134.27); $142.07 is the most consistent.
- The October 15 share count comes from a secondary source, though July figures plus the Cursor shares back it up. It's also unclear which share count the resolver will use and whether stock-compensation issuance through November matters.
- I couldn't get realized or implied volatility figures; the 50–80% range is inferred from price moves.
- There are no confirmed dates for Starship flights or for merger news.
- I couldn't establish how big the remaining staggered lockup releases are between October 24 and December 8.

## Sources
- [StockAnalysis: SpaceX (SPCX) market cap](https://stockanalysis.com/stocks/spcx/market-cap/)
- [SpaceX Valuation (Nov 2026): $1.85T Market Cap Explained](https://value-investor.io/hub/spacex-latest-valuation-2026)
- [Tokenomist: SPCX update (share counts)](https://tokenomist.ai/stocks/spcx/update)
- [Motley Fool: Alphabet and Nvidia own more SpaceX than BlackRock](https://fool.com/investing/2026/08/20/alphabet-and-nvidia-own-more-spacex-than-blackrock)
- [StockTitan: Schedule 13G SPCX](https://www.stocktitan.net/sec-filings/SPCX/schedule-13g-space-exploration-technologies-corp-passive-investment-d-c4c38f2c12ba.html)
- [Heygotrade: SpaceX Stock Rises 5.8% After NASA Moon Base Awards (Nov 9)](https://www.heygotrade.com/en/news/spacex-spcx-stock-news-november-10-2026/)
- [Yahoo Finance: SpaceX, Rocket Lab blast higher as NASA hands out $10B in moon base awards](https://finance.yahoo.com/markets/article/spacex-rocket-lab-blast-higher-as-nasa-hands-out-10-billion-in-moon-base-awards-164320855.html)
- [Stocktwits: SPCX rises as SpaceX advances $24B Texas data center](https://stocktwits.com/news-articles/markets/equity/spcx-stock-rises-as-space-x-advances-24-b-texas-data-center-and-gas-plant-plans/cNGrFNUR97B)
- [FX Leaders: SPCX reclaims $140 (Nov 9, 2026)](https://www.fxleaders.com/news/2026/11/09/spcx-stock-reclaims-140-as-stifel-and-deutsche-bank-reiterate-buy-while-spacex-plans-gas-power-plant-and-data-center-in-starbase/)
- [TradingKey: Deutsche Bank sees pullback as buying opportunity](https://www.tradingkey.com/analysis/stocks/us-stocks/262296847-spacex-stock-forecast-pullback-buying-opportunity-deutsche-bank-political-risk-tradingkey)
- [CNBC: Tesla, SpaceX stocks fall after 2026 midterms](https://www.cnbc.com/2026/11/05/tesla-spacex-stocks-fall-after-2026-midterms.html)
- [Benzinga: SpaceX stock stays in a bear market after the midterms](https://www.benzinga.com/markets/equities/26/11/63018347/spacex-stock-stays-in-a-bear-market-after-the-midterm-elections-as-analysts-stay-upbeat)
- [Motley Fool: SpaceX Stock Fell After the Midterm Elections (Nov 8)](https://www.fool.com/investing/2026/11/08/spacex-stock-fell-after-the-midterm-elections-is-this-a-buying-opportunity/)
- [Motley Fool: Here's What Must Happen for SpaceX Stock to Rebound (Nov 9)](https://www.fool.com/investing/2026/11/09/heres-what-must-happen-for-spacex-stock-will-rebou/)
- [TechCrunch: SpaceX reportedly wants to buy Boost Mobile (Nov 2)](https://techcrunch.com/2026/11/02/spacex-reportedly-wants-to-buy-boost-mobile-to-compete-with-att-t-mobile-and-verizon/)
- [American Bazaar: Musk hints SpaceX could acquire major US wireless carrier (Nov 9)](https://americanbazaaronline.com/2026/11/09/elon-musk-hints-spacex-could-acquire-major-us-wireless-carrier-491876/)
- [Stocktwits: Which US wireless carrier makes most sense for SpaceX (Barclays)](https://stocktwits.com/news-articles/markets/equity/spcx-stock-barclays-tmobile-cleanest-fit-for-potential-spacex-buyout/cNGudG2R97L)
- [CNBC: SpaceX Q3 2026 earnings live updates (Oct 20)](https://www.cnbc.com/2026/10/20/spacex-spcx-earnings-live-updates-q3-2026html.html)
- [Fortune: SpaceX posts first operating profit as public company (Oct 20)](https://fortune.com/2026/10/20/spacex-q3-profit-ai-si-elon-musk/)
- [Yahoo Finance: SpaceX beats on earnings, capex less than expected](https://finance.yahoo.com/markets/stocks/live/spacex-earnings-live-updates-133218212.html)
- [Deep Quarry: SpaceX Q3 Earnings — The Accounting Behind the Numbers](https://deepquarry.substack.com/p/spacex-q3-earnings-the-accounting)
- [CNN: SpaceX stock surges after Musk says Tesla merger would be 'a good idea'](https://www.cnn.com/2026/10/20/business/spacex-tesla-merger-musk)
- [Bloomberg: Tesla-SpaceX deal news possible this year, Barclays says (Oct 14)](https://www.bloomberg.com/news/articles/2026-10-14/tesla-spacex-deal-news-possible-this-year-barclays-analyst-says)
- [Orbitalpha: SpaceX lockup calendar](https://www.orbitalpha.cloud/spacex-stock/lockup-calendar)
- [Stockcar: SPCX lockup schedule](https://www.stockcar.app/insights/spacex-lockup-schedule)
- [Motley Fool: SpaceX's lockup expires Aug. 6](https://www.fool.com/investing/2026/08/05/spacexs-lockup-expires-on-aug-6-heres-why-9115-mil/)
- [CNN: SpaceX is joining the Nasdaq 100 (Jul 7)](https://www.cnn.com/2026/07/07/economy/spacex-nasdaq-100-stocks)
- [Seeking Alpha: SpaceX has had limited impact on stock indexes, Goldman says](https://seekingalpha.com/news/4668759-spacex-has-had-limited-impact-on-stock-indexes-goldman-sachs-says)
- [NBC News: SpaceX stock gains 19% its first trading day](https://www.nbcnews.com/business/markets/spacex-ipo-stock-price-rcna349760)
- [NPR: SpaceX IPO makes history as largest ever (Jun 12)](https://www.npr.org/2026/06/12/nx-s1-5855004/stock-ai-spacex-ipo-elon-musk)
- [Wikipedia: Initial public offering of SpaceX](https://en.wikipedia.org/wiki/Initial_public_offering_of_SpaceX)
- [Investing.com: SpaceX stock](https://www.investing.com/equities/spacex)
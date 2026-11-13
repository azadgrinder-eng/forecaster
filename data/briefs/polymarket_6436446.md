# Research Brief: Will NVIDIA (NVDA) close above $160 on the last trading day of November 2026?

## 1. Resolution mechanics
- **What counts as YES:** The Pyth "Close" of the 1-minute candle covering the last minute of regular trading on Monday, **November 30, 2026** must be **strictly above $160.00**. Exactly $160.00 resolves NO. Pyth's figure is used without rounding.
- **Which day:** November 30 is a Monday and a normal full session, closing at 16:00 ET (21:00 UTC). That matches the market's close time. The Thanksgiving half-day is Friday, November 27, not the resolution day.
- **Fallbacks:**
  - If Pyth has no valid 1-minute close, the last valid Pyth price during regular hours is used.
  - If Pyth has no valid data at all that day, the primary exchange's (Nasdaq) official close is used.
  - If NVDA doesn't trade at all that day, the market resolves 50-50.
- **Edge cases:**
  - Pyth's last-minute candle close can differ by a few cents from Nasdaq's official closing-auction price. This only matters if the price ends within roughly ±$0.20 of $160.
  - Splits would adjust the target, but no split has been announced. The last split was the 10-for-1 in June 2024, so a split before November 30 is very unlikely.
- **Who decides:** The market operator, using Pyth data from pythdata.app (Equity.US.NVDA/USD).

## 2. Reference classes and base rates
1. **Random-walk / volatility model (main anchor):**
   - Last confirmed close: **$166.19 on November 12**. The $160 strike is about 3.7% below that (ln ratio about −0.038).
   - There are about 11–12 trading days left, including an earnings release.
   - Recent daily moves show very high realized volatility: −9% on Nov 5, −5.47% on Nov 10, +2.87% on Nov 11, −4.34% on Nov 12 after an intraday low 14% down. That suggests roughly 60–80% annualized.
   - At 65% volatility over 12 days, the standard deviation is about 14%. P(close > $160) is then about 60% from $166, about 50% from $160, and about 40% from $154.
   - **The answer depends heavily on where NVDA closed on Friday, November 13, which I could not confirm.** Each $1 of starting price shifts the result by roughly 2.5–3 percentage points.
2. **NVDA's moves after earnings:**
   - Over 10 years, the median move is +0.3% after one day, +3.3% after one week, and +0.4% after one month (Yahoo Finance analysis).
   - The stock rose in the five trading days after only 5 of the 10 reports from May 2023 to August 2025 (Nasdaq/Motley Fool).
   - It fell after 3 of the last 4 reports (Yahoo Finance, Nov 2026).
   - Options typically price a ±5–6% move on the report day. The previous quarter's implied move was about ±5.4%. I found no implied move for this report.
3. **Abrupt CEO exits driven by scandal** (from background knowledge, not searched this session):
   - Large-cap examples: Intel/Krzanich in 2018 (relationship policy), McDonald's/Easterbrook in 2019, and Intel/Gelsinger's ouster in 2024.
   - In those cases the stock usually fell about 2–5% at first, and the business fundamentals then mattered more over the following weeks.
   - Losing a founder seen as the company's visionary, combined with a national-security angle, is less common and probably carries a longer-lasting discount.
   - The drawdown from peak already exceeds 30%, which is the deepest since the 2022 bear market.

## 3. Current state of the world (most recent first)
- **Nov 13 (today):** I could not confirm the Friday close or where the stock is trading now. Snapshots conflict:
  - After hours Thursday: $167.84 (Benzinga) vs. $159.25, −5.65% (Kraken).
  - CNBC said the stock was trading "about $160" at one point.
  - Investing.com shows 163.95, and lists 164.78 as the Nov 12 close.
  - Trading Economics mentions a low of 150.55, the lowest since June 2025.
  - **Forecasters should check the live price first.**
- **Nov 12:**
  - Jensen Huang resigned as CEO, president and board member, effective immediately (SEC Form 8-K; CBS; Fox Business).
  - CFO Colette Kress is interim CEO and stays on as CFO. Harvey C. Jones was named the board's first independent chair. The CEO search covers internal and external candidates; Lisa Su and Rene Haas have been mentioned in speculation.
  - NVDA opened at $151.01, hit a low of $148.80, and closed at **$166.19 (−4.34%)** (CNBC; StockTitan; Gotrade).
  - Retail investors bought about $111M net in the first 30 minutes (Vanda Research, via Stocktwits). The stock was down about 10.9% for the week.
  - The stock is about 30.5% below its record close of about $239 on October 6. The 52-week high is $243.37.
- **Nov 11–12, analyst actions (reported; a few numbers look garbled, so verify):**
  - Bernstein: downgraded to Market Perform, target $200.
  - Baird: downgraded to Neutral, target $200.
  - Citi: target cut from $285 to $225.
  - Evercore: downgraded to In Line, target $186.
  - Truist: downgraded to Hold, target cut from $346 to $174.
  - Craig-Hallum: downgraded to Hold, target cut from $275 to $180.
  - Oppenheimer: downgraded to Perform, target withdrawn.
  - Consensus is still "Strong Buy," with an average target around $284 (TipRanks; TheStreet; CNBC). These dates are close together, so a few of these numbers may be off.
- **Background to the scandal:**
  - The board investigated Huang's relationship with Alice Huang, a former executive of Megaspeed, a Singapore company under US investigation for possibly diverting chips to China. The NYT reported a second affair, and later reports allege a third.
  - A shareholder class action has been filed.
  - Three House Republican chairs (Mast, Moolenaar, Crawford) asked for a voluntary closed-door briefing, proposed for **November 18**. China has denied the spy allegations.
- **Nov 5:** NVDA fell about 9%, part of a chip selloff linked to Democratic midterm wins and fears of more scrutiny of AI infrastructure.
- **Other pressures:** Investors rotating into memory stocks such as Micron, worries about hyperscaler spending and customers building their own chips (ASICs/TPUs), and China/H200 export risk. Forward P/E is reported at about 13–18x.
- **Fundamentals:**
  - Q1 FY27 revenue was $81.6B, up 85% year over year.
  - Q3 FY27 guidance: **$108B ±2%**, gross margin 74%.
  - Consensus (pre-resignation): about $108.8–109B revenue and EPS of about $2.47 (MarketBeat; Zacks).
  - In August, Nvidia announced a $500B AI-financing initiative with Apollo, BlackRock and others, including up to 25% residual-value support. Critics call it circular financing.
- **Scheduled before resolution:**
  - **Tue Nov 17:** Q3 FY27 results after the close; the CFO commentary goes up around 4:20 pm ET and the call is at 5 pm ET. This is the first report without Huang.
  - Nov 18: proposed House briefing.
  - Nov 26: Thanksgiving, market closed.
  - Nov 27: half-day.
  - Nov 30: resolution close.

## 4. Drivers and scenarios
- **Paths to YES (close above $160):**
  - Results beat the $108B guide and the Q4 guide comes in strong (above roughly $120B?), with Kress reassuring investors on continuity of strategy and customers.
  - The heavy dip-buying (retail and Burry's "mechanical bid," meaning index and passive flows) holds the stock above the intraday low of about $149.
  - The stock is already cheap at about 13–18x forward earnings, so it could rebound sharply. The pattern so far: falling sharply at the open, then recovering into the close.
  - A credible permanent CEO is named quickly.
- **Paths to NO:**
  - Guidance disappoints, or management sounds uncertain on the call. The stock fell after 3 of the last 4 reports despite beats.
  - More scandal news: the third affair, Megaspeed or export-control findings, or Commerce/DOJ action.
  - Customers, financing partners or key executives leave.
  - The broader AI and semiconductor selloff continues after the election.
  - Downgrades keep coming and selling feeds on itself. The stock already traded at $148.80 intraday on Nov 12.
- The biggest single swing factor is the earnings report on Nov 17, with a likely ±6–10% reaction given the circumstances.

## 5. Signposts
- **Friday Nov 13 close:** This matters most. If it is $165 or higher, YES is favored. If it is near or below $160, it's roughly a coin flip or leans NO.
- **Options-implied move for Nov 17 and implied volatility:** A higher implied vol pulls the probability toward 50%.
- **Earnings:** Revenue vs. $108–109B, data-center growth, the Q4 guide, gross margin vs. 74%, comments on China/H200, and customer commitments. A raised guide and strong demand commentary move toward YES; a cut guide or vague answers move toward NO.
- **CEO search:** Naming a credible permanent CEO moves toward YES. Departures of other senior leaders move toward NO.
- **Regulation and law:** New investigation findings, subpoenas, export-license actions, or more SEC disclosures (8-Ks) move toward NO.
- **Peers and the sector:** The Philadelphia Semiconductor Index (SOX), hyperscaler capex commentary, and the rotation into Micron and memory stocks.

## 6. Uncertainties
- I could not confirm the Nov 13 close or the current intraday price. Snapshots range from about $159 to $168.
- Sources disagree slightly on the Nov 12 close: $166.19 in most sources, 164.78 on Investing.com.
- The exact analyst targets may be garbled. For example, "Baird $500→$200" may mix in a 2022 article.
- There is no current options-implied move or implied volatility figure.
- Whether Huang will attend the Nov 18 briefing as a private citizen, and how far the Megaspeed probe extends.
- Whether the Q3 consensus has changed since the resignation.
- Many sources were aggregators or AI summaries. Direct page fetches were blocked by this environment's proxy, so these facts rely on search snippets.

## Sources
- [Nvidia Stock (NVDA) Falls 4.3% After Huang Resigns as CEO (Gotrade)](https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-november-13-2026/)
- [Stocks Closed Slightly Lower, Nov 12 2026 (StockTitan)](https://www.stocktitan.net/articles/stock-market-today-live-november-12-2026)
- [Key Nvidia stock levels to watch (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/key-nvidia-stock-levels-watch-144414101.html)
- [NVIDIA Stock Price History (Investing.com)](https://www.investing.com/equities/nvidia-corp-historical-data)
- [Is Nvidia Undervalued? (Motley Fool, Nov 12 2026)](https://www.fool.com/investing/2026/11/12/is-nvidia-undervalued/)
- [NVIDIA Form 8-K CEO transition (SEC)](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvidiaannouncesceotransiti.htm)
- [Nvidia CEO Jensen Huang resigns (CBS News)](https://www.cbsnews.com/news/nvidia-ceo-jensen-huang-resigns/)
- [Nvidia CEO resigns amid investigation (Fox Business)](https://www.foxbusiness.com/business-leaders/nvidia-ceo-jensen-huang-resigns-amid-investigation-relationship-alleged-chinese-spy)
- [Jensen Huang resigns (Washington Post)](https://www.washingtonpost.com/technology/2026/11/12/nvidia-board-weighs-jensen-huangs-future-after-affair-with-allege-chinese-spy/)
- [Nvidia live updates (CNBC, Nov 12 2026)](https://www.cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- [Nvidia stock closes down over 4% (CNBC)](https://www.cnbc.com/2026/11/12/nvidia-nvda-jensen-huang-second-affair.html)
- [NVDA quote (Kraken)](https://www.kraken.com/stocks/nvda)
- [Nvidia (Trading Economics)](https://tradingeconomics.com/nvda:us)
- [Nvidia Shares Rise After Hours as Huang Resigns (Benzinga)](https://www.benzinga.com/markets/equities/26/11/63228901/nvidia-shares-rise-after-hours-jensen-huang-resigns)
- [Burry 'mechanical bid' (Stocktwits)](https://stocktwits.com/news-articles/markets/equity/michael-burry-mechanical-bid-nvda-stock-questions-nvidia-succession-plan-asia-sales/cNbbpPXR9O1)
- [NVDA heads for worst week in over a year (Stocktwits)](https://stocktwits.com/news-articles/markets/equity/nvda-stock-jensen-huang-resigns-ceo-retail-traders-buying-dip/cNbb8xFR9Oh)
- [NVIDIA Sets Conference Call for Q3 Results (NVIDIA IR)](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Sets-Conference-Call-for-Third-Quarter-Financial-Results/)
- [Nvidia's $108B Q3 guide (Motley Fool, Sep 15 2026)](https://www.fool.com/investing/2026/09/15/prediction-nvidias-108-billion-q3-guide-will-look/)
- [NVIDIA Gears Up for Q3 Earnings (Zacks/TradingView)](https://www.tradingview.com/news/zacks:58c899221094b:0-nvidia-gears-up-for-q3-earnings-should-investors-buy-the-stock/)
- [Nvidia Reports Earnings Tuesday Without Huang (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/articles/nvidia-reports-earnings-tuesday-without-164548681.html)
- [Nvidia Stock Hit by 10 Downgrades (TipRanks)](https://www.tipranks.com/news/article/nvidia-stock-hit-by-10-downgrades-heres-what-wall-street-analysts-have-to-say)
- [Rasgon revamps Nvidia target (TheStreet)](https://www.thestreet.com/investing/stocks/nvidia-stacy-rasgon-200-target)
- [Analysts on Huang's departure (CNBC)](https://www.cnbc.com/2026/11/12/jensen-huang-nvidia-affair-ceo.html)
- [Nvidia shares fall up to 25% from record (Crypto Briefing)](https://cryptobriefing.com/nvidia-forward-pe-below-sp-500-walmart/)
- [Nvidia sheds $1T as investors rotate to rivals (VKTR)](https://www.vktr.com/ai-news/nvidia-sheds-1t-as-investors-rotate-to-rivals/)
- [House chairs ask Huang for briefing (The Next Web)](https://thenextweb.com/news/house-chairs-jensen-huang-briefing-megaspeed)
- [NVIDIA and six finance firms to mobilize $500B (W.Media)](https://w.media/nvidia-and-six-finance-firms-to-mobilize-over-us-500-billion-for-ai-infrastructure-buildout/)
- [Markets live Nov 13 (ABC News)](https://abc.net.au/news/2026-11-13/asx-markets-business-news-live-updates-nov-13/107337368)
- [How Nvidia stock performed after earnings (Yahoo Finance)](https://finance.yahoo.com/markets/stocks/article/heres-how-nvidia-stock-has-historically-performed-after-earnings-090000788.html)
- [Will Nvidia soar after Nov 19? History (Nasdaq)](https://www.nasdaq.com/articles/will-nvidia-soar-after-nov-19-history-offers-strikingly-clear-answer)
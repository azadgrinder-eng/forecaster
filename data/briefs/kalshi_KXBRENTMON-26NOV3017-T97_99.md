# Research Brief: Will Brent crude be above $97.99/bbl at 5:00 PM EST on Monday, November 30, 2026?

## 1. Resolution mechanics

- **What resolves YES:** The 1-minute candlestick for "brent crude oil" covering 4:59:00–4:59:59 PM EST on Monday, Nov 30, 2026 must close strictly above $97.99, rounded to 2 decimals. A close of exactly $97.99 resolves NO, so in practice the price needs to be $98.00 or higher. If the source publishes no data for that minute, the most recent published price is used.
- **Timing:** 5:00 PM EST is 22:00 London time. ICE Brent trades until about 23:00 London, so the market should still be open. Nov 30 is an ordinary Monday. US Thanksgiving (Thu, Nov 26) falls inside the window and may mean thin trading or shortened hours that week.
- **Edge case: the contract roll.** This is probably the most important detail in the question.
  - ICE Brent futures stop trading on the last business day of the second month before delivery. That makes **Nov 30, 2026 the last trading day of the January 2027 contract (CBF27)**. The ICE rule supports this, but I could not find the January 2027 date on ICE's published expiry calendar (ICE Brent spec, ICE.com).
  - The January contract settles around 19:30 London (2:30 PM EST). By 5 PM EST a continuous front-month series has very likely rolled to the **February 2027 contract**. Many CFD and data vendors roll several days earlier anyway.
  - The rules don't name the "source agency," and that matters here.
  - On Nov 13, January settled at **$95.84** and February at about **$93.03**, so February was about $2.81 lower (commoditypriceapi Brent futures page, Nov 13, 2026). Over the past month the Jan–Feb gap has ranged from about $2.3 to $4.2.
  - **Practical effect:** if the reference is February, the price needs to rise about **5.3%** from the Nov 13 level. If it were still January, it would need only about **2.2%**.
- **Other ambiguity:** Some resolution sources show a CFD or spot "Brent" price, which can differ from the ICE futures settlement by a few tenths of a dollar.

## 2. Reference classes and base rates

All three use my own calculations, not published statistics. No published Brent implied-volatility figure for November 2026 was available.

1. **Statistical random walk (lognormal, no drift) over about 11 trading days (Nov 16–30).**
   - **Volatility estimate:** Realized volatility is very high. Recent daily moves include −7.6% on Nov 2, a fall to $91.49 on Nov 10, and +3.3% on Nov 12. WTI's OVX index was about 50 in September, down from about 125 in March (SpotGamma, Sept 2026). Annualized volatility of 40–55% implies an 11-day standard deviation of about 8.4–11.5%.
   - **If February is the reference ($93.03 → needs +5.2% in log terms):** z ≈ 0.45–0.62, so **P(YES) ≈ 27–33%**.
   - **If January is the reference ($95.84 → needs +2.2%):** z ≈ 0.19–0.26, so **P(YES) ≈ 40–43%**.
   - In calmer markets (about 30% volatility), the February case falls to about 20%.
2. **Unwinding of a supply-shock premium after the peak.**
   - In 1990–91 Brent peaked around $41 in October 1990 and was about $20 by February 1991. The biggest one-day collapse came when the war began and supply fears faded.
   - In 2022 Brent peaked around $120–128 (March and June) and was about $80 by December.
   - In both episodes, once the market believed the disruption was ending, prices kept drifting lower for months, with sharp counter-rallies along the way.
   - This favors NO-leaning drift but does not rule out spikes.
3. **Short-horizon momentum after two weekly losses.**
   - Brent fell from an October average of about **$124** (EIA STEO, Nov 10, 2026) to about $96. That is roughly −21–23% in November (Coinpaper, Nov 2026).
   - Short-term momentum in crude is weak. Over two to three weeks, direction is close to a coin flip, with a slight continuation tendency. This doesn't shift the estimate much either way.

## 3. Current state of the world (most recent first)

- **Sat, Nov 14:** Iran's navy and IRGC say three tankers hit mines and caught fire in the Strait of Hormuz. Reuters could not verify this, and US Central Command (CENTCOM) calls the claims false and says the main routes are cleared (whbl/Reuters, Nov 14; houseofsaud.com, Nov 14). Earlier mine claims did not reliably lift prices: on Nov 2, mine reports were followed by a 1.95% drop on Monday (mitrade, Nov 2). I found no report of how prices opened on Sunday, Nov 15.
- **Fri, Nov 13:**
  - Brent (January contract) settled at **$95.84**, up 2 cents on the day and down $2.48 (−2.52%) on the week from $98.32 on Nov 6. It was the second straight weekly loss. WTI settled at $88.56 (EnergyNow, Nov 2026; Gate, Nov 13).
  - Trump said a deal with Iran was "not necessary" to end the war and that he will keep the US blockade of Iranian oil and the sanctions in place (Business Recorder/Reuters, Nov 13).
  - The US Dollar Index (DXY) was at 103.17, a headwind for oil.
- **Thu, Nov 12:** Brent rose $3.06 (+3.3%) to $95.82 on Houthi claims of attacks on Saudi oil sites and reports of tanker explosions in Hormuz (FinanceFeeds, Nov 2026).
- **Week of Nov 9–13:**
  - The IEA projects a **Q4 surplus of about 1.7 million bbl/day** and says Gulf exports reached 18.4 million bbl/day in October (Oil & Gas Middle East, Nov 2026).
  - US crude stocks rose 4.66 million barrels to 414.4 million in the week to Nov 6, against an expected draw (EIA via HDFC Sky, Nov 2026).
  - The UK Maritime Trade Operations agency (UKMTO) counted 7 tanker attacks in the week. In October there were 37 attacks on ships, a monthly high for the war (Reuters, Nov 11).
- **Tue, Nov 10:** Brent settled at **$91.49**, its lowest since August. The EIA's November Short-Term Energy Outlook (STEO) was released the same day, with assumptions fixed on Nov 5. It expects Brent to average **about $100 in November and December**; one report gives $104 for November and $99 for December. It forecasts a 2026 average of $97 and $86 for 2027 (EIA STEO; Rigzone, Nov 12; OGJ).
- **Nov 2:** Brent fell 7.6% to $104.77 on US–Iran peace-talk hopes ahead of the US midterms (CNBC, Nov 2).
- **Nov 1:** OPEC+'s seven core countries kept December targets unchanged (OPEC press release, Nov 1, 2026).
- **Background:**
  - The US and Israel attacked Iran on Feb 28, 2026. Iran has restricted Hormuz since then with a permit-and-fee regime. The IEA calls it the largest supply disruption in history (Gulf Times).
  - Brent began 2026 near $60.75 (Majalla). Global stocks fell by about 509 million barrels between before the war and the end of September (IRIS, Oct 28).
  - Goldman says Brent could reach $140 in 2027 if Gulf output stays 3.5 million bbl/day below its 2025 level.
- **Scheduled before resolution:**
  - EIA weekly inventory reports on about Nov 18 and Nov 25 (timing may shift for Thanksgiving).
  - US Thanksgiving on Nov 26.
  - **OPEC+ 42nd ministerial meeting and JMMC on Sun, Nov 29**, the day before resolution. It is expected to set the 2027 quota framework under the new capacity-based system; the capacity audit has been delayed by the war (OPEC; Engineering News, Nov 2).
  - January contract expiry on Mon, Nov 30.

## 4. Drivers and scenarios

- **Paths to YES (front month at or above $98):**
  - **Escalation:** a confirmed mine strike or tanker loss, verified Houthi damage to Saudi facilities, or US–Iran talks collapsing into renewed direct fighting. Any one of these could add $5–15 within days. A one-week outlook put its bull case at $98 (FinanceFeeds, Nov 14).
  - **Data surprises:** large US inventory draws, or a weaker dollar.
  - **A tight OPEC+ outcome on Nov 29**, such as delaying 2027 increases or cutting baselines, though Gulf producers are already constrained by the war.
  - **Source quirk:** if the source still shows the January contract, or a vendor series priced near it, the bar is only about +2%.
- **Paths to NO:**
  - **The war premium keeps fading:** the market is "pricing in peace" (OilPrice), the IEA sees a surplus, US stocks are building, and Gulf exports are recovering to 18.4 million bbl/day.
  - **Mine claims stay unverified and get ignored**, as on Nov 2.
  - **A ceasefire or deal headline.** Trump currently says a deal isn't needed, which leaves the blockade in place but also signals no escalation.
  - **The roll:** the switch to February takes about $2.8 off the quoted price.
  - **OPEC+ signals higher 2027 baselines.**

## 5. Signposts

- **Sunday-evening and Monday open (Nov 15–16) reaction to the mine claims.** A gap above $98 on the January contract would push probability up sharply; little reaction would push it down.
- **The Jan–Feb spread.** If it narrows, YES gets more likely even with an unchanged January price; if it widens, YES gets less likely.
- **Independent confirmation of tanker damage** (UKMTO, CENTCOM, insurers) or a Hormuz transit shutdown points toward YES.
- **US–Iran diplomacy:** talks starting or a ceasefire points toward NO; talks collapsing or US strikes point toward YES.
- **EIA inventory reports on Nov 18 and 25.**
- **OPEC+ outcome on Nov 29 and leaks beforehand.**
- **The February contract crossing $98** at any point in the final week would mean the market is near the line.

## 6. Uncertainties

- **Which data source and contract month** the resolver uses at 5 PM EST on Nov 30. This is a roll day, and it is unconfirmed whether the source shows January, February, or a CFD.
- **Exact current Jan–Feb spread.** The only figure is from one secondary aggregator page.
- **Current implied volatility** for Brent options. No November 2026 figure was found.
- **The Sunday Nov 15 open** and any news after Nov 14.
- **Whether the Nov 14 mine strikes are real.**
- **The exact agenda and expectations for the Nov 29 OPEC+ meeting.**
- **Source reliability:** several price figures come from aggregator or blog sites with small inconsistencies. For example, Nov 2 is reported as both $104.77 (CNBC) and about $111 (Mitrade).
- **Verification:** I could not open any page directly. Every page fetch was blocked by the network proxy, so all facts above come from search-result summaries, not from reading the articles.

## Sources
- [Brent Crude Oil Price: $95.84 Saturday Week Ahead After a Second Weekly Loss (FinanceFeeds)](https://financefeeds.com/brent-crude-oil-price-95-84-saturday-week-ahead-second-weekly-loss-bull-98-bear-91/)
- [Brent Crude Oil Price: $95 Friday After a 3.3% Jump on Saudi Attack Claims (FinanceFeeds)](https://financefeeds.com/brent-crude-oil-price-95-friday-after-3-3-percent-jump-saudi-attack-claims-bull-98-bear-92/)
- [Oil Prices Fall for Second Straight Week… Brent at $95.84 (EnergyNow)](https://energynow.ca/2026/11/oil-prices-fall-for-second-straight-week-as-global-supply-surplus-emerges-wti-closes-at-88-56-brent-at-95-84/)
- [Brent Crude Settles $95.84 After Second Weekly Loss (Gate)](https://www.gate.com/news/detail/brent-crude-settles-9584-after-second-weekly-loss-on-supply-surplus-25618627)
- [Brent crude flat as IEA sees surplus (Oil & Gas Middle East)](https://oilandgasmiddleeast.com/news/brent-crude-tanker-attack-uae)
- [Oil prices set for second weekly decline as Trump to stay with Iran blockade (Business Recorder)](https://www.brecorder.com/news/40448723/oil-prices-set-for-second-weekly-decline-as-trump-to-stay-with-iran-blockade)
- [Brent Crude Falls 2.4% as OPEC+ Supply Rises (HDFC Sky)](https://hdfcsky.com/news/crude-oil-slides-2-4percent-to-95-41-as-opec-output-surge-and-us-inventory-build-overpower-hormuz-risk-premium)
- [Oil rises from two-month low as Hormuz shipping attacks offset Iran truce hopes (Reuters via Investing.com)](https://www.investing.com/news/commodities-news/oil-rises-from-twomonth-low-as-hormuz-shipping-attacks-offset-iran-truce-hopes-5017512)
- [Iran's navy says three tankers on fire after hitting mines in Hormuz (WHBL/Reuters)](https://whbl.com/2026/11/14/irans-navy-says-three-tankers-on-fire-after-hitting-mines-in-hormuz/)
- [IRGC Claims 2 More Tankers Hit Mines in Hormuz on November 14 (House of Saud)](https://houseofsaud.com/irgc-2-tankers-mines-hormuz-nov14/)
- [Brent slips to $111 as a two-day Hormuz plan lands (Mitrade)](https://www.mitrade.com/insights/commodity-analysis/oil-news/brent-111-hormuz-two-day-plan-premium-20261102J1102)
- [Crude oil prices sell off more than 7% on Iran peace talk hopes (CNBC)](https://www.cnbc.com/2026/11/02/oil-prices-fall-as-iran-us-pursue-diplomacy.html)
- [The Iran War Isn't Over, but Oil Traders Are Already Pricing In Peace (OilPrice)](https://oilprice.com/Energy/Energy-General/The-Iran-War-Isnt-Over-but-Oil-Traders-Are-Already-Pricing-In-Peace.html)
- [November 2026 Short-Term Energy Outlook (EIA)](https://www.eia.gov/outlooks/steo/pdf/steo_full.pdf)
- [EIA Raises 2026, 2027 Oil Price Forecasts Yet Again (Rigzone)](https://www.rigzone.com/news/eia_raises_2026_2027_oil_price_forecasts_yet_again-12-nov-2026-185067-article/)
- [EIA sees Brent near $100/bbl through yearend 2026 (OGJ)](https://www.ogj.com/general-interest/economics-markets/news/55418180/eia-sees-brent-near-100-bbl-through-yearend-2026-as-middle-east-supply-constraints-persist)
- [EIA Sees Oil Near $100 Through 2026 Despite Brent's 21% November Crash (Coinpaper)](https://coinpaper.com/38682/eia-sees-oil-near-100-through-2026-despite-brent-s-21-november-crash)
- [Crude Oil Brent Futures Jan 2027 Price, Settlement & Expiry (CommodityPriceAPI)](https://commoditypriceapi.com/tools/brentoil-fut-jan27/prices)
- [Brent Crude Oil Price Near Six-Month High on Iran War (Admiral Markets)](https://admiralmarkets.com/analytics/traders-blog/brent-crude-oil-price-iran-war)
- [Brent Crude Futures contract specification (ICE)](https://www.ice.com/products/219/Brent-Crude-Oil-Futures)
- [OPEC press release, 1 November 2026](https://www.opec.org/pr-detail/2033620-1-november-2026.html)
- [OPEC+ keeps December oil output targets steady ahead of tougher call for 2027 (Engineering News)](https://engineeringnews.co.za/article/opec-keeps-december-oil-output-targets-steady-ahead-of-tougher-call-for-2027-2026-11-02)
- [OPEC+ subgroup keeps oil production quotas unchanged for December (World Oil)](https://worldoil.com/news/2026/11/1/opec-subgroup-keeps-oil-production-quotas-unchanged-for-december/)
- [OVX: The Oil Volatility Index (SpotGamma)](https://spotgamma.com/?p=20417)
- [How the US-Iran war took oil prices on a wild ride (Majalla)](https://en.majalla.com/node/332465/infographics/how-us-iran-war-took-oil-prices-wild-ride)
- [War in Iran and tensions in the Middle East: impact on oil markets (IRIS)](https://www.iris-france.org/en/war-in-iran-and-tensions-in-the-middle-east-what-impact-will-this-have-on-the-oil-markets/)
- [Iran war causes the biggest ever oil market disruption, says IEA (Gulf Times)](https://www.gulf-times.com/article/722343/business/iran-war-causes-the-biggest-ever-oil-market-disruption-says-iea)
- [Energy markets' relatively small reaction to Iran war (Fortune, Mar 2, 2026)](https://fortune.com/2026/03/02/energy-markets-relatively-small-reaction-iran-war-prices-spike-oil-gas-flowing-end-week/?showAdminBar=true)
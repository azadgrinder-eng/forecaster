# Research Brief: Will Polymarket's favorite be right on every 2026 Fed decision?

## 1. Resolution mechanics

- **What counts as YES:** For every 2026 FOMC rate decision, the option Polymarket rated most likely 24 hours before the announcement must turn out to be the actual result. The options are things like "No change", "25 bps increase" and "25 bps decrease". One wrong favorite makes the question NO.
- **2026 schedule:** Jan 27–28, Mar 17–18, Apr 28–29, Jun 16–17, Jul 28–29, Sep 15–16, Oct 27–28 and Dec 8–9. Seven meetings are done. Only **Dec 8–9** is left. Its decision comes out around 2:00 pm ET (19:00 UTC) on Dec 9, which is the same moment the question closes. The check point is therefore Polymarket's favorite at about 2 pm ET on **Tuesday Dec 8**.
- **Who decides:** The question creator, using the Polymarket "Fed decision in [month]" markets. The reference link points to the January market. Its `tid` timestamp suggests the question was created around Jan 7, 2026.
- **Edge cases and ambiguities:**
  - An unscheduled emergency move between meetings may have no Polymarket market at all, so it's unclear whether it would count. Nothing like this has happened in 2026 so far.
  - If two options are roughly tied 24 hours out, the rules don't say what happens.
  - The rules don't say whether "most likely" means the last trade or the midpoint between bids and offers.
  - Typos ("gusses") and loose wording leave room for the creator's judgment.
  - I deliberately did **not** check Polymarket's own prices, past or current. Past correctness below is inferred from fed funds futures pricing (CME FedWatch) and press reports that each decision was "expected". Polymarket favorites normally match FedWatch favorites, but whether the creator agrees each past meeting was a hit is an assumption.

## 2. Reference classes and base rates

1. **Scheduled FOMC decisions against the favorite in futures pricing the day before, roughly 1994 to 2025.** Since the Fed began announcing decisions in 1994, and especially since about 2008, it has almost never delivered a rate outcome at a scheduled meeting that futures rated under 50% the day before. The closer calls were all won by the favorite: Sep 2015 hold, Jun 2022 75 bp, Sep 2024 50 bp (about 60/40 the day before). This comes from my background knowledge, not a fresh tally. Rough estimate: the day-before favorite is right in more than 97% of scheduled meetings. The surprises that did happen were mostly emergency moves between meetings (2001, 2008, March 2020).
2. **2026 so far: 7 of 7 favorites correct, based on futures:**
   - **Jan:** hold. It was "fully discounted" by money markets beforehand.
   - **Mar:** hold. Futures put it above 99%.
   - **Apr:** hold, with an 8–4 vote. It was expected; the dissents concerned the statement's wording, not the rate.
   - **Jun:** hold. FedWatch had it at 96–99.6%.
   - **Jul:** hold, with 3 dissents favoring a hike. Reports say the hold "matched expectations".
   - **Sep:** 25 bp hike. FedWatch was about 49% a week before Sep 10, 62% on Sep 10, and **92.5%** on decision day.
   - **Oct:** hold. FedWatch put a hike at only about 7%.
3. **Meetings where the outcome was still uncertain weeks out (favorite at 60–80% about a month before).** These usually firm up toward the favorite by the day before (Sep 2026, Sep 2024, Jun 2022). Sometimes the favorite flips in between; in Sep 2026 a hold was favored before Jackson Hole. This matters because the question is judged 24 hours out, not today.

## 3. Current state of the world (most recent first)

- **Nov 6–7, 2026:** The October jobs report showed +165k payrolls against a consensus of 59k. The FedWatch probability of a December hike rose from 72.8% before the report to about 77%. Other trackers put it at 74–83%, and an OIS-based tracker at about 69% on Nov 6 (MPA, Nov 2026; KuCoin/PANews, Nov 6, 2026; TradingKey, Nov 2026).
- **Early Nov:** Warsh repeated that he opposes forward guidance (TradingKey, Nov 2026). Less signaling from the chair means pricing could stay uncertain until late.
- **Oct 28:** The Fed held at **3.75–4.00%** by a 10–2 vote. Hammack and Cook dissented in favor of a hike. The December hike probability rose from 78% to 85% right after (Noradar, Oct 2026; Newsquawk, Oct 28, 2026). Before that meeting, Warsh's remarks had collapsed the odds of an October hike (Benzinga, Oct 2026), which shows the chair can move expectations a lot between meetings.
- **Oct 2:** Hike odds fell after the September jobs report (CNBC, Oct 2, 2026). Core PCE for August came in at a cooler 3.0% (Yahoo Finance, Oct 2026). December pricing has already swung both ways this autumn.
- **Sep 16:** The Fed hiked 25 bp, unanimously (12–0), to 3.75–4.00%, its first hike since 2023. The September projections imply one more hike in 2026. The 10-year Treasury yield was around 5% (CNBC; CNN; Yahoo, Sep 16, 2026).
- **Background:** Warsh became chair after Powell's term ended May 15. Inflation is above 3%, energy prices have risen sharply, and the committee is split and hawkish, with repeated dissents.
- **Scheduled before Dec 8:**
  - October CPI, around mid-November.
  - FOMC minutes on **Nov 18**.
  - October PCE, late November.
  - Fed speeches, until the pre-meeting quiet period (when officials stop commenting publicly) starts around **Nov 28**.
  - November jobs report, around **Dec 4**.
  - November CPI probably comes out around Dec 10, after the decision.

## 4. Drivers and scenarios

- **YES (main path):** Data stays firm, the hike is priced at 85–95% by Dec 8, and the Fed hikes 25 bp to 4.00–4.25%. A second path also leads to YES: data softens enough that a hold becomes the clear favorite by Dec 8, and the Fed holds.
- **NO paths:**
  - (a) The Fed defies a clear favorite. This is historically very rare, but Warsh's dislike of forward guidance and the divided committee make it somewhat more likely than usual.
  - (b) Pricing is near 50/50 on Dec 8 and the less-favored option happens. This is the main risk if the November jobs report or PCE data are mixed.
  - (c) An emergency move between meetings, or a 50 bp move, catches the market off guard.
  - (d) The creator rules a past meeting a miss. Unlikely: all 7 past outcomes were favored by futures at more than 90% near the decision, as far as I can tell.

## 5. Signposts

- **Toward NO risk:** December hike odds drifting toward 50–60% in late November. Watch the minutes, PCE, any Warsh comments before the quiet period, and the Dec 4 jobs report. A weak November jobs report or soft core PCE would also push this way.
- **Toward YES:** December pricing firming above 85–90%, or collapsing below 15%, by early December. Hawkish minutes on Nov 18. Strong inflation data. Fed officials clearly signaling the outcome before the quiet period starts.
- **Key quantity:** How lopsided the odds for the leading option are on Dec 7–8. Historically, when the favorite is above 80% the day before, it has essentially always been right.

## 6. Uncertainties

- I did not check Polymarket's own favorites 24 hours before each 2026 meeting; that was intentional. Past correctness is inferred from FedWatch and press reports. There is a small chance Polymarket differed from futures, for example at the September meeting a week or more out.
- I could not open the Fed's primary documents (access was blocked). Vote counts and rate ranges come from multiple secondary reports that agree with each other.
- I don't have exact November CPI and PCE release dates. Government data schedules could be disrupted.
- The base rate in class 1 comes from my memory, not a fresh count.
- How the creator would rule on ties or emergency moves is unknown.

## Sources
- [FOMC October 2026 Results: Fed Holds Rates, Dissents Emerge (BYDFi)](https://www.bydfi.com/market-intelligence/article/fomc-october-2026-results-1/1356)
- [FOMC SNAP ANALYSIS: Fed holds rates, as expected (Newsquawk)](https://www.newsquawk.com/headlines/fomc-snap-analysis-fed-holds-rates-as-expected-with-two-hawkish-dissenters-as-attention-turns-to-the-presser)
- [Fed meeting recap Oct 28 (CNBC)](https://www.cnbc.com/2026/10/28/fed-meeting-today-live-updates.html)
- [Interest Rates Hike Odds for December 2026 Jump to 85% (Noradar)](https://www.noradarealestate.com/blog/interest-rates-hike-odds-december-2026-jump-85-after-feds-recent-decision/)
- [Fed December rate hike probability 72.8% ahead of NFP (KuCoin)](https://www.kucoin.com/news/flash/fed-s-december-rate-hike-probability-at-72-8-before-nonfarm-payrolls-release)
- [October jobs shock seals case for December Fed rate hike (MPA)](https://www.mpamag.com/us/mortgage-industry/industry-trends/october-jobs-shock-seals-case-for-december-fed-rate-hike/596487)
- [Fed Chair Warsh Reiterates Opposition to Forward Guidance (TradingKey)](https://www.tradingkey.com/analysis/economic/central-banks/262247759-fed-kevin-warsh-forward-guidance-december-hike-83-percent-tradingkey)
- [October Fed Hike Odds Collapse After Warsh Remarks (Benzinga)](https://www.benzinga.com/markets/prediction-markets/26/10/62408879/fed-rate-hike-odds-warsh-ai)
- [Fed rate hike odds decline after September jobs report (CNBC)](https://www.cnbc.com/2026/10/02/fed-rate-hike-odds-decline-after-september-jobs-report.html)
- [The Fed was unanimous about raising rates in September (Yahoo Finance)](https://finance.yahoo.com/economy/policy/article/the-fed-was-unanimous-about-raising-rates-in-september-economic-signals-have-since-changed-184839972.html)
- [Fed meeting recap Sep 16 (CNBC)](https://www.cnbc.com/2026/09/16/fed-meeting-today-live-updates.html)
- [Fed raises interest rates for the first time since 2023 (CNN)](https://www.cnn.com/2026/09/16/business/live-news/federal-reserve-interest-rate-september)
- [Stock market today Sep 16 (Yahoo Finance)](https://finance.yahoo.com/markets/live/stock-market-today-wednesday-september-16-dow-sp-500-nasdaq-fed-meeting-decision-080356525.html)
- [Fed Rate Hike Sept 16, 2026 (StockTitan)](https://www.stocktitan.net/articles/fed-rate-hike-september-16-2026)
- [September Fed decision is now a coin flip (CNBC, Aug 28)](https://www.cnbc.com/2026/08/28/-september-fed-decision-now-a-coin-flip-as-rate-hike-odds-increase.html)
- [CME FedWatch Provides A 66% Chance Fed Will Hike in September (Forbes)](https://www.forbes.com/sites/digital-assets/2026/08/31/cme-fedwatch-provides-a-66-chance-fed-will-hike-rates-in-september/)
- [Fed holds rates steady as three policymakers dissent for a hike (Investing.com)](https://www.investing.com/news/economic-indicators/instant-view-fed-holds-rates-steady-as-three-policymakers-dissent-for-a-hike-4821495)
- [Kevin Warsh first Fed meeting (Fortune)](https://fortune.com/2026/06/17/kevin-warsh-first-fed-meeting-rates-steady-forward-guidance-dropped/)
- [Hawkish-leaning committee, Warsh's first meeting (PIMCO)](https://www.pimco.com/fi/en/insights/hawkish-leaning-committee-reform-minded-chair-warshs-first-fed-meeting)
- [Fed holds rates steady, most divided since 1992 (Kitco)](https://www.kitco.com/news/off-the-wire/2026-04-29/fed-holds-rates-steady-board-vote-most-divided-1992)
- [March FOMC: Fed holds interest rates steady (Fox Business)](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-march-18-2026)
- [The Fed didn't move rates, markets moved anyway (BabyPips, Mar 19)](https://www.babypips.com/analysis/headlines-the-fed-didnt-move-rates-markets-moved-anyway-heres-why-2026-03-19)
- [January 2026 FOMC Review (Pepperstone)](https://pepperstone.com/en-gb/analysis/navigating-markets/january-2026-fomc-review/)
- [Fed holds rates steady, dovish dissents, Jan 29 (BabyPips)](https://www.babypips.com/news/headline-fed-holds-rates-steady-signals-extended-pause-despite-dovish-dissents-2026-01-29)
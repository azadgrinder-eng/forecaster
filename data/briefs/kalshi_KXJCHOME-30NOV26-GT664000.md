# Research brief: Will Jersey City's single-family ZHVI (region 25320) be above $664,000 for November 2026?

## 1. Resolution mechanics
- **What counts:** The question resolves YES if Zillow's monthly Home Value Index for single-family homes in Jersey City, NJ (region ID 25320) is strictly above $664,000 for November 2026. A value exactly at $664,000 resolves NO. The source is Zillow and the market is run by Kalshi.
- **When the number arrives:** Zillow's national November market report is expected around December 4, 2026 (Zillow October report, Nov 5, 2026). City-level figures usually follow in mid-month data files; the FRED schedule shows October national data due November 19 (FRED, Oct 15, 2026). The November Jersey City value should therefore be out shortly before the market closes on December 17, 2026, 15:00 UTC. If Zillow publishes late, Kalshi's fallback rules apply, and I could not check those.
- **Which series counts is the biggest unknown.** The question says single-family homes. Zillow's headline city figure, the one quoted on its city page and in every source I found, is the all-homes index, which includes condos and co-ops. Jersey City has many condos, so the single-family-only number could sit well above or below the all-homes number. I could not get the single-family value: every attempt to load Zillow's pages and data files was refused by the network proxy. **Forecasters should get the latest single-family value for region 25320 before pricing this.**
- **Index properties:** The index is smoothed and seasonally adjusted, so month-to-month moves are small and change direction slowly. Zillow also revises past months, so the value first published for November is presumably the one that counts. I have not confirmed this in Kalshi's rules.

## 2. Reference classes and base rates
1. **How much a smoothed city index moves in two months.** The latest Jersey City value is for September 2026, two months before November. For a stable large-city index in a flat market, two-month moves are usually well under ±1%. Using the all-homes figures:
   - September 2026: $656,649, up 0.1% from August and 0.4% from a year earlier.
   - Clearing $664,000 would take a rise of about 1.1% in two months, roughly 6–7% annualized, while the past year grew 0.4%.
   - Moves that fast mostly happened in the 2020–22 boom.
   - These rates come from general knowledge of how the index behaves, not from a series I computed.
2. **Jersey City's all-homes level during 2026.** The city has stayed between about $653,000 and $666,000 all year:
   - January: $654,778 (city-stats, citing Zillow)
   - End of February: $653,810 (a third-party page republishing Zillow data)
   - May: $665,309 (Properties by Southern)
   - June: $665,140, down 1.3% from a year earlier (a Zillow page; its region ID may not be the city's)
   - September: $656,649 (Zillow, cited on housing-market.org)
   
   The all-homes index topped $664,000 in roughly 2 of the 5 readings I found (May and June), and has not since.
3. **Market direction.** Nationally, October 2026 values fell 0.6% from September and were up just 0.7% from a year earlier (Zillow October report, Nov 5, 2026). In September, 22% of the 300 largest metros were down from a year earlier (ResiClub, October 2026). The New York area has been stronger than the nation (New York State up about 4–5% a year; Manhattan up 3.0% as of August), but Jersey City itself has been roughly flat.

## 3. Current state of the world (most recent first)
- **Nov 19, 2026:** The October national figure is scheduled for release on FRED today (FRED). The Jersey City October value had not appeared in any source I found; the latest is September.
- **Nov 15, 2026:** National sales are slowing and New York inventory is rising (FingerLakes1).
- **Nov 5, 2026 (Zillow October report):**
  - The typical U.S. home value is $364,812, down 0.6% from September and up 0.7% from a year earlier.
  - Freddie Mac mortgage rates averaged 7.33% in October, up from 6.86% in September.
  - Newly pending listings fell 16.8% from a year earlier, the biggest drop since August 2023.
  - Zillow's preliminary existing-home sales fell 8.7% from a year earlier.
  - The November report is due December 4.
- **October 2026, local sales data (these are not the Zillow index):**
  - RealtyTrac: median sold price $650,500, down 7.4% from a year earlier; estimated median value $658,218.
  - Redfin: median sale price $764,968, up 5.9%.
  - Jill Biggs Group: median sold price $760,500, a median of about 28 days on market, and 37% of homes selling at or above asking.
  - Movoto: median listing price $685,000, up about 1%.
  
  These sources point in different directions, so the local picture is mixed.
- **October 2026, New York City:** StreetEasy reports inventory at its lowest October level since 2017, down 3.1% from a year earlier, and homes selling for a median 97.8% of asking.
- **Sep 30, 2026:** Jersey City all-homes value was $656,649, up 0.1% from August and 0.4% from a year earlier (Zillow page via search; housing-market.org).
- **Earlier 2026:**
  - Hudson County all-homes value was $647,064 through June, up 0.5% from a year earlier (Zillow page via search).
  - PropertyIQ reported Hudson County values down 2.53% from a year earlier in February.

## 4. Drivers and scenarios
**Paths to YES:**
- **The single-family series already sits well above $664,000.** This is plausible, since many Jersey City houses are brownstones and townhomes in the Heights and Downtown. If so, YES is very likely given how slowly the index moves. This scenario depends entirely on the single-family level, which I could not find.
- **A strong local rebound.** Low NYC-area inventory and strong reported closing prices (Redfin up 5.9%, 37% of homes over asking) could push the index up more than 1% in two months. This is unlikely while mortgage rates are above 7%.

**Paths to NO:**
- **The single-family series sits near or below the all-homes level** (about $657,000 in September). The index would then have to gain about 1.1% or more in two months, against national values falling 0.6% in October, rates jumping to 7.33%, and pending sales collapsing. Flat or slightly lower readings for October and November would keep it below $664,000.
- **The index moves slowly.** Even a turn upward would show up gradually because the series is smoothed.

## 5. Signposts
- **The actual single-family value for region 25320 for September or October 2026** matters more than anything else. If October is at or above about $668,000, lean strongly YES. If it is at or below about $660,000, lean strongly NO. Around $664,000, the direction of the latest monthly change decides it.
- **Jersey City's October monthly change, expected mid-to-late November.** A third straight negative or flat month, given the national -0.6%, points to NO.
- **Zillow's November national report (around December 4)** and mortgage rates in November. If rates ease back below 7%, that is mildly YES.
- **Revisions to earlier Jersey City values** when new data comes out.
- **Hudson County and New York metro index trends for October.**

## 6. Uncertainties
- **The single-family value for Jersey City is unknown** and is the key missing input. The $664,000 strike is close to the all-homes level, which suggests (but does not prove) that the single-family series is in the same range.
- **Conflicting historical values.** The June figure ($665,140, down 1.3% from a year earlier) and the September figure ($656,649, up 0.4%) don't fit together cleanly. The cause could be revisions or a different region ID: the June page used ID 188299, not 25320.
- **Kalshi's rules** on which published version counts, and its fallback if Zillow publishes late, were not verified.
- **No local October index reading** was available.

## Sources
- [Zillow – Jersey City, NJ home values (region 25320)](https://www.zillow.com/home-values/25320/jersey-city-nj/)
- [Zillow – Jersey City home values page (188299)](https://www.zillow.com/home-values/188299/jersey-city-nj/)
- [Zillow – Jersey City 07395 home values page](https://www.zillow.com/home-values/60650/jersey-city-nj-07395/)
- [housing-market.org – New Jersey housing market](https://housing-market.org/new-jersey-housing-market/)
- [city-stats – Housing in Jersey City](https://city-stats.com/new-jersey/jersey-city/housing)
- [PropertyIQ – Jersey City real estate market 2026](https://www.propertyiq.app/blog/jersey-city-nj-real-estate-market-2026)
- [Properties by Southern – Jersey City market 2026](https://propertiesbysouthern.com/blog/jersey-city-real-estate-market-2026-prices-trends-and-what-buyers-and-sellers-need-to-know)
- [Properties Incorporated – Jersey City housing market](https://propertiesincorporated.com/new-jersey/jersey-city)
- [Zillow October 2026 Market Report (PDF)](https://s25.q4cdn.com/975009107/files/doc_news/Newly-pending-listings-fell-17-in-October-the-biggest-year-over-year-drop-since-2023-2026.pdf)
- [Finviz – Newly pending listings fell 17% in October](https://finviz.com/news/416869/newly-pending-listings-fell-17-in-october-the-biggest-year-over-year-drop-since-2023)
- [ResiClub – Major housing markets, October 2026](https://www.resiclubanalytics.com/p/major-housing-markets-home-price-declines-mild-gains-october-2026)
- [FRED – U.S. ZHVI all homes](https://fred.stlouisfed.org/series/USAUCSFRCONDOSMSAMID)
- [RealtyTrac – Jersey City market trends](https://www.realtytrac.com/market-trends/jersey-city-nj/)
- [Redfin – Jersey City housing market](https://www.redfin.com/city/9168/NJ/Jersey-City/housing-market)
- [Jill Biggs Group – Jersey City market report, October 2026](https://www.thejillbiggsgroup.com/blog/jersey-city-real-estate-market-report-october-2026)
- [Movoto – Jersey City](https://www.movoto.com/jersey-city-nj/)
- [StreetEasy – October 2026 NYC market report](https://streeteasy.com/blog/inventory-not-mortgage-rates-weighing-on-nyc-sales/)
- [FingerLakes1 – Housing market today (Nov 15, 2026)](https://www.fingerlakes1.com/2026/11/15/housing-market-today-sales-slow-nationally-as-new-york-inventory-grows/)
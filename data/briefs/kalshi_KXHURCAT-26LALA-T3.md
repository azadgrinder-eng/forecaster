# Research brief: Will Lala reach Category 3 (max sustained winds ≥111 mph)?

**Short answer:** official advisories say this already happened. On August 18, 2026, the Central Pacific Hurricane Center put Lala at 125 mph. Lala is now a dead storm. The only way this resolves NO is an administrative or resolution error.

**Note on method:** every WebFetch call was refused by the network proxy. Everything below comes from search-result snippets of NHC/CPHC advisories and news articles. I could not read the full pages.

## 1. Resolution mechanics
- **What counts as YES:** Lala reaches maximum sustained winds of ≥111 mph, which is the bottom of Category 3 on the Saffir-Simpson scale.
- **Deadline:** the event must occur before December 1, 2026. If it does, the market "expires at the first 10:00 AM ET following the occurrence." The market closes December 2, 2026 at 04:59 UTC.
- **Who decides:** the rules don't say. The standard source would be NHC/CPHC advisories, since CPHC is run out of NHC in Honolulu and Lala was storm CP01-2026.
- **Edge cases and ambiguities:**
  - The rules don't say whether operational advisories or the final post-season report (best track) decides. In this case both are well above the threshold, so the difference shouldn't matter.
  - The rules imply the market should already have expired, at 10:00 AM ET on August 19, 2026. That it still shows as open on November 6 suggests a settlement delay, a stale listing, or a data-pipeline artifact. It does not suggest real uncertainty.
  - There is no other "Lala" in 2026. Central Pacific names are used once in order, and Lala was CP01-2026. I found no active or new Lala as of November 2026 (search, November 6, 2026).

## 2. Reference classes and base rates
- **Post-season reports cutting a peak by 14+ mph:** to resolve NO, the final report would have to cut Lala's peak from 125 mph (about 110 kt) to under 111 mph (about 96 kt), a drop of 14 kt or more. Post-season reviews of Atlantic and East Pacific hurricanes usually move peaks by 0–10 kt. Downgrades of 15 kt or more for a major hurricane with a clear satellite signal are very rare. My rough estimate from NHC report practice is under 2%, and that is not a tallied count. Secondary sources (Wikipedia, Weather Underground) already list a higher peak of 130 mph and 947 mb, which suggests any revision went up.
- **Weather markets misresolving or getting voided:** on major regulated or crypto platforms, markets whose official data clearly cross the threshold almost always resolve as the data says. My rough estimate is that disputes or misresolutions happen less than 1–2% of the time. That is an impression, not a measured rate.
- **Storms that cross a threshold and stay there:** Lala was at or above 111 mph in several advisories over roughly 24+ hours: 125 mph at 4 PM HST on August 18, and 115 mph still Category 3 at 2 PM HST on August 19. This was not a one-advisory blip.

## 3. Current state of the world (most recent first)
- **Nov 6, 2026:** searches show no active storm named Lala and no reuse of the name. The 2026 East and Central Pacific season has been very active; by October it was tied with 1994, 2002 and 2018 for the most Category 5 hurricanes (Coeur d'Alene Press, Oct 5, 2026).
- **Aug 27–28, 2026:** CPHC issued its final advisory on Lala as a post-tropical cyclone near the Date Line, forecast to dissipate. It was described as post-tropical by Aug 28 (NHC TCP advisories, Aug 27, 2026; AP via WBNG, Aug 2026).
- **Aug 21, 2026:** winds down to 100 mph as Lala moved north-northeast away from Papahānaumokuākea (NHC TCP, Aug 21, 2026).
- **Aug 19, 2026, 2 PM HST:** about 115 mph, still Category 3 (NHC TCP 191133, Aug 19, 2026). A late-Aug 19 discussion put it at 90 kt (about 104 mph) and said satellite estimates had dropped (NHC discussion 32, Aug 19, 2026).
- **Aug 18, 2026, 4 PM HST:** CPHC update said "Lala has strengthened rapidly," with 125 mph and 953 mb, about 505 miles southeast of Lisianski Island. CPHC called it the first major hurricane of 2026 in the Central Pacific (NHC TCU 151859 / Boston Globe/AP, Aug 19, 2026; US News/AP headline "Lala Strengthens to a Category 3 Hurricane," Aug 19, 2026).
- **Other peak reports:** the SF Chronicle said Lala reached Category 4. Wikipedia and Weather Underground list a peak of 130 mph and 947 mb on Aug 19. These may reflect best-track revisions.
- **Aug 15–17, 2026:** Lala became a hurricane at 75 mph on Aug 15. Its eyewall brushed the southern Big Island, with more than 40 inches of rain in places, 2 deaths, and over 100 homes damaged. It then weakened to a tropical storm and moved west (CNN, Aug 16, 2026; CBS; ABC; AP via KSLA, Aug 19, 2026).
- **Scheduled events before close:** CPHC may publish Lala's post-season Tropical Cyclone Report. That usually happens months after the season, so it may not come before December 2.

## 4. Drivers and scenarios
- **YES (dominant path):** the resolver uses CPHC advisories (125 mph) or best track (125–130 mph) and settles YES. This depends only on the resolver doing its job.
- **NO path 1:** an extreme post-season downgrade to under 96 kt that the resolver then uses. This is implausible given multiple Category 3 advisories and secondary sources showing an upgrade.
- **NO path 2:** an administrative error, the market being voided, or the resolver tying the question to a different entity or time window, for example reading it as "after market creation" if the market was opened after August 19. The rules contain no such restriction.

## 5. Signposts
- **Toward YES:** the platform settles the market, or CPHC publishes a post-season report confirming a peak of 110 kt or more.
- **Toward NO (very unlikely):** the platform announces a dispute or void, or a post-season report states a peak under 96 kt.

## 6. Uncertainties
- I could not read any primary pages directly, so the advisory numbers come from search snippets. Several independent sources agree, though: AP/US News, the Boston Globe, NHC update text, and a blog titled "Lala Rapidly Intensifies to a Major Hurricane."
- I don't know why the market is still open after an event that should have triggered expiry in August, or exactly which source it settles on.
- I could not confirm whether the 130 mph / 947 mb Category 4 figure is official best track. Either 125 or 130 mph is well above 111 mph.
- A Vietnamese article mentions a "super typhoon Lala." It is probably a mislabel or a different context. I could not open it, and Lala's last advisories said it was forecast to dissipate near the Date Line.

## Sources
- [Hurricane Lala hammers Hawaii… (FOX Weather)](https://www.foxweather.com/live-news/live-updates-hurricane-warning-issued-for-hawaii-as-tropical-storm-lala-bears-down-on-the-islands)
- [Tropical Storm Lala officially forms (KHON2)](https://www.khon2.com/weather-blog/tropical-storm-lala-forms/)
- [Tropical Storm Lala Tracker (Weather Underground)](https://www.wunderground.com/hurricane/central-pacific/2026/tropical-storm-lala)
- [Lala spins out to sea… (ABC News)](https://abcnews.com/US/tropical-storm-lala-forecast-impact-hawaiian-islands-weekend/story?id=135610026)
- [Former Hurricane Lala drenches Hawaii (CBS News)](https://www.cbsnews.com/news/tropical-storm-lala-big-island-hawaii-hurricane-track/)
- [At least one dead… in wake of Hurricane Lala (CNN, Aug 16, 2026)](https://www.cnn.com/2026/08/16/weather/tropical-storm-lala-hawaii-damage-climate)
- [2026 Pacific hurricane season (Wikipedia)](https://en.wikipedia.org/wiki/2026_Pacific_hurricane_season)
- [Hurricane LALA Discussion 14 (NHC archive)](https://nhc.noaa.gov/archive/2026/cp01/cp012026.discus.014.shtml?text=)
- [Hurricane LALA Update, Aug 15 (NHC archive)](https://www.nhc.noaa.gov/archive/2026/cp01/cp012026.update.08151858.shtml)
- [Hurricane Lala Tropical Cyclone Update (NHC)](https://www.nhc.noaa.gov/mobile/text/refresh/HFOTCUCP2%2Bhtml/151859.shtml)
- [Hurricane Lala Public Advisory, Aug 19 (NHC)](https://www.nhc.noaa.gov/text/refresh/HFOTCPCP2+shtml/191133.shtml)
- [Hurricane Lala Public Advisory, Aug 21 (NHC)](https://www.nhc.noaa.gov/text/refresh/HFOTCPCP2+shtml/210852.shtml)
- [Lala Forecast Discussion, late August (NHC)](https://www.nhc.noaa.gov/text/refresh/HFOTCDCP2+shtml/232033.shtml)
- [Hurricane Lala explodes into major storm (SF Chronicle)](https://www.sfchronicle.com/weather/article/hurricane-lala-explodes-22393820.php)
- [Lala Strengthens to a Category 3 Hurricane… (US News/AP, Aug 19, 2026)](https://www.usnews.com/news/us/articles/2026-08-19/lala-strengthens-into-a-hurricane-while-moving-west-away-from-hawaii)
- [Hurricane Lala strengthens while moving west away from Hawaii (Boston Globe, Aug 19, 2026)](https://www.bostonglobe.com/2026/08/19/nation/hurricane-lala/)
- [Lala Rapidly Intensifies to a Major Hurricane (Jay Hobgood)](https://jayhobgood.com/?p=24993)
- [Forecasters warn another tropical system… after Lala left 2 dead (WBNG/AP, Aug 19, 2026)](https://www.wbng.com/2026/08/19/forecasters-warn-another-tropical-system-could-be-brewing-southeast-hawaii-after-lala-left-2-dead/)
- [A very active Pacific hurricane season (Coeur d'Alene Press, Oct 5, 2026)](https://cdapress.com/news/2026/oct/05/a-very-active-pacific-hurricane-season/)
- [Typhoon Lala strengthens into a super typhoon (Lao Động)](https://news.laodong.vn/the-gioi/bao-lala-manh-len-thanh-cuong-phong-du-bao-mua-toi-630mm-1751372.ldo)
- [Post-tropical Cyclone Lala floater (NOAA/NESDIS STAR)](https://www.star.nesdis.noaa.gov/goes/floater.php?stormid=CP012026)
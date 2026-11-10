# Research brief: Will ChatGPT have fewer than 3 outage days in November 2026?

*Prepared 2026-11-10. My fetch tool was blocked on every site, including status.openai.com. Everything below comes from search-engine summaries of the pages, not from reading them directly. Treat the counts and labels as approximate.*

## 1. Resolution mechanics

- **What gets counted:** calendar days in November 2026, using ET, when the ChatGPT status box on status.openai.com shows a red shade. Red means "Partial outage" or "Full outage". Green means no incidents and yellow means "Degraded performance"; neither counts.
- **YES (fewer than 3)** means 0, 1 or 2 qualifying days. NO means 3 or more.
- **Only ChatGPT incidents count.** ChatGPT must be listed under "Affected components". Incidents that hit only APIs, Codex, FedRamp or Ads Platform don't count. Incidents that hit ChatGPT together with the API or Codex do count, and these are common (for example "Elevated errors across ChatGPT, Codex and the API", Sept 29, 2026).
- **When a day is final:** once the next day's box appears. The market can stay open up to 7 days past Nov 30 if an incident that started in November is still unresolved.
- **Who decides:** the official status page. "A consensus of credible reporting" is a fallback.
- **Edge cases and ambiguities:**
  - **Colour.** OpenAI's status page appears to run on incident.io, which normally shows partial outages in orange and full outages in red. The rules lump them together as "a shade of red", so an orange day almost certainly counts.
  - **Time zone.** The rules use ET days, but the status page may draw day boxes in the viewer's local time zone. An incident that crosses midnight could light up two days, or a different day than expected.
  - **Sub-components.** The ChatGPT group contains many sub-components: Conversations, Login, Voice mode, Image generation, File uploads, ChatGPT Work, GPTs, Codex in ChatGPT Desktop, and others (isitdown mirror). A partial outage in any one of them, for example image generation alone, could probably turn the whole ChatGPT day red. That makes red days more likely than headline "ChatGPT is down" news would suggest.
  - **Relabelling.** OpenAI sometimes changes an incident's impact level after the fact. Changes published within the timeframe count.
  - **Duplicate days.** Several incidents on one day count as one day.

## 2. Reference classes and base rates

**A. Share of OpenAI incidents labelled partial or full outage (90 days to Oct 17, 2026).** Whizi counted 105 incidents across all OpenAI products. Only 1 was a "Full outage" (Codex, Sept 25, 56 minutes) and 12 more were "Partial outage", so about 12% (Whizi, Oct 2026).
- That is about 13 red-level incidents in 90 days, or roughly 4.3 per month across all products.
- If 60–80% of those involved ChatGPT, that is about 2.6–3.5 per month for ChatGPT, and slightly fewer distinct days.
- Caveat: Whizi's total of 105 is about double other trackers' counts, and I could not see the per-component list.

**B. All incidents of any severity.** IsDown averages about 16.9 ChatGPT incidents per month since October 2025. Another monitor counts about 18 per month since January 2025 (IsDown, accessed Nov 2026). Most of these are yellow "Degraded performance". If roughly 10–20% are red, that gives about 2–3.5 red incidents per month, which matches class A.

**C. Uptime.** OpenAI's page showed 99.52% uptime for the ChatGPT group over July–October 2026, against 99.95% for both the API and Codex (Whizi, Oct 2026). ChatGPT is the least reliable component, though the uptime figure doesn't translate directly into a count of red days.

**Recent months, for texture (not official red-day counts):**
- **September 2026** had many ChatGPT incidents: Sept 2, 3 (the big one, more than 74,000 Downdetector reports), 9, 15, 19, 20, 22, 25, 29 and 30 (tech-insider; IsDown; Pulsetic; Uptime Robot). Several of those were probably red. Full outage days so far seem to cluster in heavy months like this one.
- **October 2026** had at least one confirmed red day. On Oct 15 a "Widespread feature degradation" incident, labelled "Partial outage", broke login and signup on iOS and Android for about 2h50m (status.openai.com via search). There was also a multi-product incident on Oct 5–6.
- **Earlier red ChatGPT incidents** I found: Aug 31 (ChatGPT Work partial outage), Aug 19 (login and signup failure), and a multi-day image-generation incident in July labelled "Partial outage".

**Rough Poisson model for the rest of the month (Nov 10–30, about 21 days), assuming no red days so far:**

| Red-day rate per month | Expected red days left | P(2 or fewer more) |
|---|---|---|
| 2 | 1.4 | about 0.83 |
| 3 | 2.1 | about 0.65 |
| 4 | 2.8 | about 0.47 |
| 5 | 3.5 | about 0.32 |

Outages cluster, so the real spread is probably wider than Poisson.

## 3. Current state of the world (most recent first)

- **Nov 9:** "Elevated ChatGPT Conversation Errors", 52 minutes, rated "Minor" and resolved (Pulsetic). Downdetector reports rose around 12:56 PM ET (DesignTAXI). Sunday Guardian found no confirmed widespread outage.
- **Nov 8:** "Elevated errors with image generation", about 1h49m, rated "Minor" (Pulsetic).
- **Nov 6:** an incident about errors with some U.S. business Mastercards (Brex-related), still in monitoring for about 2 days. It probably affects billing and payments rather than ChatGPT's core service (VisualSentinel; Pulsetic).
- **Nov 5:** "ChatGPT Work and Dots Errors". The official page showed it as "Degraded performance", so yellow (status.openai.com via search). Pulsetic rated it "Minor" and gave a duration of about 13 hours. A separate "ChatGPT Issues" incident lasted about 35 minutes (StatusGator).
- **Nov 4:** "Elevated error rates across paid ChatGPT plans", 5:38–7:32 PM ET, about 1h54m. Pulsetic rated it "Minor"; I could not confirm the official label (Technobezz; Pulsetic).
- **Since Nov 1:** a user reports ChatGPT Work broken for more than 48 hours, with a server-side failure confirmed. This is one account, not a status-page outage (OpenAI Developer Community).
- **Bottom line so far:** I found no evidence that any November 1–9 incident was officially labelled Partial or Full outage. Pulsetic's "Minor" probably means degraded, but I could not confirm that mapping. StatusGator showed "warn" (amber) on most days from Nov 3 to 7, not "down". **My best estimate is 0 red days so far, possibly 1.**
- **Scheduled events:** I found no confirmed OpenAI model or product launches for late November. Launches often coincide with capacity incidents. US Thanksgiving is Nov 26, and lighter US traffic and fewer deploys that week may lower risk slightly.

## 4. Drivers and scenarios

**Paths to YES (0–2 red days):**
- November continues like its first 10 days: frequent incidents, but labelled degraded.
- OpenAI keeps the "Partial outage" label for login, conversation or broad multi-product failures, which happen about 1–3 times per month.

**Paths to NO (3 or more):**
- A cluster like September: launches or infrastructure problems causing repeated conversation-error incidents labelled partial outage.
- A single multi-day incident that stays red across 2–3 days. This has happened before, such as the multi-day image-generation incident in July.
- Sub-component partial outages (image generation, voice, file uploads, connectors) turning ChatGPT days red.
- Upstream cloud-provider outages that hit ChatGPT and the API together.

## 5. Signposts

- **A red day officially recorded between Nov 1 and 10 (verify on status.openai.com/history):** a big move toward NO. YES would then need at most one more red day in about 21 days.
- **A major model or feature launch announced for late November:** toward NO.
- **A large Downdetector spike (more than 10,000 reports) with OpenAI acknowledging errors in conversations or logins:** usually labelled partial outage, so toward NO.
- **Each week that passes with only yellow days:** toward YES. By around Nov 24 with 0 red days, YES becomes very likely.
- **Any relabelling of the Nov 4, 5, 8 or 9 incidents to "Partial outage":** toward NO.

## 6. Uncertainties

- **I could not view status.openai.com, so I can't confirm the colours of the Nov 1–9 ChatGPT day boxes.** This is the most important gap, and the forecaster should check it directly.
- I don't have an exact monthly history of red ChatGPT days from the official page. My base rate of about 2–4 per month is inferred from Whizi's 90-day severity breakdown and from incident lists, and may be off.
- It's unclear whether a partial outage in a ChatGPT sub-component always turns the group's day box red.
- It's unclear whether day boxes follow ET or the viewer's local time zone.
- Third-party trackers disagree on counts and severity, and their "Minor" or "warn" labels don't map cleanly onto OpenAI's impact levels.
- I don't know whether any OpenAI launches are scheduled before Nov 30.

## Sources
- [OpenAI Status – incident history](https://status.openai.com/history)
- [Elevated error rates across paid ChatGPT plans – OpenAI Status (Nov 4, 2026)](https://status.openai.com/incidents/01M6MBCX427A7113A3T4FJ1N6Y)
- [ChatGPT Issues – OpenAI Status (Nov 5, 2026)](https://status.openai.com/incidents/01M6P50GPP1V98EF8MJ9SH393R)
- [Widespread feature degradation – OpenAI Status (Oct 15, 2026)](https://status.openai.com/incidents/01M506BA4XRSWH7THR53HQGN3Z)
- [ChatGPT Work seeing elevated errors and latency – OpenAI Status](https://status.openai.com/incidents/01M1C5M4K0WC8PPT0Z175RJA1E)
- [Is ChatGPT Down? ChatGPT Status & Outage Tracker – Pulsetic](https://pulsetic.com/status/chatgpt/)
- [OpenAI ChatGPT Status – StatusGator](https://statusgator.com/services/openai/chatgpt)
- [OpenAI Outage History – StatusGator](https://statusgator.com/services/openai/outage-history)
- [Is OpenAI ChatGPT Down? – IsDown](https://isdown.app/status/chatgpt)
- [AI Outages: 105 OpenAI Incidents in 90 Days, Anthropic 72 – Whizi](https://whizi.io/resources/ai-chatbot-outages/)
- [OpenAI Reports Elevated Error Rates Across Paid ChatGPT Plans – Technobezz](https://www.technobezz.com/news/openai-service-incident-a8e2e7b4)
- [OpenAI Outage Today… – Sunday Guardian Live (Nov 9, 2026)](https://sundayguardianlive.com/trending/openai-outage-today-is-openai-down-today-in-the-us-users-report-chatgpt-api-login-image-generation-server-issues-openai-downdetector-status-319939/)
- [Is OpenAI / ChatGPT down? [November 9, 2026] – DesignTAXI](https://community.designtaxi.com/topic/46252-is-openai-chatgpt-down-november-9-2026/)
- [ChatGPT Work broken for over 48 hours – OpenAI Developer Community](https://community.openai.com/t/chatgpt-work-broken-for-over-48-hours-server-side-failure-confirmed-but-openai-support-has-stopped-responding/1412217)
- [ChatGPT Down Again: 74,000 Reports, Codex Hit Too – Tech Insider](https://tech-insider.org/chatgpt-outage-74000-reports-codex-2026/)
- [Elevated errors across ChatGPT, Codex and the API – IsDown (Sept 29, 2026)](https://isdown.app/status/openai/incidents/662419-elevated-errors-across-chatgpt-codex-and-the-api)
- [OpenAI status 2026-09-25 – UptimeRobot](https://uptimerobot.com/is-it-down/openai/2026-09-25/)
- [ChatGPT outage on 22 Oct 2026 – HostTracker](https://www.host-tracker.com/en/is-chatgpt-down/incidents/2026-10-22-1258)
- [Is OpenAI Down Right Now? – isitdown mirror](https://isitdown.mediapage.workers.dev/status/openai)
- [ChatGPT Down Right Now? – VisualSentinel](https://visualsentinel.com/tools/status/chatgpt)
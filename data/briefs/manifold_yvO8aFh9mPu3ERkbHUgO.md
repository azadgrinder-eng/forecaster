# Research Brief: Will iPhones have an AI that can access and remember everything you do on your phone by EOY 2026?

*Research note: every page fetch was refused by the network proxy. Everything below comes from search-result summaries of the cited articles, not from reading the full pages. Treat the finer details as needing confirmation.*

## 1. Resolution mechanics
- **What counts as YES:** At some point before the deadline, the newest iPhone model ships with a built-in feature or app that has access to "a full record of everything you do on your phone" (or everything from when you switch it on), and an AI can use that record.
  - Opt-in is allowed.
  - Per-app or per-activity toggles are allowed.
  - Being able to delete data or memories is allowed.
  - It does not count if you have to download something from the App Store, so ChatGPT, Gemini and other third-party apps are out.
- **Deadline:** The question closes on 2026-12-25. The text says "EOY 2026", so the practical cutoff is about Dec 25–31.
- **Who decides:** The question creator, using their own judgment. No objective test is given.
- **The central ambiguity is what "a full record of everything you do" means.**
  - Strict reading: something like Microsoft Recall, a continuous log of screens, app usage and actions across all apps. Nothing like that exists on the iPhone today.
  - Lenient reading: Siri AI's index of your personal data plus its memory, which reaches Mail, Messages, Photos, Notes, Calendar, Files, Reminders, voicemails, Safari history, past Siri conversations, the current screen, and third-party apps that plug into Spotlight. A generous resolver might accept this as "access to everything." A careful one probably would not: there is no record of what you did inside most third-party apps, and on-screen awareness only sees the current screen, not a history.
- **Other wording issues:**
  - "Resolves NO if this is not true continuously until the deadline" sits awkwardly next to "at any point before resolution." It may mean the feature has to stay available once it ships.
  - Siri AI is still labelled a beta. It is not available in the EU, and some reports say it is also unavailable in China. The criteria don't say whether a beta label or regional limits disqualify it. Most resolvers would probably ignore both.
- **"Newest iPhone model":** The iPhone 18 Pro and 18 Pro Max were announced Sept 9, 2026 and shipped Sept 18 with iOS 27 (Apple Newsroom, Sept 2026). I could not confirm whether an iPhone Fold has launched. It wouldn't matter much, because any new iPhone ships with iOS 27 and Siri AI.

## 2. Reference classes and base rates
1. **Features found in Apple beta code that ship in that same point release.**
   - The "memory graph" was found in iOS 27.3 beta 1 (Nov 3, 2026). Reports say no process creates memory records yet and there are no menus to view or delete them.
   - Unannounced, half-built features found in Apple betas usually take one or more release cycles to ship, and some never do.
   - Apple's own recent record is relevant. The "personal context" Siri announced at WWDC 2024 slipped from iOS 18 to iOS 26.4 and finally arrived as "Siri AI" in iOS 27 (Sept 2026), about 2 years late.
   - My rough estimate: under 15% of features in this "unfinished in beta 1" state ship publicly within about 6 weeks. This is a judgment call, not a counted statistic.
2. **Big-platform "remember everything you do" features.**
   - Microsoft announced Recall in May 2024. After the privacy backlash it was pulled, made opt-in, and only rolled out widely about a year later (2025, from memory).
   - Apple's public stance consistently stresses privacy ("grounded in personal context, built with privacy at every step," Federighi, WWDC 2026). Apple has never announced a screen- or activity-logging feature.
   - Base rate for Apple shipping a feature its own messaging has never described: very low in any given 6-week window.
3. **What Apple has actually shipped toward "memory" in 2026.**
   - Siri AI arrived with iOS 27 on Sept 14, 2026.
   - Conversation memory plus wider data access arrived in iOS 27.2 on Oct 26, 2026.
   - So Apple is moving in this direction step by step, roughly every 6 weeks, with each step limited in scope.

## 3. Current state of the world (most recent first)
- **Nov 3, 2026:** iOS 27.3 developer beta 1 is out (build 24C5037i).
  - It opens Siri AI to third-party apps and developers (Cult of Mac; Memeburn).
  - Code researcher pdfu found a Siri "memory graph" in it (Notebookcheck; Schmidtisblog; BigGo). Details:
    - It covers 26 categories of personal information, grouped into 21 topic areas such as food, finance and travel. These include contacts, relationships, frequently visited places, routines, activities and health information.
    - It is built around a profile of the user, made of "memory atoms": facts, opinions, intentions and events.
    - It is unfinished: nothing creates these records automatically yet, and there are no menus to view or delete them. Apple has not announced it.
  - Apple says iOS 27.3 will ship to the public in December, with no date given. Estimates cluster around Dec 12–26 (9to5Mac, Oct 29; TechRepublic; Mihata.jp). TidBITS expects mid-December.
- **Oct 26, 2026:** iOS 27.2 shipped (MacRumors; 9to5Mac; TidBITS; TheNextWeb; TechCrunch Oct 27).
  - Siri AI can recall past conversations (English only).
  - Personal context now reaches photos sent in Messages, Calendar attendees, voicemails, and Safari history and Reading List.
  - A new setting (Settings > Siri > Excluded Apps) lets you block apps from Siri, Search and Suggestions in one place.
  - Five new languages were added.
  - Requires an iPhone 15 Pro/Pro Max or any iPhone 16 or later.
  - Siri AI is still labelled beta and is still absent in the EU.
  - Coverage reports no continuous screen capture and no searchable activity timeline.
- **Sept 30, 2026:** Macworld ("Siri may know a lot more, but it's still not smart") says Siri AI knows more but has usability problems.
- **Sept 9–18, 2026:**
  - iPhone 18 Pro and Pro Max announced (Sept 9) and on sale Sept 18.
  - iOS 27 with Siri AI (beta) released Sept 14.
  - Siri AI "can draw on messages, emails and photos… act on what's on screen" (Apple Newsroom; Thurrott).
- **June 8, 2026, WWDC:** Siri AI unveiled.
  - It is built on Apple Foundation Models developed with Google Gemini, running on-device and on Private Cloud Compute.
  - It has three layers: personal context, on-screen awareness and world knowledge.
  - Personal context comes from a semantic (Spotlight) index of Mail, Messages, Photos, Files, Notes, Calendar and Reminders. Third-party apps are included only if they integrate with Spotlight; one tester found Snapchat, Flighty and Expedia were not searchable.
  - In iOS 27, apps can attach hidden labels (annotations) to what they show on screen, so Siri reads structured data instead of screenshots (MacStories review).
  - A standalone Siri app with auto-deleting chats was reported (MacRumors, May 18).
- **Scheduled before close:** iOS 27.3 public release in December, possibly before Dec 25, possibly not. Further 27.3 betas will come in mid-to-late November. iOS 27.4 is not expected until about spring 2027.

## 4. Drivers and scenarios
**Paths to YES**
- **(a) Lenient resolution of today's features (most likely YES path).** The resolver decides that Siri AI's personal context, Safari history, voicemail, conversation memory, on-screen awareness and Excluded Apps toggles together amount to "access to everything you do." This depends entirely on how the resolver reads the wording. The Excluded Apps toggle fits the "toggle access to certain apps" clause neatly, which may push a resolver toward YES.
- **(b) The memory graph ships in iOS 27.3 before about Dec 25–31.** All of the following would have to happen:
  - The feature gets finished in later betas.
  - Apple enables it publicly.
  - 27.3 releases in time.
  - The resolver counts a profile of facts, routines and activities as a "full record."

  Each step is uncertain, and the second is the least likely.
- **(c) A surprise launch of a Recall-style activity log.** Nothing in the evidence suggests this is coming.

**Paths to NO**
- The resolver applies the literal "full record of everything you do" test. Siri AI indexes data from selected apps and the current screen. It does not record your actions across the phone (time spent in third-party apps, what you viewed, taps, and so on).
- The memory graph slips to 27.4 or later, which is typical for features that are only stubs in beta 1.
- A minor factor: the beta label and EU unavailability.

## 5. Signposts
- **iOS 27.3 beta 2 and 3 (mid-to-late November):** If memory-graph settings appear (a menu to view or delete memories, or records being created automatically), that is a strong move up for path (b). If it is still dormant or removed, that is a move down.
- **iOS 27.3 release date and notes:** A release before Dec 25 whose notes mention Siri "memory," "remembers your activities," or "learns your routines" would push the probability up a lot. A release after Dec 25, or notes without memory, pushes it down.
- **Any clarification from the question creator** on whether index-based personal context counts. This is the single biggest swing factor.
- **Apple wording:** Phrases like "Siri remembers everything you do" or "activity history" push toward YES. Messaging that stresses Siri only uses specific data pushes toward NO.
- **Privacy backlash** to the memory-graph reports (several outlets are already framing it as "remembering things you'd rather forget") could make Apple more cautious. That would push toward NO.

## 6. Uncertainties
- I could not read Apple's own iOS 27.2 or 27.3 release notes or developer documentation directly, because page fetches were blocked. The exact list of what Siri AI indexes comes from secondary sources, and they disagree in places.
- I could not determine whether the memory graph's "activities" category logs in-app or phone activity, or whether it covers life events and routines inferred from your data.
- I could not confirm whether an iPhone Fold or another newer model has launched, which affects which device counts as "newest." Probably irrelevant, since all new iPhones run iOS 27.
- The exact iOS 27.3 release date relative to the Dec 25 close is unknown.
- I don't know how the resolver will treat the beta label, regional limits, or the "continuously until the deadline" clause.
- I don't know when the question was created, which would show what the creator considered "not yet existing." If it was written after Siri personal context was announced (WWDC 2024), the creator probably meant something beyond it.

## Sources
- [Siri AI: iOS 27.3 reveals Apple's personal memory feature – Notebookcheck](https://www.notebookcheck.net/Siri-AI-iOS-27-3-reveals-Apple-s-personal-memory-feature.1446188.0.html)
- [Apple Siri: Neues Gedächtnis in iOS 27.3 entdeckt – Schmidtisblog](https://www.schmidtisblog.de/apple-siri-gedaechtnis-ios-27-3-memory-graph-1820686/)
- [Apple's iOS 27.3 Beta Code Points to Siri Memory Graph – BigGo Finance](https://finance.biggo.com/news/72fd4102-11ff-414c-8fa7-b931896d2dc1)
- [Your iPhone Could Soon Remember Things About Your Life… – Gotechtor](https://www.gotechtor.com/apple-siri-memory-graph-ios-27-3-beta/)
- [iOS 27.2 Features: Everything New – MacRumors (Oct 26, 2026)](https://www.macrumors.com/2026/10/26/ios-27-2-features/)
- [Apple releases iOS 27.2, here's what's new – 9to5Mac (Oct 26, 2026)](https://9to5mac.com/2026/10/26/apple-releases-ios-27-2-heres-whats-new/)
- [OS 27.2 Gives Siri AI a Memory – TidBITS (Oct 26, 2026)](https://tidbits.com/2026/10/26/os-27-2-gives-siri-ai-a-memory-and-brings-small-improvements/)
- [Apple's iOS 27.2 gives Siri AI a memory – TheNextWeb](https://thenextweb.com/news/ios-27-2-siri-ai-memory-languages-excluded-apps-eu)
- [Apple rolls out iOS 27.2 – TechCrunch (Oct 27, 2026)](https://techcrunch.com/2026/10/27/apple-rolls-out-ios-27.2-with-new-siri-ai-languages-and-security-fixes/)
- [iOS 27.2 Adds Siri Conversation Memory – The Mac Observer](https://www.macobserver.com/news/ios-27-2-adds-siri-conversation-memory-so-it-can-remember-what-you-asked-before/)
- [iOS 27.2 is here: Siri remembers past conversations – Techwire](https://www.techwire.co.il/en/article/ios-27-2-siri-memory)
- [Siri AI gets Memory – Matthew Cassinelli](https://appleintelligence.substack.com/p/siri-ai-gets-memory)
- [iOS 27.3 release date – 9to5Mac (Oct 29, 2026)](https://9to5mac.com/2026/10/29/ios-27-3-release-date-heres-when-to-expect-new-iphone-features/)
- [Apple Says iOS 27.3 Beta Coming Next Week – MacRumors (Oct 30, 2026)](https://www.macrumors.com/2026/10/30/apple-says-ios-27-3-beta-coming-next-week/)
- [iOS 27.3 Coming in December – TechRepublic](https://www.techrepublic.com/article/news-ios-27-3-release-date-features-beta-apac-china/)
- [iOS 27.3 Release Date: Beta 1 Out, Final Likely in December – Mihata](https://mihata.jp/en/column/ios-27-3-when)
- [Siri AI opens to third-party apps in iOS 27.3 beta – Cult of Mac](https://www.cultofmac.com/news/ios-27-3-beta-siri-ai-audio-intelligence)
- [iOS 27.3 Beta 2026: Siri AI for Every App – Memeburn](https://memeburn.com/ios-27-3-beta-siri-ai-developers/)
- [Apple debuts iPhone 18 Pro and iPhone 18 Pro Max – Apple Newsroom (Sept 2026)](https://apple.com/newsroom/2026/09/apple-debuts-iphone-18-pro-and-iphone-18-pro-max/)
- [iPhone 18 Pro and Pro Max coming Sept 18 – Thurrott](https://www.thurrott.com/apple/341444/apples-iphone-18-pro-and-pro-max-are-coming-on-september-18-with-a-1199-starting-price)
- [Apple finally ships its AI do-over: Siri AI – TheNextWeb (WWDC 2026)](https://thenextweb.com/news/apple-wwdc-2026-siri-ai-gemini-ios-27)
- [WWDC 2026: Apple introduces Siri AI – MacTech (June 8, 2026)](https://www.mactech.com/2026/06/08/wwdc-2026-apple-introduces-siri-ai-a-major-overhaul-of-its-personal-digital-assistant/)
- [Siri as a General Assistant – MacStories iOS 27 review](https://www.macstories.net/stories/ios-and-ipados-27-review/6/)
- [Siri personal context guide – WhistleOut](https://www.whistleout.com/CellPhones/Guides/siri-personal-context)
- [Siri may know a lot more, but it's still not smart – Macworld (Sept 30, 2026)](https://www.macworld.com/article/3246839/siri-may-know-a-lot-more-but-its-still-not-smart.html)
- [iOS 27: Dedicated Siri App to Include Auto-Deleting Chats – MacRumors (May 18, 2026)](https://www.macrumors.com/2026/05/18/ios-27-siri-app-auto-deleting-chats-feature/)
- [Why Apple's iOS 26.4 Siri Upgrade Will Be Bigger – MacRumors (Feb 6, 2026)](https://www.macrumors.com/2026/02/06/siri-ios-26-4-rumors/)
- [iPhone Fold expected to launch in 2026 but ship in 2027, says Kuo – GSMArena](https://m.gsmarena.com/iphone_fold_expected_to_launch_in_2026_but_ship_in_2027_says_kuo-news-70780.php)
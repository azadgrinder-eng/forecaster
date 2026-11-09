# Research brief: will a public GTA VI decompilation appear within 31 days of release?

## 1. Resolution mechanics

**What counts as YES:** The game releases on November 19, 2026, so the window runs to about December 20, 2026. Within that window, a community project must publicly release a source repository that meets all three conditions:
- (a) it is written in a high-level language such as C or C++;
- (b) it was reconstructed by reverse-engineering the retail compiled binaries;
- (c) it compiles into a working executable that runs at least the intro sequence or the first playable mission.

**What is excluded:** Leaked official Rockstar or Take-Two source code does not count. If release slips, the window moves with it. The question closes on December 19, 2026 at 23:59 UTC, which is about a day before the 31-day window ends. That gap is a minor ambiguity that only matters for a release on the last day.

**Who decides:** The market creator, judging informally. No neutral body checks whether the code is a "true decompilation."

**Edge cases and ambiguities:**
- **Hybrid projects:** Earlier decompilations such as re3 started as code injected into the original executable, replacing functions one at a time. It is unclear whether a hybrid build counts as a "functional executable."
- **Static recompilation:** Tools in the N64Recomp or XenonRecomp style produce machine-generated C that compiles. A lenient judge might accept this; a strict one might not.
- **Which platform it runs on:** The rules say "on any platform," and a build that only runs on a jailbroken PS5 seems to qualify. The rules don't say whether the user may supply their own game assets. Every legitimate decompilation project requires this.
- **Takedowns:** If a repository is posted and removed by DMCA within hours, it is unclear whether it was "made publicly available." Take-Two is aggressive about takedowns (see section 3).
- **Proof of playability:** A claim of playability with no independent check would leave the judge with little to go on. Unverifiable claims are likely.

## 2. Reference classes and base rates

1. **Any commercial game publicly decompiled and playable within one month of its retail release:** I found no case at all, for retro or modern games, human or AI-assisted. Examples of the usual gap:
   - Super Mario 64: 1996 release, decompilation 2019 (about 23 years).
   - GTA III (re3): 2001 release, 2020 decompilation (about 18 years).
   - GTA Vice City (reVC): 2002 release, 2020 decompilation (about 17 years).
   - Super Smash Bros. Melee: reached 100% matching in September 2026 after roughly 6 years of work (Decompiled/AI lists, October–November 2026).
   
   Base rate: 0 of several hundred projects. A tracker listed 273 AI-assisted projects on October 30, 2026, and PlayPorted listed 171 decompiled games in November 2026.
2. **AI-agent decompilation of a modern-ish x86 AAA game, from start to finish:** The best data point is momo5502's agent project on Call of Duty: Modern Warfare 2 (2009).
   - It took about 11 weeks to 3 months with up to 17 parallel agents (Claude Opus 5.5 and Codex).
   - It used an estimated 500–700 billion tokens, though one secondary report says 235 billion.
   - 99% of functions were reconstructed, with 83% byte-exact.
   - The source code is private, and it started from an unencrypted PC binary (momo5502 blog, October 9, 2026; Runtimewire; Tom's Hardware via secondary coverage).
   - An earlier agent run was about 80% done after a month and ran, but its code was semantically wrong until byte-matching checks were added.
   - The N64 game Snowboard Kids (2,145 functions) took 84 days with AI.
   
   GTA VI's executable is almost certainly far larger and more complex than MW2 2009 (the RAGE engine, its own scripting, a modern console graphics API). So 0 of about 1 modern AAA game was done in 31 days, and the fastest known was about 2.5 times too slow, on a much smaller target.
3. **Console-exclusive games whose executable could be decrypted within a month of launch, when launch requires the latest firmware:** For PS5, public exploits have always lagged the newest firmware by months to years. In November 2026, public jailbreaks covered firmware up to about 13.60. A 14.10 debug-menu demo existed but was not a public kernel exploit. Xbox Series consoles have had no public game-dumping exploit since Collateral Damage was patched in 2024. My rough estimate is that fewer than 10% of major console exclusives had public decrypted executables within a month of release in this generation.

## 3. Current state of the world (most recent first)

- **Nov 5–9, 2026:** The release is still set for November 19, 2026, on PS5 and Xbox Series X|S. There is no PC version, and 2027 is only speculation. Rockstar released a launch trailer on October 15 and screenshots on November 5, and Take-Two reconfirmed the date on August 7. Preloads start November 10–12, with a PS5 download of about 210 GB (Endgame Tools; PC Gamer; GTA 6 Library).
- **Nov 2, 2026:** Sony released PS5 firmware 26.07-14.22.00. Its only patch note is "security fixes." Store-tracker data, which Sony and Rockstar haven't confirmed, suggests GTA VI requires 14.22; an earlier report said 14.10. Coverage describes this as blocking the Relapse jailbreak, which works on firmware 7.00–13.60 (Godisageek, November 2026; ARY News; PC Guide).
- **Late Oct 2026:** "No confirmed public method" exists to dump and run GTA VI through a PS5 jailbreak as of October 29. Shattered.io's headline was "0 proven PS5 exploits." The hacker Gezine showed debug-menu access on firmware 14.10 (GamesRadar, October 2026).
- **Late Oct 2026 (single source):** Claude Code reportedly added a rule against recreating games. As of October 30, no project had publicly reported a refusal because of it (HeldGames).
- **Oct 2026:** Former Rockstar North technical director Obbe Vermeij said someone could feed the PS5 version to AI to make a PC version. He estimated it would take "hours and hours" and cost "tens of thousands of dollars in tokens," adding "if it's GTA, people are gonna try it." He has no inside information (EGW News; GameGPU; TalkEsport).
- **Oct 9–10, 2026:** Kotaku reported hundreds of AI-assisted browser ports, including Halo CE and Vice City, built with help from Claude Opus 5.5. Many build on long-running human decompilations; the Vice City ones likely build on reVC. How much of the work AI did is often unclear (Kotaku via Techmeme; Heise).
- **Oct 6, 2026:** Take-Two shut down the playgta5.com browser port within hours. It apparently relied on leaked GTA V source code rather than decompilation (Startup Fortune). Earlier Take-Two actions: DOS Zone in December 2025, and re3/reVC taken down in 2021 followed by a lawsuit.
- **Jan 2026:** PS5 boot ROM keys leaked. Notebookcheck said this lowers barriers for homebrew but is "not an overnight jailbreak." I could not establish whether it lets anyone decrypt executables for current-firmware games.

## 4. Drivers and scenarios

**Paths to YES (each needs every step in its chain):**
- **A. PS5 route:**
  1. A new kernel exploit on firmware 14.22 or later, or a way to decrypt using the leaked boot ROM keys, becomes public in the first one to two weeks.
  2. The GTA VI executable is dumped.
  3. A well-funded team runs a massive agent swarm. Vermeij's "tens of thousands of dollars" is likely an underestimate given MW2's hundreds of billions of tokens.
  4. The team gets enough code for the intro or first mission to compile against the PS5 homebrew SDK, then runs it on a jailbroken console or ports the graphics to PC.
  5. They publish the code openly despite near-certain Take-Two legal action.
- **B. Lenient resolution:** A static recompilation, a hybrid hook build, or an unverified claim gets posted, and the judge accepts it.
- **C. Hoax or misresolution:** Someone posts a fake "decompiled GTA 6" repository. GTA hype makes fakes likely; the judge would have to accept it.

**Paths to NO:**
- No decrypted binary in time. This is the main bottleneck on both consoles.
- Not enough time even with a binary: MW2 took about 11 weeks for a smaller game.
- Groups that could do it keep their code private, as momo5502 did with MW2.
- DMCA takedown within hours.
- Model rules against game recreation and the cost of tokens.
- Even a "playable" build would need translation of the console graphics and OS APIs, or a jailbroken console on the required firmware.

## 5. Signposts

**Toward YES (large moves):**
- A public PS5 kernel exploit for firmware 14.22 or later, or a working decryption of GTA VI's executable (the eboot), before or soon after November 19.
- Reports of the GTA VI executable being dumped.
- A credible team (momo5502-tier, or decomp.dev regulars) announcing a GTA VI project with progress percentages.

**Toward YES (smaller moves):**
- Early physical copies leaking before release, which gives more time only if decryption is possible.

**Toward NO:**
- Sony shipping further firmware updates.
- No exploit news by around December 1.
- Take-Two lawsuits or pre-emptive DMCA notices.
- Any confirmed refusal by AI tools on GTA VI work.
- A large release delay would shift the window but not change the structural barriers.

## 6. Uncertainties

- The size of GTA VI's executable and how many functions it has: unknown.
- Whether the leaked PS5 boot ROM keys allow decrypting executables for current-firmware games.
- The actual required firmware: 14.22 versus 14.10 is unconfirmed by Sony and Rockstar.
- Whether any private exploit holders have the capability and the willingness to use it.
- How the market creator would treat hybrid builds, static recompilation, takedowns, or unverifiable claims.
- The accuracy of AI-decompilation statistics: many come from aggregator blogs, and token counts and agent numbers conflict between sources.
- Whether the reported Claude game-recreation rule exists and what it covers (single source).
- WebFetch was blocked in this session, so all facts come from search-result summaries rather than full primary pages.

## Sources
- [GTA 6 guide (PC Gamer)](https://www.pcgamer.com/grand-theft-auto/gta-6-guide/)
- [GTA 6 release date: November 19, 2026 (Endgame Tools)](https://endgametools.com/en/gta-6/news/gta-6-release-date-latest-news)
- [GTA 6 News (GTA 6 Library)](https://gta6library.com/news)
- [GTA 6 Reportedly Requires PS5 Firmware 14.22 (Godisageek, Nov 2026)](https://godisageek.com/2026/11/gta-6-ps5-firmware-requirement/)
- [New PS5 firmware update blocks Relapse jailbreak ahead of GTA 6 (ARY News)](https://arynews.tv/new-ps5-firmware-update-blocks-relapse-jailbreak-ahead-of-gta-6-release)
- [Sony updates PS5 software again ahead of GTA 6 (PC Guide)](https://www.pcguide.com/news/sony-updates-ps5-software-yet-again-with-security-updates-ahead-of-gta-6-launch/)
- [Another PS5 jailbreak has seemingly arrived ahead of GTA 6 (GamesRadar)](https://www.gamesradar.com/games/grand-theft-auto/another-ps5-jailbreak-has-seemingly-arrived-ahead-of-gta-6-and-sony-and-rockstars-worst-nightmare-could-be-on-the-horizon/)
- [GTA 6 Piracy Claim: 0 Proven PS5 Exploits (Shattered.io)](https://shattered.io/gta-6-piracy-ps5-launch-zelnick-zero-proven-exploits-2026/)
- [PS5 BootROM keys dumped (Notebookcheck)](https://www.notebookcheck.net/Sony-faces-an-unfixable-PS5-vulnerability-as-BootROM-keys-are-dumped-and-shared-publicly.1194911.0.html)
- [PS5 jailbreak explained (Sweet TNT)](https://sweettntmagazine.com/playstation-5-jailbreak/)
- [Xbox Series X Kernel Exploit Collateral Damage (Wccftech)](https://wccftech.com/xbox-series-x-kernel-exploit/)
- [Collateral Damage GitHub](https://github.com/exploits-forsale/collateral-damage)
- [500+ Billion Tokens Later: AI Agents Decompile an FPS (momo5502)](https://momo5502.com/posts/2026-10-09-game-decompilation/)
- [AI agents reconstruct 99% of MW2 functions (Runtimewire)](https://runtimewire.com/article/ai-agents-mw2-decompilation-byte-matching)
- [Byte-matching check in a three-month game decompilation (Braindetox)](https://braindetox.kr/en/posts/ai_agent_game_decompilation_byte_match_judge_2026.html)
- [How AI Decompiles Old Games: N64 in 84 days (AI Signal)](https://aisignal.day/en/ai-game-decompilation-2026/)
- [Claude added a rule against recreating games (HeldGames)](https://heldgames.com/guides/ai-game-recreation-rule-decomp-scene)
- [Game decompilations list Oct 2026 (ReadOnlyMemo)](https://readonlymemo.com/decompilation-projects-and-n64-recompiled-list/)
- [Decompiled Games List Nov 2026 (PlayPorted)](https://playported.com/guides/decompiled-games/)
- [Kotaku AI browser ports (Techmeme)](https://www.techmeme.com/261010/p17)
- [Halo, Vice City, Black Ops: AI ports run in the browser (Heise)](https://www.heise.de/en/news/Halo-Vice-City-Black-Ops-AI-ports-of-games-run-in-the-browser-11485764.html)
- [AI reverse engineering turns GTA 5 and Halo into browser games (Startup Fortune)](https://startupfortune.com/ai-reverse-engineering-turns-gta-5-and-halo-into-browser-games-overnight/)
- [Take-Two's DMCA hammer falls on GTA browser revival (Generation Amiga, Dec 2025)](https://www.generationamiga.com/2025/12/27/take-twos-dmca-hammer-falls-on-fan-made-gta-browser-revival/)
- [GTA 6 PC release could move up to beat AI rip-offs (EGW News)](https://egw.news/gaming/news/38284/gta-6-pc-release-could-move-up-to-beat-ai-rip-offs-NYqgrnajg)
- [Former Rockstar CTO on GTA 6 PC (GameGPU)](https://en.gamegpu.com/news/igry/byvshij-tekhnicheskij-direktor-rockstar-obyasnil-pochemu-gta-6-vyjdet-na-pk-bystree)
- [Ex-Rockstar Dev: AI Ports Could Bring GTA 6 to PC Sooner (TalkEsport)](https://www.talkesport.com/gta-6/gta-6-pc-release-ai-ports-obbe-vermeij/)
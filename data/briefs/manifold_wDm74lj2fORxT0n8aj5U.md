# Research brief: Will "yeet" be the final keyword for throwing exceptions in Rust?

## 1. Resolution mechanics

- **What the question means:** The criteria only give background: "yeet" was "proposed as a temporary keyword to stop people from bikeshedding over the throw operator name." The most natural YES condition is that Rust adopts `yeet` (the current nightly syntax is `do yeet expr`) as the official, stable keyword for early-exit or "throw" expressions. The usual signs of that would be an approved RFC that keeps the name and stabilization in a stable Rust release.
- **Deadline:** The close date is 2026-12-30. The rules do not say whether the question resolves at close or waits for a final decision on the name. If nothing is decided by close, it is unclear whether the creator resolves NO, resolves N/A, or extends the deadline. The forecaster should keep this ambiguity in mind.
- **Who decides:** The question creator decides the resolution. In practice that decision follows the Rust language team, which approves RFCs and stabilizations.
- **Edge cases:**
  - Rust might never stabilize any throw-style syntax, for example by dropping the feature or relying on `Err(e)?` or macros. That most plausibly counts as NO, or possibly N/A.
  - `yeet` might be reserved as a keyword in a future edition without being stabilized. That alone is probably not "final."
  - A stable keyword with a different name, such as `throw`, `fail`, `raise` or `bail`, would clearly be NO.
  - The library type `core::ops::Yeet` is a separate item, but its name is tied to the same decision.
- **Release-train limits (my calculation from the 6-week cadence):**
  - Rust 1.93 shipped 2026-01-22. Counting forward gives 1.99.0 around 2026-10-01, which matches reports of 1.99.1 shipping 2026-10-15 to fix 1.99.0 regressions (LinuxCompatible / Releasebot, Oct 2026). On the same count, 1.100 was around 2026-11-12 and 1.101 is around 2026-12-24.
  - 1.101 is the only stable release left before close. Its beta branched around early-to-mid November.
  - So even if something were stabilized today, it would reach stable no earlier than about 1.102 in early February 2027. On a strict "in stable Rust by close" reading, YES is mechanically almost impossible.

## 2. Reference classes and base rates

1. **Explicitly labeled placeholder names in Rust that became final.**
   - The tracking issue itself says the feature "will certainly not stabilize under the name `yeet`" (rust-lang/rust #96373, opened 2022-04-25).
   - The compiler-team proposal calls `yeet` "a bikeshed-avoidance name for 'fail, raise, throw, etc'" and says it won't be used outside nightly (compiler-team MCP #501, 2022).
   - Comparable cases mostly ended in renaming: `do catch { }` became `try { }` (2018-edition keyword reservation), and `await!()` became `.await`.
   - I know of no Rust case where a name the lang team called a "placeholder" was stabilized unchanged. My rough estimate is 0 of about 3–5 cases. That count is approximate and from memory, not from a systematic search.
2. **Time from nightly experiment to stable for error-handling features.**
   - `try` blocks have been unstable since about 2018, roughly 8 years. A new homogeneous `try_blocks` tracking issue (#154391) opened 2026-03-25 and is still unstable.
   - The `Try` trait v2 (RFC 3058, accepted 2021) is still unstable. Stabilizing it is a 2026 project goal, with its tracking issue opened 2026-05-05 (rust-lang/goals #654).
   - The never type `!` has been unstable for about 10 years.
   - Base rate for these error-handling features: 0 of 3 stabilized within 4 or more years.
3. **Lang experiments that still need an RFC.** "Per the lang process, this cannot go further than experimenting without an approved RFC" (#96373). As of 2026, I found no RFC for yeet or throw expressions. The only earlier throw RFC, `throw` expressions in rfcs PR #2426 (2018), was a separate proposal. Without a filed RFC, the chance of stabilization within about 6 weeks is effectively zero.

## 3. Current state of the world (most recent first)

- **2026-09-30:** The lang-team triage notes list blockers for stabilizing `try` blocks, including homogeneity and its effect on `Poll` (rust-lang/rust #155368). They do not mention yeet (Lang triage meeting, 2026-09-30, from search snippet).
- **2026-08-05:** Lang triage discussed a `try Type {}` syntax. The note says there is "no formal lang experiment for try blocks yet" (Lang triage, 2026-08-05, snippet).
- **2026-05-05:** The tracking issue for the 2026 project goal "Stabilize the Try trait" opened. It aims at a limited stabilization of the `Try` trait and does not mention yeet, throw or try blocks (stabilize-try.md, 2026). Lang feedback described the work as bottlenecked by design edge cases and limited champion bandwidth (Project Goal Feedback 2026 (Lang), HackMD).
- **2026-03-25:** The homogeneous `try_blocks` tracking issue #154391 opened. It is tied to RFC 3721 and is still unstable.
- **2026-03-13:** An Internals thread, "Why `yeet` in `try` blocks if `break` is good enough?", was closed. I could not read what it concluded.
- **Dec 2025 – Feb 2026:** Compiler-team MCP #945, "Parse unstable keywords for experimental syntax," appeared on T-compiler agendas as pending FCP. It could let experimental syntax use unstable keywords; I could not confirm whether it is linked to yeet (T-compiler agendas, 2025-12-11 and 2026-02-19).
- **About 2025:** Yosh Wuyts' blog argues the feature should be spelled `throw`. This is a personal proposal, not lang-team policy.
- **Ongoing:** `do yeet` is still nightly-only under `#![feature(yeet_expr)]`, with `ops::Yeet` under `try_trait_v2_yeet`. The Unstable Book calls it "highly experimental" with "placeholder syntax." Tracking issue #96373 appears to still be open, and no stabilization PR is listed.
- **Scheduled before close:** Rust 1.101 around 2026-12-24 (estimated). Lang-team triage meetings happen weekly. I found no scheduled RFC decision on throw or yeet syntax.

## 4. Drivers and scenarios

**Paths to YES (all remote):**
- **Status-quo resolution:** the creator decides that because no other name has replaced `yeet` by close, it counts as the de facto keyword. This conflicts with the plain meaning of "final" and with the lang team's explicit statement that it won't ship under that name.
- **Lang-team reversal:** the team adopts `yeet`, perhaps half-jokingly, in an RFC accepted before 2026-12-30. No RFC exists, and the deadline is about 6 weeks away.

**Paths to NO:**
- **Default:** nothing is decided by close, and a creator who resolves at the close date picks NO because `yeet` has not been made final.
- **Rename:** an RFC or design decision picks `throw`, `fail`, `raise` or `bail`. This is very unlikely before close.
- **Removal:** the experiment is dropped in favor of `Err(e)?`, `break` from `try` blocks, or macros.

**What these depend on:**
- How the creator handles an undecided outcome (NO vs. N/A vs. extension).
- How much bandwidth the lang team has. Its priorities are the `Try` trait and `try` blocks, which both rank ahead of throw syntax.

## 5. Signposts

- **Toward YES (each very unlikely):**
  - An RFC proposing to keep `yeet` as the final keyword, or a lang-team FCP to do so.
  - A creator comment saying the question will resolve on the status quo at close.
- **Toward NO:**
  - A creator comment that it resolves NO if nothing is final.
  - An RFC using `throw`, `fail` or `raise`.
  - Removal of `yeet_expr`.
  - Lang notes saying yeet is deprioritized.
- **Toward N/A or extension:** the creator signaling they will wait for a final decision.
- **Low impact:** progress on try blocks or the Try trait. These are prerequisites but say nothing about the keyword's name.

## 6. Uncertainties

- **Live GitHub data:** WebFetch was blocked for GitHub, HackMD, Rust docs and forum pages. I could not read the latest comments on #96373 or #96374, or the outcome of MCP #945. Status is inferred from search snippets.
- **Creator intent:** I could not establish how the creator will resolve if no final decision exists by close. This is the main ambiguity.
- **Release dates:** the Rust 1.100 and 1.101 dates are calculated from the cadence, not confirmed.
- **2026 discussion:** I could not confirm whether any 2026 lang-team discussion explicitly addressed the yeet or throw naming, or what the March 2026 Internals thread concluded.

## Sources
- [Tracking Issue for experimental yeet expressions #96373 (GitHub)](https://github.com/rust-lang/rust/issues/96373)
- [Tracking Issue for ops::Yeet #96374 (GitHub)](https://github.com/rust-lang/rust/issues/96374)
- [Add `yeet` experimentally · compiler-team #501](https://github.com/rust-lang/compiler-team/issues/501)
- [Parse unstable keywords for experimental syntax · compiler-team #945](https://github.com/rust-lang/compiler-team/issues/945)
- [Initiative: `?` traits, `try` blocks, `yeet` exprs · lang-team #160](https://github.com/rust-lang/lang-team/issues/160)
- [yeet_expr – The Rust Unstable Book](https://doc.rust-lang.org/unstable-book/language-features/yeet-expr.html)
- [Yeet in std::ops](https://doc.rust-lang.org/std/ops/struct.Yeet.html)
- [rust-project-goals 2026: stabilize-try.md](https://github.com/rust-lang/rust-project-goals/blob/main/src/2026/stabilize-try.md)
- [Stabilize the Try trait · rust-lang/goals #654](https://github.com/rust-lang/goals/issues/654)
- [Tracking Issue for homogeneous try_blocks #154391](https://github.com/rust-lang/rust/issues/154391)
- [Lang Triage meeting 2026-09-30 (HackMD)](https://hackmd.io/@rust-lang-team/SkBcQj5qGg)
- [Lang Triage meeting 2026-08-05 (HackMD)](https://hackmd.io/@rust-lang-team/B1GAEslUMg)
- [Project Goal Feedback 2026 (Lang) (HackMD)](https://hackmd.io/@rust-lang-team/S13LVYk9Ze)
- [T-compiler Meeting Agenda 2026-02-19 (HackMD)](https://hackmd.io/@rust-compiler-team/ByTlyHiDbe)
- [T-compiler Meeting Agenda 2025-12-11 (HackMD)](https://hackmd.io/@rust-compiler-team/B1ouHeJGbg)
- [Why `yeet` in `try` blocks if `break` is good enough? (Rust Internals)](https://internals.rust-lang.org/t/why-yeet-in-try-blocks-if-break-is-good-enough/21552)
- [Please tell me 'yeet' is not a thing in Rust! (Rust Users Forum)](https://users.rust-lang.org/t/please-tell-me-yeet-is-not-a-thing-in-rust/84843)
- [Syntactic Musings on the Fallibility Effect (Yosh Wuyts)](https://blog.yoshuawuyts.com/syntactic-musings-on-the-fallibility-effect/)
- [RFC: `throw` expressions · rfcs #2426](https://github.com/rust-lang/rfcs/pull/2426)
- [RFC 0243 trait-based exception handling](https://rust-lang.github.io/rfcs/0243-trait-based-exception-handling.html)
- [Rust 1.99.1 released (LinuxCompatible)](https://www.linuxcompatible.org/story/rust-1991-released-three-critical-bugs-fixed-in-record-twoweek-turnaround/)
- [Rust Release Notes (Releasebot)](https://releasebot.io/updates/rust)
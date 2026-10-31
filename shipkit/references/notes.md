# Release content

Draft during release preparation so the text is reviewable before a version bump reaches the publishing branch. Start from explicit previous/current source commits, scoped release decisions and the actual feature diffs. Include commits inside merge promotions: `--first-parent --no-merges` on a promotion branch can hide all feature changes. Inspect files and linked acceptance evidence before turning commit titles into claims. Distinguish feature availability, flags, prerequisites and unverified behavior.

Use a shared evidence set with separate authored outputs:

| Output | Content |
| --- | --- |
| GitHub Release | Useful release summary, changes, compatibility and relevant technical context |
| App Store What's New | Concise user-visible benefits and fixes, plain text, no internal implementation chatter |
| TestFlight What to Test | Concrete tester actions and observable expected results; relevant setup and known limitations |
| Web release notes | User-visible changes and meaningful operational/compatibility notes for the project's audience |

Example: What's New: "Find older entries by searching their text." What to Test: "Search for a word in an older entry. Confirm the entry appears and opens correctly; try a word with no matches and confirm the empty state." Only use such claims when the underlying release contains that behavior.

Exclude internal maintenance from store copy unless it has a supported user benefit. Do not describe a fixed bug or passed test without evidence. Keep known limitations distinct from test instructions. Do not promise public availability from a source tag or TestFlight upload. Follow the project's language, locale and tone; never invent translations as approved copy.

Render exact committed text in CI rather than regenerating prose at publication time. Keep channel limits configurable and validate current provider constraints when wiring an integration; fail with an actionable message rather than silently truncating. Preserve separate previews and final text. A technical GitHub body can exceed a store-field limit. Review the release range, scope and rendered output before publishing.

Writing approaches informed by [App Store Changelog](https://github.com/Dimillian/Skills/blob/main/app-store-changelog/SKILL.md) and [TestFlight Release Notes](https://github.com/gannonh/macrokinetic/blob/main/.agents/skills/testflight-release-notes/SKILL.md). These are optional references, not runtime dependencies; do not inherit another app's IDs, scripts, commit filters or publication permissions.

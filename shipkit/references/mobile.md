# Mobile profile

Use this starting mapping when it matches the project; confirm actual distribution mechanisms:

| Environment | Client | Backend | Acceptance |
| --- | --- | --- | --- |
| dev | Local dev server on a phone/dev client | Deployed development API/Worker | Local physical-device checks |
| stage | Preview/internal device build | Staging API/Worker | Installed preview build and device checks |
| main | Production-profile build distributed through TestFlight (iOS) | Production API/Worker | Exact TestFlight build and device checks |

An EAS internal/Preview distribution and an App Store Connect/TestFlight upload are different routes. Discover the actual EAS distribution profile, signing and device registration or TestFlight group. Do not infer a route from the phrase "send to my phone". Adapt Android to its actual internal/closed/production track; do not invent Apple steps for Android.

Record marketing version, build number/versionCode, bundle/package ID, EAS project/account, build profile, API selector, Worker/resource identities and distribution channel. For OTA updates, record runtime compatibility and channel-to-backend mapping. Keep development/staging resources isolated from production and verify authentication and target bindings using existing project checks.

Decide separately which source changes trigger Preview builds, which marketing-version change triggers production builds, and which source commit publishes a GitHub Release. Backend-only deployment, source publication, build, upload, TestFlight text, App Store text, review submission and public-store release each have their own triggers and receipts. Reaching main/TestFlight does not mean public App Store availability.

For Apple metadata operations, default to a dry-run of exact app, platform, locale, version and build where applicable. What's New targets the intended editable store-version locale; What to Test targets the exact processed TestFlight build/locale. Fail on ambiguous app/build selection or non-editable target. Upsert without duplicating locale entries. Store-only metadata need not require an unrelated build number. Keep signing/API keys in secure provider or CI storage, never in config or output.

Before starting another build, inspect existing artifacts for the exact app, platform, source, profile, version/build and processing state. Reuse only a matching eligible artifact; if selection remains ambiguous, stop the dependent action. Installation should record the project-specific lookup, selection and retry commands. Before distributing, verify the artifact's source SHA, version/build and backend environment. Track build completion, upload/processing, tester availability and physical-device acceptance separately. Existing installed binaries may keep talking to an older backend; rollback must account for that compatibility. A replacement binary can require a higher build number and processing, so record realistic recovery rather than promising instant rollback.

<p align="center">
  <img src="./assets/profile-ribbon.png" alt="A flowing multicolored wireframe ribbon on a black background" width="100%" />
</p>

# Bhupesh Cholake

I build AI agents, computational physics tools, and full-stack products.
My work ranges from airfoil-flow solvers to community automation and tools that make software changes easier to verify.

Lately: resumable coding agents, evidence-first research, and practical AI with explicit boundaries between model output and application state.

[Projects](#building-lately) · [Open source](#open-source) · [All repositories](#complete-repository-index) · [Email](mailto:realbhupesh@gmail.com)

## Building lately

| Project | What I'm building |
| --- | --- |
| [Relay](https://github.com/RealBhupesh/harness) | A resumable coding-agent harness with persisted progress, isolated worktrees, bounded usage, and independent verification. In development. |
| [STOCKEX](https://github.com/RealBhupesh/stokex-research-harness-for-your-agents) | Indian-equity research tooling with point-in-time evidence, NSE data import, screening, backtesting, and auditable research bundles. No trade execution. |
| [APAS V3](https://github.com/RealBhupesh/apasaiproject) | A multi-tenant GraphRAG reference implementation with access controls, temporal evidence, claim verification, and audit trails. Uses synthetic demo regulations. |
| [Resend SDK](https://github.com/RealBhupesh/resend-sdk) | Unofficial TypeScript and Python clients generated from OpenAPI, with offline test mode. Package publishing pending. |
| [Parley](https://github.com/RealBhupesh/parley) | A browser extension for exporting Discord conversations to Markdown, CSV, HTML, and PDF. |
| [Asteria](https://github.com/RealBhupesh/Aichatbot) | A hotel guest-assistant demo with deterministic availability, staff-confirmed reservations, and human chat takeover. |
| [CMF Watch AI](https://github.com/RealBhupesh/CMF-WATCH-AI) | BLE protocol research for CMF Watch Pro 2, plus a Python reply engine and proxy. Watch integration is still being validated. |
| [ChangeGraph](https://github.com/RealBhupesh/changegraph) | Developer-infrastructure research into software changes and the evidence needed to ship them. |
| [Indian Shopify Store Discovery](https://github.com/RealBhupesh/indian-shopify-stores) | A discovery pipeline that accepts stores only with Shopify signals and evidence of an Indian operating business. |
| [Personal Website](https://github.com/RealBhupesh/personal-website) | My portfolio, writing, and public GitHub contribution discovery with attribution evidence. |

## More of my work

- **[Bell Agentic Discord Bot](https://github.com/RealBhupesh/Bell-Agentic-Discord-Bot)**: community moderation, AI tools, music, and a virtual economy.
- **[Physicore PCANN](https://github.com/RealBhupesh/physicore-pcann)**: neural airfoil-flow prediction with custom autodiff and physics residuals. Related work: [AeroAssist](https://github.com/RealBhupesh/aeroassist) and the [NACA 4418 CFD kernel](https://github.com/RealBhupesh/naca4418-cfd-kernel).
- **[AI Fitness Coach](https://github.com/RealBhupesh/ai-fitness-coach)**: fitness, dance, and nutrition coaching with real-time pose feedback.
- **[Beacon Uptime](https://github.com/RealBhupesh/beacon-uptime)**: Cloudflare-native monitoring with endpoint checks, browser journeys, incidents, and alerts.
- **[Nestly Homes](https://github.com/RealBhupesh/nestly-homes)**: housing search with maps, tours, messaging, and owner tools.

I work mainly with **Python, TypeScript, JavaScript, and Kotlin**, using React / Next.js, FastAPI / Flask, Cloudflare Workers, and Android tooling where they fit.

## Open source

**32 merged · 29 open · 25 closed without merge**, across **34 upstream repositories**. Checked on **22 October 2026**.

This is a snapshot of 76 authored public upstream PRs plus 10 verified co-authored or credited PRs. Own-repository PRs are excluded. Closed submissions remain visible as part of the history; they are not counted as merged work.

A few merged changes:

| Upstream | Contribution |
| --- | --- |
| Grafana Faro | [Report zero TLS time for non-secure resources (#2308)](https://github.com/grafana/faro-web-sdk/pull/2308) and [preserve signals queued during a batch flush (#2257)](https://github.com/grafana/faro-web-sdk/pull/2257). |
| Cloudflare Workers SDK | [Ignore Wrangler persistence writes in Vite's watcher (#15574)](https://github.com/cloudflare/workers-sdk/pull/15574), [handle dynamic workflow retry delays (#15569)](https://github.com/cloudflare/workers-sdk/pull/15569), and [recover from loopback bind failures (#15485)](https://github.com/cloudflare/workers-sdk/pull/15485). |
| NanoCoder | [Restore ACP provider discovery (#830)](https://github.com/Nano-Collective/nanocoder/pull/830), [bound tool-result context (#798)](https://github.com/Nano-Collective/nanocoder/pull/798), and [preserve multibyte terminal input (#744)](https://github.com/Nano-Collective/nanocoder/pull/744). |
| Prompt Scrubber | [Avoid treating numbered prose as a postal address (#156)](https://github.com/Nano-Collective/prompt-scrubber/pull/156). |
| NestJS | [Set an explicit rootDir in generated application configuration (#2435)](https://github.com/nestjs/schematics/pull/2435). |
| Sentry | [Stop tagging DOMException.code on browser events (#23992)](https://github.com/getsentry/sentry-javascript/pull/23992). |
| Gumroad | Co-authored [provider-specific blast retries (#6904)](https://github.com/antiwork/gumroad/pull/6904), [logging and redirect hardening (#6932)](https://github.com/antiwork/gumroad/pull/6932), and [subscription magic-link preservation (#7124)](https://github.com/antiwork/gumroad/pull/7124). |

<details>
<summary><strong>23 authored PRs: merged</strong></summary>

| Repository / PR | Change |
| --- | --- |
| [grafana/faro-web-sdk #2308](https://github.com/grafana/faro-web-sdk/pull/2308) | fix(web-sdk): report zero TLS time for non-secure resources |
| [Nano-Collective/prompt-scrubber #156](https://github.com/Nano-Collective/prompt-scrubber/pull/156) | fix: do not flag numbered prose as a postal address |
| [Nano-Collective/nanocoder #743](https://github.com/Nano-Collective/nanocoder/pull/743) | docs: add local-first memory MCP recipe |
| [makeplane/plane #9804](https://github.com/makeplane/plane/pull/9804) | fix(web): show sub-work items on the parent in local |
| [grafana/faro-web-sdk #2257](https://github.com/grafana/faro-web-sdk/pull/2257) | fix(core): do not drop signals added during BatchExecutor flush |
| [nestjs/schematics #2435](https://github.com/nestjs/schematics/pull/2435) | fix(application): set explicit rootDir in generated tsconfig |
| [cloudflare/workers-sdk #15574](https://github.com/cloudflare/workers-sdk/pull/15574) | [vite-plugin] Ignore .wrangler persistence writes in Vite's file watcher |
| [cloudflare/workers-sdk #15569](https://github.com/cloudflare/workers-sdk/pull/15569) | [wrangler] Handle dynamic retry delays in workflows instances describe |
| [cloudflare/workers-sdk #15485](https://github.com/cloudflare/workers-sdk/pull/15485) | fix(miniflare): reject loopback bind failures during startup |
| [getsentry/sentry-javascript #23992](https://github.com/getsentry/sentry-javascript/pull/23992) | fix(browser)!: stop tagging DOMException.code on events |
| [Nano-Collective/nanocoder #785](https://github.com/Nano-Collective/nanocoder/pull/785) | fix: summarize oversized git diffs |
| [Nano-Collective/nanocoder #786](https://github.com/Nano-Collective/nanocoder/pull/786) | fix: cap oversized tool results |
| [Nano-Collective/nanocoder #782](https://github.com/Nano-Collective/nanocoder/pull/782) | fix: preview very large files before ranged reads |
| [Nano-Collective/nanocoder #830](https://github.com/Nano-Collective/nanocoder/pull/830) | fix: restore ACP provider discovery |
| [Nano-Collective/nanocoder #820](https://github.com/Nano-Collective/nanocoder/pull/820) | fix: normalize Atlas Cloud GPT-5.6 model IDs |
| [Nano-Collective/nanocoder #798](https://github.com/Nano-Collective/nanocoder/pull/798) | fix: bound diff_edit result context |
| [Nano-Collective/nanocoder #784](https://github.com/Nano-Collective/nanocoder/pull/784) | fix: bound string_replace result context |
| [Nano-Collective/nanocoder #744](https://github.com/Nano-Collective/nanocoder/pull/744) | fix: preserve multibyte input in alternate-screen TUI |
| [Nano-Collective/nanocoder #742](https://github.com/Nano-Collective/nanocoder/pull/742) | Fix wide terminal content width |
| [Nano-Collective/organisation #85](https://github.com/Nano-Collective/organisation/pull/85) | Add Bhupesh Cholake to contributors |
| [Nano-Collective/nanocoder #741](https://github.com/Nano-Collective/nanocoder/pull/741) | Fix update checks, cache presence, and network error classification |
| [lokus-ai/lokus #439](https://github.com/lokus-ai/lokus/pull/439) | Feature/txt support |
| [firstcontributions/first-contributions #114183](https://github.com/firstcontributions/first-contributions/pull/114183) | Add Bhupesh Cholake to Contributors list |

</details>

<details>
<summary><strong>29 authored PRs: open</strong></summary>

| Repository / PR | Change |
| --- | --- |
| [grafana/faro-web-sdk #2307](https://github.com/grafana/faro-web-sdk/pull/2307) | fix(core): keep setSession payload overrides when options are set |
| [BerriAI/litellm #39077](https://github.com/BerriAI/litellm/pull/39077) | fix(vertex): send audio/webm for Gemini transcription of webm |
| [grafana/faro-web-sdk #2258](https://github.com/grafana/faro-web-sdk/pull/2258) | fix(web-sdk): coalesce session rotation on collector invalidation |
| [Nano-Collective/nanocoder #1448](https://github.com/Nano-Collective/nanocoder/pull/1448) | fix: keep the selected file suggestion visible |
| [Nano-Collective/nanocoder #1447](https://github.com/Nano-Collective/nanocoder/pull/1447) | fix: only ellipsize truncated subagent tool results |
| [Nano-Collective/nanocoder #1446](https://github.com/Nano-Collective/nanocoder/pull/1446) | fix: submit an exact slash command on the first Enter |
| [neugence/whipscribe-buildathon #89](https://github.com/neugence/whipscribe-buildathon/pull/89) | Track 0: Bhupesh Cholake - Track Record |
| [makeplane/plane #9821](https://github.com/makeplane/plane/pull/9821) | fix(aio): honor CORS_ALLOWED_ORIGINS instead of overwriting it |
| [makeplane/plane #9819](https://github.com/makeplane/plane/pull/9819) | fix(web): relayout stickies masonry after refresh |
| [makeplane/plane #9820](https://github.com/makeplane/plane/pull/9820) | fix(web): drop deleted workflow states on refetch |
| [makeplane/plane #9818](https://github.com/makeplane/plane/pull/9818) | fix(aio): create supervisor log directories on boot |
| [llvm/llvm-project #214765](https://github.com/llvm/llvm-project/pull/214765) | [TargetParser] Recognize legacy GNU/Hurd triples |
| [makeplane/plane #9803](https://github.com/makeplane/plane/pull/9803) | fix(web): hide work item IDs when Display → IDs is off |
| [dagster-io/dagster #34166](https://github.com/dagster-io/dagster/pull/34166) | fix(dagster-dbt): error on colliding dbt test names at definition time |
| [nextauthjs/next-auth #13492](https://github.com/nextauthjs/next-auth/pull/13492) | fix(next-auth): do not assume x-forwarded-proto on server actions |
| [clerk/javascript #9629](https://github.com/clerk/javascript/pull/9629) | fix(clerk-js): keep SignIn identity after resetSignIn |
| [inngest/inngest-js #1720](https://github.com/inngest/inngest-js/pull/1720) | Cursor/fix middleware sentry sampled fae4 |
| [openmrs/openmrs-core #6409](https://github.com/openmrs/openmrs-core/pull/6409) | Harden UUID reference and updater authorization boundaries |
| [python/cpython #155343](https://github.com/python/cpython/pull/155343) | gh-155321: Avoid Python.h POSIX macro redefinition |
| [python/cpython #155342](https://github.com/python/cpython/pull/155342) | gh-155286: Write a valid empty zstd archive |
| [react/react-native #57791](https://github.com/react/react-native/pull/57791) (draft) | [iOS][Fabric] Reset keyboard inset state when recycling ScrollViews |
| [dodopayments/billingsdk #382](https://github.com/dodopayments/billingsdk/pull/382) (draft) | fix: persist sidebar state and remove interaction logs |
| [react/react-native #57788](https://github.com/react/react-native/pull/57788) | Fix Image.getSize for Android data URIs |
| [microsoft/aspire #18939](https://github.com/microsoft/aspire/pull/18939) | Allow assigning parent account roles to Foundry project identities |
| [microsoft/aspire #18941](https://github.com/microsoft/aspire/pull/18941) (draft) | Preserve unique suffixes in App Service site names |
| [microsoft/aspire #18942](https://github.com/microsoft/aspire/pull/18942) (draft) | Allow descriptions on connection string parameters |
| [cofeed-19/cofeed-19.github.io #99](https://github.com/cofeed-19/cofeed-19.github.io/pull/99) | Fix: limit unvisited feed items with native details collapse (closes #28) |
| [makkorjamal/PLSduino #3](https://github.com/makkorjamal/PLSduino/pull/3) | Add SD-loaded data and pretrained model support |
| [GaneshByte1/wastex-ai-management-platform #1](https://github.com/GaneshByte1/wastex-ai-management-platform/pull/1) | feat: Comprehensive production-level development |

</details>

<details>
<summary><strong>24 authored PRs: closed without merge</strong></summary>

| Repository / PR | Change |
| --- | --- |
| [Nano-Collective/nanocoder #1445](https://github.com/Nano-Collective/nanocoder/pull/1445) | fix: do not offer to clear an empty composer |
| [arc53/DocsGPT #2353](https://github.com/arc53/DocsGPT/pull/2353) | feat: page-aware sources + numbered RAG citations (#2106) |
| [airbytehq/airbyte #83317](https://github.com/airbytehq/airbyte/pull/83317) | fix(source-vitally): mark the secret token as sensitive |
| [airbytehq/airbyte #83319](https://github.com/airbytehq/airbyte/pull/83319) | feat(source-github): support wildcard repositories for users |
| [cloudflare/workers-sdk #15799](https://github.com/cloudflare/workers-sdk/pull/15799) | [miniflare] Keep Hyperdrive client socket errors from crashing local dev |
| [cloudflare/workers-sdk #15798](https://github.com/cloudflare/workers-sdk/pull/15798) | [wrangler] Fall back to per-zone routes when a 403 omits code 10000 |
| [makeplane/plane #9805](https://github.com/makeplane/plane/pull/9805) | fix(api): decode HTML entities in plain-text email bodies |
| [hatchet-dev/hatchet #4867](https://github.com/hatchet-dev/hatchet/pull/4867) | fix(sdks/ts): recover from inactive listener stream on heartbeat rejection |
| [Nano-Collective/prompt-scrubber #78](https://github.com/Nano-Collective/prompt-scrubber/pull/78) (draft) | Add n8n workflow integration |
| [airbytehq/airbyte #83318](https://github.com/airbytehq/airbyte/pull/83318) | fix(source-google-analytics-data-api): fix offset pagination |
| [oliexdev/openScale #1440](https://github.com/oliexdev/openScale/pull/1440) (draft) | Add Lenovo HS10 and Dr.Trust SSW526 support |
| [python/cpython #155341](https://github.com/python/cpython/pull/155341) | gh-155305: Preserve user-provided sockets on transport errors |
| [Nano-Collective/nanocoder #836](https://github.com/Nano-Collective/nanocoder/pull/836) | fix: normalize Copilot reasoning stream IDs |
| [react/react-native #57790](https://github.com/react/react-native/pull/57790) | Fix iOS Codegen fallback for libraries without an iOS config |
| [react/react-native #57789](https://github.com/react/react-native/pull/57789) | Treat NaN border widths as unset |
| [triggerdotdev/trigger.dev #4473](https://github.com/triggerdotdev/trigger.dev/pull/4473) (draft) | docs(cli): clarify dev env-file propagation |
| [triggerdotdev/trigger.dev #4472](https://github.com/triggerdotdev/trigger.dev/pull/4472) (draft) | fix(cli): redact env vars from attempt debug logs |
| [triggerdotdev/trigger.dev #4471](https://github.com/triggerdotdev/trigger.dev/pull/4471) (draft) | perf(supervisor): inspect Docker resources concurrently |
| [triggerdotdev/trigger.dev #4474](https://github.com/triggerdotdev/trigger.dev/pull/4474) (draft) | fix(build): support Playwright 1.58+ browser metadata |
| [open-webui/open-webui #25770](https://github.com/open-webui/open-webui/pull/25770) | Codex/fix loguru secret tracebacks |
| [open-webui/open-webui #25769](https://github.com/open-webui/open-webui/pull/25769) (draft) | fix: prevent secrets in Loguru tracebacks |
| [servo/servo #43601](https://github.com/servo/servo/pull/43601) | docs(script_bindings): document Bindings.conf configuration and descriptor schema |
| [oppia/oppia #25525](https://github.com/oppia/oppia/pull/25525) | add feedback thread subject length validation |
| [oppia/oppia #25524](https://github.com/oppia/oppia/pull/25524) | add feedback thread subject length validation |

</details>

<details>
<summary><strong>10 co-authored or credited PRs, with attribution evidence</strong></summary>

Credit is verified against public commit trailers or explicit maintainer attribution. These PRs are separate from the authored lists above.

| Repository / PR | Change | Status / credit |
| --- | --- | --- |
| [makeplane/plane #9841](https://github.com/makeplane/plane/pull/9841) | fix(api): decode HTML entities in plain-text email bodies | Merged; [Maintainer credit](https://github.com/makeplane/plane/pull/9805) |
| [Nano-Collective/nanocoder #817](https://github.com/Nano-Collective/nanocoder/pull/817) | Added visual loading indicator for vscode extension | Merged; [Co-author trailer](https://github.com/Nano-Collective/nanocoder/commit/cfec1a842cfdba4106e2c12070ea0bd62f78b829) |
| [antiwork/gumroad #7124](https://github.com/antiwork/gumroad/pull/7124) | Preserve subscription magic links on invalid requests | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/0ebee4240a4dd964e70e2cf8bb61f9ffbea30502) |
| [antiwork/gumroad #6831](https://github.com/antiwork/gumroad/pull/6831) | Port sales tax calculator spec to Minitest (#5801) | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/117824881e4c93bbae87ef53121eed612c58de38) |
| [antiwork/gumroad #6904](https://github.com/antiwork/gumroad/pull/6904) | Split blast retries by provider | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/29ea1c451f57c21dfd84c6bf429f8312d6356db1) |
| [antiwork/gumroad #6930](https://github.com/antiwork/gumroad/pull/6930) | Port the SidekiqUtility spec to Minitest (#5801) | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/58b75e62c4b55efa2f0ba1e15c08c4f165095e35) |
| [antiwork/gumroad #6932](https://github.com/antiwork/gumroad/pull/6932) | Harden sensitive logging and bundle redirects | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/834652c9c4d644a986783830103e63886353c759) |
| [antiwork/gumroad #6912](https://github.com/antiwork/gumroad/pull/6912) | Clear stale accepted cross-sell offer on cart update | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/88d43f0d71b23d4cdb46a7c77bdc96d9e2e6747c) |
| [antiwork/gumroad #6830](https://github.com/antiwork/gumroad/pull/6830) | Port the sales tax calculator spec to Minitest and fixtures | Closed without merge; [Co-author trailer](https://github.com/antiwork/gumroad/commit/9eb91690da2f3dd68537d2c2f4f8230d761553e5) |
| [antiwork/gumroad #6609](https://github.com/antiwork/gumroad/pull/6609) | Port the price checker service spec to Minitest and fixtures | Merged; [Co-author trailer](https://github.com/antiwork/gumroad/commit/a57d24a819083d76198e64aa13eecb2dc2946f8f) |

</details>

[Browse my pull requests](https://github.com/pulls?q=is%3Apr+author%3ARealBhupesh) · [Contribution calendar and activity](https://github.com/RealBhupesh?tab=overview)

## GitHub activity

![Bhupesh's GitHub contribution graph](https://gitlyy.vercel.app/api/contribution?username=RealBhupesh&hide_border=true)

## Complete repository index

**123 public repositories: 78 project repositories and 45 forks.** Checked on **22 October 2026**. Both lists are alphabetical and include experiments and empty repositories, labelled where applicable.

The project list uses GitHub's non-fork classification; it also contains demos, studies, and this profile repository. Forks are listed separately and do not, by themselves, imply a contribution to the upstream project.

<details>
<summary><strong>78 project repositories (not forks)</strong></summary>

| Repository | What it contains |
| --- | --- |
| [aeroassist](https://github.com/RealBhupesh/aeroassist) | Local aerodynamic analysis, mini-CFD solving, and interactive 3D visualization. |
| [agripulse](https://github.com/RealBhupesh/agripulse) | Agriculture platform exploring IoT, drones, water management, and distribution. |
| [ai-fitness-coach](https://github.com/RealBhupesh/ai-fitness-coach) | AI fitness, dance, and nutrition coaching with real-time pose feedback. |
| [Aichatbot](https://github.com/RealBhupesh/Aichatbot) | Asteria: fictional hotel guest-assistant demo with deterministic availability, staff-confirmed bookings, and human chat takeover. |
| [aidcbot](https://github.com/RealBhupesh/aidcbot) | Empty repository reserved for a Discord-bot experiment. |
| [anthra-agency-website](https://github.com/RealBhupesh/anthra-agency-website) | Interactive Next.js site for Anthra digital agency services. |
| [anthra-ai-whiteboard](https://github.com/RealBhupesh/anthra-ai-whiteboard) | AI collaborative whiteboard that structures free-form brainstorming. |
| [anthra-voting](https://github.com/RealBhupesh/anthra-voting) | Voting platform with secure participation, live analytics, and administration. |
| [anushka-career-navigator](https://github.com/RealBhupesh/anushka-career-navigator) | Flask career-navigation demo with profiles, resumes, jobs, and interviews. |
| [apasaiproject](https://github.com/RealBhupesh/apasaiproject) | APAS V3: multi-tenant GraphRAG reference implementation with authorization, temporal evidence, claim checks, and audit trails. Synthetic demo regulations. |
| [beacon-uptime](https://github.com/RealBhupesh/beacon-uptime) | Cloudflare-native uptime monitoring with endpoint checks, browser journeys, and alerts. |
| [Bell-Agentic-Discord-Bot](https://github.com/RealBhupesh/Bell-Agentic-Discord-Bot) | Discord moderation, AI utilities, music, community tools, and a virtual economy. |
| [binix-it-services](https://github.com/RealBhupesh/binix-it-services) | Marketing website for IT services and digital transformation. |
| [blahblah](https://github.com/RealBhupesh/blahblah) | One-commit scratch repository retained for history. |
| [book-it-doctor-appointments](https://github.com/RealBhupesh/book-it-doctor-appointments) | Flask application for doctor discovery and appointment scheduling. |
| [career-ai-platform](https://github.com/RealBhupesh/career-ai-platform) | AI career guidance with resume analysis, interviews, and job matching. |
| [changegraph](https://github.com/RealBhupesh/changegraph) | Research-driven developer infrastructure for understanding software changes and the evidence needed to ship them. |
| [CMF-WATCH-AI](https://github.com/RealBhupesh/CMF-WATCH-AI) | CMF Watch Pro 2 BLE research, Python reply engine, and backend proxy. Watch integration remains at the protocol-validation stage. |
| [collegeProjectRepo](https://github.com/RealBhupesh/collegeProjectRepo) | College-project monorepo containing separate mobile and web applications. |
| [couples-companion-app](https://github.com/RealBhupesh/couples-companion-app) | React Native app for shared memories, goals, planning, and activities. |
| [creators-clash](https://github.com/RealBhupesh/creators-clash) | Android creator-collaboration app with discovery, messaging, and projects. |
| [credit-card-celebration](https://github.com/RealBhupesh/credit-card-celebration) | Playful single-page celebration interface for a first credit-card milestone. |
| [daily-planner](https://github.com/RealBhupesh/daily-planner) | Daily planning and task-management interface with Python utilities. |
| [digital-marketing-site](https://github.com/RealBhupesh/digital-marketing-site) | React marketing website for strategy, services, and lead generation. |
| [digital-marketing-terminal](https://github.com/RealBhupesh/digital-marketing-terminal) | Marketing site with an interactive terminal-style business experience. |
| [experiment1-website](https://github.com/RealBhupesh/experiment1-website) | Static website mirror retained as an early web experiment. |
| [fitnessapp](https://github.com/RealBhupesh/fitnessapp) | Kotlin Android fitness application developed as a FitForge concept. |
| [focus-timer](https://github.com/RealBhupesh/focus-timer) | Advanced Pomodoro timer with themes, statistics, and productivity controls. |
| [folio-whiteboard-study](https://github.com/RealBhupesh/folio-whiteboard-study) | Study and adaptation of the Folio infinite whiteboard. |
| [gayatri-gallery-shop](https://github.com/RealBhupesh/gayatri-gallery-shop) | Responsive gallery and shop website with project showcases and visual portfolio content. |
| [gift4corp-admin-dashboard](https://github.com/RealBhupesh/gift4corp-admin-dashboard) | Administrative dashboard for managing the Gift4Corp platform and its operational workflows. |
| [githubrepo2](https://github.com/RealBhupesh/githubrepo2) | Empty experimental repository. |
| [githubrepo3](https://github.com/RealBhupesh/githubrepo3) | Empty experimental repository. |
| [githubrepo4](https://github.com/RealBhupesh/githubrepo4) | Empty experimental repository. |
| [harness](https://github.com/RealBhupesh/harness) | Relay: resumable autonomous coding-agent harness with checkpoints, worktrees, usage limits, and independent verification. In development. |
| [hospital-iq](https://github.com/RealBhupesh/hospital-iq) | AI-assisted hospital triage, doctor assignment, and clinical workflow management. |
| [indian-shopify-stores](https://github.com/RealBhupesh/indian-shopify-stores) | Store-discovery pipeline that requires Shopify signals and Indian operating-business evidence before accepting a result. |
| [infinite-cats](https://github.com/RealBhupesh/infinite-cats) | Playful single-page website dedicated to an endless stream of cats. |
| [internship-polling-system](https://github.com/RealBhupesh/internship-polling-system) | Internship polling exercise using JavaScript, JSX, and C++ components. |
| [maharashtra-trade-hub](https://github.com/RealBhupesh/maharashtra-trade-hub) | Trade portal connecting Maharashtra businesses with global opportunities. |
| [maiee-sarees-platform](https://github.com/RealBhupesh/maiee-sarees-platform) | Full-stack e-commerce platform for artisanal sarees with catalog, cart, checkout, order tracking, and administration. |
| [multi-currency-converter-pro](https://github.com/RealBhupesh/multi-currency-converter-pro) | TypeScript application for converting and comparing multiple currencies. |
| [naca4418-cfd-kernel](https://github.com/RealBhupesh/naca4418-cfd-kernel) | Standalone finite-volume RANS CFD kernel for a NACA 4418 airfoil. |
| [NeoCity](https://github.com/RealBhupesh/NeoCity) | Empty experimental repository. |
| [nestly-homes](https://github.com/RealBhupesh/nestly-homes) | AI-assisted housing marketplace with natural-language search, maps, tours, messaging, and owner tools. |
| [new-website-checking](https://github.com/RealBhupesh/new-website-checking) | HTTrack website mirror retained for frontend study. |
| [novapulse-platform](https://github.com/RealBhupesh/novapulse-platform) | Full-stack platform with auth, dashboards, administration, and realtime collaboration. |
| [parley](https://github.com/RealBhupesh/parley) | Browser extension exporting Discord conversations as Markdown, CSV, HTML, or PDF. |
| [personal-website](https://github.com/RealBhupesh/personal-website) | Personal portfolio with projects, writing, and evidence-backed public GitHub contribution discovery. |
| [personal-website-using-opus](https://github.com/RealBhupesh/personal-website-using-opus) | Empty repository reserved for a personal-site experiment. |
| [php-mini-projects](https://github.com/RealBhupesh/php-mini-projects) | PHP trackers, calculators, registration flows, and inventory exercises. |
| [physicore-pcann](https://github.com/RealBhupesh/physicore-pcann) | Physics-controlled neural network for 2D airfoil flow with custom autodiff and CFD export. |
| [physicore-website](https://github.com/RealBhupesh/physicore-website) | Marketing site for the Physicore deterministic physics-engine work. |
| [pollify](https://github.com/RealBhupesh/pollify) | Room-code polling with creation, sharing, participation, and live results. |
| [Pollify_Polling_System](https://github.com/RealBhupesh/Pollify_Polling_System) | Empty repository reserved for an earlier Pollify implementation. |
| [portfolio-site-study](https://github.com/RealBhupesh/portfolio-site-study) | Portfolio study adapted from a freeCodeCamp project. |
| [python-security-mini-projects](https://github.com/RealBhupesh/python-security-mini-projects) | Password-strength and text-encryption mini-projects in Python. |
| [Realbhupesh](https://github.com/RealBhupesh/Realbhupesh) | This GitHub profile README and its visual assets. |
| [resend-sdk](https://github.com/RealBhupesh/resend-sdk) | Unofficial TypeScript and Python SDKs generated from the Resend OpenAPI specification, with offline test mode. Package publishing pending. |
| [secure-login-system](https://github.com/RealBhupesh/secure-login-system) | Node.js, Express, and MySQL authentication workflow. |
| [shield-grow-website](https://github.com/RealBhupesh/shield-grow-website) | React website for the Shield Grow brand and its services. |
| [single-file-todo-app](https://github.com/RealBhupesh/single-file-todo-app) | Compact to-do application implemented in one HTML file. |
| [Spa4Car](https://github.com/RealBhupesh/Spa4Car) | Static website concept for automotive care and detailing services. |
| [stokex-research-harness-for-your-agents](https://github.com/RealBhupesh/stokex-research-harness-for-your-agents) | STOCKEX: Python research harness with point-in-time evidence, NSE data import, screening, backtesting, and research validation. No trade execution. |
| [sweetcrumb-bakery](https://github.com/RealBhupesh/sweetcrumb-bakery) | Bakery commerce site with catalog, inquiries, ordering, and newsletter flows. |
| [tempo-timer](https://github.com/RealBhupesh/tempo-timer) | Minimal browser-based timer called Tempo. |
| [testingWebsite](https://github.com/RealBhupesh/testingWebsite) | Web testing and frontend experiments. |
| [to-do-list](https://github.com/RealBhupesh/to-do-list) | Empty repository reserved for an early to-do-list exercise. |
| [untilrich](https://github.com/RealBhupesh/untilrich) | Personal milestone page titled Until Bhupesh Becomes Rich. |
| [valora-agentic-bot](https://github.com/RealBhupesh/valora-agentic-bot) | Discord community-operations agent with specialist subagents and approval gates. |
| [vanilla-js-todo](https://github.com/RealBhupesh/vanilla-js-todo) | Minimal to-do application built with vanilla web technologies. |
| [vedant-bank-demo](https://github.com/RealBhupesh/vedant-bank-demo) | Online banking interface covering accounts, transfers, cards, and statements. |
| [vidhyasarthi-quiz](https://github.com/RealBhupesh/vidhyasarthi-quiz) | Quiz application created for the Vidhyasarthi learning experience. |
| [vmedulife-feedback-autofill](https://github.com/RealBhupesh/vmedulife-feedback-autofill) | Brave extension for autofilling repetitive Vmedulife student feedback forms. |
| [waitlist-for-anthra](https://github.com/RealBhupesh/waitlist-for-anthra) | Empty repository reserved for an Anthra waitlist. |
| [website](https://github.com/RealBhupesh/website) | Empty repository reserved for an early website. |
| [year-progress-clock](https://github.com/RealBhupesh/year-progress-clock) | Visual clock showing how much of the current year has elapsed. |
| [your-campus-merch](https://github.com/RealBhupesh/your-campus-merch) | React and Vite storefront experience for discovering and buying campus merchandise. |

</details>

<details>
<summary><strong>45 forks and upstream explorations</strong></summary>

| Repository | Upstream project / purpose |
| --- | --- |
| [airbyte](https://github.com/RealBhupesh/airbyte) | Airbyte data integration and movement platform. |
| [App](https://github.com/RealBhupesh/App) | Expensify financial-collaboration application. |
| [aspire](https://github.com/RealBhupesh/aspire) | Aspire application development and deployment tooling. |
| [billingsdk](https://github.com/RealBhupesh/billingsdk) | Billing and monetization UI components. |
| [cofeed-19.github.io](https://github.com/RealBhupesh/cofeed-19.github.io) | A private, client-only feed reader with no accounts or tracking. |
| [core](https://github.com/RealBhupesh/core) | Home Assistant automation platform. |
| [cpython](https://github.com/RealBhupesh/cpython) | Python language implementation. |
| [dagster](https://github.com/RealBhupesh/dagster) | Dagster data orchestration platform. |
| [DocsGPT](https://github.com/RealBhupesh/DocsGPT) | Document analysis, agent building, enterprise search, and multi-model workflows. |
| [facebook-clone](https://github.com/RealBhupesh/facebook-clone) | Responsive React and Firebase implementation of login and posting flows. |
| [faro-web-sdk](https://github.com/RealBhupesh/faro-web-sdk) | Grafana Faro browser observability SDK. |
| [first-contributions](https://github.com/RealBhupesh/first-contributions) | The open-source contribution process for first-time contributors. |
| [flexifit-ai](https://github.com/RealBhupesh/flexifit-ai) | Fitness-product fork; currently no committed project content. |
| [Gift4corp](https://github.com/RealBhupesh/Gift4corp) | Gift4Corp storefront fork. |
| [Gift4corpAdmin](https://github.com/RealBhupesh/Gift4corpAdmin) | Gift4Corp administration-interface fork. |
| [gumroad](https://github.com/RealBhupesh/gumroad) | Gumroad commerce platform. |
| [hatchet](https://github.com/RealBhupesh/hatchet) | Hatchet background-task and workflow orchestration. |
| [inngest-js](https://github.com/RealBhupesh/inngest-js) | Inngest TypeScript and JavaScript workflow SDK. |
| [javascript](https://github.com/RealBhupesh/javascript) | Clerk JavaScript authentication SDKs. |
| [kalshi-genai-trading-bot](https://github.com/RealBhupesh/kalshi-genai-trading-bot) | Generative-AI experimentation for prediction-market trading. |
| [litellm](https://github.com/RealBhupesh/litellm) | LiteLLM gateway for multiple language-model providers. |
| [llvm-project](https://github.com/RealBhupesh/llvm-project) | LLVM compiler and toolchain infrastructure. |
| [lokus](https://github.com/RealBhupesh/lokus) | Modern note-taking architecture and rich editing workflows. |
| [nanocoder](https://github.com/RealBhupesh/nanocoder) | NanoCoder terminal coding agent. |
| [next-auth](https://github.com/RealBhupesh/next-auth) | Auth.js / NextAuth authentication library. |
| [open-webui](https://github.com/RealBhupesh/open-webui) | Self-hosted interface patterns for local and hosted language models. |
| [opencode](https://github.com/RealBhupesh/opencode) | OpenCode coding agent. |
| [openmrs-core](https://github.com/RealBhupesh/openmrs-core) | OpenMRS API and application core. |
| [openScale](https://github.com/RealBhupesh/openScale) | Bluetooth weight and body-metrics tracking. |
| [oppia](https://github.com/RealBhupesh/oppia) | Open-source educational platform architecture and contribution workflow. |
| [organisation](https://github.com/RealBhupesh/organisation) | Nano Collective website and community discussions. |
| [plane](https://github.com/RealBhupesh/plane) | Plane project-management platform. |
| [PLSduino](https://github.com/RealBhupesh/PLSduino) | Partial Least Squares modeling for Arduino and ESP32 hardware. |
| [prompt-scrubber](https://github.com/RealBhupesh/prompt-scrubber) | Local-first prompt redaction and response rehydration. |
| [react-native](https://github.com/RealBhupesh/react-native) | React Native application framework. |
| [schematics](https://github.com/RealBhupesh/schematics) | NestJS application and component generators. |
| [sentry-javascript](https://github.com/RealBhupesh/sentry-javascript) | Sentry JavaScript SDKs. |
| [servo](https://github.com/RealBhupesh/servo) | Embeddable browser-engine architecture and high-performance web rendering. |
| [t3code](https://github.com/RealBhupesh/t3code) | Fork of the T3 Code project. |
| [trigger.dev](https://github.com/RealBhupesh/trigger.dev) | Trigger.dev background jobs and workflow platform. |
| [twitter-clone](https://github.com/RealBhupesh/twitter-clone) | Social-feed interface and interaction study based on X/Twitter. |
| [wastex-ai-management-platform](https://github.com/RealBhupesh/wastex-ai-management-platform) | AI-assisted waste-management platform concept. |
| [whipscribe-buildathon](https://github.com/RealBhupesh/whipscribe-buildathon) | WhipScribe public UI and desktop-recorder challenge. |
| [workers-sdk](https://github.com/RealBhupesh/workers-sdk) | Cloudflare Workers tooling, including Wrangler and Miniflare. |
| [x-algorithm](https://github.com/RealBhupesh/x-algorithm) | The open-source recommendation algorithm behind X’s For You feed. |

</details>

## Connect

[GitHub](https://github.com/RealBhupesh) · [Email](mailto:realbhupesh@gmail.com)

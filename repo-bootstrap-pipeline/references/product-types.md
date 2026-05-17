# Product Types

Use this reference after inspecting the repo. Infer first, ask only when unclear.

## Primary Split

- **Repo-hidden product**: users do not need the repo to use the product. Examples: hosted web apps, mobile apps, normal desktop GUI apps, consumer AI assistants. Keep usage docs lighter unless developers/operators need them.
- **Repo-facing product**: users may use a terminal, API, SDK, self-hosted install, local config, or code repo. Examples: CLI, API, SDK, automation tools, coding agents, local-first tools. Require install, config, usage, examples, and validation docs.
- **Hybrid product**: has a UI but still needs operator/dev setup. Examples: desktop apps with install, self-hosted web apps, local AI assistants. Cover both product behavior and setup.

## Types

### web-app

Signals: `next.config.*`, `vite.config.*`, `app/`, `pages/`, `src/routes`, web framework packages.

Docs: root README with setup, env, dev server, build, test, deploy notes. `DESIGN.md` required if UI exists. i18n should be detected from locale folders, translation files, or i18n libraries.

### mobile-app

Signals: React Native, Expo, Swift/iOS, Android/Kotlin, Flutter.

Docs: README with platform setup, simulator/device run commands, env, build/release notes. `DESIGN.md` required. Mention app store/deployment flow if present.

### desktop-app

Signals: Electron, Tauri, SwiftUI/macOS, WinUI, WPF, Avalonia, Qt, JavaFX.

Docs: README with install/run/build/package steps. `DESIGN.md` required for GUI apps. Treat CLI-only desktop tools as `cli`.

### cli

Signals: command parser packages, console entry points, `bin`, `click`, `typer`, `commander`, `System.CommandLine`.

Docs: README must include install, commands, options, examples, config/env, exit/error behavior if relevant. `DESIGN.md` not required unless there is TUI/GUI.

### api

Signals: server framework, routes/controllers, OpenAPI, RPC, service ports.

Docs: README must include setup, env, run/test, API usage, auth, local examples. Add API docs standard if OpenAPI/Swagger/etc. exists or should exist.

### library-sdk

Signals: exported packages, public API surface, package publishing config.

Docs: README must include install, import/use examples, versioning, compatibility, public API docs. Generated docs may be TypeDoc, JavaDoc, XML docs, DocFX, or similar.

### ai-assistant

Signals: prompts, tools, agent runtime, chat UI, model/provider config.

Docs: README covers setup, env, model/provider config, tool permissions, usage. PRODUCT covers user goals, safety boundaries, and success criteria.

### coding-agent

Signals: agent skills, coding workflows, repo automation, MCP/tools integration.

Docs: README covers setup and execution. AGENTS.md and local skills are central. Include permissions, repo routing, validation, and git workflow rules.

### automation-script

Signals: scripts folder, cron/scheduler config, one-off automation, shell/Python/Node scripts.

Docs: README covers purpose, inputs, outputs, scheduling, config, dry-run/safety behavior, validation.

### monorepo

Signals: `apps/`, `packages/`, workspaces, Turborepo, Nx, pnpm/yarn/npm workspaces, multiple services.

Docs: root README explains the whole repo. Root AGENTS.md routes agents by app/package. Each app/package gets a tiny local README only when it has independent setup, commands, env vars, deployment, usage, or ownership rules.

## Optional Capabilities

Detect and document these when present or confirmed:

- i18n/localization: supported locales, copy ownership, translation paths, validation commands, and no-hardcoded-user-facing-text rules.
- Generated docs: JavaDoc, XML docs, TypeDoc, DocFX, OpenAPI, Swagger, or similar.
- CI/CD: workflow files, required checks, deploy flow.
- Pull request templates: `.github/pull_request_template.md`, `.github/PULL_REQUEST_TEMPLATE/*`, or platform equivalent. Review the template when present and route PR body drafting through it.
- Lint/format/test/typecheck: real commands only.
- Schema validation: current library/tool if present; recommend the need generically if absent.
- ORM/migrations: migration location, generation/apply commands, rollback rules if known.
- Env/config: `.env.example`, compose files, deployment env, code reading env vars.

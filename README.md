# Skills

[![skills.sh](https://skills.sh/b/DevBD1/skills)](https://skills.sh/DevBD1/skills)

Curated AI agent skills maintained by DevBD1.

## Install

Install a skill from this repository with:

```bash
npx skills add DevBD1/skills --skill <skill-name>
```

Example:

```bash
npx skills add DevBD1/skills --skill continuous-dev-cycle
```

## Available Skills

| Skill | Purpose |
| --- | --- |
| `openclaw-skill-scrapling-mcp` | Scrapling MCP guidance, recipes, and helper scripts for web scraping workflows. Curated for OpenClaw. |
| `antigravity-cli-delegate` | Delegate bounded work from an agent to the local Antigravity CLI. |
| `codex-cli-delegate` | Delegate bounded work from an agent to the local Codex CLI. |
| `continuous-dev-cycle` | Establish or operate a continuous development workflow for repositories. |
| `hytale-modder` | Hytale modding guidance for Java ECS, threading, and KuksoHyLib conventions. |

## What Each Skill Contains

Each top-level skill folder includes a `SKILL.md` entrypoint. Some skills also
include supporting material:

- `references/` for detailed background and usage notes.
- `scripts/` for helper scripts and smoke checks.
- `assets/` for reusable templates or starter files.
- `agents/` for agent configuration examples.

## Metadata

`skills.yml` provides the machine-readable catalog for this repository. It lists
each published skill, source URL, install command, license status, and notes.

## License

Some skill folders include their own license files. This repository does not
apply one blanket license to every skill; check the individual skill folder
before reusing code or assets.

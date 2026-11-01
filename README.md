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
npx skills add DevBD1/skills --skill loopdev
```

## Available Skills

| Skill | Purpose |
| --- | --- |
| `openclaw-skill-scrapling-mcp` | Scrapling 0.5.x MCP guidance, recipes and tested Python helpers for OpenClaw. Install/select as `scrapling-mcp`. |
| `loopdocs` | Define and maintain repository documentation roles, contents and links, including README, PRODUCT, DESIGN and agent instructions; complement LoopDev and LoopShip. |
| `loopdev` | Adapt repo-specific development: work inventory, optional plans, implementation, validation and one feature PR reviewed before merge; hand releases to LoopShip. |
| `xpost` | Algorithm Edge — code-grounded guide and draft optimizer for high-performing X (Twitter) posts, grounded in X's open-sourced 2026 recommendation algorithm. |
| `loopcast` | Build-in-public content layer: ideas and drafts grounded in development/release evidence, post history, metrics, retros, playbook and reply drafts. Formerly Buildcast. |
| `loopship` | Adapt repo-specific mobile/web releases: environments, promotion, builds, release notes, publication and delivery evidence; complement LoopDev. |

## Loop Skill Family

- **LoopDocs** defines what repository documents contain, where authoritative
  information lives, and how documents link and stay current. It replaces Autoscrum
  as the documentation layer, without sprint tracking or release operations.
- **LoopDev** manages work inventory, optional plans, implementation, validation,
  and a feature PR through authorized merge.
- **LoopShip** manages release policy, preparation, promotion, publication, and
  delivery evidence.
- **LoopCast** turns development and delivery evidence into content ideas and
  drafts, preserving post history and lessons from metrics. It replaces Buildcast;
  social publication remains manual.

Each skill can be used independently. Together they reference owning documents
instead of maintaining duplicate product, development, or release rules.

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

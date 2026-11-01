# Rename an existing project installation

Read this only when updating a repo that used the previous skill names. The
shared skill rename does not authorize modifying every project on disk.
Within the requested target repo, inspect old configs, active agent bindings,
workflow consumers and automation prompts before changing paths.

- Development config: `.agents/skills/loopscrum/config.md` becomes
  `.agents/skills/loopdev/config.md`.
- Release config: `.shipkit/config.md` becomes
  `.agents/skills/loopship/config.md`.
- Invocations: `$loopscrum` becomes `$loopdev`; `$shipkit` becomes `$loopship`.

Preserve actual project choices, unfinished work, evidence and links. Move an
existing config instead of replacing it with template defaults. If both old
and new configs exist, compare them and resolve conflicts explicitly before
retiring either. Update active entrypoints, links and consumers in the same
change; verify old live paths are no longer required. Do not rewrite historical
release receipts or rename existing archive directories solely for branding.
Do not keep parallel active configs or compatibility stubs unless requested.
If an external consumer cannot be changed within scope, record it as an
unresolved migration prerequisite rather than claiming complete cutover.

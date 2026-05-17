# Doc Templates

Use these as shape, not boilerplate. Remove sections that do not apply. Do not invent commands, env vars, architecture, or status.

## Template Files

- `references/templates/docs/README.md`: root README shape.
- `references/templates/docs/PRODUCT.md`: lightweight product spec.
- `references/templates/docs/PLAN.md`: vision, roadmap, and recommended standards.
- `references/templates/docs/AGENTS.md`: thin repo router.
- `references/templates/docs/DESIGN.md`: UI/UX standards, only when UI exists.
- `references/templates/docs/implementation-history-entry.md`: per-change history entry.
- `references/templates/docs/app-package-README.md`: tiny monorepo app/package README.

Only read the template file you need.

## Notes

- Keep `PRODUCT.md` and `PLAN.md` at repo root.
- Create `DESIGN.md` only for UI products.
- Create an implementation-history entry for the bootstrap itself when files are written.
- Only add `Recommended Next Standards` items that came from repo inspection or user confirmation.
- Keep `AGENTS.md` short. Put repeated workflows in local skills.
- Use tiny app/package READMEs in monorepos only when the app/package has independent setup, commands, env vars, deployment, usage, or ownership rules.

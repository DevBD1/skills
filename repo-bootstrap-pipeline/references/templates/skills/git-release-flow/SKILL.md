---
name: git-release-flow
description: Prepare repo changes for commit, pull request, push, or release. Use when reviewing diffs, validating changes, writing commit messages, drafting PR bodies from templates, preparing release notes, or finishing a git workflow.
---

# Git Release Flow

Use this skill when the user asks to commit, open a pull request, push, release, or prepare changes.

## Workflow

1. Run `git status --short`.
2. Inspect the diff for files you touched. Do not revert unrelated user changes.
3. Run the repo validation commands that apply to the changed area.
4. Update docs or implementation history when the change altered repo truth.
5. Stage only intended files.
6. Write a concise commit message:
   - `type(scope): summary`
   - Use the repo convention if one exists.
7. If preparing a pull request, review the repo PR template before drafting the body.
8. Push, create a PR, or release only when the user asked for it.

## Pull Requests

1. Check for PR templates:
   - `.github/pull_request_template.md`
   - `.github/PULL_REQUEST_TEMPLATE/*`
   - platform-specific equivalents if the repo uses another host.
2. If a template exists, read and follow it exactly.
3. Even when a template exists, review whether it is clear, current, and aligned with the repo's validation/release flow. Mention issues to the user instead of silently ignoring them.
4. If no template exists, draft a simple PR body with:
   - Summary
   - Verification
   - Risks
   - Screenshots or recordings, only for UI changes
5. If the repo uses pull requests but has no PR template, recommend adding one as `P2` in `PLAN.md`; do not create it by default.

## Validation

Use real commands from README.md, AGENTS.md, package files, CI config, or app/package docs.

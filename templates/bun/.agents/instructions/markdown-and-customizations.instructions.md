---
description: "Use when editing markdown documentation, prompts, or instruction files. Covers markdownlint-aware style, concise linking strategy, and safe customization frontmatter practices."
name: "Markdown and Customization Authoring"
applyTo: "**/*.md"
---
# Markdown and Customization Authoring

- Keep markdown concise, scannable, and task-oriented.
- Follow repository lint behavior from `.markdownlint.jsonc` (and
  `.agents/.markdownlint.jsonc` for `.agents/**`).
- Prefer linking to canonical files instead of duplicating long content.
- Keep customizations composable: one primary concern per instruction file.
- For `.instructions.md`, include YAML frontmatter with a keyword-rich
  `description` using a clear "Use when ..." phrase.
- Use narrow `applyTo` globs whenever possible to avoid unnecessary context
  load.
- When documenting commands, keep examples aligned with project scripts. If
  Python tooling is enabled, include UV-locked examples (`uv run --locked`).

For workspace-wide guidance, update root `AGENTS.md` and keep it short.

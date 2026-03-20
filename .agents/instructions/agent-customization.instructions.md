---
name: Agent Customization Guidelines
description: "Use when editing AGENTS.md, opencode.json, or .agents customizations."
applyTo: "AGENTS.md,.agents/**/*.md,opencode.json"
---

# Agent Customization Guidelines

- Use only root `AGENTS.md` for workspace-wide instructions.
- Do not add `.github/copilot-instructions.md`.
- Move task-specific detail into `.agents/instructions/*.instructions.md`.
- Keep reusable workflows in `.agents/prompts/`.
- Keep skill code, tests, and assets under `.agents/skills/`.
- Keep each instruction file focused on one concern.
- Start each `description` with `Use when ...` and include useful keywords.
- Link to authoritative files instead of copying them.
- Usual anchors are `package.json`, `pyproject.toml`, and `tests/test_*.py`.
- Also link `.lintstagedrc.mjs` and workflow files when relevant.
- Keep `opencode.json` aligned with any new instruction or skill paths.
- Markdown under `.agents/` also follows `.agents/.markdownlint.jsonc`.
- Python under `.agents/skills/` must satisfy the repo Python policy tests.
- When a repo-wide rule changes, update tests or config in the same change.
- Update the focused instruction file and `AGENTS.md` too.

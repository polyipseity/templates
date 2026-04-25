---
name: Testing and CI Guidelines
description: "Use when editing tests, workflows, package scripts, or validation config."
applyTo: "tests/**/*.py,.github/workflows/**/*.yml,.github/workflows/**/*.yaml,package.json,pyproject.toml,.lintstagedrc.mjs"
---

# Testing and CI Guidelines

- `package.json` is the source of truth for top-level repo commands.
- Keep `AGENTS.md`, workflows, and prompts aligned with those scripts.
- CI installs with `bun install --frozen-lockfile --ignore-scripts`.
- CI also installs with `uv sync --locked`.
- Prefer the same locked flags locally.
- `bun run check` validates Markdown, Prettier files, Ruff, and Ty.
- `bun run test` runs `uv run --locked pytest`.
- `bun run build` depends on `check` first.
- Pytest discovers `tests/` and `.agents/skills/**/tests_*`.
- Put new Python skill tests under one of those paths.
- `tests/conftest.py` defines the shared AnyIO backend.
- Use that backend or `@pytest.mark.anyio` instead of custom loop setup.
- Add regression tests when fixing behavior.
- Update tests, config, and this instruction together when a rule changes.

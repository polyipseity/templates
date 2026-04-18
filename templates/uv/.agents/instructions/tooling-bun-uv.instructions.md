---
description: "Use when editing pyproject.toml, prek.toml, CI workflows, commitlint config, or dependency automation. Preserves UV-first tooling contracts and lockfile-safe workflows."
name: "UV and Tooling Contracts"
applyTo: "pyproject.toml, prek.toml, opencode.json, .commitlintrc.mjs, .github/workflows/**/*.yml, .github/dependabot.yml"
---

# UV and Tooling Contracts

- Preserve the UV-first workflow for install/test/build and local hooks.
- Keep version constraints intentional:
  - `requires-python = ">=3.14.0"`
  - `[tool.uv].required-version = ">=0.9.0,<0.11.0"`
- Keep CI commands in `.github/workflows/ci.yml` aligned with repository policy:
  - `uv sync --locked --all-extras --dev`
  - `uv run --locked pytest`
  - `uv run --locked rumdl check`
  - `uv run --locked ruff check`
  - `uv run --locked ruff format --check`
  - `uv run --locked ty`
  - `uv build`
- Prefer `uv run --locked ...` for Python lint/format/test commands.
- Keep commit-message conventions compatible with `.commitlintrc.mjs`
  (`@commitlint/config-conventional`).
- When changing dependency config, ensure `uv.lock` stays in sync and
  `dependabot.yml` remains accurate.
- Keep `opencode.json` instruction/skill paths valid when moving directories.
- If Bun or other JS orchestration is introduced later, update `AGENTS.md` and
  this instruction intentionally instead of assuming it is always present.

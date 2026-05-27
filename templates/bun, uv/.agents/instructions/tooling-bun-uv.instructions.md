---
description: "Use when editing package.json, pyproject.toml, CI workflows, pre-commit hooks, or dependency automation. Preserves Bun+UV dual-tooling contracts and pre-commit-only hook workflow."
name: "Bun and UV Tooling Contracts"
applyTo: "package.json, pyproject.toml, bunfig.toml, opencode.json, prek.toml, .commitlintrc.mjs, .github/workflows/**/*.yml, .github/dependabot.yml"
---

# Bun and UV Tooling Contracts

- Preserve the dual-runtime workflow:
  - JavaScript orchestration through Bun
  - Python tooling through UV
- Keep version constraints intentional:
  - `packageManager: bun@1.3.10`
  - `[tool.uv].required-version = ">=0.11.0"`
- Keep canonical scripts coherent in `package.json`:
  - `check`, `format`, `test`, `build`
- Manage all pre-commit hooks in `prek.toml` (not `.pre-commit-config.yaml`).
  - Husky and lint-staged are removed; pre-commit runs all formatting and checks on hook stages.
  - Local hooks using `language: system` invoke Bun for Node.js tools (e.g., prettier, commitlint).
  - Prefer `uv run --locked ...` for Python lint/format/test commands in hooks.
- Prefer `uv run --locked ...` for Python CLI commands in CI and local scripts.
- Keep CI install and test flow compatible with current lockfile strategy
  (`bun install --frozen-lockfile --ignore-scripts` + `uv sync --locked ...`).
- When changing dependency config, ensure corresponding lockfiles remain in
  sync (`bun.lock`, `uv.lock`) and dependabot scope remains accurate.
- Keep `opencode.json` instruction/skill paths valid when moving directories.

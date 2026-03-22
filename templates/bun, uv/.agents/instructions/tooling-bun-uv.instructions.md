---
description: "Use when editing package.json, pyproject.toml, CI workflows, lint-staged, or dependency automation. Preserves Bun+UV dual-tooling contracts and lockfile-safe workflows."
name: "Bun and UV Tooling Contracts"
applyTo: "package.json, pyproject.toml, bunfig.toml, opencode.json, .lintstagedrc.mjs, .commitlintrc.mjs, .github/workflows/**/*.yml, .github/dependabot.yml"
---
# Bun and UV Tooling Contracts

- Preserve the dual-runtime workflow:
  - JavaScript orchestration through Bun
  - Python tooling through UV
- Keep version constraints intentional:
  - `packageManager: bun@1.3.10`
  - `[tool.uv].required-version = ">=0.9.0,<0.11.0"`
- Keep canonical scripts coherent in `package.json`:
  - `check`, `format`, `test`, `build`
- In lint-staged commands, invoke underlying CLIs directly for staged-file
  argument forwarding (avoid `bun run` wrappers for file-list-sensitive tools).
- Prefer `uv run --locked ...` for Python lint/format/test commands.
- Keep CI install and test flow compatible with current lockfile strategy
  (`bun install --frozen-lockfile --ignore-scripts` + `uv sync --locked ...`).
- When changing dependency config, ensure corresponding lockfiles remain in
  sync (`bun.lock`, `uv.lock`) and dependabot scope remains accurate.
- Keep `opencode.json` instruction/skill paths valid when moving directories.

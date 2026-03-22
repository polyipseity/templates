# Project Guidelines

## Repository Shape

- Root `AGENTS.md` is the workspace-wide source of truth. Do not add
  `.github/copilot-instructions.md`.
- Keep this file short and durable. Put focused guidance in
  `.agents/instructions/*.instructions.md`, reusable workflows in
  `.agents/prompts/`, and skill code/assets in `.agents/skills/`.

## Architecture

- This repository is a Bun-first template with optional UV-backed Python
  quality gates.
- The current scaffold is intentionally minimal (`src/`, `tests/`, `scripts/`
  contain placeholders until features are added).
- Runtime/config boundaries are file-driven:
  - `package.json` + `bunfig.toml` for JS/task orchestration
  - `pyproject.toml` + `uv.lock` only when Python tooling is enabled
  - `opencode.json` for agent instruction/skill discovery

## Build and Test

- Install dependencies with Bun:
  - `bun install --frozen-lockfile --ignore-scripts`
- Standard project checks:
  - `bun run check`
  - `bun run test`
  - `bun run build`
- Formatting:
  - `bun run format`
- When Python tooling is enabled, prefer locked UV execution (for example,
  `uv sync --all-extras --dev`, `uv run --locked ruff check`,
  `uv run --locked pytest`).

## Conventions

- For staged-file workflows, run underlying CLIs directly (not `bun run`) when
  file arguments must be forwarded by lint-staged.
- If Python quality gates are enabled in this template, add/update
  `pyproject.toml`, `uv.lock`, and policy tests under `tests/` in the same
  change.
- Keep `.opencode/**` link targets valid when adding/removing agent assets.

## Key References

- `package.json` — canonical Bun scripts (`check`, `format`, `test`, `build`)
- `.lintstagedrc.mjs` — staged-file command forwarding conventions
- `opencode.json` — `.agents/instructions/**` and skill path configuration
- `.agents/instructions/tooling-bun-uv.instructions.md` — Bun contracts and
  optional UV enablement guidance

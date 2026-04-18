# Project Guidelines

## Repository Shape

- Root `AGENTS.md` is the workspace-wide source of truth. Do not add
  `.github/copilot-instructions.md`.
- Keep this file short and durable. Put focused guidance in
  `.agents/instructions/*.instructions.md`, reusable workflows in
  `.agents/prompts/`, and skill code/assets in `.agents/skills/`.
- Treat `package.json`, `pyproject.toml`, `tests/`, and `.github/workflows/`
  as the authoritative contract. `README.md` is intentionally minimal.
- `templates/` contains self-contained variants (`bun/`, `uv/`, and
  `bun, uv/`). Do not treat them as shared runtime code.
- `.agents/` contains repo-local customizations used by `opencode.json`.
- `.github/workflows/` defines CI, and `tests/` holds policy-style checks.

## Build and Test

- Use the root scripts in `package.json` as the source of truth:
  - `bun run check` — runs markdownlint, Prettier checks, Ruff, and Ty
  - `bun run test` — runs `uv run --locked pytest`
  - `bun run build` — runs `check` before `build:force`
  - `bun run format` — fixes Markdown, Prettier-supported files, and Python
- For fresh setup, CI installs dependencies with:
  - `bun install --frozen-lockfile --ignore-scripts`
  - `uv sync --locked --all-extras --dev`
- Prefer locked Python CLI runs (`uv run --locked ...`) to match CI and
  lint-staged behavior.
- When a change affects validation or release automation, check both
  `.github/workflows/ci.yml` and `.github/workflows/commitlint.yml`.

## Code Style

- Follow formatting and line-ending rules from `.editorconfig`,
  `.gitattributes`, `.markdownlint.jsonc`, `.agents/.markdownlint.jsonc`, and
  `pyproject.toml`.
- Python targets `3.14`, uses strict Ty settings, and uses Ruff with an
  88-character line length.
- Preserve file-specific line endings: Markdown and shell files use LF;
  PowerShell and batch files use CRLF.
- In `.lintstagedrc.mjs`, prefer direct CLIs that can receive the staged file
  list instead of wrapping them in `bun run`.

## Conventions

- For Python under `tests/`, `src/`, `scripts/`, and `.agents/skills/`,
  follow `.agents/instructions/python-module-policy.instructions.md`.
- When changing tests, CI, package scripts, or validation behavior, follow
  `.agents/instructions/testing-and-ci.instructions.md`.
- When editing files under `templates/**`, follow
  `.agents/instructions/template-variants.instructions.md`.
- When editing `AGENTS.md`, `.agents/**`, or `opencode.json`, follow
  `.agents/instructions/agent-customization.instructions.md`.
- When editing Husky, commitlint, lint-staged, formatting, or line-ending
  rules, follow `.agents/instructions/tooling-and-automation.instructions.md`.
- If you add helper scripts under `scripts/`, make sure git tracks executable
  ones with the correct mode; see `tests/test_git_executable.py`.
- Do not assume content under `templates/*/**` is type-checked by the root
  Ty configuration; those paths are excluded in `pyproject.toml`.
- For commit-related automation, follow Conventional Commits and the existing
  commitlint + Husky setup; see `.commitlintrc.mjs`, `.husky/commit-msg`, and
  `.agents/prompts/commit-staged.prompt.md`.
- If you change a repository policy, update the enforcing tests/configuration
  and the relevant instruction file in the same change.

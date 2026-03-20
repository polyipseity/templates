# Project Guidelines

## Repository Shape

- `AGENTS.md` at the repository root is the single source of truth for workspace-wide agent instructions. Do not add `.github/copilot-instructions.md` in this repo.
- Keep this file concise. If the root guidance grows too large, split focused customizations into `.agents/instructions/`, `.agents/prompts/`, and `.agents/skill/`, then link to them from here instead of duplicating content.
- `templates/` contains the template variants (`bun/`, `uv/`, and `bun, uv/`). Treat each variant as self-contained template content rather than shared runtime code.
- `.agents/` contains repo-local agent customizations used by `opencode.json`; keep agent-specific prompts, skills, and instructions there.
- `.github/workflows/` defines the CI contract, and `tests/` contains policy-style tests that enforce repository conventions.

## Build and Test

- Use the root scripts in `package.json` as the source of truth:
  - `bun run check`
  - `bun run test`
  - `bun run build`
- For fresh setup, CI installs dependencies with:
  - `bun install --frozen-lockfile --ignore-scripts`
  - `uv sync --locked --all-extras --dev`
- Prefer locked Python CLI runs (`uv run --locked ...`) to match CI and lint-staged behavior.

## Code Style

- Follow formatting and line-ending rules from `.editorconfig`, `.gitattributes`, `.markdownlint.jsonc`, and `pyproject.toml`.
- Python targets `3.12`, uses strict Pyright settings, and uses Ruff with an 88-character line length.
- Preserve file-specific line endings: Markdown and shell files use LF; PowerShell and batch files use CRLF.

## Conventions

- New Python files under `tests/`, `src/`, `scripts/`, and `.agents/skill/` are validated by `tests/test_docstrings.py` and `tests/test_module_exports.py`. Keep these files compliant:
  - add a non-empty module docstring
  - define `__all__` as a tuple
  - place `__all__` after top-level imports
  - add docstrings for exported symbols, top-level definitions, nested definitions, and documented top-level assignments
- If you add executable helper scripts under `scripts/`, make sure git tracks them with executable mode where applicable; see `tests/test_git_executable.py`.
- When editing lint-staged flows, prefer direct CLIs that can accept the staged file list instead of wrapping them in `bun run`; see `.lintstagedrc.mjs`.
- Do not assume content under `templates/*/**` is type-checked by the root Pyright configuration; those paths are excluded in `pyproject.toml`.
- For commit-related automation, follow Conventional Commits and the existing commitlint + Husky setup; see `.commitlintrc.mjs`, `.husky/commit-msg`, and `.agents/prompts/commit-staged.prompt.md`.

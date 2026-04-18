# Project Guidelines

## Repository Shape

- Root `AGENTS.md` is the workspace-wide source of truth. Do not add
  `.github/copilot-instructions.md`.
- Keep this file short and durable. Put focused guidance in
  `.agents/instructions/*.instructions.md`, reusable workflows in
  `.agents/prompts/`, and skill code/assets in `.agents/skills/`.

## Architecture

- This repository is a Bun + UV template for mixed JavaScript tooling and
  Python quality gates.
- Python source and checks center on `src/`, `tests/`, `scripts/`, and
  `.agents/skills/**` (when present).
- Runtime/config boundaries are file-driven:
  - `package.json` + `bunfig.toml` for JS/task orchestration
  - `pyproject.toml` for Python deps, lint/type/test config
  - `opencode.json` for agent instruction/skill discovery

## Build and Test

- Install dependencies with Bun and UV:
  - `bun install`
  - `uv sync --all-extras --dev`
- Standard project checks:
  - `bun run check`
  - `bun run test`
  - `bun run build`
- Formatting:
  - `bun run format`
- Prefer locked Python tool execution through UV (for example,
  `uv run --locked ruff check`, `uv run --locked pytest`).

## Conventions

- Python version is `3.12` with strict type checking (`ty` in
  `pyproject.toml`).
- Every Python module in scoped paths must define module-level `__all__` as a
  tuple of string literals (enforced by `tests/test_module_exports.py`).
- Module, top-level definitions, and top-level assignments must be documented
  with docstrings (enforced by `tests/test_docstrings.py`).
- Keep `__all__` after top-level imports.
- For staged-file workflows, run underlying CLIs directly (not `bun run`) when
  file arguments must be forwarded by lint-staged.
- Async tests use AnyIO conventions from `tests/conftest.py`.

## Key References

- `package.json` — canonical Bun scripts (`check`, `format`, `test`, `build`)
- `pyproject.toml` — Python dependencies, Ruff, Ty, pytest, UV constraints
- `.lintstagedrc.mjs` — staged-file command forwarding conventions
- `tests/test_module_exports.py` — `__all__` policy and ordering checks
- `tests/test_docstrings.py` — docstring policy for modules/definitions/variables
- `tests/test_git_executable.py` — executable-bit checks for script files
- `opencode.json` — `.agents/instructions/**` and skill path configuration

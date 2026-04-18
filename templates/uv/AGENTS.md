# Project Guidelines

## Repository Shape

- Root `AGENTS.md` is the workspace-wide source of truth. Do not add
  `.github/copilot-instructions.md`.
- Keep this file short and durable. Put focused guidance in
  `.agents/instructions/*.instructions.md`, reusable workflows in
  `.agents/prompts/`, and skill code/assets in `.agents/skills/`.

## Architecture

- This repository is a UV-first Python quality-gates template, with Node.js
  used only where required by commit tooling.
- Python source and checks center on `src/`, `tests/`, `scripts/`, and
  `.agents/skills/**` (when present).
- Runtime/config boundaries are file-driven:
  - `pyproject.toml` for Python deps, lint/type/test config
  - `prek.toml` for pre-commit/push hook orchestration
  - `.github/workflows/*.yml` for CI build/test policy
  - `.commitlintrc.mjs` for commit message lint policy
  - `opencode.json` for agent instruction/skill discovery

## Build and Test

- Install dependencies with UV:
  - `uv sync --locked --all-extras --dev`
- Standard project checks (as used in CI):
  - `uv run --locked pytest`
  - `uv run --locked rumdl check`
  - `uv run --locked ruff check`
  - `uv run --locked ruff format --check`
  - `uv run --locked ty`
  - `uv build`
- Prefer locked Python tool execution through UV (for example,
  `uv run --locked ruff check`, `uv run --locked pytest`).

## Conventions

- Python version is `3.14` with strict type checking (`ty` in
  `pyproject.toml`).
- Every Python module in scoped paths must define module-level `__all__` as a
  tuple of string literals (enforced by `tests/test_module_exports.py`).
- Module, top-level definitions, and top-level assignments must be documented
  with docstrings (enforced by `tests/test_docstrings.py`).
- Keep `__all__` after top-level imports.
- Keep commit messages compatible with `.commitlintrc.mjs`
  (`@commitlint/config-conventional`).
- Async tests use AnyIO conventions from `tests/conftest.py`.

## Key References

- `pyproject.toml` — Python dependencies, Ruff, Ty, pytest, UV constraints
- `prek.toml` — pre-commit and pre-push hook policy
- `.commitlintrc.mjs` — commit message linting policy
- `.github/workflows/ci.yml` — canonical CI install/test/build commands
- `tests/test_module_exports.py` — `__all__` policy and ordering checks
- `tests/test_docstrings.py` — docstring policy for modules/definitions/variables
- `tests/test_git_executable.py` — executable-bit checks for script files
- `opencode.json` — `.agents/instructions/**` and skill path configuration

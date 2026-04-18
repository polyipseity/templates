---
description: "Use when editing Python modules in src, tests, scripts, or .agents/skills. Enforces __all__ tuple rules, docstring coverage, strict typing, and uv-locked quality commands."
name: "Python Quality Gates"
applyTo: "**/*.py"
---

# Python Quality Gates

- Apply these rules when Python scaffolding is enabled (for example,
  `pyproject.toml` exists or Python modules are being added).
- Keep a non-empty module docstring in every Python module.
- Define module-level `__all__` as a tuple of string literals.
- Keep `__all__` after top-level imports.
- Add docstrings for:
  - all top-level functions, async functions, and classes
  - nested functions and methods
  - top-level assignments/constants via an immediately preceding
    string-literal expression
- Use complete type annotations compatible with Ty strict mode
  (`python-version = "3.12"`).
- Prefer top-level imports; avoid import-outside-top-level patterns unless
  there is a strong reason (`PLC0415` is enabled in Ruff).
- When UV tooling is configured, validate/fix Python quality with:
  - `uv run --locked ruff check`
  - `uv run --locked ruff format`
  - `uv run --locked pytest`
- When adding or renaming exported symbols, update `__all__` in the same
  change.

If present, keep policy tests (for example `tests/test_module_exports.py` and
`tests/test_docstrings.py`) aligned with these rules.

---
name: Python Module Policy
description: "Use when creating or editing Python under tests, src, scripts, or .agents/skills."
applyTo: "tests/**/*.py,src/**/*.py,scripts/**/*.py,.agents/skills/**/*.py"
---

# Python Module Policy

- Treat `tests/test_docstrings.py` and `tests/test_module_exports.py` as the
  source of truth.
- Every module must have a non-empty module docstring.
- After top-level imports, define `__all__` as a tuple of string literals.
- If nothing is exported, use `__all__ = ()`.
- Do not build `__all__` dynamically.
- Do not use a list for `__all__`.
- Docstring every top-level function, class, and method.
- Docstring every nested function and nested class.
- Put a string-literal docstring immediately above each top-level assignment.
- Exported functions and classes named in `__all__` must also have non-empty docstrings.
- Keep files friendly to Python 3.12, strict Pyright, and Ruff.
- Update the tests with any policy change.

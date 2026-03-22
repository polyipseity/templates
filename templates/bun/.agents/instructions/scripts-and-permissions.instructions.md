---
description: "Use when adding or editing files under scripts/. Covers executable-bit expectations, cross-platform line endings, and script placement rules enforced by tests."
name: "Scripts and Executable Permissions"
applyTo: "scripts/*.sh, scripts/*.py, scripts/*.ps1, scripts/*.bat, scripts/*.cmd"
---
# Scripts and Executable Permissions

- Keep top-level scripts inside `scripts/` unless test/config paths are updated.
- Respect line-ending conventions:
  - `.sh` uses LF
  - `.ps1` and `.bat` use CRLF
- On non-Windows platforms, ensure executable scripts have executable bits set.
- If executable-bit policy tests are present (for example
  `tests/test_git_executable.py`), keep git index mode expectations compatible.
- Prefer explicit, portable script behavior and avoid shell-specific assumptions
  unless the script extension already constrains the shell.
- If introducing new script extensions or locations, update tests and glob
  specifications intentionally.

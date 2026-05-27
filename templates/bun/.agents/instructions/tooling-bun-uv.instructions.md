---
description: "Use when editing package.json, bunfig.toml, prek.toml, opencode.json, or CI/dependency automation. Preserves Bun script contracts, prek hook configuration, and optional UV contracts when Python tooling is enabled."
name: "Bun Tooling Contracts"
applyTo: "package.json, pyproject.toml, bunfig.toml, prek.toml, opencode.json, .commitlintrc.mjs, .github/workflows/**/*.yml, .github/dependabot.yml"
---
# Bun Tooling Contracts

- Preserve Bun as the default orchestration runtime.
- Keep version constraints intentional:
  - `packageManager: bun@1.3.10`
- Keep canonical scripts coherent in `package.json`:
  - `check`, `format`, `test`, `build`
- Ensure each script only references defined subscripts (for example, avoid
  dangling `check:*`/`format:*` entries).
- Git hooks are managed by `prek.toml` (Prek is a Rust-based drop-in replacement
  for pre-commit). Keep hook stages aligned with `prek.toml`: `pre-commit` for
  formatting/linting, `commit-msg` for message validation, `pre-push` for tests.
  See https://prek.j178.dev/ for details.
- If Python tooling is enabled (`pyproject.toml` + `uv.lock`), prefer
  `uv run --locked ...` and keep CI/dependency automation aligned.
- Keep lockfiles in sync for enabled package managers (`bun.lock` always;
  `uv.lock` when UV is enabled) and keep dependabot scope accurate.
- Keep `opencode.json` instruction/skill paths and `.opencode/**` symlink
  targets valid when moving directories.

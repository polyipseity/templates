---
description: "Use when editing package.json, bunfig.toml, opencode.json, lint-staged, or CI/dependency automation. Preserves Bun script contracts and optional UV contracts when Python tooling is enabled."
name: "Bun Tooling Contracts"
applyTo: "package.json, pyproject.toml, bunfig.toml, opencode.json, .lintstagedrc.mjs, .commitlintrc.mjs, .github/workflows/**/*.yml, .github/dependabot.yml"
---
# Bun Tooling Contracts

- Preserve Bun as the default orchestration runtime.
- Keep version constraints intentional:
  - `packageManager: bun@1.3.10`
- Keep canonical scripts coherent in `package.json`:
  - `check`, `format`, `test`, `build`
- Ensure each script only references defined subscripts (for example, avoid
  dangling `check:*`/`format:*` entries).
- In lint-staged commands, invoke underlying CLIs directly for staged-file
  argument forwarding (avoid `bun run` wrappers for file-list-sensitive tools).
- If Python tooling is enabled (`pyproject.toml` + `uv.lock`), prefer
  `uv run --locked ...` and keep CI/dependency automation aligned.
- Keep lockfiles in sync for enabled package managers (`bun.lock` always;
  `uv.lock` when UV is enabled) and keep dependabot scope accurate.
- Keep `opencode.json` instruction/skill paths and `.opencode/**` symlink
  targets valid when moving directories.

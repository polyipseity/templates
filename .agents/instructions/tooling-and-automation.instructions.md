---
name: Tooling and Automation Guidelines
description: "Use when changing lint-staged, Husky, commitlint, formatting, or line-ending automation."
applyTo: ".commitlintrc.mjs,.editorconfig,.gitattributes,.husky/**,.lintstagedrc.mjs,.markdownlint.jsonc,.markdownlint-cli2.mjs,.agents/.markdownlint.jsonc,.agents/prompts/**/*.md"
---

# Tooling and Automation Guidelines

- Preserve line endings from `.editorconfig` and `.gitattributes`.
- Markdown and shell files use LF.
- PowerShell and batch files use CRLF.
- In `.lintstagedrc.mjs`, call underlying CLIs directly.
- Avoid wrapping file-list-sensitive commands in `bun run`.
- Prefer `uv run --locked` for Python tools used by automation.
- Husky runs `lint-staged` on `pre-commit`.
- Husky runs `commitlint` on `commit-msg`.
- Husky runs `bun run test` on `pre-push`.
- Conventional Commits are enforced locally and in GitHub Actions.
- Commit bodies should wrap to 72 characters.
- `.agents/prompts/commit-staged.prompt.md` is the source of truth for commit automation.
- Keep formatting globs aligned across `.markdownlint-cli2.mjs`,
  `.lintstagedrc.mjs`, and `package.json`.
- Markdown in `.agents/` also follows `.agents/.markdownlint.jsonc`.

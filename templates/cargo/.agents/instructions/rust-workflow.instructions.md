---
description: "Use when editing Rust source, Cargo config, Rust CI validation, or Rust scripts in this repository."
name: "Rust Workflow Guidance"
applyTo: "**/*.rs, Cargo.toml, Cargo.lock, rust-toolchain.toml, rustfmt.toml, clippy.toml, .cargo/**/*.toml, .github/workflows/**/*.yml, .github/workflows/**/*.yaml, scripts/**/*.sh, scripts/**/*.ps1, scripts/**/*.bat"
---

# Rust Workflow Guidance

## Scope

- Apply this guidance when working on Rust source or Rust-specific tooling.
- Treat this repository as a template with a Rust bootstrap setup that may grow
  additional packages over time.
- Do not assume `PLAN.md` or other planning docs are already implemented unless
  task scope explicitly asks for them.

## Source-of-truth files

- `Cargo.toml` for workspace structure, package identity, and dependency graph.
- `.cargo/config.toml` for local cargo behavior, target directory, and aliases.
- `rust-toolchain.toml` for toolchain channel, profile, and components.
- `rustfmt.toml` and `clippy.toml` for style and lint policy.
- `.github/workflows/ci.yml` for canonical CI validation behavior.
- `scripts/` for any helper scripts (shell scripts use LF, PowerShell/batch use CRLF).

## Cargo aliases (defined in `.cargo/config.toml`)

The `.cargo/config.toml` defines cargo aliases to standardize validation commands
across local development and CI. Use these aliases instead of inline cargo commands.

### Workspace-wide aliases (slow; CI/pre-push only)

| Alias        | Command                                                          | Purpose                                       |
| ------------ | ---------------------------------------------------------------- | --------------------------------------------- |
| `build-all`  | `build --workspace --all-targets --all-features`                 | Full workspace build including tests/docs     |
| `clippy-all` | `clippy --workspace --all-targets --all-features -- -D warnings` | Workspace-wide lint with deny-warnings policy |
| `fmt-check`  | `fmt --all -- --check`                                           | Workspace-wide formatting check               |
| `test-all`   | `test --workspace --all-targets --all-features`                  | Workspace-wide test suite                     |

### Package-targeted aliases (recommended for development)

| Alias        | Command                                                       | Purpose                |
| ------------ | ------------------------------------------------------------- | ---------------------- |
| `build-pkg`  | `build -p <pkg> --all-targets --all-features`                 | Fast per-package build |
| `clippy-pkg` | `clippy -p <pkg> --all-targets --all-features -- -D warnings` | Fast per-package lint  |
| `test-pkg`   | `test -p <pkg> --all-targets --all-features`                  | Fast per-package tests |

### Special alias

| Alias | Command                      | Purpose                            |
| ----- | ---------------------------- | ---------------------------------- |
| `bin` | `run --package cargo-bin --` | Run the primary `cargo-bin` binary |

## Validation workflow

### During development

Use package-targeted aliases for fast feedback:

```bash
cargo build-pkg -p <package-name>
cargo clippy-pkg -p <package-name>
cargo test-pkg -p <package-name>
```

### Before commit/push

Use workspace-wide aliases for comprehensive validation:

```bash
cargo fmt-check
cargo test-all
cargo clippy-all
```

### CI behavior

The CI workflow runs the following sequence:

1. `cargo test-all` — run full test suite
2. `cargo bin rumdl check` — check `rumdl` linter (workspace member)
3. `cargo clippy-all` — workspace-wide clippy with deny-warnings
4. `cargo fmt-check` — formatting verification
5. `cargo build-all` — final build verification

## When configs are incomplete

If `Cargo.toml`, `rust-toolchain.toml`, or other configs are incomplete or
missing, report the gaps explicitly rather than inventing fallback commands.
A sparse template is expected; agents should not pretend validation infrastructure
exists when it does not.

## Editing conventions

- Prefer the cargo aliases over inline commands; they are the canonical reference
  in `.cargo/config.toml`.
- When adding a new package to the workspace, update validation guidance to
  mention the new package name in examples.
- Avoid introducing hidden mutable state or external service dependencies unless
  explicitly requested.
- Keep Rust-specific detail in this file rather than growing root `AGENTS.md`.

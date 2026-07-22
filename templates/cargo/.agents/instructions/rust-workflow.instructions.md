---
description: "Use when editing Rust source, Cargo config, Rust CI validation, or Rust scripts in this repository."
name: "Rust Workflow Guidance"
applyTo: "**/*.rs, Cargo.toml, Cargo.lock, rust-toolchain.toml, rustfmt.toml, clippy.toml, .config/**/*.toml, .cargo/**/*.toml, .github/workflows/**/*.yml, .github/workflows/**/*.yaml, scripts/**/*.sh, scripts/**/*.ps1, scripts/**/*.bat"
---

# Rust Workflow Guidance

## Scope

- Apply this guidance when working on Rust source or Rust-specific tooling.
- Treat this repository as a template with a Rust bootstrap setup that may grow additional packages over time.
- Do not assume `PLAN.md` or other planning docs are already implemented unless task scope explicitly asks for them.

## Source-of-truth files

- `Cargo.toml` for workspace structure, package identity, and dependency graph.
- `.cargo/config.toml` for local cargo behavior, target directory, and aliases.
- `.config/nextest.toml` for nextest runner configuration (profiles, timeouts, retries).
- `rust-toolchain.toml` for toolchain channel, profile, and components.
- `rustfmt.toml` and `clippy.toml` for style and lint policy.
- `.github/workflows/ci.yml` for canonical CI validation behavior.
- `prek.toml` for local git hooks (pre-commit framework configured as TOML).
- `scripts/` for any helper scripts (shell scripts use LF, PowerShell/batch use CRLF).

## Cargo aliases (defined in `.cargo/config.toml`)

The `.cargo/config.toml` defines cargo aliases to standardize validation commands across local development and CI. Use these aliases instead of inline cargo commands.

### Workspace-wide aliases (slow; CI/pre-push only)

| Alias        | Command                                           | Purpose                                                                          |
| ------------ | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| `build-all`  | `build --workspace --all-targets --all-features`  | Full workspace build including tests/docs                                        |
| `clippy-all` | `clippy --workspace --all-targets --all-features` | Workspace-wide lint; lint levels are set in `Cargo.toml` via `[workspace.lints]` |
| `fmt-check`  | `fmt --all -- --check`                            | Workspace-wide formatting check                                                  |
| `test-all`   | `run --package cargo-bin -- cargo-nextest run --workspace --all-targets --all-features` | Workspace-wide test suite via nextest (auto-installs via binstall)               |

### Package-targeted aliases (recommended for development)

| Alias        | Command                                        | Purpose                                                                  |
| ------------ | ---------------------------------------------- | ------------------------------------------------------------------------ |
| `build-pkg`  | `build -p <pkg> --all-targets --all-features`  | Fast per-package build                                                   |
| `clippy-pkg` | `clippy -p <pkg> --all-targets --all-features` | Fast per-package lint; lint levels are set in `Cargo.toml` via `[lints]` |
| `test-pkg`   | `run --package cargo-bin -- cargo-nextest run --all-targets --all-features -p` | Fast per-package tests via nextest (auto-installs via binstall)          |

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

Use the canonical full test script or workspace-wide aliases:

```bash
scripts/run-all-tests.sh      # nextest + doctests
# or individually:
cargo fmt-check
cargo test-all                # nextest only (no doctests)
cargo clippy-all
```

### Full test suite (nextest + doctests)

The canonical way to run the complete test suite (nextest for integration/unit tests + doctests) is:

```bash
scripts/run-all-tests.sh
```

The script runs `cargo test-all` (nextest) then `cargo test --doc --workspace` (doctests, which nextest does not cover). Both invocations use `--locked` for reproducible dependency resolution. CI uses this same script.

### CI behavior

The CI workflow runs the following sequence:

1. `scripts/run-all-tests.sh` — nextest test suite + doctests (auto-installs nextest via cargo-binstall on first run)
2. `cargo bin rumdl check` — check `rumdl` linter (workspace member)
3. `cargo clippy-all` — workspace-wide clippy with deny-warnings
4. `cargo fmt-check` — formatting verification
5. `cargo build-all` — final build verification

## Git hooks and pre-commit

This repository uses the pre-commit framework (configured via `prek.toml`) to manage local git hooks. The hooks run automatically on `git commit` and `git push` to catch issues early and auto-fix formatting:

- **pre-commit stage** (on `git commit`): runs `cargo fmt` (formats code), `cargo check`, `cargo clippy`, and `rumdl fmt` (formats markdown)
- **pre-push stage** (on `git push`): runs nextest (via `cargo run --package cargo-bin -- cargo-nextest run --workspace --all-targets --all-features`, auto-installs nextest via binstall on first run)

To install or update hooks locally, run:

```bash
pre-commit install
```

You can also run hooks manually:

```bash
pre-commit run --all-files          # Run all hooks
pre-commit run nextest              # Run the nextest hook
```

To temporarily skip hooks during a commit, use `SKIP`:

```bash
SKIP=nextest git commit -m "message"
```

## Known nextest caveats

cargo-nextest has several behavioral differences from `cargo test`. Be aware of these when using nextest in this template:

1. **No doctest support.** Nextest does not run doctests. This is why `scripts/run-all-tests.sh` runs `cargo test --doc --workspace` separately after nextest.

2. **Binary/test executable detection only.** Nextest only discovers binary and test crate targets. It does not run examples or benchmarks. Use `cargo build --examples` or `cargo bench` separately for those.

3. **`#[should_panic]` tests may timeout.** Nextest has a default per-test timeout. A `#[should_panic]` test that panics via an infinite loop or deadlock will eventually be killed by the timeout rather than hanging indefinitely. This is usually desirable, but adjust `slow-timeout` in `.config/nextest.toml` if needed.

4. **Leak detection is experimental.** Nextest's leak detection (configured via `leak-timeout` in `.config/nextest.toml`) can produce false positives for tests that hold OS resources (file descriptors, sockets). Disable it globally or per-test if it causes CI flakiness.

5. **No `--nocapture` by default.** Nextest captures stdout/stderr per test and displays it grouped by pass/fail. To see live output, use `cargo nextest run --show-output`. The cargo alias `test-all` does not pass `--show-output`; use `cargo bin cargo-nextest run --show-output` for debugging.

## When configs are incomplete

If `Cargo.toml`, `rust-toolchain.toml`, or other configs are incomplete or missing, report the gaps explicitly rather than inventing fallback commands. A sparse template is expected; agents should not pretend validation infrastructure exists when it does not.

## Editing conventions

- Prefer the cargo aliases over inline commands; they are the canonical reference in `.cargo/config.toml`.
- When adding a new package to the workspace, update validation guidance to mention the new package name in examples.
- Avoid introducing hidden mutable state or external service dependencies unless explicitly requested.
- Keep Rust-specific detail in this file rather than growing root `AGENTS.md`.

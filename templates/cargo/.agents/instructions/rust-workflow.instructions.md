---
description: "Use when editing Rust source, Cargo config, or Rust CI validation in this repository."
name: "Rust Workflow Guidance"
applyTo: "**/*.rs, Cargo.toml, Cargo.lock, rust-toolchain.toml, rustfmt.toml, clippy.toml, .cargo/**/*.toml, .github/workflows/**/*.yml, .github/workflows/**/*.yaml"
---
# Rust Workflow Guidance

## Scope

- Apply this guidance when working on Rust source or Rust-specific tooling.
- Treat this repository as a template that now includes a Rust bootstrap setup.
- Do not treat `PLAN.md` as already implemented unless task scope explicitly asks for it.

## Source-of-truth files

- `Cargo.toml` for package identity and dependency graph.
- `.cargo/config.toml` for local cargo behavior and aliases.
- `rust-toolchain.toml` for toolchain/channel/components.
- `rustfmt.toml` and `clippy.toml` for style and lint policy.
- `.github/workflows/ci.yml` for canonical CI validation behavior.

## Validation workflow

- Preferred local checks:
  - `cargo fmt --all -- --check`
  - `cargo clippy --workspace --all-targets --all-features -- -D warnings`
  - `cargo test --workspace --all-targets --all-features`
- If source or configs are incomplete, report gaps explicitly instead of inventing commands.

## Editing conventions

- Keep changes minimal, deterministic, and aligned with the functional-core direction in `PLAN.md`.
- Avoid adding hidden mutable state or introducing databases unless explicitly requested.
- Keep stack-specific detail in this file rather than growing root `AGENTS.md`.

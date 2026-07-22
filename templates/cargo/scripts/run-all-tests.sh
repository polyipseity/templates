#!/usr/bin/env bash
set -euo pipefail

cd "$(git rev-parse --show-toplevel)"

cargo --locked test-all
cargo --locked test --doc --workspace

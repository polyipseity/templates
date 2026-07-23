#!/bin/sh
set -eu

cd "$(git rev-parse --show-toplevel)"

cargo --locked test-all
cargo --locked test --doc --workspace

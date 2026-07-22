#!/usr/bin/env pwsh
Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

cargo --locked test-all
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

cargo --locked test --doc --workspace
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

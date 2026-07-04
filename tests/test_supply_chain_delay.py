"""Tests that package manager configurations include supply chain delay hardening.

The repository policy requires that all package manager configuration files
include a minimum release age or equivalent delay to mitigate supply chain
attacks. This test verifies that:

- ``bunfig.toml`` files include ``minimumReleaseAge`` under ``[install]``.
- ``bunfig.toml`` files include ``exact = true`` under ``[install]``.
- ``pyproject.toml`` files include ``exclude-newer`` under ``[tool.uv]``.
- ``pyproject.toml`` files include ``add-bounds = "exact"`` under ``[tool.uv]``.

Where applicable, each checked value is verified against a specific minimum
delay (currently 5 days / 432000 seconds for Bun).
"""

import tomllib
from pathlib import Path
from typing import Any

import pytest

"""Public API of this test module (empty)."""
__all__ = ()

"""Paths to check relative to the repository root.

Entries are ``(path, package_manager)`` pairs where ``package_manager`` is
either ``"bun"`` or ``"uv"``.
"""
_CHECK_PATHS = (
    ("bunfig.toml", "bun"),
    ("pyproject.toml", "uv"),
    ("templates/bun/bunfig.toml", "bun"),
    ("templates/uv/pyproject.toml", "uv"),
    ("templates/bun, uv/bunfig.toml", "bun"),
    ("templates/bun, uv/pyproject.toml", "uv"),
)

"""Minimum acceptable delay in seconds for Bun."""
_BUN_MIN_DELAY_S = 432000  # 5 days


def _load_toml(path: Path) -> dict[str, Any]:
    """Load and parse a TOML file, returning the parsed dictionary."""
    raw = path.read_bytes()
    return tomllib.loads(raw.decode("utf-8"))


@pytest.mark.parametrize(("rel_path", "pm"), _CHECK_PATHS)
def test_supply_chain_delay_present(rel_path: str, pm: str) -> None:
    """Verify that the configuration file at *rel_path* includes the
    expected supply chain delay setting for the given *pm* tool."""
    path = Path(rel_path)
    assert path.exists(), f"Missing config file: {rel_path}"
    config = _load_toml(path)

    if pm == "bun":
        install = config.get("install", {})
        age = install.get("minimumReleaseAge")
        assert age is not None, f"{rel_path}: missing [install].minimumReleaseAge"
        assert isinstance(age, int), (
            f"{rel_path}: minimumReleaseAge must be an integer, got {type(age).__name__}"
        )
        assert age >= _BUN_MIN_DELAY_S, (
            f"{rel_path}: minimumReleaseAge {age} < {_BUN_MIN_DELAY_S}"
        )
    elif pm == "uv":
        tool_uv = config.get("tool", {}).get("uv", {})
        newer = tool_uv.get("exclude-newer")
        assert newer is not None, f"{rel_path}: missing [tool.uv].exclude-newer"
        assert newer == "P5D", (
            f'{rel_path}: exclude-newer should be "P5D", got {newer!r}'
        )
    else:
        pytest.fail(f"Unknown package manager: {pm}")


@pytest.mark.parametrize(("rel_path", "pm"), _CHECK_PATHS)
def test_pinning_config_present(rel_path: str, pm: str) -> None:
    """Verify that the configuration file at *rel_path* includes the
    expected exact-version-pinning setting for the given *pm* tool."""
    path = Path(rel_path)
    assert path.exists(), f"Missing config file: {rel_path}"
    config = _load_toml(path)

    if pm == "bun":
        install = config.get("install", {})
        exact = install.get("exact")
        assert exact is True, (
            f"{rel_path}: [install].exact should be true, got {exact!r}"
        )
    elif pm == "uv":
        tool_uv = config.get("tool", {}).get("uv", {})
        bounds = tool_uv.get("add-bounds")
        assert bounds == "exact", (
            f'{rel_path}: [tool.uv].add-bounds should be "exact", got {bounds!r}'
        )
    else:
        pytest.fail(f"Unknown package manager: {pm}")

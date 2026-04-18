---
name: Template Variant Guidelines
description: "Use when editing files under templates/** or adding a template variant."
applyTo: "templates/**"
---

# Template Variant Guidelines

- Each `templates/*` directory is a self-contained variant.
- Do not treat one variant as shared runtime code for another.
- Prefer explicit variant updates over hidden root-only coupling.
- `pyproject.toml` excludes `templates/*/**` from the root Ty run.
- Put any variant-specific checks or build config inside that variant.
- Favor small intentional duplication over brittle cross-variant abstractions.
- Optimize template files for downstream clarity and standalone setup.
- Preserve line endings and executable-bit expectations for stored scripts.

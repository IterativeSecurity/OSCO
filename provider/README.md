# Provider Artifacts

This directory contains provider registry data used directly by OSCO runtime.

## Purpose

Providers represent implementation surfaces (operating systems, cloud platforms, SaaS systems, identity providers, container platforms, databases, browsers).

Provider records are loaded by [osco/registry.py](../osco/registry.py) and used by:

- `osco provider list` CLI output
- graph construction (`provider -> capability` `implements` edges)
- capability/provider consistency checks

## Files

- [providers.json](providers.json): canonical provider registry

## Validation

Validate provider model shape and capability provider references:

```bash
uv run scripts/validate_provider_registry.py
```

CI workflow:

- [.github/workflows/provider-registry.yml](../.github/workflows/provider-registry.yml)

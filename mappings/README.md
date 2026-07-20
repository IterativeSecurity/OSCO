# Mapping Artifacts

This directory defines OSCO's external framework mapping registry.

## Purpose

Mapping data in capability/detection/validation catalogs references external frameworks (for example ATT&CK, Sigma, OCSF, ECS).

This folder provides the canonical allow-list of framework identifiers that
mapping entries are allowed to use.

## Files

- [frameworks.yaml](frameworks.yaml): canonical mapping framework registry

## Runtime vs Governance

- Runtime mapping behavior is driven by catalog mapping entries in:
	- [capability/catalog.json](../capability/catalog.json)
	- [capability/catalog.extended.json](../capability/catalog.extended.json)
	- [detection/detections.json](../detection/detections.json)
	- [validation/validations.json](../validation/validations.json)
- Governance/enforcement is driven by this folder and the validation script.

## Enforcement Contract

`frameworks.yaml` must stay in sync with:

- `MappingFramework` enum in [osco/models/core.py](../osco/models/core.py)
- all `mapping.framework` values used in capability/detection/validation catalogs

Validation command:

```bash
uv run scripts/validate_mapping_frameworks.py
```

CI workflow:

- [.github/workflows/mapping-frameworks.yml](../.github/workflows/mapping-frameworks.yml)

## Authoring Guidance

- Add a new framework in `frameworks.yaml` and `MappingFramework` together in the same change.
- Add catalog mappings only after the framework is registered.
- Keep framework IDs stable and lowercase (snake_case).

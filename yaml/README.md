# yaml

This directory contains YAML schema and governance files for the OSCO project.

## Files & Purpose

### Structural Validation

**[capability.schema.yaml](capability.schema.yaml)** — JSON Schema for capability records
- Defines required fields: `capability_id`, `stable_id`, `name`, `description`, `category`, `domain`, `platforms`
- Validates optional fields: `providers`, `status`, `confidence`, `safety`, `mappings`
- Enforces patterns: capability_id must be dot-separated (e.g., `lateral.movement.execution`)
- Used by: JSON Schema validation in CI and local validation scripts

### Governance & Taxonomy

**[../ontology/domains.yaml](../ontology/domains.yaml)** — Capability domain taxonomy
- Auto-generated tree structure of all supported domain.object.action paths
- Enforced by: `scripts/validate_ontology_taxonomy.py` (ensures all capability_id values exist in taxonomy)
- CI workflow: `.github/workflows/ontology-taxonomy.yml` validates on catalog/ontology changes
- See: [ontology/README.md](../ontology/README.md) for details

**[../mappings/frameworks.yaml](../mappings/frameworks.yaml)** — Mapping framework registry
- Declares all supported external frameworks (ATT&CK, AWS, Azure, etc.)
- Cross-validated against: `MappingFramework` enum in `osco/models/core.py`
- Enforced by: `scripts/validate_mapping_frameworks.py` (ensures consistency across YAML, enum, and catalogs)
- CI workflow: `.github/workflows/mapping-frameworks.yml` validates on mapping changes
- See: [mappings/README.md](../mappings/README.md) for details

## Validation Chain

All YAML files are validated via:
1. **Pydantic models** — osco/models/core.py enforces type system
2. **Governance scripts** — validate_ontology_taxonomy.py, validate_mapping_frameworks.py, validate_provider_registry.py
3. **CI workflows** — automated enforcement on PR/push

Run locally: `uv run osco/scripts_validate.py`

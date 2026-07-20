# validation

This directory contains validation artifacts for OSCO — curated security validation scenarios that bridge detection logic with external frameworks.

## Files & Purpose

### Validation Catalog

**[validations.json](validations.json)** — Validation scenarios and test cases
- **validation_id**: Semantic identifier (e.g., `val.persistence.endpoint.001`)
- **name**: Human-readable title
- **description**: Scenario details (what is being validated, how it's tested)
- **mappings**: Cross-references to external frameworks (ATT&CK, Atomic Red Team, Velociraptor, etc.)
  - `framework`: External framework name
  - `external_id`: Framework technique/artifact ID
  - `external_name`: Framework human-readable name
  - `relation`: Type of relationship (validates, maps_to, implements)
  - `confidence`: Mapping confidence score (0–1)

**Current entries (6):**
1. Endpoint persistence validation (scheduled tasks)
2. PowerShell encoded command validation
3. Credential access simulation
4. IAM policy access validation
5. Kubernetes RBAC validation
6. SaaS mail delegation validation

## Validation & Governance

- **Model validation**: `osco/models/core.py` enforces Validation record schema (validation_id, name, description, mappings)
- **Reference integrity**: `scripts/validate_provider_registry.py` ensures mapping framework names are declared
- **Framework consistency**: `scripts/validate_mapping_frameworks.py` validates all mapping frameworks against declared registry
- **CI enforcement**: `.github/workflows/mapping-frameworks.yml` validates on validation catalog changes

## Adding New Validations

1. Add entry to [validations.json](validations.json) following existing pattern:
   ```json
   {
     "validation_id": "val.DOMAIN.OBJECT.NNN",
     "name": "...",
     "description": "...",
     "mappings": [
       {
         "framework": "<declared in mappings/frameworks.yaml>",
         "external_id": "...",
         "external_name": "...",
         "relation": "validates|maps_to|implements",
         "confidence": 0.0-1.0
       }
     ]
   }
   ```

2. Ensure `framework` values exist in [../mappings/frameworks.yaml](../mappings/frameworks.yaml)

3. Run validation: `uv run scripts/validate_mapping_frameworks.py`

## Related Documentation

- [../ontology/README.md](../ontology/README.md) — Capability taxonomy and governance
- [../mappings/README.md](../mappings/README.md) — Framework registry and consistency
- [../provider/README.md](../provider/README.md) — Provider reference integrity

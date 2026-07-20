# JSON Schema Artifacts

This directory contains JSON Schema definitions for OSCO objects.

## Purpose

These schemas provide structural validation for OSCO data:

- required fields
- value types
- basic constraints (regex, enum, numeric bounds, min items)

JSON Schema is the structural contract. Semantic taxonomy validation is handled separately by [ontology/domains.yaml](../ontology/domains.yaml) and
`scripts/validate_ontology_taxonomy.py`.

## Files

- [capability.schema.json](capability.schema.json): schema for `Capability` records in [capability/catalog.json](../capability/catalog.json) and [capability/catalog.extended.json](../capability/catalog.extended.json).

## Capability Schema Highlights

`capability.schema.json` currently enforces:

- `capability_id` format: `^[a-z0-9_]+(\.[a-z0-9_]+)+$`
- required core fields: `capability_id`, `stable_id`, `name`, `description`, `category`, `domain`, `platforms`
- `platforms` must be a non-empty array
- `confidence` range: 0.0 to 1.0
- `safety` enum: `safe`, `caution`, `destructive`
- mapping object requirements: `framework`, `external_id`, `external_name`

## Validation Commands

Run structural validation (Pydantic + JSON Schema):

```bash
uv run osco/scripts_validate.py
```

Run semantic taxonomy validation for `capability_id` coverage:

```bash
uv run scripts/validate_ontology_taxonomy.py
```

## Structural vs Semantic Validation

- JSON Schema answer: "Is this record shaped correctly?"
- Ontology taxonomy answer: "Is this capability ID in an approved ontology branch?"

Both are required for high-quality catalog changes.

## Contributor Notes

- When changing capability model fields in [osco/models/core.py](../osco/models/core.py), keep this schema synchronized.
- When adding new capability taxonomy branches, update catalogs and then refresh taxonomy with:

```bash
uv run scripts/sync_ontology_domains.py
```

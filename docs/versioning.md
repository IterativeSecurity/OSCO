# Versioning

OSCO uses versioning at multiple layers.

## Current Version

The current ontology version is defined in `pyproject.toml` (`version = "0.1.0"`) and is also reflected in the `OSCOBundle.ontology_version` field of any exported bundle.

## Ontology and Catalog Versioning

- **Ontology version** identifies semantic model evolution. Changing the ontology version signalsm that the object model, field semantics, or naming conventions have changed.
- **Capability record version** (`Capability.version`) tracks the revision of an individual capability entry.

## Schema Artifact Versioning

Schema formats in `jsonschema/`, `yaml/`, `protobuf/`, and `openapi/` evolve in sync with model changes. When a model field is added, renamed, or removed, all schema artifacts should be updated in the same commit or PR.

## Compatibility Guidance

| Change type | Version increment | Notes |
|---|---|---|
| Add optional field | Minor | Existing consumers unaffected |
| Add required field | Major | Breaks existing catalog entries without default |
| Remove field | Major | Breaking for any consumer reading that field |
| Rename field | Major | Treat as remove + add |
| Change enum values | Major (remove) / Minor (add) | Adding values is backward-compatible |
| Change ID regex pattern | Major | May invalidate existing entries |
| Change `stable_id` format | Major | High impact; avoid if possible |

## Capability Status Lifecycle

Individual capability entries move through a defined status progression.

```
draft ──────────────────► stable ──────────────────► deprecated
  │                          │                            │
  │ (still in review)        │ (validated, in use)       │ (retired or superseded)
  │                          │                            │
  └──────────── x ◄──────────┘                            └── (do not use)
               (no regression from stable to draft)
```

### Transition Criteria

| Transition | Criteria |
|---|---|
| `draft` → `stable` | Capability has been reviewed, validated by at least one discovery or verification method, and schema validation passes |
| `stable` → `deprecated` | Capability is superseded by a more precise entry, the domain is retired, or the behavior is no longer relevant |
| `deprecated` → (removed) | Removal requires a major version increment and must be preceded by at least one release cycle in `deprecated` state |

A capability must never regress from `stable` to `draft`. If a stable capability requires significant
correction, create a new draft entry and deprecate the original.

## Stable ID Policy

`stable_id` values (e.g., `OSCO-CAP-0042`) are **permanent**. They are:
- Never reused after a capability is deprecated or removed
- Never reassigned to a different capability
- The authoritative reference for integrations, attestation records, and external citations

If a capability is deprecated, its `stable_id` is retired with it. The next assigned ID continues
from the current maximum, ensuring no ambiguity from gaps in the sequence.

## Deprecation Practice

When deprecating a capability:
1. Set `status` to `deprecated`
2. Add a `references` entry pointing to the replacement capability or rationale document
3. Leave the entry in the catalog for at least one release cycle
4. Document the migration path in the PR description and relevant changelog entry

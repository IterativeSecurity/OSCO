# Ontology Artifacts

This folder stores low-level ontology artifacts that are useful for maintainers and future schema/runtime work.

## Why This Folder Exists

OSCO separates:

- Concept documentation (in [docs/ontology.md](../docs/ontology.md))
- Machine-readable ontology artifacts (in this folder)

The `ontology/` directory is the machine-readable side of that split.

## Current Contents

- [domains.yaml](domains.yaml): canonical domain/object/action taxonomy seed.

## Current Status

These files are now used as a semantic validation source for capability IDs.

- Runtime query behavior is still driven by capability catalogs (for example, [capability/catalog.json](../capability/catalog.json)).
- Taxonomy validation ensures catalog `capability_id` values are present in [domains.yaml](domains.yaml).
- CI runs both taxonomy freshness and taxonomy coverage checks.

## How To Use This Folder

- Use [docs/ontology.md](../docs/ontology.md) for semantic guidance and authoring rules.
- Use [domains.yaml](domains.yaml) to review and discuss taxonomy structure.
- Keep this folder aligned with catalog and documentation updates.
- When catalogs change, run `uv run scripts/sync_ontology_domains.py` to refresh taxonomy entries.
- Run `uv run scripts/validate_ontology_taxonomy.py` to verify taxonomy coverage.

## Planned Direction

This folder is intended to become the home for deeper ontology artifacts such as
formal taxonomies, reusable profiles, and additional machine-readable constraints
as OSCO runtime/schema layers mature.

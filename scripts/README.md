# Scripts

This directory contains repeatable maintenance, generation, and validation scripts
for OSCO.

## Usage

Run scripts from repository root with `uv run`:

```bash
uv run scripts/<script_name>.py
```

## Generation Scripts

- [generate_capability_corpus.py](generate_capability_corpus.py)
	- Generates/expands capability corpus entries in [capability/catalog.json](../capability/catalog.json).

- [curate_gold_catalog.py](curate_gold_catalog.py)
	- Curates the full corpus into a gold subset and writes:
		- [capability/catalog.json](../capability/catalog.json) (gold)
		- [capability/catalog.extended.json](../capability/catalog.extended.json) (full)

- [generate_capability_table.py](generate_capability_table.py)
	- Generates markdown registry tables for catalog docs.
	- Typical usage:

```bash
uv run scripts/generate_capability_table.py \
	--catalog capability/catalog.json \
	--output capability/README.md \
	--title "Capability Registry"
```

- [generate_component_docs_report.py](generate_component_docs_report.py)
	- Generates component doc coverage report.
	- Modes:
		- `--write`: write [docs/component-doc-coverage.md](../docs/component-doc-coverage.md)
		- `--check`: fail if report is stale or docs are missing

## Ontology Governance Scripts

- [sync_ontology_domains.py](sync_ontology_domains.py)
	- Syncs [ontology/domains.yaml](../ontology/domains.yaml) from capability catalogs.
	- Supports `--check` mode for CI freshness enforcement.

- [validate_ontology_taxonomy.py](validate_ontology_taxonomy.py)
	- Validates all `capability_id` values are covered by [ontology/domains.yaml](../ontology/domains.yaml).

## Mapping Governance Scripts

- [validate_mapping_frameworks.py](validate_mapping_frameworks.py)
	- Enforces consistency across:
		- [mappings/frameworks.yaml](../mappings/frameworks.yaml)
		- `MappingFramework` enum in [osco/models/core.py](../osco/models/core.py)
		- mapping entries in capability/detection/validation catalogs

## Provider Governance Scripts

- [validate_provider_registry.py](validate_provider_registry.py)
	- Validates provider records and ensures capability provider references resolve
		to declared provider IDs.

## Documentation Validation

- [check_markdown_links.py](check_markdown_links.py)
	- Scans repository markdown files and fails on broken local links.

## Common Validation Run

Typical local validation sequence:

```bash
uv run osco/scripts_validate.py
uv run scripts/validate_ontology_taxonomy.py
uv run scripts/validate_mapping_frameworks.py
uv run scripts/validate_provider_registry.py
uv run scripts/check_markdown_links.py
uv run pytest tests/ -q
```

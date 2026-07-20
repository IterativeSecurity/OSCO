# OSCO CLI

This package contains OSCO's command-line interface implementation.

Primary entry point:
- [main.py](main.py)

## Overview

The CLI exposes query and export operations for OSCO catalogs:

- capability search and listing
- provider listing
- mapping inspection/comparison/conversion
- graph export and relationship inspection
- schema validation

## Command Groups

The root command is `osco` with these groups:

- `capability`
- `provider`
- `mapping`
- `graph`
- `schema`

Get help:

```bash
uv run osco --help
uv run osco capability --help
```

## Capability Commands

Search capabilities by free-text query:

```bash
uv run osco capability search persistence
```

List all capabilities:

```bash
uv run osco capability list
```

## Provider Commands

List all providers:

```bash
uv run osco provider list
```

## Mapping Commands

List all mappings:

```bash
uv run osco mapping list
```

List mappings for a specific framework:

```bash
uv run osco mapping list --framework mitre_attack
```

Find capabilities with no mappings:

```bash
uv run osco mapping unmapped
```

Compare mapping coverage between two frameworks:

```bash
uv run osco mapping compare mitre_attack sigma
```

Convert a framework identifier to OSCO capabilities:

```bash
uv run osco mapping convert mitre_attack T1053.005
```

## Graph Commands

Export capability graph as JSON:

```bash
uv run osco graph export --format json --output examples/osco_graph.json
```

Other supported export formats:

- `graphml`
- `cypher`

Inspect graph relationships for one capability:

```bash
uv run osco graph relationships windows.task.create
```

## Schema Commands

Validate all capabilities against JSON schema:

```bash
uv run osco schema validate
```

## Notes

- The CLI reads from repository catalogs (for example [capability/catalog.json](../../capability/catalog.json)).
- Output is rendered as Rich tables for terminal readability.
- Mapping framework values are constrained by `MappingFramework` in [osco/models/core.py](../models/core.py).

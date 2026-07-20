# OSCO Python Package

This package contains OSCO's core runtime implementation for:

- loading catalog data into typed models
- querying capabilities and providers
- building and exporting relationship graphs
- exposing CLI operations

## Module Map

- [registry.py](registry.py): loads catalogs and provides query helpers via `OSCORegistry`
- [models/core.py](models/core.py): Pydantic models and enums for OSCO objects
- [graph_builder.py](graph_builder.py): builds relationship graph from registry bundle
- [exporters.py](exporters.py): exports graph as JSON, GraphML, and Cypher
- [scripts_validate.py](scripts_validate.py): model + schema validation script
- [cli/main.py](cli/main.py): Typer-based CLI implementation

## Public Entry Point

The package exports:

- `OSCORegistry` from [__init__.py](__init__.py)

Example:

```python
from osco import OSCORegistry

registry = OSCORegistry()
print(len(registry.list_capabilities()))
```

## Runtime Data Flow

1. [registry.py](registry.py) loads JSON catalogs (`capability`, `provider`, `detection`, `validation`).
2. [models/core.py](models/core.py) validates and types records.
3. [graph_builder.py](graph_builder.py) builds relationship graph.
4. [exporters.py](exporters.py) serializes graph for downstream systems.
5. [cli/main.py](cli/main.py) exposes this flow through `osco` commands.

## Validation

Run package-level validation:

```bash
uv run osco/scripts_validate.py
```

This validates capability records against both:

- Pydantic models
- [jsonschema/capability.schema.json](../jsonschema/capability.schema.json)

## Related Docs

- [osco/cli/README.md](cli/README.md)
- [osco/models/README.md](models/README.md)
- [docs/architecture.md](../docs/architecture.md)

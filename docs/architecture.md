# OSCO Architecture

## Architectural Principles

- Capability-first semantic model
- Separation of ontology semantics from execution implementations
- Many-to-many mapping interoperability
- Graph-native relationship representation
- Versioned machine-readable artifacts

## Core Components

1. Core Ontology
2. Capability Registry
3. Knowledge Graph
4. Mapping Framework
5. Discovery Framework
6. Verification Framework
7. SDK and Schema Artifacts
8. Validation and Governance Tooling

## Data Flow

1. Authors create or update capabilities in the registry.
2. Providers declare implementation support.
3. External frameworks map to capabilities with relation and confidence metadata.
4. Registry data is loaded into typed models.
5. Graph builders export relationship views for analysis and integrations.
6. CLI commands expose search, mapping, validation, and export operations.

## Repository Implementation Map

The sections below describe what exists in this repository today versus roadmap targets.

Implemented:
- Capability registry: capability/catalog.json and capability/catalog.extended.json
- Provider registry: provider/providers.json
- Typed models: osco/models/core.py
- Registry loader: osco/registry.py
- Graph builder/exporters: osco/graph_builder.py and osco/exporters.py
- CLI commands: osco/cli/main.py
- Schema artifacts: jsonschema/, yaml/, protobuf/, openapi/
- CI generation/check workflows: .github/workflows/

Planned:
- Richer SDK implementations in sdk/
- Expanded runtime query and API services
- Additional provider and mapping depth beyond initial corpus

Contributors should treat the Implemented list as the source of truth for current code-backed behavior.

## Object Relationships

- Capability is the primary semantic unit.
- Provider implements one or more capabilities.
- Evidence and telemetry describe observability.
- Detection and validation content map through capability semantics.
- Mapping frameworks provide external equivalence/relationship context.

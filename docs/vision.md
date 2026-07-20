# OSCO Vision

Open Security Capability Ontology (OSCO) is a canonical, vendor-neutral semantic layer for cybersecurity capabilities.

OSCO connects operating systems, cloud providers, SaaS platforms, security tools, and automation frameworks through shared capability semantics.

## Why OSCO

Security teams currently translate between many framework-specific terms.
OSCO provides a stable vocabulary so capabilities can be described once and mapped many times.

Examples:
- API/function concept: CreateFileW -> filesystem.file.create
- Cloud action concept: CreateRole -> cloud.iam.role.create
- SaaS behavior concept: Mail forwarding rule creation -> mail.forwarding.create

## Non-Goals

OSCO does not replace ATT&CK, Atomic Red Team, Velociraptor, Sigma, CAR, OCSF, ECS, or OpenTelemetry. OSCO maps to those ecosystems rather than competing with them.

OSCO does not model vendors or products as ontology primitives.
It models capabilities and implementation metadata separately.

## Design Commitments

- Provider-neutral
- Framework-neutral
- Cloud and OS neutral
- Implementation-neutral
- AI-native
- Graph-first
- Machine-readable and human-readable
- Versioned and extensible
- Open governance

## Current Project Maturity

Current repository state includes:
- A curated capability registry and extended corpus
- Typed models for core objects
- Graph export support (JSON, GraphML, Cypher)
- Multi-format schema artifacts (JSON Schema, YAML, Protobuf, OpenAPI)
- CI checks for generated docs and markdown link integrity

Implemented now:
- Registry, provider catalog, and mapping-ready object model
- CLI for capability/provider/mapping queries and graph export
- Generated documentation and documentation-coverage enforcement

Planned:
- Deeper SDK implementations across all language folders
- Richer runtime services (API/query surfaces)
- Continued provider and mapping expansion and refinement

Planned next layers include deeper SDK implementations and richer runtime services.

# Open Security Capability Ontology (OSCO)

OSCO is a vendor-neutral semantic layer for cybersecurity capabilities.

It provides a canonical ontology that connects operating systems, cloud providers, SaaS platforms, security tools, telemetry schemas, AI agents, and automation frameworks without modeling vendors, products, or scripts as first-class ontology entities.

## What OSCO Models

OSCO models **security capabilities** as stable semantic objects.

Examples:

- `CreateFileW()` -> `filesystem.file.create`
- `New-ScheduledTask` -> `windows.task.create`
- `CreateRole()` -> `cloud.iam.role.create`
- `Create Gmail Forwarding Rule` -> `mail.forwarding.create`

## What OSCO Does

OSCO provides query, mapping, and export operations against a canonical capability registry:

- **Search and query**: Find capabilities by domain, name, or framework mapping.
- **Resolve mappings**: Translate between security frameworks (ATT&CK, Sigma, Atomic Red Team, OCSF, ECS, etc.) and capabilities.
- **Export graphs**: Generate JSON, GraphML, or Cypher representations for analysis and integration.
- **Validate schemas**: Ensure capability entries conform to model and ontology rules.
- **Link evidence**: Connect observable artifacts (files, registry keys, events, audit records) to capabilities.
- **Plan verification**: Find appropriate validation/simulation techniques for a given capability and environment.

## Why

Security operations are still fragmented by implementation language.
One team says "run Atomic test T1053.005," another says "query CloudTrail CreateRole," and a third says "hunt for registry persistence."
They are often talking about the same underlying capability, but the tooling vocabulary differs.

OSCO exists to normalize that translation layer.

### Real Use Cases

- Cross-tool reasoning: Map one security idea (for example persistence) across endpoint, cloud, and SaaS tooling without rewriting intent each time.
- Detection engineering: Connect Sigma/analytics content to capability semantics so coverage can be measured by behavior, not just rule count.
- Validation planning: Ask "what persistence capabilities are testable here" instead of manually chasing framework IDs.
- IR and triage: Pivot from observed evidence/telemetry to related capabilities and likely detections or validation paths.
- Program reporting: Describe gaps in capability coverage with vendor-neutral language that leadership and engineering can both understand.

### Keep It Real

- OSCO does not magically integrate every tool out of the box.
- Mapping quality varies and needs iteration, review, and evidence.
- Capability abstraction helps decision-making, but implementation details still matter in execution.

### Near-Term Direction

- Integrate OSCO into `gleam` as a fully working example.
- Increase high-quality capability coverage with curated semantics.
- Improve mapping precision and confidence scoring.
- Expand provider-specific implementation metadata without polluting ontology semantics.
- Grow SDK/runtime ergonomics so external systems can consume OSCO catalogs directly.

## Core Components

- [Core Ontology](ontology/)
- [Capability Registry](capability/)
- [Knowledge Graph](graph/)
- [Mapping Framework](mappings/)
- [Discovery Framework](discovery/)
- [Detection Framework](detection/)
- [Validation Framework](validation/)
- [SDKs and Schemas](sdk/), [jsonschema/](jsonschema/), [yaml/](yaml/), [protobuf/](protobuf/)

## Repository Layout

See [docs/architecture.md](docs/architecture.md) and [docs/ontology.md](docs/ontology.md).

## Capability Catalog Tiers

- `capability/catalog.json`: curated "gold" catalog for day-to-day use (currently 320 capabilities).
- `capability/catalog.extended.json`: full generated corpus for broad semantic coverage (currently 1015 capabilities).

To regenerate the curated tier from the full corpus:

```bash
uv run scripts/curate_gold_catalog.py
```

## Quick Start

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -e .[dev]
osco capability search persistence
osco provider list
osco mapping list --framework mitre_attack
osco graph export --format json --output examples/osco_graph.json
uv run pytest
```

## License

Apache-2.0

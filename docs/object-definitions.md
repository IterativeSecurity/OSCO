# Object Definitions

This document describes OSCO's core object types, their roles, and their key fields. For the complete field-by-field reference including types, defaults, and valid values, see [Field Reference](field-reference.md).

---

## Capability

The canonical semantic object in OSCO. A capability represents a single, discrete security-relevant
behavior that a system, platform, or tool can perform — independent of how it is implemented.

Capabilities are identified by a stable dotted semantic ID (`capability_id`) and a permanent registry
number (`stable_id`). Both are immutable once published.

**Key fields:**

| Field | Purpose |
|---|---|
| `capability_id` | Semantic identifier in `domain.object.action` format. Example: `filesystem.file.create`. |
| `stable_id` | Permanent registry number (e.g., `OSCO-CAP-0042`). Used for stable references and integrations. |
| `status` | Lifecycle state: `draft`, `stable`, or `deprecated`. |
| `safety` | Risk classification: `safe`, `caution`, or `destructive`. Controls automated use. |
| `confidence` | Float 0–1. Author's confidence in the accuracy of this definition. |
| `mappings` | References to external framework artifacts (ATT&CK, Sigma, etc.). |
| `evidence` | Observables that confirm capability execution. |
| `verification_methods` | Safe procedures for exercising and confirming the capability. |
| `discovery_methods` | Procedures for detecting whether the capability is supported in an environment. |

**Implementation reference:**
- `osco/models/core.py` (Capability)
- `capability/catalog.json` (curated catalog)
- `capability/catalog.extended.json` (extended corpus)

---

## Provider

Represents a platform, service, or tool that exposes one or more capabilities. Providers describe the *supply side* of the capability ontology — where capabilities come from.

Providers must be implementation-oriented. They should not embed product marketing, version numbers, or feature lists. A provider entry describes the scope of a platform's capability surface, not a product roadmap.

**Key fields:**

| Field | Purpose |
|---|---|
| `provider_id` | Unique identifier. Convention: `provider.<name>`. Example: `provider.aws`. |
| `category` | Provider type: `cloud`, `os`, `saas`, `edr`, `siem`, `identity`, etc. |
| `platforms` | Platforms this provider operates on. |
| `supports` | Domain or capability surface areas the provider exposes. |

**Implementation reference:**
- `osco/models/core.py` (Provider)
- `provider/providers.json`

---

## Evidence

Describes an observable artifact that proves a capability was executed or is currently active. Evidence objects bridge capability semantics and real artifact inspection — they answer the question "how do I know this capability was used?"

Evidence types include: files, registry keys, process handles, network connections, cloud resources, audit records, and log entries.

**Key fields:**

| Field | Purpose |
|---|---|
| `evidence_id` | Unique identifier. Convention: `evidence.<capability_id>.<n>`. |
| `type` | Evidence category: `file`, `registry_key`, `process`, `audit_record`, etc. |
| `location` | Path, key, URL, or query where the artifact can be found. |
| `description` | What this artifact is and why its presence confirms the capability. |

**Implementation reference:**
- `osco/models/core.py` (Evidence)

---

## Telemetry

Describes a log or event stream produced during capability execution. Telemetry objects are observability context — they describe what a monitoring system would see when a capability is exercised, not the capability itself.

This distinction is important: telemetry and capabilities have a many-to-many relationship. One capability may produce multiple telemetry streams; one stream may cover multiple capabilities.

**Key fields:**

| Field | Purpose |
|---|---|
| `telemetry_id` | Unique identifier. Convention: `telemetry.<capability_id>.<n>`. |
| `source` | The system that produces this telemetry (e.g., `sysmon`, `cloudtrail`, `auditd`). |
| `event_type` | The specific event class or log category (e.g., `ProcessCreate`, `S3.GetObject`). |
| `description` | What information this telemetry provides about capability execution. |

**Relationship to OCSF:** OCSF normalizes the *schema* of telemetry events. OSCO normalizes the *capability semantics* those events represent. Map telemetry sources to OCSF classes using `CapabilityMapping` with `framework: ocsf`.

**Implementation reference:**
- `osco/models/core.py` (Telemetry)

---

## Detection

Represents defensive content — a detection rule, analytic, or query — that identifies capability execution. Detection objects are references to external detection artifacts, not the detection logic itself.

**Key fields:**

| Field | Purpose |
|---|---|
| `detection_id` | Unique identifier. References the external detection (e.g., `sigma-4201`). |
| `name` | Human-readable detection name. |
| `description` | What behavior this detection identifies and its data source requirements. |
| `mappings` | Framework references for this detection content. |

**Implementation reference:**
- `osco/models/core.py` (Detection)
- `detection/detections.json`

---

## Validation

Represents offensive simulation or test content — an adversary simulation test, red team procedure, or atomic test — used to verify that a detection fires when a capability is exercised.

Validation and Detection objects are complementary. Validation exercises the capability; Detection alerts on it. A coverage gap exists when a capability has validation without corresponding detection.

**Key fields:**

| Field | Purpose |
|---|---|
| `validation_id` | Unique identifier. References the external test (e.g., `art-t1059.001-01`). |
| `name` | Human-readable validation name. |
| `description` | What this validation exercises, its prerequisites, and expected outcomes. |
| `mappings` | Framework references for this validation artifact. |

**Implementation reference:**
- `osco/models/core.py` (Validation)
- `validation/validations.json`

---

## Scope Status

Implemented now:
- Capability, Provider, Evidence, Telemetry, Detection, and Validation object models (all six)
- Catalog-backed instances for capabilities, providers, detections, and validations
- Pydantic-typed validation for all objects

Planned:
- Deeper object enrichment fields and expanded cross-object relationship metadata
- Additional supporting object catalogs as coverage grows
- Formal profile mechanism for reusable cross-object attribute sets

# Mapping Guide

Mappings connect OSCO capabilities to external standards and tools.

## Mapping Model

Mappings are many-to-many.
A single capability may map to multiple external artifacts, and one external artifact may map to multiple capabilities.

Required mapping fields:
- `framework` — the external standard being referenced (see [MappingFramework](field-reference.md#mappingframework))
- `external_id` — the identifier used by that framework
- `external_name` — the human-readable name of the external artifact

Recommended mapping fields:
- `relation` — semantic relationship type (see [Relation Types](relation-types.md)); defaults to `maps_to`
- `confidence` — float 0.0–1.0 representing mapping certainty
- `url` — direct link to the external artifact for verification

## Relation Types

The `relation` field expresses the semantic connection between the capability and the external artifact.
See [Relation Types](relation-types.md) for full semantics and a decision guide.

| Relation | Use when |
|---|---|
| `maps_to` | The external artifact describes the same behavior as the capability |
| `detects` | The external artifact is a detection rule or analytic for this capability |
| `validates` | The external artifact is a simulation test or red team procedure |
| `related_to` | Partial or inferred overlap only |
| `enables` | This capability is a prerequisite for the external artifact |
| `implements` | The external artifact is a concrete implementation of this capability |

## Complete Mapping Example

The following shows a capability with three mapping entries covering ATT&CK technique alignment,
a Sigma detection, and an Atomic Red Team validation test:

```json
{
  "capability_id": "windows.task.create",
  "stable_id": "OSCO-CAP-0042",
  "name": "Create Scheduled Task",
  "description": "Creates a scheduled task on a Windows host. Tasks can run at startup, on schedule, or triggered by system events.",
  "category": "persistence",
  "domain": "windows",
  "platforms": ["windows"],
  "providers": ["provider.windows"],
  "status": "stable",
  "confidence": 0.95,
  "safety": "caution",
  "mappings": [
    {
      "framework": "mitre_attack",
      "external_id": "T1053.005",
      "external_name": "Scheduled Task/Job: Scheduled Task",
      "relation": "maps_to",
      "confidence": 0.95,
      "url": "https://attack.mitre.org/techniques/T1053/005/"
    },
    {
      "framework": "sigma",
      "external_id": "sigma-schtask-creation",
      "external_name": "Scheduled Task Creation Via Schtasks.EXE",
      "relation": "detects",
      "confidence": 0.8,
      "url": "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml"
    },
    {
      "framework": "atomic_red_team",
      "external_id": "T1053.005-1",
      "external_name": "Scheduled Task Startup Script",
      "relation": "validates",
      "confidence": 0.9,
      "url": "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1053.005/T1053.005.md"
    }
  ]
}
```

## OCSF Alignment

OSCO capabilities that describe runtime system events have corresponding OCSF event classes.
When mapping to OCSF, use the `ocsf` framework and reference the class ID.

Example: `process.create` maps to OCSF `Process Activity [1007]`:

```json
{
  "framework": "ocsf",
  "external_id": "1007",
  "external_name": "Process Activity",
  "relation": "maps_to",
  "confidence": 0.9,
  "url": "https://schema.ocsf.io/1.8.0/classes/process_activity"
}
```

OSCO and OCSF serve different purposes: OCSF normalizes the **event schema** (what a log record looks like);
OSCO normalizes the **capability semantics** (what behavior the event represents). They are complementary.

## Initial Framework Coverage

Current repository includes initial mapping coverage for:
- `mitre_attack` — ATT&CK Techniques and Sub-Techniques
- `atomic_red_team` — Atomic Red Team adversary simulation tests
- `velociraptor` — Velociraptor artifact library
- `sigma` — Generic detection rules
- `event_maturity_matrix` — Telemetry coverage maturity model
- `ocsf` — Open Cybersecurity Schema Framework event classes
- `ecs` — Elastic Common Schema fields
- `osquery` — osquery table and query definitions

## Mapping Quality Guidance

- Prefer precise semantic alignment over forced one-to-one mappings. A capability may have zero mappings
  if no external artifact currently describes it — this is valid.
- Use `confidence` to represent certainty of alignment, not priority or importance.
- A detection that covers only one execution path of a multi-path capability should have confidence ≤ 0.6.
- Include `url` whenever an authoritative reference is publicly available.
- Use `related_to` rather than `maps_to` when alignment is partial or inferred.

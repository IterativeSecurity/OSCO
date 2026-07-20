# Relation Types

This document defines the semantic meaning of every relationship type used in OSCO.
Relation types appear in two places:

1. **`CapabilityMapping.relation`** — the relationship between a capability and an external framework artifact.
2. **Graph edges** — relationships between OSCO objects in the knowledge graph (see `osco/graph_builder.py`).

Using the correct relation type is important for reasoning quality. An incorrect relation type
will produce misleading graph queries and mapping results.

---

## Mapping Relation Types

Used in `CapabilityMapping.relation` to express the semantic connection between an OSCO
capability and an artifact in an external framework.

| Relation | Direction | Description |
|---|---|---|
| `maps_to` | capability → external | The capability semantically corresponds to the external artifact. The external artifact and the capability describe the same behavior. Use this as the default when no more precise relation applies. |
| `detects` | external → capability | The external artifact is a **detection mechanism** for this capability (e.g., a Sigma rule, SIEM query, or audit configuration). The external artifact produces an alert or evidence when this capability is exercised. |
| `validates` | external → capability | The external artifact is a **validation or simulation test** for this capability (e.g., an Atomic Red Team test, a custom adversary simulation). Exercising the external artifact should trigger detections mapped with `detects`. |
| `related_to` | capability ↔ external | A loose semantic relationship. The capability and the external artifact share context or domain but do not precisely describe the same behavior. Use when alignment is partial or inferential. |
| `enables` | capability → external | This capability is a **prerequisite** or necessary condition for the external artifact's function. Example: a persistence capability enables a lateral movement technique. |
| `implements` | external → capability | The external artifact is a **concrete implementation** of this capability. For example, a specific API call or tool command that realizes the abstract capability. |
| `supersedes` | capability → external | This capability replaces or extends the external artifact in a more current version or standard. Used during version transitions. |

### Choosing the Right Relation

```
Does the external artifact describe the same behavior as the capability?
→ Yes → maps_to

Is the external artifact a detection rule or analytic?
→ Yes → detects

Is the external artifact a simulation test or red team procedure?
→ Yes → validates

Does the external artifact require this capability to function?
→ Yes → enables

Is the external artifact a specific API call or command implementing this capability?
→ Yes → implements

Is there only partial or inferred overlap?
→ Yes → related_to
```

### Examples

```json
[
  {
    "framework": "mitre_attack",
    "external_id": "T1053.005",
    "external_name": "Scheduled Task/Job: Scheduled Task",
    "relation": "maps_to",
    "confidence": 0.95
  },
  {
    "framework": "sigma",
    "external_id": "sigma-0001",
    "external_name": "Windows Scheduled Task Creation",
    "relation": "detects",
    "confidence": 0.85,
    "url": "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_creation.yml"
  },
  {
    "framework": "atomic_red_team",
    "external_id": "T1053.005-1",
    "external_name": "At.exe Scheduled Task",
    "relation": "validates",
    "confidence": 0.9
  }
]
```

---

## Graph Edge Types

Used in the OSCO knowledge graph (built by `osco/graph_builder.py`). Graph edges connect
OSCO objects to each other, forming a queryable relationship graph.

| Edge Type | Source → Target | Description |
|---|---|---|
| `implements` | Provider → Capability | The provider exposes or implements this capability. |
| `enables` | Capability → Capability | The source capability is a prerequisite for the target capability. |
| `related_to` | Capability ↔ Capability | Non-hierarchical semantic relationship between capabilities. |
| `maps_to` | Capability → External artifact | The capability corresponds to an external framework artifact. |
| `detects` | Detection → Capability | The detection artifact identifies this capability when exercised. |
| `validates` | Validation → Capability | The validation artifact exercises this capability for test and verification purposes. |
| `parent_of` | Capability → Capability | Hierarchical parent-child relationship (derived from `parent_capability` / `child_capabilities` fields). |

### Graph Query Pattern

To find all Sigma detections for persistence capabilities:

```cypher
MATCH (d:Detection)-[:detects]->(c:Capability {category: "persistence"})
WHERE d.framework = "sigma"
RETURN d.detection_id, d.name, c.capability_id
```

To find all capabilities that enable a given technique:

```cypher
MATCH (prereq:Capability)-[:enables]->(target:Capability {capability_id: "windows.task.create"})
RETURN prereq.capability_id, prereq.name
```

---

## Confidence Scoring Guidelines

All mapping relations include a `confidence` score (0.0–1.0). Use the following guidance
for consistent scoring:

| Score Range | Meaning |
|---|---|
| `0.9 – 1.0` | Authoritative, machine-verified, or directly confirmed by the external framework's maintainers |
| `0.7 – 0.89` | High confidence; based on direct documentation review or multiple independent sources |
| `0.5 – 0.69` | Medium confidence; inferred from related documentation, context, or partial alignment |
| `0.3 – 0.49` | Low confidence; speculative or based on single indirect source |
| `0.0 – 0.29` | Very low confidence; placeholder or highly uncertain; should be reviewed before use |

For `detects` and `validates` relations, confidence reflects the completeness of coverage,
not just the correctness of the mapping. A Sigma rule that only partially covers a capability
(e.g., one of three execution paths) should have confidence ≤ 0.6.

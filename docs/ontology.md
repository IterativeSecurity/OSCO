# Ontology Model

## Capability Naming

Capabilities use dotted semantic identifiers following a `domain.object.action` hierarchy.

Examples:
- `filesystem.file.create`
- `windows.task.create`
- `cloud.iam.role.create`
- `mail.forwarding.create`

Pattern: `^[a-z0-9_]+(\.[a-z0-9_]+)+$` — lowercase letters, digits, and underscores in each segment, separated by dots. A minimum of two segments is required.

Naming rules:
- The first segment is the **domain** (e.g., `filesystem`, `cloud`, `windows`).
- The second segment is the **object** being acted on (e.g., `file`, `iam.role`, `task`).
- The final segment is the **action** verb (e.g., `create`, `delete`, `read`, `modify`).
- Use nouns for objects and verbs for actions. Avoid adjectives and qualifiers in IDs.
- Once a `capability_id` is published with a `stable_id`, it is permanent. Rename via deprecation only.

## Modeling Rules

- Model capability **semantics**, not products or implementations.
- Keep execution details in `execution_metadata`, not in ontology identity or descriptions.
- Keep capability IDs stable once published.
- Use `mappings` objects for external framework relationships; never embed external IDs in `capability_id`.
- Prefer clear, implementation-neutral descriptions. A description must be true regardless of which provider implements it.
- A capability should represent one discrete behavior. Split compound behaviors into separate capabilities linked by `related_capabilities`.

## Domain Taxonomy

Capabilities are organized into operational domains. Each domain groups behaviors by the system surface they act on.
Current primary domains include:

| Domain prefix | Description |
|---|---|
| `ai` | AI assistant, model, and agent operations |
| `auth` | Authentication and session management |
| `browser` | Web browser state, storage, and navigation |
| `cloud` | Cloud platform control-plane operations |
| `cloud.iam` | Cloud identity and access management |
| `cloud.storage` | Cloud object and block storage |
| `container` | Container image, runtime, and orchestration |
| `database` | Database query, schema, and access operations |
| `dns` | DNS query, zone, and record management |
| `email` | Email send, receive, and management |
| `filesystem` | File and directory operations |
| `hardware` | Physical device and firmware operations |
| `identity` | Identity provider, user, and group operations |
| `mail` | Mail relay and forwarding operations |
| `network` | Network traffic, socket, and interface operations |
| `os` | Operating system primitives |
| `process` | Process creation, injection, and lifecycle |
| `registry` | Windows registry key and value operations |
| `saas` | SaaS platform-specific operations |
| `supply_chain` | Software supply chain operations |
| `telemetry` | Observability, logging, and metrics operations |
| `windows` | Windows-specific system operations |
| `workflow` | Business workflow and automation operations |

## Capability Lifecycle

Status transitions follow a defined progression. See [Versioning](versioning.md) for transition criteria.

| Status | Meaning | Stability |
|---|---|---|
| `draft` | Proposal or incomplete coverage. May change without notice. | Unstable |
| `stable` | Validated, reviewed, and actively maintained. ID and semantics are stable. | Stable |
| `deprecated` | Retained for compatibility but not recommended for new use. Migration path documented if available. | No new references |

## Safety Model

The safety classification constrains how a capability may be used in automated workflows.

| Safety | Meaning | Automated use |
|---|---|---|
| `safe` | Read-only or fully reversible. No persistent state changes. No credentials or data at risk. | Permitted without human review |
| `caution` | May alter system state. Cleanup is defined and supported. Limited blast radius. | Requires human review before production use |
| `destructive` | Significant or potentially irreversible state change. Requires privileged access. | Requires explicit authorization and controlled environment |

Safety defaults to `caution` when unspecified. Authors must not downgrade safety to `safe` unless the
capability is verifiably non-destructive in all platforms listed.

## Scope Status

Implemented now:
- Capability naming conventions with schema/model validation
- Lifecycle (`status`) and safety (`safety`) classifications in typed models
- Discovery state progression (`declared` → `proven`)
- Mapping-oriented semantic structure for external framework integration

Planned:
- Additional ontology depth across more specialized capability branches
- Broader cross-framework semantic refinement and normalization
- Formal profile mechanism for reusable capability attribute sets

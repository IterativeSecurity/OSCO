# Field Reference

This document is the authoritative reference for every field in every OSCO object.
It is the equivalent of OCSF's attribute dictionary: each field is listed with its type,
requirement level, valid values, and a semantic description precise enough to populate
correctly from raw data.

Fields marked **Required** must be present for a catalog entry to pass validation.
Fields marked **Optional** have defaults defined in the model when omitted.

---

## Capability

The core object in OSCO. Represents a single, semantically stable security behavior.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `capability_id` | string | Required | — | Dot-separated semantic identifier following the `domain.object.action` convention. Pattern: `^[a-z0-9_]+(\.[a-z0-9_]+)+$`. Example: `filesystem.file.create`. Never changes once published. |
| `stable_id` | string | Required | — | Immutable registry identifier. Format: `OSCO-CAP-NNNN`. Assigned at creation; never reused or reassigned. Used for stable cross-system references. |
| `name` | string | Required | — | Short human-readable name. Should complete "the system can…". Example: `Create File`. |
| `description` | string | Required | — | Implementation-neutral description of what the capability does. Two to three sentences maximum. Must not reference specific vendors, products, or scripts. |
| `category` | string | Required | — | High-level grouping, typically matching the first `capability_id` segment. Example: `filesystem`. |
| `domain` | string | Required | — | Primary operational domain. Drives categorization and corpus organization. Examples: `filesystem`, `cloud.iam`, `windows.task`. |
| `platforms` | array of [Platform](#platform) | Required | — | One or more platforms where this capability is supported. At least one value required. |
| `providers` | array of string | Optional | `[]` | Provider IDs that expose this capability. References entries in `provider/providers.json`. |
| `version` | string | Optional | `"0.1.0"` | Semantic version of this capability entry. Incremented on substantive changes. |
| `status` | [Status](#status) | Optional | `"draft"` | Lifecycle state of the capability. See [Status Lifecycle](versioning.md). |
| `confidence` | float 0–1 | Optional | `0.7` | Author's confidence in the accuracy of this definition. `1.0` = fully validated by multiple sources; `0.0` = speculative. |
| `safety` | [SafetyClassification](#safetyclassification) | Optional | `"caution"` | Risk level of exercising or verifying this capability. Used to gate automated workflows. |
| `parent_capability` | string | Optional | `null` | `capability_id` of the parent in the capability hierarchy. Used for hierarchical browsing. |
| `child_capabilities` | array of string | Optional | `[]` | `capability_id`s of more specific (child) capabilities. |
| `related_capabilities` | array of string | Optional | `[]` | `capability_id`s of semantically related but non-hierarchical capabilities. |
| `required_privileges` | array of string | Optional | `[]` | Privileges, roles, or permissions required to exercise this capability. Example: `SeDebugPrivilege`, `roles/storage.admin`. |
| `required_software` | array of string | Optional | `[]` | Software, agents, or packages that must be installed. Example: `osquery`, `sysmon`. |
| `required_configuration` | array of string | Optional | `[]` | Configuration states that must be active. Example: `audit logging enabled`. |
| `required_dependencies` | array of string | Optional | `[]` | External service or system dependencies. Example: `AWS CloudTrail`, `Azure Monitor`. |
| `preconditions` | array of string | Optional | `[]` | Human-readable descriptions of the system state required before capability execution. |
| `postconditions` | array of string | Optional | `[]` | Expected observable state changes after capability execution completes. |
| `parameters` | object | Optional | `{}` | Named parameter definitions. Keys are parameter names; values describe the parameter. |
| `inputs` | array of string | Optional | `[]` | Named inputs consumed by the capability. Example: `["target_path", "permissions"]`. |
| `outputs` | array of string | Optional | `[]` | Named outputs produced by the capability. Example: `["file_handle", "result_code"]`. |
| `evidence` | array of [Evidence](#evidence) | Optional | `[]` | Observable artifacts that confirm capability execution or state. |
| `produced_artifacts` | array of string | Optional | `[]` | Artifact types created as side effects. Example: `["registry_key", "log_entry"]`. |
| `produced_telemetry` | array of [Telemetry](#telemetry) | Optional | `[]` | Telemetry streams emitted during capability execution. |
| `consumed_telemetry` | array of string | Optional | `[]` | Telemetry stream IDs that this capability reads or depends on. |
| `cleanup_supported` | boolean | Optional | `true` | Whether post-execution cleanup is supported. Set `false` for capabilities that cannot be reversed. |
| `verification_methods` | array of [VerificationMethod](#verificationmethod) | Optional | `[]` | Methods for safely exercising and confirming the capability in a controlled environment. |
| `discovery_methods` | array of [DiscoveryMethod](#discoverymethod) | Optional | `[]` | Methods for detecting whether this capability is supported in a given environment. |
| `execution_metadata` | array of [ExecutionImplementation](#executionimplementation) | Optional | `[]` | Known implementation surfaces (APIs, commands, interfaces) for this capability. |
| `references` | array of string | Optional | `[]` | External reference URLs: documentation, specifications, CVEs, advisories. |
| `mappings` | array of [CapabilityMapping](#capabilitymapping) | Optional | `[]` | References to external security framework artifacts. See [Mapping Guide](mapping-guide.md). |

---

## CapabilityMapping

Links a capability to an artifact in an external security framework.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `framework` | [MappingFramework](#mappingframework) | Required | — | The external framework being referenced. |
| `external_id` | string | Required | — | The identifier used by the external framework. Example: `T1059.001` (ATT&CK), `sigma-4201` (Sigma). |
| `external_name` | string | Required | — | The human-readable name of the external artifact. |
| `relation` | string | Optional | `"maps_to"` | Semantic relationship type. See [Relation Types](relation-types.md) for valid values and semantics. |
| `confidence` | float 0–1 | Optional | `0.8` | Confidence in the accuracy of this specific mapping. `1.0` = machine-verified or authoritative; `0.5` = inferred. |
| `url` | string | Optional | `null` | Direct URL to the external artifact for verification. |

---

## DiscoveryMethod

Describes how to determine whether a capability is supported in a real environment.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `method_id` | string | Required | — | Unique identifier for this discovery method. Convention: `discover.<capability_id>`. |
| `type` | string | Required | — | Mechanism type. Examples: `api_query`, `wmi_query`, `registry_check`, `filesystem_probe`, `audit_api`. |
| `state` | [DiscoveryState](#discoverystate) | Required | — | Confidence level of discovery evidence. |
| `description` | string | Required | — | Human-readable description of the discovery procedure. Should be reproducible by a human or automation. |
| `query` | string | Optional | `null` | Legacy single-provider query string. Prefer `queries[]` for new entries. |
| `queries` | array of [DiscoveryQuery](#discoveryquery) | Optional | `[]` | List of provider-specific query objects. Use when the same capability can be discovered via multiple tools or platforms. |

---

## DiscoveryQuery

A single provider-specific query within a `DiscoveryMethod`.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `provider` | string | Required | — | Tool or runtime that executes the query. Examples: `powershell`, `velociraptor`, `osquery`, `cmd`, `bash`, `aws`, `gcp`, `azure`. |
| `platform` | string | Optional | `null` | OS or environment context. Examples: `windows`, `linux`, `macos`, `cloud`. |
| `query` | string | Required | — | Literal, executable query or command string. Should be copy-pasteable and produce deterministic output. |
| `notes` | string | Optional | `null` | Caveats, prerequisites, or interpretation guidance. Examples: "Requires Sysmon installed", "Heuristic only". |

---

## VerificationMethod

Describes a safe way to exercise and confirm capability behavior.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `method_id` | string | Required | — | Unique identifier. Convention: `verify.<capability_id>`. |
| `type` | string | Required | — | Verification approach. Examples: `safe_execute`, `dry_run`, `passive_observe`, `simulation`. |
| `description` | string | Required | — | Human-readable description of how verification is performed, including cleanup steps. |
| `supports_dry_run` | boolean | Optional | `true` | Whether verification can run without committing state changes. |
| `supports_safe_mode` | boolean | Optional | `true` | Whether verification operates in a constrained safe mode. |
| `supports_cleanup` | boolean | Optional | `true` | Whether post-verification cleanup is available. |
| `supports_rollback` | boolean | Optional | `true` | Whether verification state can be fully rolled back on failure. |

---

## ExecutionImplementation

Documents a known concrete implementation surface for a capability.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `implementation_id` | string | Required | — | Unique identifier for this implementation. |
| `implementation_type` | string | Required | — | Type of implementation surface. Examples: `api`, `cli`, `wmi`, `com`, `syscall`, `sdk`. |
| `interface` | string | Required | — | The specific interface name. Example: `CreateFileW`, `New-ScheduledTask`, `PUT /api/v1/roles`. |
| `language` | string | Optional | `null` | Programming language or scripting environment. Example: `powershell`, `python`, `go`. |
| `artifact` | string | Optional | `null` | Associated binary, module, or package. Example: `kernel32.dll`, `aws-sdk-go`. |
| `notes` | string | Optional | `null` | Implementation-specific notes, version constraints, or known quirks. |

---

## Evidence

Describes an observable artifact that confirms capability execution or current state.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `evidence_id` | string | Required | — | Unique identifier. Convention: `evidence.<capability_id>.<n>`. |
| `type` | string | Required | — | Evidence category. Examples: `file`, `registry_key`, `process`, `network_connection`, `cloud_resource`, `audit_record`, `log_entry`. |
| `description` | string | Required | — | What this artifact is and why its presence confirms the capability. |
| `location` | string | Optional | `null` | Path, key, URL, or query where the artifact can be found. Example: `HKLM\SOFTWARE\...`, `/var/log/audit/audit.log`. |

---

## Telemetry

Describes a log or event stream associated with capability execution.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `telemetry_id` | string | Required | — | Unique identifier. Convention: `telemetry.<capability_id>.<n>`. |
| `source` | string | Required | — | The system or agent that produces this telemetry. Examples: `sysmon`, `cloudtrail`, `auditd`, `windows_event_log`. |
| `event_type` | string | Required | — | The event type or log category emitted. Examples: `ProcessCreate`, `S3.GetObject`, `SYSCALL`. |
| `description` | string | Required | — | What information this telemetry provides about the capability execution. |

---

## Provider

Represents a platform, service, or tool that exposes one or more capabilities.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `provider_id` | string | Required | — | Unique identifier. Convention: `provider.<name>`. Example: `provider.aws`. |
| `name` | string | Required | — | Human-readable name. Example: `Amazon Web Services`. |
| `category` | string | Required | — | Provider type. Examples: `cloud`, `os`, `saas`, `edr`, `siem`, `identity`. |
| `platforms` | array of [Platform](#platform) | Required | — | Platforms this provider operates on. |
| `description` | string | Required | — | Neutral technical description of the provider's scope and capability surface. No marketing language. |
| `homepage` | string | Optional | `null` | URL to provider documentation or homepage. |
| `supports` | array of string | Optional | `[]` | Domains or capability surface areas the provider exposes. Examples: `["cloud.iam", "cloud.storage"]`. |

---

## Detection

Represents a defensive detection artifact mapped to one or more capabilities.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `detection_id` | string | Required | — | Unique identifier. Example: `sigma-4201`, `custom-det-001`. |
| `name` | string | Required | — | Human-readable detection name. |
| `description` | string | Required | — | What behavior this detection identifies and its data source requirements. |
| `mappings` | array of [CapabilityMapping](#capabilitymapping) | Optional | `[]` | Framework references for this detection content. |

---

## Validation

Represents an offensive simulation or test artifact used to verify controls and detections.

| Field | Type | Req | Default | Description |
|---|---|---|---|---|
| `validation_id` | string | Required | — | Unique identifier. Example: `art-t1059.001-01`, `custom-val-001`. |
| `name` | string | Required | — | Human-readable validation name. |
| `description` | string | Required | — | What this validation exercises, its prerequisites, and expected outcomes. |
| `mappings` | array of [CapabilityMapping](#capabilitymapping) | Optional | `[]` | Framework references for this validation artifact. |

---

## Enumerations

### Platform

Valid values for `platforms` fields.

| Value | Description |
|---|---|
| `windows` | Microsoft Windows (desktop and server editions) |
| `linux` | Linux (any distribution) |
| `macos` | Apple macOS |
| `cloud` | Cloud infrastructure: compute, storage, networking, and control-plane APIs |
| `saas` | Software-as-a-Service applications accessed via web or API |
| `container` | Container runtime environments (Docker, containerd, Kubernetes pods) |
| `network` | Network devices, switches, routers, and infrastructure |
| `browser` | Web browser environment and browser-hosted applications |
| `database` | Database management systems |
| `identity` | Identity and access management systems (Active Directory, Okta, etc.) |
| `cross_platform` | Capability applies across multiple or all platforms; platform-agnostic |

### SafetyClassification

Defines the risk level of exercising or verifying a capability.

| Value | Description |
|---|---|
| `safe` | No persistent side effects. Fully reversible. No credentials, data, or system state changed. Suitable for automated testing in any environment. |
| `caution` | May alter system state. Cleanup is defined and supported. Limited blast radius. Requires human review before running in production. |
| `destructive` | Significant or potentially irreversible state change. Requires explicit authorization, privileged access, and a controlled environment. Not suitable for automated execution without human approval. |

### DiscoveryState

Confidence level of evidence that a capability is supported in a given environment.

| Value | Description |
|---|---|
| `declared` | Capability is described in a specification, vendor documentation, or API reference. Not yet confirmed at runtime. |
| `observed` | Capability has been seen in runtime or API surface inspection evidence, but not through a repeatable documented procedure. |
| `verified` | Capability has been confirmed through a repeatable, documented, and auditable check. |
| `proven` | Capability has been repeatedly validated with strong, independent evidence across multiple environments or sources. |

### Status

Lifecycle state of a capability entry.

| Value | Description |
|---|---|
| `draft` | Work in progress. Not yet validated or widely reviewed. May change without notice. |
| `stable` | Reviewed, validated, and ready for production use. ID and semantics are stable. |
| `deprecated` | Superseded or retired. Do not reference in new integrations. See migration guidance if available. |

### MappingFramework

Supported external security framework identifiers.

| Value | Description |
|---|---|
| `mitre_attack` | MITRE ATT&CK Techniques and Sub-Techniques |
| `mitre_car` | MITRE Cyber Analytics Repository |
| `atomic_red_team` | Atomic Red Team test library |
| `velociraptor` | Velociraptor artifact library |
| `sigma` | Sigma generic detection rule format |
| `yara` | YARA malware and pattern detection rules |
| `semgrep` | Semgrep static analysis rules |
| `event_maturity_matrix` | Event Maturity Matrix (telemetry coverage model) |
| `opentelemetry` | OpenTelemetry observability standard |
| `openc2` | OpenC2 actuator profiles and commands |
| `openioc` | OpenIOC indicator of compromise format |
| `stix` | STIX 2.x threat intelligence standard |
| `taxii` | TAXII threat intelligence sharing protocol |
| `cve` | Common Vulnerabilities and Exposures |
| `cwe` | Common Weakness Enumeration |
| `capec` | Common Attack Pattern Enumeration and Classification |
| `cis_benchmarks` | CIS Security Benchmarks |
| `nist_800_53` | NIST SP 800-53 Security Controls |
| `pci_dss` | PCI Data Security Standard |
| `iso_27001` | ISO/IEC 27001 Information Security Management |
| `microsoft_security_baselines` | Microsoft Security Compliance Toolkit baselines |
| `aws_security_hub` | AWS Security Hub findings and standards |
| `google_scc` | Google Cloud Security Command Center findings |
| `ocsf` | Open Cybersecurity Schema Framework event classes |
| `ecs` | Elastic Common Schema fields |
| `osquery` | osquery table and query definitions |

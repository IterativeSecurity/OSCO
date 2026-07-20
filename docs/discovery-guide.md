# Discovery Guide

Discovery metadata describes how capability support is identified in a real environment.
It answers the question: "can this capability actually be used here, and how do we know?"

For field-level reference (types, defaults, required fields), see [Field Reference: DiscoveryMethod](field-reference.md#discoverymethod).

## Discovery States

Discovery state represents the confidence level of evidence that a capability is supported.
States progress from documentation-only to independently proven.

| State | Meaning |
|---|---|
| `declared` | Described in specification, vendor documentation, or API reference. Not yet confirmed at runtime. |
| `observed` | Seen in runtime or API surface inspection, but not via a repeatable documented procedure. |
| `verified` | Confirmed through a repeatable, documented, and auditable check. |
| `proven` | Repeatedly validated with strong, independent evidence across multiple environments or sources. |

For full semantic definitions, see [Field Reference: DiscoveryState](field-reference.md#discoverystate).

## Discovery Method Types

The `type` field on a `DiscoveryMethod` describes the mechanism used to detect capability support.
Common types include:

| Type | Description |
|---|---|
| `api_query` | An API or SDK call that returns capability presence or support |
| `wmi_query` | A WMI or CIM query that enumerates system capabilities |
| `registry_check` | A Windows registry key or value inspection |
| `filesystem_probe` | A filesystem path or file presence check |
| `cloud_control_plane` | A cloud API call that confirms resource or service availability |
| `audit_api` | An audit log or metadata endpoint query |
| `osquery` | An osquery table query |

## Authoring Discovery Methods

For simple single-tool discovery:

```json
{
  "method_id": "discover.windows.task.create",
  "type": "api_query",
  "state": "verified",
  "description": "Query the Windows Task Scheduler COM interface to confirm scheduled task creation support.",
  "query": "Get-ScheduledTask | Select-Object -First 1"
}
```

For capabilities discoverable across multiple tools or platforms, use `queries[]`:

```json
{
  "method_id": "discover.cloud.iam",
  "type": "api",
  "state": "verified",
  "description": "Enumerate IAM roles and policies via the cloud provider's identity management API.",
  "queries": [
    {
      "provider": "aws",
      "platform": "cloud",
      "query": "aws iam list-roles --query 'Roles[*].[RoleName,Arn]' --output table"
    },
    {
      "provider": "gcp",
      "platform": "cloud",
      "query": "gcloud iam roles list --format='table(name,title,stage)'"
    },
    {
      "provider": "azure",
      "platform": "cloud",
      "query": "az role definition list --query '[*].[roleName,roleType]' --output table"
    }
  ]
}
```

## Practical Guidance

- Start with `declared` when bootstrapping a provider. It is valid to have no runtime evidence yet.
- Promote state as operational evidence accumulates. Do not skip states — each represents a distinct evidence threshold.
- Prefer `queries[]` over the legacy `query` field for any new API-based discovery method. It is provider-agnostic and composable.
- Each query in `queries[]` must be a literal, executable command or query string — copy-pasteable, no placeholders.
- Use the `notes` field on a `DiscoveryQuery` to capture caveats (e.g., "Requires Sysmon installed"), not in the query string itself.
- Keep discovery method descriptions reproducible: a human or system following the description should reach the same conclusion.
- A discovery method is not a verification method. Discovery confirms capability support; [verification](verification-guide.md) confirms capability behavior.
- Common `provider` values: `powershell`, `cmd`, `bash`, `velociraptor`, `osquery`, `aws`, `gcp`, `azure`, `wmic`.

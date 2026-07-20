# discovery

This directory contains discovery method definitions for OSCO — techniques for discovering or enumerating security capabilities in systems.

## Purpose

Discovery methods represent ways to detect, query, or enumerate capabilities within a system or environment. They are referenced by capabilities to indicate how that capability can be discovered:

- **Declared**: Capability is only known to exist via documentation or declaration (no active discovery available)
- **API**: Capability can be discovered through active querying of APIs, scripts, or system commands

## Files & Structure

### Discovery Catalog

**[discoveries.json](discoveries.json)** — Central registry of discovery methods
- **method_id**: Unique identifier (e.g., `discover.tasks.api`, `discover.ai.assistant.classify`)
- **type**: Discovery mechanism type (`api` or `declared`)
- **state**: Current discovery state (`verified` for tested APIs, `declared` for declared-only)
- **description**: How the discovery works and what it discovers
- **query** (optional, legacy): Single executable query/command string. Prefer `queries[]` for new entries.
- **queries** (optional): List of provider-specific query objects, each with `provider`, `platform`, `query`, and optional `notes`.

**Current entries (1017):**
- **API-based (13)**: Critical capabilities with verified multi-provider queries
- **Declared (1004)**: All other capabilities are discovered via declaration/documentation

### API-Based Discovery Methods

See [catalog.md](catalog.md) — auto-generated, regenerate with .

## Usage in Capabilities

Capabilities reference discovery methods to indicate how they can be found:

```json
{
  "capability_id": "windows.task.create",
  "discovery_methods": [
    {
      "method_id": "discover.tasks.api",
      "type": "api",
      "state": "verified",
      "description": "Enumerate task scheduler API and cmdlets"
    }
  ]
}
```

## Multi-Provider Queries

For capabilities discoverable across multiple tools or platforms, use the `queries[]` array instead of the legacy `query` field:

```json
{
  "method_id": "discover.windows.services",
  "type": "api",
  "state": "verified",
  "description": "Enumerate Windows services and identify suspicious entries.",
  "queries": [
    {
      "provider": "powershell",
      "platform": "windows",
      "query": "Get-Service | Where-Object {$_.StartType -eq 'Automatic'} | Select-Object Name, DisplayName, Status"
    },
    {
      "provider": "velociraptor",
      "platform": "windows",
      "query": "SELECT * FROM Artifact.Windows.System.Services()"
    },
    {
      "provider": "osquery",
      "platform": "windows",
      "query": "SELECT name, display_name, status, start_type, path FROM services WHERE start_type = 'AUTO_START'"
    }
  ]
}
```

Each query object supports:
- **provider** (required): Tool or runtime — e.g., `powershell`, `velociraptor`, `osquery`, `cmd`, `bash`, `aws`, `gcp`, `azure`
- **platform** (optional): OS or environment — e.g., `windows`, `linux`, `macos`, `cloud`
- **query** (required): Literal executable command or query string
- **notes** (optional): Caveats, prerequisites, or interpretation guidance

## Related Documentation

- [../capability/README.md](../capability/README.md) — Capability catalog structure and governance
- [../osco/models/README.md](../osco/models/README.md) — DiscoveryMethod model definition
- [../scripts/README.md](../scripts/README.md) — Discovery-related validation scripts

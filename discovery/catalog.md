<!-- AUTO-GENERATED — do not edit manually. Regenerate with: make generate  # or: uv run scripts/generate_discovery_readme.py -->

# Discovery Catalog

| Method ID | State | Description | Providers |
|---|---|---|---|
| `discover.cloud.iam` | verified | Enumerate IAM roles and policies via the cloud provider's identity management API | aws, azure, gcp |
| `discover.network.proxy` | verified | Query configured proxy settings and active network connections | bash, cmd, powershell |
| `discover.process.hollow` | verified | Detect hollowed processes by comparing on-disk PE with in-memory image | powershell, velociraptor |
| `discover.process.injection.dll` | verified | Enumerate loaded modules in running processes to detect injected DLLs | osquery, powershell, velociraptor |
| `discover.process.lsass.access` | verified | Enumerate LSASS process handles via process inspection tools | osquery, powershell, velociraptor |
| `discover.registry.run.keys` | verified | Enumerate registry run keys for persistence entries | cmd, powershell, velociraptor |
| `discover.tasks.api` | verified | Enumerate task scheduler API and cmdlets | — |
| `discover.windows.amsi.bypass` | verified | Check AMSI provider registration and amsi.dll integrity | powershell, velociraptor |
| `discover.windows.certutil` | verified | Query recent certutil process executions in event logs | powershell, velociraptor |
| `discover.windows.defender.status` | verified | Query Windows Defender real-time protection status | cmd, powershell, velociraptor |
| `discover.windows.services` | verified | Enumerate Windows services and identify suspicious entries | cmd, osquery, powershell, velociraptor |
| `discover.windows.vss` | verified | Enumerate existing volume shadow copies | cmd, powershell, velociraptor |
| `discover.wmi.subscription` | verified | Enumerate WMI permanent event subscriptions | powershell, velociraptor |

**Total:** 1017 entries — 13 API-based, 1004 declared.
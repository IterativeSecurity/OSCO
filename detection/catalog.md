<!-- AUTO-GENERATED — do not edit manually. Regenerate with: make generate  # or: uv run scripts/generate_detection_readme.py -->

# Detection Catalog

| Detection ID | Name | Severity | Platforms | Capabilities | ATT&CK |
|---|---|---|---|---|---|
| `det.defense.vss.delete.001` | Volume Shadow Copy Deletion via vssadmin or wmic | 🔴 critical | windows | `windows.vss.delete` | T1490 |
| `det.injection.hollow.001` | Process Hollowing via NtUnmapViewOfSection | 🔴 critical | windows | `process.injection.hollow` | T1055.012 |
| `det.credential.lsass.access.001` | LSASS Memory Access from Non-SYSTEM Account | 🟠 high | windows | `process.lsass.access` | T1003.001 |
| `det.defense.amsi.bypass.001` | AMSI Bypass via Memory Patching or Provider Removal | 🟠 high | windows | `windows.amsi.bypass` | T1562.001 |
| `det.defense.defender.disable.001` | Windows Defender Real-Time Protection Disabled | 🟠 high | windows | `windows.defender.disable` | T1562.001 |
| `det.execution.certutil.lolbin.001` | certutil LOLBin Abuse for Download or Decode | 🟠 high | windows | `windows.lolbin.certutil` | T1105, T1140 |
| `det.injection.dll.001` | Suspicious DLL Loaded into Remote Process | 🟠 high | windows | `process.injection.dll` | T1055.001 |
| `det.persistence.service.create.001` | Suspicious Windows Service Created | 🟠 high | windows | `windows.service.create` | T1543.003 |
| `det.persistence.wmi.subscription.001` | WMI Permanent Event Subscription Created | 🟠 high | windows | `wmi.subscription.create` | T1546.003 |
| `det.command_and_control.proxy.tunnel.001` | Suspicious Proxy or Tunnel Configuration for C2 | 🟡 medium | windows, linux, macos | `network.proxy.tunnel` | T1090 |
| `det.discovery.cloud.iam.enumerate.001` | Cloud IAM Role and Policy Enumeration | 🟡 medium | cloud | `cloud.iam.enumerate` | T1069.003 |
| `det.persistence.registry.run.001` | Registry Run Key Persistence | 🟡 medium | windows | `registry.run.persist` | T1547.001 |

**Total:** 12 detections — 🔴 critical: 2, 🟠 high: 7, 🟡 medium: 3.
"""
Critical capabilities for the OSCO gold catalog.

These are hand-authored, practitioner-reviewed capability definitions
for high-value security behaviors missing from auto-generated corpus.

To add a new capability: append an entry to CRITICAL_CAPABILITIES.
Stable IDs must be sequentially assigned and unique across the catalog.
"""
from __future__ import annotations

CRITICAL_CAPABILITIES: list[dict] = [
    {
        "capability_id": "process.lsass.access",
        "stable_id": "OSCO-CAP-0321",
        "name": "Access LSASS Process Memory",
        "description": (
            "Open a handle to the LSASS process (Local Security Authority Subsystem Service) "
            "and read its memory to extract Kerberos tickets, NTLM hashes, and plaintext "
            "credentials cached by WDigest. This is the most common credential dumping technique "
            "and a high-fidelity indicator of credential access activity."
        ),
        "category": "credential_access",
        "domain": "process",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.98,
        "safety": "caution",
        "required_privileges": ["SeDebugPrivilege"],
        "preconditions": ["LSASS process is running", "caller has SeDebugPrivilege or SYSTEM context"],
        "postconditions": ["process handle to lsass.exe", "memory dump of credential material"],
        "inputs": ["target_pid"],
        "outputs": ["credential_material", "memory_dump"],
        "cleanup_supported": False,
        "verification_methods": [
            {
                "method_id": "verify.process.lsass.access",
                "type": "safe_execute",
                "description": "Verify LSASS access detection via handle open without memory read",
                "supports_dry_run": True,
                "supports_safe_mode": True,
                "supports_cleanup": False,
                "supports_rollback": False,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.process.lsass.access",
                "type": "api",
                "state": "verified",
                "description": "Enumerate LSASS process handles via Process Explorer or Get-Process",
                "query": "Get-Process lsass | Select-Object Id, HandleCount",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1003.001", "external_name": "OS Credential Dumping: LSASS Memory", "relation": "maps_to", "confidence": 0.98},
            {"framework": "sigma", "external_id": "win_lsass_access_non_system_account", "external_name": "LSASS Access from Non-SYSTEM Account", "relation": "detected_by", "confidence": 0.92},
            {"framework": "atomic_red_team", "external_id": "T1003.001", "external_name": "LSASS Memory Credential Dump", "relation": "validated_by", "confidence": 0.95},
            {"framework": "velociraptor", "external_id": "Windows.Memory.Acquisition", "external_name": "Memory Acquisition Artifact", "relation": "collected_by", "confidence": 0.88},
        ],
    },
    {
        "capability_id": "windows.vss.delete",
        "stable_id": "OSCO-CAP-0322",
        "name": "Delete Volume Shadow Copies",
        "description": (
            "Delete Windows Volume Shadow Copies (VSS) via vssadmin, wmic, or PowerShell, "
            "preventing system restore and backup recovery after ransomware deployment. "
            "Shadow copy deletion is a near-universal pre-ransomware step and a high-confidence "
            "indicator of destructive intent."
        ),
        "category": "impact",
        "domain": "windows",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.98,
        "safety": "destructive",
        "required_privileges": ["Administrator", "SYSTEM"],
        "preconditions": ["volume shadow copies exist", "administrator context"],
        "postconditions": ["shadow copies deleted", "backup recovery paths removed"],
        "inputs": ["volume"],
        "outputs": [],
        "cleanup_supported": False,
        "verification_methods": [
            {
                "method_id": "verify.windows.vss.delete",
                "type": "safe_execute",
                "description": "Verify VSS enumeration without deletion (list-only mode)",
                "supports_dry_run": True,
                "supports_safe_mode": True,
                "supports_cleanup": False,
                "supports_rollback": False,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.windows.vss",
                "type": "api",
                "state": "verified",
                "description": "Enumerate existing volume shadow copies",
                "query": "vssadmin list shadows",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1490", "external_name": "Inhibit System Recovery", "relation": "maps_to", "confidence": 0.98},
            {"framework": "sigma", "external_id": "win_vssadmin_delete_shadows", "external_name": "Shadow Copies Deletion Using OS Utilities", "relation": "detected_by", "confidence": 0.95},
            {"framework": "atomic_red_team", "external_id": "T1490", "external_name": "Inhibit System Recovery - Delete Shadow Copies", "relation": "validated_by", "confidence": 0.95},
        ],
    },
    {
        "capability_id": "windows.defender.disable",
        "stable_id": "OSCO-CAP-0323",
        "name": "Disable Windows Defender",
        "description": (
            "Disable Windows Defender real-time protection, tamper protection, or "
            "cloud-delivered protection via PowerShell (Set-MpPreference), registry keys, "
            "or Group Policy. Disabling AV is a near-universal pre-ransomware and "
            "post-exploitation step. Often combined with exclusion path additions."
        ),
        "category": "defense_evasion",
        "domain": "windows",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.98,
        "safety": "caution",
        "required_privileges": ["Administrator", "SYSTEM"],
        "preconditions": ["Windows Defender enabled", "administrator privileges"],
        "postconditions": ["real-time protection disabled", "detection gap created"],
        "inputs": [],
        "outputs": [],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.windows.defender.disable",
                "type": "safe_execute",
                "description": "Verify Defender status query without modification",
                "supports_dry_run": True,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.windows.defender.status",
                "type": "api",
                "state": "verified",
                "description": "Query Windows Defender real-time protection status",
                "query": "Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled, TamperProtectionSource",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1562.001", "external_name": "Impair Defenses: Disable or Modify Tools", "relation": "maps_to", "confidence": 0.98},
            {"framework": "sigma", "external_id": "win_susp_disable_defender", "external_name": "Suspicious Windows Defender Disabled via Registry", "relation": "detected_by", "confidence": 0.92},
            {"framework": "atomic_red_team", "external_id": "T1562.001", "external_name": "Disable or Modify Tools", "relation": "validated_by", "confidence": 0.92},
        ],
    },
    {
        "capability_id": "registry.run.persist",
        "stable_id": "OSCO-CAP-0324",
        "name": "Persist via Registry Run Keys",
        "description": (
            "Write to HKLM or HKCU Run/RunOnce registry keys to achieve user-logon "
            "or system-boot persistence. Registry run keys are one of the most common "
            "and oldest persistence mechanisms on Windows. "
            "Keys: HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        ),
        "category": "persistence",
        "domain": "registry",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.98,
        "safety": "caution",
        "required_privileges": ["User (HKCU)", "Administrator (HKLM)"],
        "preconditions": ["registry writable"],
        "postconditions": ["payload executes on next logon or boot"],
        "inputs": ["registry_path", "value_name", "payload_path"],
        "outputs": [],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.registry.run.persist",
                "type": "safe_execute",
                "description": "Verify run key write and validate detection; rollback on cleanup",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.registry.run.keys",
                "type": "api",
                "state": "verified",
                "description": "Enumerate registry run keys for persistence entries",
                "query": "reg query HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1547.001", "external_name": "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder", "relation": "maps_to", "confidence": 0.98},
            {"framework": "sigma", "external_id": "win_registry_persistence_run_key", "external_name": "Registry Persistence via Run Keys", "relation": "detected_by", "confidence": 0.92},
            {"framework": "atomic_red_team", "external_id": "T1547.001", "external_name": "Registry Run Keys Persistence", "relation": "validated_by", "confidence": 0.95},
            {"framework": "velociraptor", "external_id": "Windows.Registry.RunKeys", "external_name": "Registry Run Keys Artifact", "relation": "discovered_by", "confidence": 0.95},
        ],
    },
    {
        "capability_id": "wmi.subscription.create",
        "stable_id": "OSCO-CAP-0325",
        "name": "Create WMI Event Subscription",
        "description": (
            "Create a permanent WMI event subscription (EventFilter + EventConsumer + "
            "FilterToConsumerBinding) for fileless persistence. WMI subscriptions survive "
            "reboots and are stored in the WMI repository, not the file system. "
            "Commonly used by sophisticated actors for long-term stealthy persistence."
        ),
        "category": "persistence",
        "domain": "wmi",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.97,
        "safety": "caution",
        "required_privileges": ["Administrator", "SYSTEM"],
        "preconditions": ["WMI service running", "administrator privileges"],
        "postconditions": ["subscription active in WMI repository", "payload executes on trigger event"],
        "inputs": ["event_filter_query", "consumer_script", "binding_name"],
        "outputs": [],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.wmi.subscription.create",
                "type": "safe_execute",
                "description": "Create test WMI subscription and verify detection; cleanup removes subscription",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.wmi.subscription",
                "type": "api",
                "state": "verified",
                "description": "Enumerate WMI permanent event subscriptions",
                "query": "Get-WMIObject -Namespace root\\subscription -Class __EventFilter",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1546.003", "external_name": "Event Triggered Execution: Windows Management Instrumentation Event Subscription", "relation": "maps_to", "confidence": 0.97},
            {"framework": "sigma", "external_id": "win_wmi_persistence", "external_name": "WMI Persistence", "relation": "detected_by", "confidence": 0.9},
            {"framework": "atomic_red_team", "external_id": "T1546.003", "external_name": "WMI Event Subscription Persistence", "relation": "validated_by", "confidence": 0.92},
            {"framework": "velociraptor", "external_id": "Windows.Persistence.PermanentWMIEvents", "external_name": "Permanent WMI Events", "relation": "discovered_by", "confidence": 0.92},
        ],
    },
    {
        "capability_id": "process.injection.dll",
        "stable_id": "OSCO-CAP-0326",
        "name": "DLL Injection",
        "description": (
            "Inject a DLL into a remote process by writing the DLL path into the target "
            "process memory and calling CreateRemoteThread with LoadLibrary as the start address. "
            "DLL injection is a classic code injection technique used for defense evasion, "
            "persistence, and privilege escalation."
        ),
        "category": "defense_evasion",
        "domain": "process",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.95,
        "safety": "caution",
        "required_privileges": ["SeDebugPrivilege or matching process owner"],
        "preconditions": ["target process running", "DLL available on disk"],
        "postconditions": ["DLL loaded in target process address space", "attacker code executing in target context"],
        "inputs": ["target_pid", "dll_path"],
        "outputs": [],
        "cleanup_supported": False,
        "verification_methods": [
            {
                "method_id": "verify.process.injection.dll",
                "type": "safe_execute",
                "description": "Verify DLL injection detection via benign test DLL in isolated process",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": False,
                "supports_rollback": False,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.process.injection.dll",
                "type": "api",
                "state": "verified",
                "description": "Enumerate loaded modules in running processes to detect injected DLLs",
                "query": "Get-Process | ForEach-Object { $_.Modules } | Where-Object { $_.FileName -notlike 'C:\\Windows\\*' }",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1055.001", "external_name": "Process Injection: Dynamic-link Library Injection", "relation": "maps_to", "confidence": 0.97},
            {"framework": "sigma", "external_id": "win_susp_createremotethread", "external_name": "CreateRemoteThread API Call in Suspicious Context", "relation": "detected_by", "confidence": 0.82},
            {"framework": "atomic_red_team", "external_id": "T1055.001", "external_name": "DLL Injection", "relation": "validated_by", "confidence": 0.9},
        ],
    },
    {
        "capability_id": "process.injection.hollow",
        "stable_id": "OSCO-CAP-0327",
        "name": "Process Hollowing",
        "description": (
            "Create a legitimate process in a suspended state, unmap its original executable "
            "memory, write attacker-controlled payload into the process address space, and "
            "resume execution. Process hollowing allows attacker code to execute under a "
            "legitimate process identity, evading process-based detections."
        ),
        "category": "defense_evasion",
        "domain": "process",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.95,
        "safety": "caution",
        "required_privileges": ["User"],
        "preconditions": ["host process binary accessible"],
        "postconditions": ["payload running under hollowed process identity"],
        "inputs": ["host_process_path", "payload"],
        "outputs": [],
        "cleanup_supported": False,
        "verification_methods": [
            {
                "method_id": "verify.process.injection.hollow",
                "type": "safe_execute",
                "description": "Verify process hollowing detection via known benign payload",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": False,
                "supports_rollback": False,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.process.hollow",
                "type": "api",
                "state": "verified",
                "description": "Detect hollowed processes by comparing on-disk PE with in-memory image",
                "query": "Compare-MemoryAndDiskPE -ProcessName svchost.exe",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1055.012", "external_name": "Process Injection: Process Hollowing", "relation": "maps_to", "confidence": 0.97},
            {"framework": "sigma", "external_id": "win_process_hollow", "external_name": "Hollow Process Creation Indicators", "relation": "detected_by", "confidence": 0.78},
            {"framework": "atomic_red_team", "external_id": "T1055.012", "external_name": "Process Hollowing", "relation": "validated_by", "confidence": 0.9},
        ],
    },
    {
        "capability_id": "windows.amsi.bypass",
        "stable_id": "OSCO-CAP-0328",
        "name": "Bypass AMSI",
        "description": (
            "Bypass the Antimalware Scan Interface (AMSI) by patching the AmsiScanBuffer "
            "function in amsi.dll, loading a null AMSI provider, or corrupting the AMSI "
            "context in memory. AMSI bypass is a prerequisite for many in-memory "
            "script-based attacks and PowerShell post-exploitation frameworks."
        ),
        "category": "defense_evasion",
        "domain": "windows",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.95,
        "safety": "caution",
        "required_privileges": ["User"],
        "preconditions": ["PowerShell or .NET runtime running", "AMSI enabled"],
        "postconditions": ["AMSI scanning disabled in current process", "malicious scripts execute unscanned"],
        "inputs": [],
        "outputs": [],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.windows.amsi.bypass",
                "type": "safe_execute",
                "description": "Verify AMSI bypass detection by patching with known benign string",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.windows.amsi.bypass",
                "type": "api",
                "state": "verified",
                "description": "Check AMSI provider registration and amsi.dll integrity",
                "query": "Get-ItemProperty 'HKLM:\\SOFTWARE\\Microsoft\\AMSI\\Providers'",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1562.001", "external_name": "Impair Defenses: Disable or Modify Tools", "relation": "maps_to", "confidence": 0.92},
            {"framework": "sigma", "external_id": "win_amsi_bypass", "external_name": "AMSI Bypass Pattern in PowerShell", "relation": "detected_by", "confidence": 0.88},
            {"framework": "atomic_red_team", "external_id": "T1562.001", "external_name": "AMSI Bypass Techniques", "relation": "validated_by", "confidence": 0.88},
        ],
    },
    {
        "capability_id": "network.proxy.tunnel",
        "stable_id": "OSCO-CAP-0329",
        "name": "Establish Network Proxy Tunnel",
        "description": (
            "Establish a proxy or tunnel for command-and-control traffic to route "
            "through intermediate hosts, bypass network controls, or obfuscate the "
            "true C2 destination. Includes SOCKS proxies, SSH tunnels, DNS-over-HTTPS "
            "tunneling, and multi-hop proxy chains."
        ),
        "category": "command_and_control",
        "domain": "network",
        "platforms": ["windows", "linux", "macos", "cloud"],
        "providers": ["provider.windows", "provider.linux", "provider.macos"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.88,
        "safety": "caution",
        "required_privileges": ["User"],
        "preconditions": ["network access available", "proxy/tunnel binary or capability available"],
        "postconditions": ["C2 traffic obfuscated or relayed through proxy"],
        "inputs": ["proxy_host", "proxy_port", "tunnel_type"],
        "outputs": ["proxy_endpoint"],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.network.proxy.tunnel",
                "type": "safe_execute",
                "description": "Verify proxy tunnel establishment detection in isolated network",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.network.proxy",
                "type": "api",
                "state": "verified",
                "description": "Query configured proxy settings and active network connections",
                "query": "netsh winhttp show proxy",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1090", "external_name": "Proxy", "relation": "maps_to", "confidence": 0.88},
            {"framework": "mitre_attack", "external_id": "T1090.003", "external_name": "Proxy: Multi-hop Proxy", "relation": "maps_to", "confidence": 0.82},
            {"framework": "sigma", "external_id": "win_susp_proxy_settings", "external_name": "Suspicious Proxy Settings Change", "relation": "detected_by", "confidence": 0.78},
        ],
    },
    {
        "capability_id": "windows.service.create",
        "stable_id": "OSCO-CAP-0330",
        "name": "Create Windows Service for Persistence",
        "description": (
            "Create a Windows service via sc.exe, New-Service, or the Service Control "
            "Manager API to execute arbitrary binaries or commands with SYSTEM privileges "
            "on startup. Service creation is a heavily-used persistence and privilege "
            "escalation technique, and a key lateral movement vector when combined with "
            "remote service creation (PsExec-style execution)."
        ),
        "category": "persistence",
        "domain": "windows",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.97,
        "safety": "caution",
        "required_privileges": ["Administrator"],
        "preconditions": ["administrator context", "service binary accessible"],
        "postconditions": ["service registered", "payload executes as SYSTEM on next start"],
        "inputs": ["service_name", "binary_path", "start_type"],
        "outputs": [],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.windows.service.create",
                "type": "safe_execute",
                "description": "Create benign test service and verify detection; sc delete on cleanup",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.windows.services",
                "type": "api",
                "state": "verified",
                "description": "Enumerate Windows services and identify suspicious entries",
                "query": "Get-Service | Where-Object {$_.StartType -eq 'Automatic'} | Select-Object Name, DisplayName, Status",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1543.003", "external_name": "Create or Modify System Process: Windows Service", "relation": "maps_to", "confidence": 0.98},
            {"framework": "sigma", "external_id": "win_susp_service_install", "external_name": "Suspicious Service Installation", "relation": "detected_by", "confidence": 0.88},
            {"framework": "atomic_red_team", "external_id": "T1543.003", "external_name": "Windows Service Creation", "relation": "validated_by", "confidence": 0.95},
            {"framework": "velociraptor", "external_id": "Windows.System.Services", "external_name": "Windows Services Artifact", "relation": "discovered_by", "confidence": 0.92},
        ],
    },
    {
        "capability_id": "windows.lolbin.certutil",
        "stable_id": "OSCO-CAP-0331",
        "name": "Abuse Certutil for Download or Decode",
        "description": (
            "Abuse certutil.exe (a legitimate Windows certificate utility) to download "
            "files from remote URLs or decode Base64-encoded payloads. Certutil is a "
            "classic living-off-the-land binary (LOLBin) that bypasses application "
            "whitelisting by operating as a trusted Microsoft binary."
        ),
        "category": "defense_evasion",
        "domain": "windows",
        "platforms": ["windows"],
        "providers": ["provider.windows"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.95,
        "safety": "caution",
        "required_privileges": ["User"],
        "preconditions": ["certutil.exe available (default Windows install)"],
        "postconditions": ["payload downloaded or decoded to disk"],
        "inputs": ["url_or_encoded_file", "output_path"],
        "outputs": ["decoded_or_downloaded_file"],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.windows.lolbin.certutil",
                "type": "safe_execute",
                "description": "Verify certutil decode detection using known benign Base64 test file",
                "supports_dry_run": False,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.windows.certutil",
                "type": "api",
                "state": "verified",
                "description": "Query recent certutil process executions in event logs",
                "query": "Get-WinEvent -LogName Security | Where-Object { $_.Message -like '*certutil*' }",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1140", "external_name": "Deobfuscate/Decode Files or Information", "relation": "maps_to", "confidence": 0.88},
            {"framework": "mitre_attack", "external_id": "T1105", "external_name": "Ingress Tool Transfer", "relation": "maps_to", "confidence": 0.85},
            {"framework": "sigma", "external_id": "win_susp_certutil_encode", "external_name": "Certutil Encode Usage", "relation": "detected_by", "confidence": 0.92},
            {"framework": "atomic_red_team", "external_id": "T1140", "external_name": "Certutil Decode", "relation": "validated_by", "confidence": 0.92},
        ],
    },
    {
        "capability_id": "cloud.iam.enumerate",
        "stable_id": "OSCO-CAP-0332",
        "name": "Enumerate Cloud IAM Permissions",
        "description": (
            "Enumerate IAM roles, policies, and effective permissions for users, "
            "service accounts, or assumed roles in a cloud environment. "
            "IAM enumeration is a critical cloud reconnaissance step to identify "
            "over-privileged identities and privilege escalation paths."
        ),
        "category": "discovery",
        "domain": "cloud",
        "platforms": ["cloud"],
        "providers": ["provider.aws", "provider.azure", "provider.gcp"],
        "version": "0.1.0",
        "status": "stable",
        "confidence": 0.92,
        "safety": "safe",
        "required_privileges": ["iam:ListRoles", "iam:GetPolicy", "iam:SimulatePrincipalPolicy"],
        "preconditions": ["valid cloud credentials", "IAM read permissions"],
        "postconditions": ["IAM inventory collected", "privilege escalation paths identified"],
        "inputs": ["account_id", "principal_arn"],
        "outputs": ["iam_roles", "iam_policies", "effective_permissions"],
        "cleanup_supported": True,
        "verification_methods": [
            {
                "method_id": "verify.cloud.iam.enumerate",
                "type": "safe_execute",
                "description": "Verify IAM enumeration detection via CloudTrail/audit log monitoring",
                "supports_dry_run": True,
                "supports_safe_mode": True,
                "supports_cleanup": True,
                "supports_rollback": True,
            }
        ],
        "discovery_methods": [
            {
                "method_id": "discover.cloud.iam",
                "type": "api",
                "state": "verified",
                "description": "Enumerate IAM roles and policies via cloud provider API",
                "query": "aws iam list-roles --query 'Roles[*].[RoleName,Arn]' --output table",
            }
        ],
        "mappings": [
            {"framework": "mitre_attack", "external_id": "T1069.003", "external_name": "Permission Groups Discovery: Cloud Groups", "relation": "maps_to", "confidence": 0.85},
            {"framework": "mitre_attack", "external_id": "T1078.004", "external_name": "Valid Accounts: Cloud Accounts", "relation": "enables", "confidence": 0.78},
            {"framework": "aws_security_hub", "external_id": "IAM.1", "external_name": "IAM policies should not allow full '*' administrative privileges", "relation": "maps_to", "confidence": 0.82},
        ],
    },
]

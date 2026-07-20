"""
Curated framework mappings for OSCO capabilities.

Each entry is a verified cross-reference from an OSCO capability ID to a
real external framework identifier. Only add mappings you can directly
validate against the source framework — no placeholder IDs.

To add a new mapping: add an entry to CURATED_MAPPINGS keyed by capability_id.
To add a new description: add an entry to CURATED_DESCRIPTIONS.
"""
from __future__ import annotations


def _m(
    framework: str,
    external_id: str,
    external_name: str,
    relation: str = "maps_to",
    confidence: float = 0.9,
) -> dict:
    """Build a mapping dict with consistent field ordering."""
    return {
        "framework": framework,
        "external_id": external_id,
        "external_name": external_name,
        "relation": relation,
        "confidence": confidence,
    }


# ---------------------------------------------------------------------------
# Curated descriptions: replace auto-generated "Perform X on Y in Z domain."
# with practitioner-authored descriptions.
# ---------------------------------------------------------------------------
CURATED_DESCRIPTIONS: dict[str, str] = {
    "audit.event.disable": (
        "Disable Windows audit event logging categories via auditpol or Group Policy, "
        "removing the telemetry needed to detect attacker activity."
    ),
    "audit.event.enable": (
        "Enable Windows audit event logging categories to restore security monitoring visibility."
    ),
    "cloud.bucket.create": (
        "Create a cloud storage bucket (S3, GCS, Azure Blob), "
        "which may be used to stage data for exfiltration."
    ),
    "cloud.bucket.read": (
        "Read objects from a cloud storage bucket (S3, GCS, Azure Blob). "
        "Commonly used for data exfiltration or discovery of sensitive stored data."
    ),
    "com.activation.modify": (
        "Modify COM server activation entries in the registry to hijack COM object "
        "instantiation for persistent execution."
    ),
    "com.activation.register": (
        "Register a COM server activation entry, which can be abused to hijack COM "
        "object invocation for persistence or privilege escalation."
    ),
    "credential.credential.access": (
        "Access stored credentials from the operating system, "
        "password managers, browser stores, or application credential stores."
    ),
    "credential.credential.dump": (
        "Extract credentials from the operating system credential store, "
        "LSASS memory, or SAM database."
    ),
    "credential.hash.access": (
        "Access NTLM password hashes from SAM, NTDS.dit, or memory, "
        "enabling offline cracking or pass-the-hash authentication."
    ),
    "credential.hash.dump": (
        "Extract NTLM password hashes from the Security Account Manager (SAM) "
        "database or from domain controller NTDS.dit."
    ),
    "credential.token.dump": (
        "Extract OAuth tokens, STS tokens, or session tokens from browser storage, "
        "memory, or credential managers."
    ),
    "dns.query.create": (
        "Resolve DNS names through configured resolvers. May be observed during "
        "C2 beaconing, DNS tunneling, or domain generation algorithm (DGA) activity."
    ),
    "driver.driver.install": (
        "Install a kernel-mode driver for autostart on boot, "
        "achieving persistent kernel-level access or control."
    ),
    "driver.driver.load": (
        "Load a kernel-mode driver into the running OS. May be used for rootkit "
        "functionality, detection evasion, or direct kernel object manipulation (DKOM)."
    ),
    "etw.consumer.stop": (
        "Stop or disable an ETW consumer session, disrupting telemetry collection "
        "and potentially blinding endpoint detection tooling."
    ),
    "eventlog.channel.clear": (
        "Clear Windows Event Log channels (Security, System, Application) to destroy "
        "forensic evidence of attacker activity prior to or during an incident."
    ),
    "firewall.exception.create": (
        "Create a Windows Firewall exception rule to allow previously blocked "
        "traffic, commonly used to enable inbound C2 or lateral movement connections."
    ),
    "firewall.exception.disable": (
        "Disable or remove Windows Firewall rules to weaken network security controls "
        "and permit blocked traffic flows."
    ),
    "identity.federation.create": (
        "Create or modify an identity federation trust relationship "
        "(e.g., SAML trust, OIDC federation), enabling cross-domain authentication "
        "and potential credential access across trust boundaries."
    ),
    "kerberos.delegation.delegate": (
        "Perform Kerberos delegation using an account with delegation rights, "
        "enabling impersonation of user credentials for lateral movement "
        "or privilege escalation."
    ),
    "kerberos.delegation.request": (
        "Request a Kerberos Service Ticket (TGS) for a target SPN. "
        "Encrypted tickets can be extracted and cracked offline in Kerberoasting attacks."
    ),
    "kernel.extension.load": (
        "Load a kernel extension or module, which may implement rootkit functionality, "
        "hook system calls, or provide persistent kernel-level access."
    ),
    "kubernetes.configmap.exec": (
        "Execute commands within a running Kubernetes container via kubectl exec "
        "or the Kubernetes API server, enabling container escape or lateral movement."
    ),
    "memory.dump.dump": (
        "Dump process memory to disk or over the network. Most commonly observed "
        "targeting LSASS.exe to extract plaintext credentials and NTLM hashes."
    ),
    "memory.dump.read": (
        "Read process memory directly, bypassing file system controls. "
        "Primarily used to extract credentials from LSASS process memory."
    ),
    "named_pipe.server.create": (
        "Create a named pipe server endpoint. Named pipes are used for inter-process "
        "communication and can be abused for lateral movement or token impersonation."
    ),
    "powershell.command.constrain": (
        "Enforce PowerShell Constrained Language Mode (CLM) to limit available "
        "commands and reduce the attack surface of script-based execution."
    ),
    "powershell.command.execute": (
        "Execute a PowerShell command, script block, or encoded payload. "
        "PowerShell is the most widely abused scripting engine for living-off-the-land attacks."
    ),
    "privilege.context.delegate": (
        "Delegate process privilege context by duplicating or impersonating "
        "higher-privileged access tokens."
    ),
    "privilege.context.escalate": (
        "Escalate process privilege context via token manipulation, exploitation, "
        "or abuse of privileged system calls."
    ),
    "process.argument.inject": (
        "Inject content into process arguments or command line, "
        "enabling argument spoofing or command injection via process creation."
    ),
    "rpc.binding.invoke": (
        "Invoke a remote RPC/DCOM method, which can be used for lateral movement "
        "by executing code on a remote host via the Distributed Component Object Model."
    ),
    "service.binary.create": (
        "Create a new Windows service binary or service registration, "
        "commonly used for persistence and privilege escalation to SYSTEM."
    ),
    "service.binary.modify": (
        "Modify an existing Windows service binary path or configuration, "
        "enabling persistence via service hijacking."
    ),
    "smb.file.connect": (
        "Connect to a remote SMB share, used for lateral movement via "
        "admin shares (C$, ADMIN$) or for accessing network-shared files."
    ),
    "smb.file.mount": (
        "Mount a remote SMB share locally, enabling file access across "
        "Windows network shares including administrative shares."
    ),
    "wmi.class.create": (
        "Create a WMI class, which can be used to store attacker data or "
        "establish WMI event subscription persistence."
    ),
}


# ---------------------------------------------------------------------------
# Curated mappings: verified cross-references to external frameworks.
# Only include external_ids that exist in the real source framework.
# ---------------------------------------------------------------------------
CURATED_MAPPINGS: dict[str, list[dict]] = {
    "audit.event.disable": [
        _m("mitre_attack", "T1562.002", "Impair Defenses: Disable Windows Event Logging", confidence=0.95),
        _m("sigma", "win_susp_auditpol_usage", "Suspicious Auditpol Usage", relation="detected_by", confidence=0.88),
    ],
    "audit.event.enable": [
        _m("mitre_attack", "T1562.002", "Impair Defenses: Disable Windows Event Logging", relation="mitigates", confidence=0.85),
    ],
    "authentication.challenge.request": [
        _m("mitre_attack", "T1110", "Brute Force", relation="enables", confidence=0.65),
    ],
    "cloud.bucket.create": [
        _m("mitre_attack", "T1537", "Transfer Data to Cloud Account", relation="enables", confidence=0.72),
    ],
    "cloud.bucket.delete": [
        _m("mitre_attack", "T1485", "Data Destruction", relation="maps_to", confidence=0.7),
    ],
    "cloud.bucket.read": [
        _m("mitre_attack", "T1530", "Data from Cloud Storage", confidence=0.95),
        _m("aws_security_hub", "S3.1", "S3 Block Public Access Settings", relation="maps_to", confidence=0.75),
    ],
    "com.activation.modify": [
        _m("mitre_attack", "T1546.015", "Event Triggered Execution: Component Object Model Hijacking", confidence=0.85),
    ],
    "com.activation.register": [
        _m("mitre_attack", "T1546.015", "Event Triggered Execution: Component Object Model Hijacking", confidence=0.8),
    ],
    "credential.credential.access": [
        _m("mitre_attack", "T1003", "OS Credential Dumping", confidence=0.88),
    ],
    "credential.credential.dump": [
        _m("mitre_attack", "T1003", "OS Credential Dumping", confidence=0.95),
        _m("atomic_red_team", "T1003", "OS Credential Dumping", relation="validated_by", confidence=0.9),
    ],
    "credential.hash.access": [
        _m("mitre_attack", "T1003.002", "OS Credential Dumping: Security Account Manager", confidence=0.85),
    ],
    "credential.hash.dump": [
        _m("mitre_attack", "T1003.002", "OS Credential Dumping: Security Account Manager", confidence=0.9),
        _m("atomic_red_team", "T1003.002", "Security Account Manager Dump", relation="validated_by", confidence=0.88),
    ],
    "credential.token.access": [
        _m("mitre_attack", "T1528", "Steal Application Access Token", confidence=0.78),
    ],
    "credential.token.dump": [
        _m("mitre_attack", "T1134.001", "Access Token Manipulation: Token Impersonation/Theft", confidence=0.82),
        _m("mitre_attack", "T1528", "Steal Application Access Token", relation="maps_to", confidence=0.75),
    ],
    "dns.query.create": [
        _m("mitre_attack", "T1071.004", "Application Layer Protocol: DNS", confidence=0.8),
        _m("ocsf", "dns_activity", "DNS Activity Event", confidence=0.88),
    ],
    "driver.driver.install": [
        _m("mitre_attack", "T1547.006", "Boot or Logon Autostart Execution: Kernel Modules and Extensions", confidence=0.88),
        _m("sigma", "win_susp_driver_load", "Suspicious Driver Loaded by User", relation="detected_by", confidence=0.82),
    ],
    "driver.driver.load": [
        _m("mitre_attack", "T1014", "Rootkit", confidence=0.72),
        _m("mitre_attack", "T1547.006", "Boot or Logon Autostart Execution: Kernel Modules and Extensions", relation="maps_to", confidence=0.8),
        _m("sigma", "win_susp_driver_load", "Suspicious Driver Loaded by User", relation="detected_by", confidence=0.85),
    ],
    "etw.consumer.start": [
        _m("mitre_attack", "T1562.006", "Impair Defenses: Indicator Blocking", relation="enables", confidence=0.78),
    ],
    "etw.consumer.stop": [
        _m("mitre_attack", "T1562.006", "Impair Defenses: Indicator Blocking", confidence=0.85),
    ],
    "eventlog.channel.clear": [
        _m("mitre_attack", "T1070.001", "Indicator Removal: Clear Windows Event Logs", confidence=0.98),
        _m("sigma", "win_event_log_cleared", "Windows Event Log Cleared", relation="detected_by", confidence=0.92),
        _m("velociraptor", "Windows.EventLogs.EvtxHunter", "EvtxHunter Artifact", relation="collected_by", confidence=0.85),
        _m("atomic_red_team", "T1070.001", "Clear Windows Event Logs", relation="validated_by", confidence=0.92),
    ],
    "firewall.exception.create": [
        _m("mitre_attack", "T1562.004", "Impair Defenses: Disable or Modify System Firewall", confidence=0.88),
        _m("sigma", "win_susp_netsh_firewall_disabled", "Firewall Disabled via Netsh", relation="detected_by", confidence=0.85),
    ],
    "firewall.exception.disable": [
        _m("mitre_attack", "T1562.004", "Impair Defenses: Disable or Modify System Firewall", confidence=0.92),
    ],
    "identity.federation.create": [
        _m("mitre_attack", "T1484.002", "Domain Policy Modification: Domain Trust Modification", confidence=0.85),
    ],
    "identity.federation.delete": [
        _m("mitre_attack", "T1484.002", "Domain Policy Modification: Domain Trust Modification", relation="maps_to", confidence=0.72),
    ],
    "kerberos.delegation.delegate": [
        _m("mitre_attack", "T1558", "Steal or Forge Kerberos Tickets", confidence=0.82),
        _m("mitre_attack", "T1550.003", "Use Alternate Authentication Material: Pass the Ticket", relation="enables", confidence=0.78),
    ],
    "kerberos.delegation.request": [
        _m("mitre_attack", "T1558.003", "Steal or Forge Kerberos Tickets: Kerberoasting", confidence=0.88),
        _m("sigma", "win_susp_kerberoasting", "Kerberoasting Activity", relation="detected_by", confidence=0.88),
        _m("atomic_red_team", "T1558.003", "Kerberoasting", relation="validated_by", confidence=0.9),
    ],
    "kernel.extension.load": [
        _m("mitre_attack", "T1014", "Rootkit", confidence=0.75),
        _m("mitre_attack", "T1547.006", "Boot or Logon Autostart Execution: Kernel Modules and Extensions", relation="maps_to", confidence=0.8),
    ],
    "kubernetes.configmap.create": [
        _m("mitre_attack", "T1610", "Deploy Container", relation="enables", confidence=0.72),
    ],
    "kubernetes.configmap.exec": [
        _m("mitre_attack", "T1609", "Container Administration Command", confidence=0.88),
        _m("mitre_attack", "T1610", "Deploy Container", relation="enables", confidence=0.7),
    ],
    "memory.dump.allocate": [
        _m("mitre_attack", "T1055", "Process Injection", relation="enables", confidence=0.75),
    ],
    "memory.dump.dump": [
        _m("mitre_attack", "T1003.001", "OS Credential Dumping: LSASS Memory", confidence=0.92),
        _m("atomic_red_team", "T1003.001", "LSASS Memory Credential Dump", relation="validated_by", confidence=0.9),
    ],
    "memory.dump.read": [
        _m("mitre_attack", "T1003.001", "OS Credential Dumping: LSASS Memory", confidence=0.92),
        _m("sigma", "win_lsass_dump_comsvcs_minidump", "LSASS Dump via Comsvcs DLL", relation="detected_by", confidence=0.88),
        _m("velociraptor", "Windows.Memory.Acquisition", "Memory Acquisition Artifact", relation="collected_by", confidence=0.82),
    ],
    "named_pipe.client.connect": [
        _m("mitre_attack", "T1559.001", "Inter-Process Communication: Component Object Model", relation="maps_to", confidence=0.6),
    ],
    "named_pipe.server.create": [
        _m("mitre_attack", "T1559.001", "Inter-Process Communication: Component Object Model", relation="maps_to", confidence=0.65),
    ],
    "network.connection.monitor": [
        _m("mitre_attack", "T1040", "Network Sniffing", confidence=0.75),
    ],
    "powershell.command.constrain": [
        _m("mitre_attack", "T1059.001", "Command and Scripting Interpreter: PowerShell", relation="mitigates", confidence=0.82),
    ],
    "powershell.command.execute": [
        _m("mitre_attack", "T1059.001", "Command and Scripting Interpreter: PowerShell", confidence=0.98),
        _m("sigma", "win_susp_powershell_encode", "Suspicious PowerShell Encoded Command", relation="detected_by", confidence=0.88),
        _m("atomic_red_team", "T1059.001", "PowerShell Execution", relation="validated_by", confidence=0.95),
    ],
    "privilege.context.delegate": [
        _m("mitre_attack", "T1134.001", "Access Token Manipulation: Token Impersonation/Theft", confidence=0.82),
    ],
    "privilege.context.escalate": [
        _m("mitre_attack", "T1134", "Access Token Manipulation", confidence=0.82),
        _m("mitre_attack", "T1068", "Exploitation for Privilege Escalation", relation="maps_to", confidence=0.72),
    ],
    "process.argument.inject": [
        _m("mitre_attack", "T1055", "Process Injection", confidence=0.85),
    ],
    "rpc.binding.invoke": [
        _m("mitre_attack", "T1021.003", "Remote Services: Distributed Component Object Model", confidence=0.82),
    ],
    "service.binary.create": [
        _m("mitre_attack", "T1543.003", "Create or Modify System Process: Windows Service", confidence=0.88),
        _m("sigma", "win_susp_service_install", "Suspicious Service Installation", relation="detected_by", confidence=0.85),
        _m("velociraptor", "Windows.System.Services", "Windows Services Artifact", relation="discovered_by", confidence=0.88),
    ],
    "service.binary.modify": [
        _m("mitre_attack", "T1543.003", "Create or Modify System Process: Windows Service", confidence=0.85),
    ],
    "smb.file.connect": [
        _m("mitre_attack", "T1021.002", "Remote Services: SMB/Windows Admin Shares", confidence=0.82),
    ],
    "smb.file.mount": [
        _m("mitre_attack", "T1021.002", "Remote Services: SMB/Windows Admin Shares", confidence=0.85),
    ],
    "smb.file.read": [
        _m("mitre_attack", "T1039", "Data from Network Shared Drive", confidence=0.8),
    ],
    "token.access_token.issue": [
        _m("mitre_attack", "T1134.001", "Access Token Manipulation: Token Impersonation/Theft", relation="enables", confidence=0.72),
    ],
    "wmi.class.create": [
        _m("mitre_attack", "T1546.003", "Event Triggered Execution: WMI Event Subscription", relation="enables", confidence=0.7),
    ],
}

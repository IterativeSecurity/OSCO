from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "capability" / "catalog.json"


def titleize(token: str) -> str:
    return token.replace("_", " ").replace(".", " ").title()


def provider_set(*provider_ids: str) -> list[str]:
    return sorted(set(provider_ids))


def generate() -> list[dict]:
    existing = json.loads(CATALOG_PATH.read_text())
    existing_ids = {item["capability_id"] for item in existing}

    framework_cycle = [
        "mitre_attack",
        "sigma",
        "ocsf",
        "ecs",
        "atomic_red_team",
        "velociraptor",
        "osquery",
        "event_maturity_matrix",
    ]

    specs: list[dict] = [
        {
            "domain": "filesystem",
            "objects": ["file", "directory", "link", "permission", "metadata"],
            "actions": ["create", "read", "modify", "delete", "list", "hash"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos", "container"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.docker"),
            "safety": "caution",
        },
        {
            "domain": "registry",
            "objects": ["key", "value", "hive", "permission"],
            "actions": ["set", "read", "delete", "enumerate", "backup"],
            "category": "endpoint",
            "platforms": ["windows"],
            "providers": provider_set("provider.windows"),
            "safety": "caution",
        },
        {
            "domain": "process",
            "objects": ["process", "token", "argument", "environment"],
            "actions": ["create", "read", "modify", "inject", "terminate", "enumerate"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "thread",
            "objects": ["thread", "context", "stack"],
            "actions": ["create", "suspend", "resume", "inspect", "inject"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "memory",
            "objects": ["region", "page", "process_memory", "dump"],
            "actions": ["read", "write", "allocate", "protect", "dump"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "service",
            "objects": ["service", "config", "binary", "permission"],
            "actions": ["create", "modify", "start", "stop", "delete", "query"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "scheduled_task",
            "objects": ["task", "trigger", "action", "principal"],
            "actions": ["create", "modify", "delete", "query", "run"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "driver",
            "objects": ["driver", "driver_service", "driver_signature"],
            "actions": ["load", "unload", "install", "query", "verify"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "destructive",
        },
        {
            "domain": "kernel",
            "objects": ["module", "hook", "syscall", "extension"],
            "actions": ["load", "modify", "inspect", "register", "remove"],
            "category": "endpoint",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "destructive",
        },
        {
            "domain": "credential",
            "objects": ["credential", "hash", "token", "vault"],
            "actions": ["access", "dump", "rotate", "store", "delete"],
            "category": "identity",
            "platforms": ["windows", "linux", "macos", "cloud", "saas"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.okta", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "browser",
            "objects": ["cookie", "session", "history", "extension", "storage"],
            "actions": ["read", "write", "delete", "export", "import"],
            "category": "browser",
            "platforms": ["browser", "windows", "linux", "macos"],
            "providers": provider_set("provider.chrome", "provider.firefox"),
            "safety": "caution",
        },
        {
            "domain": "certificate",
            "objects": ["certificate", "store", "private_key", "trust_anchor"],
            "actions": ["create", "read", "import", "revoke", "delete"],
            "category": "identity",
            "platforms": ["windows", "linux", "macos", "cloud"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "eventlog",
            "objects": ["channel", "event", "subscription", "retention"],
            "actions": ["read", "write", "clear", "export", "configure"],
            "category": "telemetry",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "telemetry",
            "objects": ["stream", "collector", "pipeline", "sink"],
            "actions": ["enable", "disable", "query", "route", "transform"],
            "category": "telemetry",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp", "provider.github"),
            "safety": "safe",
        },
        {
            "domain": "etw",
            "objects": ["provider", "session", "consumer", "trace"],
            "actions": ["start", "stop", "subscribe", "emit", "parse"],
            "category": "telemetry",
            "platforms": ["windows"],
            "providers": provider_set("provider.windows"),
            "safety": "caution",
        },
        {
            "domain": "identity",
            "objects": ["user", "group", "service_principal", "federation"],
            "actions": ["create", "read", "update", "delete", "enumerate"],
            "category": "identity",
            "platforms": ["cloud", "saas", "identity"],
            "providers": provider_set("provider.okta", "provider.aws", "provider.azure", "provider.gcp", "provider.github", "provider.microsoft365", "provider.google_workspace"),
            "safety": "caution",
        },
        {
            "domain": "authentication",
            "objects": ["session", "challenge", "factor", "token"],
            "actions": ["request", "validate", "refresh", "revoke", "enforce"],
            "category": "identity",
            "platforms": ["identity", "cloud", "saas"],
            "providers": provider_set("provider.okta", "provider.aws", "provider.azure", "provider.gcp", "provider.github"),
            "safety": "caution",
        },
        {
            "domain": "authorization",
            "objects": ["role", "policy", "permission", "binding"],
            "actions": ["grant", "revoke", "attach", "detach", "evaluate"],
            "category": "identity",
            "platforms": ["identity", "cloud", "saas", "database"],
            "providers": provider_set("provider.okta", "provider.aws", "provider.azure", "provider.gcp", "provider.github", "provider.sql_server", "provider.postgresql"),
            "safety": "caution",
        },
        {
            "domain": "privilege",
            "objects": ["token", "role", "permission_set", "context"],
            "actions": ["escalate", "drop", "delegate", "inspect", "restrict"],
            "category": "identity",
            "platforms": ["windows", "linux", "macos", "cloud"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "destructive",
        },
        {
            "domain": "token",
            "objects": ["access_token", "refresh_token", "id_token", "api_token"],
            "actions": ["issue", "validate", "revoke", "exchange", "introspect"],
            "category": "identity",
            "platforms": ["identity", "cloud", "saas"],
            "providers": provider_set("provider.okta", "provider.aws", "provider.azure", "provider.gcp", "provider.github", "provider.microsoft365", "provider.google_workspace"),
            "safety": "caution",
        },
        {
            "domain": "kerberos",
            "objects": ["ticket", "tgt", "service_ticket", "delegation"],
            "actions": ["request", "renew", "validate", "delegate", "purge"],
            "category": "identity",
            "platforms": ["windows", "linux"],
            "providers": provider_set("provider.windows", "provider.linux"),
            "safety": "caution",
        },
        {
            "domain": "network",
            "objects": ["socket", "connection", "route", "interface"],
            "actions": ["open", "close", "inspect", "modify", "monitor"],
            "category": "network",
            "platforms": ["windows", "linux", "macos", "container", "cloud"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.docker", "provider.kubernetes", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "dns",
            "objects": ["record", "zone", "resolver", "query"],
            "actions": ["query", "create", "update", "delete", "monitor"],
            "category": "network",
            "platforms": ["windows", "linux", "macos", "cloud", "container"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp", "provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "firewall",
            "objects": ["rule", "policy", "profile", "exception"],
            "actions": ["create", "delete", "enable", "disable", "audit"],
            "category": "network",
            "platforms": ["windows", "linux", "macos", "cloud", "container"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp", "provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "proxy",
            "objects": ["configuration", "rule", "route", "credential"],
            "actions": ["set", "read", "delete", "bypass", "enforce"],
            "category": "network",
            "platforms": ["windows", "linux", "macos", "cloud"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "rpc",
            "objects": ["endpoint", "binding", "service", "method"],
            "actions": ["discover", "invoke", "register", "inspect", "restrict"],
            "category": "network",
            "platforms": ["windows", "linux", "cloud"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "smb",
            "objects": ["share", "session", "pipe", "file"],
            "actions": ["connect", "mount", "read", "write", "disconnect"],
            "category": "network",
            "platforms": ["windows", "linux", "macos"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos"),
            "safety": "caution",
        },
        {
            "domain": "named_pipe",
            "objects": ["pipe", "server", "client", "message"],
            "actions": ["create", "connect", "read", "write", "close"],
            "category": "endpoint",
            "platforms": ["windows", "linux"],
            "providers": provider_set("provider.windows", "provider.linux"),
            "safety": "caution",
        },
        {
            "domain": "com",
            "objects": ["object", "class", "registration", "activation"],
            "actions": ["register", "activate", "query", "modify", "remove"],
            "category": "endpoint",
            "platforms": ["windows"],
            "providers": provider_set("provider.windows"),
            "safety": "caution",
        },
        {
            "domain": "wmi",
            "objects": ["namespace", "class", "instance", "subscription"],
            "actions": ["query", "create", "modify", "delete", "subscribe"],
            "category": "endpoint",
            "platforms": ["windows"],
            "providers": provider_set("provider.windows"),
            "safety": "caution",
        },
        {
            "domain": "powershell",
            "objects": ["script", "module", "command", "runspace"],
            "actions": ["execute", "import", "inspect", "constrain", "log"],
            "category": "endpoint",
            "platforms": ["windows"],
            "providers": provider_set("provider.windows"),
            "safety": "caution",
        },
        {
            "domain": "office",
            "objects": ["macro", "addin", "document", "template"],
            "actions": ["create", "execute", "disable", "inspect", "delete"],
            "category": "saas",
            "platforms": ["saas", "windows", "macos"],
            "providers": provider_set("provider.microsoft365"),
            "safety": "caution",
        },
        {
            "domain": "cloud",
            "objects": ["resource", "instance", "bucket", "policy"],
            "actions": ["create", "read", "update", "delete", "tag"],
            "category": "cloud",
            "platforms": ["cloud"],
            "providers": provider_set("provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "container",
            "objects": ["image", "container", "runtime", "volume"],
            "actions": ["build", "run", "inspect", "stop", "delete"],
            "category": "container",
            "platforms": ["container", "cloud"],
            "providers": provider_set("provider.docker", "provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "kubernetes",
            "objects": ["pod", "secret", "configmap", "role", "service_account"],
            "actions": ["create", "read", "update", "delete", "exec"],
            "category": "container",
            "platforms": ["container", "cloud"],
            "providers": provider_set("provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "virtualization",
            "objects": ["vm", "snapshot", "hypervisor", "template"],
            "actions": ["create", "start", "stop", "clone", "delete"],
            "category": "cloud",
            "platforms": ["cloud", "container"],
            "providers": provider_set("provider.aws", "provider.azure", "provider.gcp"),
            "safety": "caution",
        },
        {
            "domain": "email",
            "objects": ["forwarding", "rule", "mailbox", "transport"],
            "actions": ["create", "read", "update", "delete", "audit"],
            "category": "saas",
            "platforms": ["saas", "cloud"],
            "providers": provider_set("provider.google_workspace", "provider.microsoft365"),
            "safety": "caution",
        },
        {
            "domain": "collaboration",
            "objects": ["workspace", "channel", "membership", "sharing"],
            "actions": ["create", "read", "update", "delete", "audit"],
            "category": "saas",
            "platforms": ["saas"],
            "providers": provider_set("provider.microsoft365", "provider.google_workspace", "provider.github"),
            "safety": "caution",
        },
        {
            "domain": "database",
            "objects": ["role", "user", "query", "table", "audit"],
            "actions": ["create", "read", "update", "delete", "grant", "revoke"],
            "category": "database",
            "platforms": ["database", "cloud"],
            "providers": provider_set("provider.sql_server", "provider.postgresql"),
            "safety": "caution",
        },
        {
            "domain": "api",
            "objects": ["token", "endpoint", "scope", "quota"],
            "actions": ["create", "read", "update", "delete", "rotate"],
            "category": "automation",
            "platforms": ["cloud", "saas", "cross_platform"],
            "providers": provider_set("provider.github", "provider.aws", "provider.azure", "provider.gcp", "provider.okta"),
            "safety": "caution",
        },
        {
            "domain": "audit",
            "objects": ["event", "trail", "policy", "retention"],
            "actions": ["enable", "disable", "query", "export", "verify"],
            "category": "telemetry",
            "platforms": ["cloud", "saas", "windows", "linux", "macos"],
            "providers": provider_set("provider.aws", "provider.azure", "provider.gcp", "provider.github", "provider.microsoft365", "provider.google_workspace", "provider.okta", "provider.windows", "provider.linux", "provider.macos"),
            "safety": "safe",
        },
        {
            "domain": "logging",
            "objects": ["pipeline", "collector", "parser", "sink"],
            "actions": ["configure", "start", "stop", "route", "validate"],
            "category": "telemetry",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.aws", "provider.azure", "provider.gcp", "provider.windows", "provider.linux", "provider.macos"),
            "safety": "safe",
        },
        {
            "domain": "detection",
            "objects": ["rule", "query", "analytic", "baseline"],
            "actions": ["create", "test", "deploy", "tune", "retire"],
            "category": "detection",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.github", "provider.aws", "provider.azure", "provider.gcp", "provider.windows", "provider.linux", "provider.macos"),
            "safety": "safe",
        },
        {
            "domain": "response",
            "objects": ["isolation", "containment", "remediation", "rollback"],
            "actions": ["plan", "execute", "verify", "rollback", "document"],
            "category": "response",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp", "provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "collection",
            "objects": ["artifact", "evidence", "timeline", "snapshot"],
            "actions": ["collect", "normalize", "enrich", "store", "export"],
            "category": "collection",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.aws", "provider.azure", "provider.gcp", "provider.kubernetes"),
            "safety": "safe",
        },
        {
            "domain": "enrichment",
            "objects": ["indicator", "entity", "context", "risk"],
            "actions": ["lookup", "correlate", "score", "annotate", "publish"],
            "category": "enrichment",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.github", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "safe",
        },
        {
            "domain": "validation",
            "objects": ["scenario", "atomic", "coverage", "result"],
            "actions": ["validate", "execute", "measure", "cleanup", "report"],
            "category": "validation",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.windows", "provider.linux", "provider.macos", "provider.kubernetes", "provider.github"),
            "safety": "caution",
        },
        {
            "domain": "automation",
            "objects": ["workflow", "playbook", "task", "orchestration"],
            "actions": ["orchestrate", "trigger", "schedule", "monitor", "rollback"],
            "category": "automation",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.github", "provider.aws", "provider.azure", "provider.gcp", "provider.kubernetes"),
            "safety": "caution",
        },
        {
            "domain": "ai",
            "objects": ["reasoning", "recommendation", "classification", "assistant"],
            "actions": ["reason", "suggest", "classify", "summarize", "explain"],
            "category": "ai",
            "platforms": ["cross_platform", "cloud", "saas"],
            "providers": provider_set("provider.github", "provider.aws", "provider.azure", "provider.gcp"),
            "safety": "safe",
        },
    ]

    generated: list[dict] = []
    generated_ids: set[str] = set()

    map_counter = 2000
    for spec in specs:
        for obj in spec["objects"]:
            for action in spec["actions"]:
                cap_id = f"{spec['domain']}.{obj}.{action}"
                if cap_id in existing_ids or cap_id in generated_ids:
                    continue

                map_counter += 1
                framework = framework_cycle[map_counter % len(framework_cycle)]
                capability = {
                    "capability_id": cap_id,
                    "stable_id": "",
                    "name": f"{titleize(action)} {titleize(obj)}",
                    "description": f"Perform {action.replace('_', ' ')} operation on {obj.replace('_', ' ')} in the {spec['domain']} domain.",
                    "category": spec["category"],
                    "domain": spec["domain"],
                    "platforms": spec["platforms"],
                    "providers": spec["providers"],
                    "version": "0.1.0",
                    "status": "stable",
                    "confidence": 0.86 if spec["safety"] != "destructive" else 0.8,
                    "safety": spec["safety"],
                    "required_privileges": [f"{spec['domain']}.{obj}.{action}"],
                    "preconditions": [f"provider exposes {spec['domain']} capability surface"],
                    "postconditions": [f"{obj.replace('_', ' ')} state may change based on action"],
                    "inputs": ["target", "context"],
                    "outputs": ["result"],
                    "cleanup_supported": spec["safety"] != "destructive",
                    "verification_methods": [
                        {
                            "method_id": f"verify.{cap_id}",
                            "type": "safe_execute",
                            "description": f"Safely verify {cap_id} with dry run and cleanup support",
                            "supports_dry_run": True,
                            "supports_safe_mode": True,
                            "supports_cleanup": True,
                            "supports_rollback": True,
                        }
                    ],
                    "discovery_methods": [
                        {
                            "method_id": f"discover.{cap_id}",
                            "type": "declared",
                            "state": "declared",
                            "description": f"Discover declared support for {cap_id}",
                        }
                    ],
                    "mappings": [
                        {
                            "framework": framework,
                            "external_id": f"{framework}-{map_counter}",
                            "external_name": f"{titleize(spec['domain'])} {titleize(obj)} {titleize(action)}",
                            "relation": "maps_to",
                            "confidence": 0.72,
                        }
                    ],
                }

                generated.append(capability)
                generated_ids.add(cap_id)

    combined = existing + generated

    for idx, capability in enumerate(combined, start=1):
        capability["stable_id"] = f"OSCO-CAP-{idx:04d}"

    combined.sort(key=lambda item: item["capability_id"])

    CATALOG_PATH.write_text(json.dumps(combined, indent=2) + "\n")
    return combined


if __name__ == "__main__":
    corpus = generate()
    print(f"Generated capability corpus with {len(corpus)} entries")

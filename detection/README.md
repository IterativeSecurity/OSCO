# detection

This directory contains detection scenario definitions for OSCO — curated detection logic that bridges capability semantics with external frameworks.

## Purpose

Detection entries represent known-good detection scenarios for specific security capabilities. They answer:
- **What behavior is being detected?** (via `capability_ids`)
- **How confident is this detection?** (via mapping confidence scores)
- **What data sources are required?** (via `data_sources`)
- **Which framework rules implement it?** (via `mappings` to Sigma, ATT&CK, etc.)

## Files & Structure

**[detections.json](detections.json)** — Central registry of detection scenarios
- **detection_id**: Semantic identifier (e.g., `det.credential.lsass.access.001`)
- **name**: Human-readable title
- **description**: What is detected, how, and key tuning notes
- **severity**: `critical`, `high`, `medium`, or `low`
- **capability_ids**: OSCO capabilities this detection covers
- **data_sources**: Telemetry/log sources required (e.g., `sysmon`, `aws_cloudtrail`)
- **platforms**: OS or environment scope
- **mappings**: Framework cross-references (ATT&CK, Sigma, AWS Security Hub, etc.)

## Detection Catalog

See [catalog.md](catalog.md) — auto-generated, regenerate with `make generate`.

## Adding New Detections

```json
{
  "detection_id": "det.<tactic>.<object>.<action>.NNN",
  "name": "...",
  "description": "...",
  "severity": "critical|high|medium|low",
  "capability_ids": ["<osco.capability.id>"],
  "data_sources": ["sysmon", "windows_security_event_log"],
  "platforms": ["windows"],
  "mappings": [
    {
      "framework": "mitre_attack",
      "external_id": "T1234.001",
      "external_name": "...",
      "relation": "detects",
      "confidence": 0.9
    }
  ]
}
```

Valid `relation` values: `detects`, `implemented_by`, `related_to`.

## Related Documentation

- [../capability/README.md](../capability/README.md) — Capability catalog
- [../validation/README.md](../validation/README.md) — Validation scenarios
- [../mappings/README.md](../mappings/README.md) — Framework registry
- [../docs/field-reference.md](../docs/field-reference.md) — Detection model field reference

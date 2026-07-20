<!-- AUTO-GENERATED — do not edit manually. Regenerate with: make generate  # or: uv run scripts/generate_capability_table.py -->

# Capability Catalog

## Summary

- **Total capabilities:** 332
- **Distinct domains:** 50
- **Distinct categories:** 22
- **Top domains:** authorization (21), collection (21), detection (21), audit (20), certificate (20), logging (20), telemetry (20), credential (13), process (7), cloud (5)
- **Top categories:** identity (72), telemetry (68), endpoint (52), network (24), collection (21), detection (21), saas (12), cloud (9), automation (8), container (8)

## Table

| Stable ID | Capability ID | Name | Domain | Category | Safety | Status | Confidence | Providers | Platforms | Mappings |
|---|---|---|---|---|---|---|---:|---:|---:|---:|
| OSCO-CAP-0001 | ai.assistant.classify | Classify Assistant | ai | ai | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0002 | ai.assistant.explain | Explain Assistant | ai | ai | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0003 | ai.assistant.reason | Reason Assistant | ai | ai | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0004 | ai.assistant.suggest | Suggest Assistant | ai | ai | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0005 | api.endpoint.create | Create Endpoint | api | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0006 | api.endpoint.delete | Delete Endpoint | api | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0007 | api.endpoint.read | Read Endpoint | api | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0008 | api.endpoint.rotate | Rotate Endpoint | api | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0009 | audit.event.disable | Disable Event | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 2 |
| OSCO-CAP-0010 | audit.event.enable | Enable Event | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 1 |
| OSCO-CAP-0011 | audit.event.export | Export Event | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0012 | audit.event.query | Query Event | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0013 | audit.event.verify | Verify Event | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0014 | audit.policy.disable | Disable Policy | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0015 | audit.policy.enable | Enable Policy | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0016 | audit.policy.export | Export Policy | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0017 | audit.policy.query | Query Policy | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0018 | audit.policy.verify | Verify Policy | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0019 | audit.retention.disable | Disable Retention | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0020 | audit.retention.enable | Enable Retention | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0021 | audit.retention.export | Export Retention | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0022 | audit.retention.query | Query Retention | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0023 | audit.retention.verify | Verify Retention | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0024 | audit.trail.disable | Disable Trail | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0025 | audit.trail.enable | Enable Trail | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0026 | audit.trail.export | Export Trail | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0027 | audit.trail.query | Query Trail | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0028 | audit.trail.verify | Verify Trail | audit | telemetry | safe | stable | 0.86 | 10 | 5 | 0 |
| OSCO-CAP-0029 | authentication.challenge.enforce | Enforce Challenge | authentication | identity | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0030 | authentication.challenge.refresh | Refresh Challenge | authentication | identity | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0031 | authentication.challenge.request | Request Challenge | authentication | identity | caution | stable | 0.86 | 5 | 3 | 1 |
| OSCO-CAP-0032 | authentication.challenge.revoke | Revoke Challenge | authentication | identity | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0033 | authorization.binding.attach | Attach Binding | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0034 | authorization.binding.detach | Detach Binding | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0035 | authorization.binding.evaluate | Evaluate Binding | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0036 | authorization.binding.grant | Grant Binding | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0037 | authorization.binding.revoke | Revoke Binding | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0038 | authorization.permission.attach | Attach Permission | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0039 | authorization.permission.detach | Detach Permission | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0040 | authorization.permission.evaluate | Evaluate Permission | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0041 | authorization.permission.grant | Grant Permission | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0042 | authorization.permission.revoke | Revoke Permission | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0043 | authorization.policy.attach | Attach Policy | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0044 | authorization.policy.detach | Detach Policy | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0045 | authorization.policy.evaluate | Evaluate Policy | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0046 | authorization.policy.grant | Grant Policy | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0047 | authorization.policy.revoke | Revoke Policy | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0048 | authorization.role.attach | Attach Role | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0049 | authorization.role.detach | Detach Role | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0050 | authorization.role.evaluate | Evaluate Role | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0051 | authorization.role.grant | Grant Role | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0052 | authorization.role.revoke | Revoke Role | authorization | identity | caution | stable | 0.86 | 7 | 4 | 0 |
| OSCO-CAP-0053 | automation.orchestration.monitor | Monitor Orchestration | automation | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0054 | automation.orchestration.orchestrate | Orchestrate Orchestration | automation | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0055 | automation.orchestration.rollback | Rollback Orchestration | automation | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0056 | automation.orchestration.schedule | Schedule Orchestration | automation | automation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0057 | browser.cookie.delete | Delete Cookie | browser | browser | caution | stable | 0.86 | 2 | 4 | 0 |
| OSCO-CAP-0058 | browser.cookie.export | Export Cookie | browser | browser | caution | stable | 0.86 | 2 | 4 | 0 |
| OSCO-CAP-0059 | browser.cookie.import | Import Cookie | browser | browser | caution | stable | 0.86 | 2 | 4 | 0 |
| OSCO-CAP-0060 | browser.cookie.read | Read Browser Cookie Store | browser | browser | caution | stable | 0.86 | 2 | 4 | 1 |
| OSCO-CAP-0061 | certificate.certificate.create | Create Certificate | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0062 | certificate.certificate.delete | Delete Certificate | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0063 | certificate.certificate.import | Import Certificate | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0064 | certificate.certificate.read | Read Certificate | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0065 | certificate.certificate.revoke | Revoke Certificate | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0066 | certificate.private_key.create | Create Private Key | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0067 | certificate.private_key.delete | Delete Private Key | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0068 | certificate.private_key.import | Import Private Key | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0069 | certificate.private_key.read | Read Private Key | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0070 | certificate.private_key.revoke | Revoke Private Key | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0071 | certificate.store.create | Create Store | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0072 | certificate.store.delete | Delete Store | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0073 | certificate.store.import | Import Store | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0074 | certificate.store.read | Read Store | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0075 | certificate.store.revoke | Revoke Store | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0076 | certificate.trust_anchor.create | Create Trust Anchor | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0077 | certificate.trust_anchor.delete | Delete Trust Anchor | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0078 | certificate.trust_anchor.import | Import Trust Anchor | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0079 | certificate.trust_anchor.read | Read Trust Anchor | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0080 | certificate.trust_anchor.revoke | Revoke Trust Anchor | certificate | identity | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0081 | cloud.bucket.create | Create Bucket | cloud | cloud | caution | stable | 0.86 | 3 | 1 | 1 |
| OSCO-CAP-0082 | cloud.bucket.delete | Delete Bucket | cloud | cloud | caution | stable | 0.86 | 3 | 1 | 1 |
| OSCO-CAP-0083 | cloud.bucket.read | Read Bucket | cloud | cloud | caution | stable | 0.86 | 3 | 1 | 2 |
| OSCO-CAP-0084 | cloud.bucket.tag | Tag Bucket | cloud | cloud | caution | stable | 0.86 | 3 | 1 | 0 |
| OSCO-CAP-0332 | cloud.iam.enumerate | Enumerate Cloud IAM Permissions | cloud | discovery | safe | stable | 0.92 | 3 | 1 | 3 |
| OSCO-CAP-0085 | cloud.iam.role.create | Create IAM Role | identity | cloud | caution | stable | 0.93 | 3 | 1 | 2 |
| OSCO-CAP-0086 | collaboration.channel.audit | Audit Channel | collaboration | saas | caution | stable | 0.86 | 3 | 1 | 0 |
| OSCO-CAP-0087 | collaboration.channel.create | Create Channel | collaboration | saas | caution | stable | 0.86 | 3 | 1 | 0 |
| OSCO-CAP-0088 | collaboration.channel.delete | Delete Channel | collaboration | saas | caution | stable | 0.86 | 3 | 1 | 0 |
| OSCO-CAP-0089 | collaboration.channel.read | Read Channel | collaboration | saas | caution | stable | 0.86 | 3 | 1 | 0 |
| OSCO-CAP-0090 | collection.artifact.collect | Collect Artifact | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0091 | collection.artifact.enrich | Enrich Artifact | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0092 | collection.artifact.export | Export Artifact | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0093 | collection.artifact.normalize | Normalize Artifact | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0094 | collection.artifact.store | Store Artifact | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0095 | collection.evidence.collect | Collect Evidence | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0096 | collection.evidence.enrich | Enrich Evidence | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0097 | collection.evidence.export | Export Evidence | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0098 | collection.evidence.normalize | Normalize Evidence | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0099 | collection.evidence.store | Store Evidence | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0100 | collection.persistence.evidence.collect | Collect Persistence Evidence | collection | collection | safe | stable | 0.89 | 5 | 1 | 2 |
| OSCO-CAP-0101 | collection.snapshot.collect | Collect Snapshot | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0102 | collection.snapshot.enrich | Enrich Snapshot | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0103 | collection.snapshot.export | Export Snapshot | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0104 | collection.snapshot.normalize | Normalize Snapshot | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0105 | collection.snapshot.store | Store Snapshot | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0106 | collection.timeline.collect | Collect Timeline | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0107 | collection.timeline.enrich | Enrich Timeline | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0108 | collection.timeline.export | Export Timeline | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0109 | collection.timeline.normalize | Normalize Timeline | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0110 | collection.timeline.store | Store Timeline | collection | collection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0111 | com.activation.activate | Activate Activation | com | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0112 | com.activation.modify | Modify Activation | com | endpoint | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0113 | com.activation.query | Query Activation | com | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0114 | com.activation.register | Register Activation | com | endpoint | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0115 | container.container.build | Build Container | container | container | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0116 | container.container.delete | Delete Container | container | container | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0117 | container.container.inspect | Inspect Container | container | container | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0118 | container.container.run | Run Container | container | container | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0119 | credential.credential.access | Access Credential | credential | identity | caution | stable | 0.86 | 7 | 5 | 1 |
| OSCO-CAP-0120 | credential.credential.delete | Delete Credential | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0121 | credential.credential.dump | Dump Credential | credential | identity | caution | stable | 0.86 | 7 | 5 | 2 |
| OSCO-CAP-0122 | credential.credential.rotate | Rotate Credential | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0123 | credential.credential.store | Store Credential | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0124 | credential.hash.access | Access Hash | credential | identity | caution | stable | 0.86 | 7 | 5 | 1 |
| OSCO-CAP-0125 | credential.hash.delete | Delete Hash | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0126 | credential.hash.dump | Dump Hash | credential | identity | caution | stable | 0.86 | 7 | 5 | 2 |
| OSCO-CAP-0127 | credential.hash.rotate | Rotate Hash | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0128 | credential.hash.store | Store Hash | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0129 | credential.token.access | Access Token | credential | identity | caution | stable | 0.86 | 7 | 5 | 1 |
| OSCO-CAP-0130 | credential.token.delete | Delete Token | credential | identity | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0131 | credential.token.dump | Dump Token | credential | identity | caution | stable | 0.86 | 7 | 5 | 2 |
| OSCO-CAP-0132 | database.audit.create | Create Audit | database | database | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0133 | database.audit.delete | Delete Audit | database | database | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0134 | database.audit.grant | Grant Audit | database | database | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0135 | database.audit.read | Read Audit | database | database | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0136 | database.role.grant | Grant Database Role | authorization | database | caution | stable | 0.87 | 2 | 1 | 1 |
| OSCO-CAP-0137 | detection.analytic.create | Create Analytic | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0138 | detection.analytic.deploy | Deploy Analytic | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0139 | detection.analytic.retire | Retire Analytic | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0140 | detection.analytic.test | Test Analytic | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0141 | detection.analytic.tune | Tune Analytic | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0142 | detection.baseline.create | Create Baseline | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0143 | detection.baseline.deploy | Deploy Baseline | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0144 | detection.baseline.retire | Retire Baseline | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0145 | detection.baseline.test | Test Baseline | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0146 | detection.baseline.tune | Tune Baseline | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0147 | detection.query.create | Create Query | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0148 | detection.query.deploy | Deploy Query | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0149 | detection.query.retire | Retire Query | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0150 | detection.query.test | Test Query | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0151 | detection.query.tune | Tune Query | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0152 | detection.registry.persistence.detect | Detect Registry Persistence | detection | detection | safe | stable | 0.91 | 1 | 2 | 2 |
| OSCO-CAP-0153 | detection.rule.create | Create Rule | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0154 | detection.rule.deploy | Deploy Rule | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0155 | detection.rule.retire | Retire Rule | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0156 | detection.rule.test | Test Rule | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0157 | detection.rule.tune | Tune Rule | detection | detection | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0158 | dns.query.create | Create Query | dns | network | caution | stable | 0.86 | 7 | 5 | 2 |
| OSCO-CAP-0159 | dns.query.delete | Delete Query | dns | network | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0160 | dns.query.monitor | Monitor Query | dns | network | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0161 | driver.driver.install | Install Driver | driver | endpoint | destructive | stable | 0.80 | 3 | 3 | 2 |
| OSCO-CAP-0162 | driver.driver.load | Load Driver | driver | endpoint | destructive | stable | 0.80 | 3 | 3 | 3 |
| OSCO-CAP-0163 | driver.driver.query | Query Driver | driver | endpoint | destructive | stable | 0.80 | 3 | 3 | 0 |
| OSCO-CAP-0164 | driver.driver.unload | Unload Driver | driver | endpoint | destructive | stable | 0.80 | 3 | 3 | 0 |
| OSCO-CAP-0165 | email.forwarding.audit | Audit Forwarding | email | saas | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0166 | email.forwarding.create | Create Forwarding | email | saas | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0167 | email.forwarding.delete | Delete Forwarding | email | saas | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0168 | enrichment.context.annotate | Annotate Context | enrichment | enrichment | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0169 | enrichment.context.correlate | Correlate Context | enrichment | enrichment | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0170 | enrichment.context.lookup | Lookup Context | enrichment | enrichment | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0171 | enrichment.context.publish | Publish Context | enrichment | enrichment | safe | stable | 0.86 | 4 | 3 | 0 |
| OSCO-CAP-0172 | etw.consumer.emit | Emit Consumer | etw | telemetry | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0173 | etw.consumer.parse | Parse Consumer | etw | telemetry | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0174 | etw.consumer.start | Start Consumer | etw | telemetry | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0175 | etw.consumer.stop | Stop Consumer | etw | telemetry | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0176 | eventlog.channel.clear | Clear Channel | eventlog | telemetry | caution | stable | 0.86 | 3 | 3 | 4 |
| OSCO-CAP-0177 | eventlog.channel.configure | Configure Channel | eventlog | telemetry | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0178 | eventlog.channel.export | Export Channel | eventlog | telemetry | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0179 | eventlog.channel.read | Read Channel | eventlog | telemetry | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0180 | filesystem.directory.create | Create Directory | filesystem | endpoint | caution | stable | 0.86 | 4 | 4 | 0 |
| OSCO-CAP-0181 | filesystem.directory.delete | Delete Directory | filesystem | endpoint | caution | stable | 0.86 | 4 | 4 | 0 |
| OSCO-CAP-0182 | filesystem.directory.hash | Hash Directory | filesystem | endpoint | caution | stable | 0.86 | 4 | 4 | 0 |
| OSCO-CAP-0183 | filesystem.file.create | Create File | filesystem | endpoint | caution | stable | 0.95 | 4 | 4 | 2 |
| OSCO-CAP-0184 | firewall.exception.audit | Audit Exception | firewall | network | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0185 | firewall.exception.create | Create Exception | firewall | network | caution | stable | 0.86 | 7 | 5 | 2 |
| OSCO-CAP-0186 | firewall.exception.delete | Delete Exception | firewall | network | caution | stable | 0.86 | 7 | 5 | 0 |
| OSCO-CAP-0187 | firewall.exception.disable | Disable Exception | firewall | network | caution | stable | 0.86 | 7 | 5 | 1 |
| OSCO-CAP-0188 | identity.federation.create | Create Federation | identity | identity | caution | stable | 0.86 | 7 | 3 | 1 |
| OSCO-CAP-0189 | identity.federation.delete | Delete Federation | identity | identity | caution | stable | 0.86 | 7 | 3 | 1 |
| OSCO-CAP-0190 | identity.federation.enumerate | Enumerate Federation | identity | identity | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0191 | kerberos.delegation.delegate | Delegate Delegation | kerberos | identity | caution | stable | 0.86 | 2 | 2 | 2 |
| OSCO-CAP-0192 | kerberos.delegation.purge | Purge Delegation | kerberos | identity | caution | stable | 0.86 | 2 | 2 | 1 |
| OSCO-CAP-0193 | kerberos.delegation.renew | Renew Delegation | kerberos | identity | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0194 | kerberos.delegation.request | Request Delegation | kerberos | identity | caution | stable | 0.86 | 2 | 2 | 3 |
| OSCO-CAP-0195 | kernel.extension.inspect | Inspect Extension | kernel | endpoint | destructive | stable | 0.80 | 3 | 3 | 0 |
| OSCO-CAP-0196 | kernel.extension.load | Load Extension | kernel | endpoint | destructive | stable | 0.80 | 3 | 3 | 2 |
| OSCO-CAP-0197 | kernel.extension.modify | Modify Extension | kernel | endpoint | destructive | stable | 0.80 | 3 | 3 | 0 |
| OSCO-CAP-0198 | kernel.extension.register | Register Extension | kernel | endpoint | destructive | stable | 0.80 | 3 | 3 | 0 |
| OSCO-CAP-0199 | kubernetes.configmap.create | Create Configmap | kubernetes | container | caution | stable | 0.86 | 1 | 2 | 1 |
| OSCO-CAP-0200 | kubernetes.configmap.delete | Delete Configmap | kubernetes | container | caution | stable | 0.86 | 1 | 2 | 0 |
| OSCO-CAP-0201 | kubernetes.configmap.exec | Exec Configmap | kubernetes | container | caution | stable | 0.86 | 1 | 2 | 2 |
| OSCO-CAP-0202 | kubernetes.secret.read | Read Kubernetes Secret | kubernetes | container | caution | stable | 0.90 | 1 | 2 | 1 |
| OSCO-CAP-0203 | logging.collector.configure | Configure Collector | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0204 | logging.collector.route | Route Collector | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0205 | logging.collector.start | Start Collector | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0206 | logging.collector.stop | Stop Collector | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0207 | logging.collector.validate | Validate Collector | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0208 | logging.parser.configure | Configure Parser | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0209 | logging.parser.route | Route Parser | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0210 | logging.parser.start | Start Parser | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0211 | logging.parser.stop | Stop Parser | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0212 | logging.parser.validate | Validate Parser | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0213 | logging.pipeline.configure | Configure Pipeline | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0214 | logging.pipeline.route | Route Pipeline | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0215 | logging.pipeline.start | Start Pipeline | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0216 | logging.pipeline.stop | Stop Pipeline | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0217 | logging.pipeline.validate | Validate Pipeline | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0218 | logging.sink.configure | Configure Sink | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0219 | logging.sink.route | Route Sink | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0220 | logging.sink.start | Start Sink | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0221 | logging.sink.stop | Stop Sink | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0222 | logging.sink.validate | Validate Sink | logging | telemetry | safe | stable | 0.86 | 6 | 3 | 0 |
| OSCO-CAP-0223 | mail.forwarding.create | Create Mail Forwarding Rule | email | saas | caution | stable | 0.92 | 2 | 1 | 2 |
| OSCO-CAP-0224 | memory.dump.allocate | Allocate Dump | memory | endpoint | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0225 | memory.dump.dump | Dump Dump | memory | endpoint | caution | stable | 0.86 | 3 | 3 | 2 |
| OSCO-CAP-0226 | memory.dump.protect | Protect Dump | memory | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0227 | memory.dump.read | Read Dump | memory | endpoint | caution | stable | 0.86 | 3 | 3 | 3 |
| OSCO-CAP-0228 | named_pipe.client.close | Close Client | named_pipe | endpoint | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0229 | named_pipe.client.connect | Connect Client | named_pipe | endpoint | caution | stable | 0.86 | 2 | 2 | 1 |
| OSCO-CAP-0230 | named_pipe.client.create | Create Client | named_pipe | endpoint | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0231 | named_pipe.client.read | Read Client | named_pipe | endpoint | caution | stable | 0.86 | 2 | 2 | 0 |
| OSCO-CAP-0232 | network.connection.close | Close Connection | network | network | caution | stable | 0.86 | 8 | 5 | 0 |
| OSCO-CAP-0233 | network.connection.inspect | Inspect Connection | network | network | caution | stable | 0.86 | 8 | 5 | 0 |
| OSCO-CAP-0234 | network.connection.modify | Modify Connection | network | network | caution | stable | 0.86 | 8 | 5 | 0 |
| OSCO-CAP-0235 | network.connection.monitor | Monitor Connection | network | network | caution | stable | 0.86 | 8 | 5 | 1 |
| OSCO-CAP-0236 | network.dns.query | Perform DNS Query | dns | network | safe | stable | 0.90 | 4 | 5 | 1 |
| OSCO-CAP-0329 | network.proxy.tunnel | Establish Network Proxy Tunnel | network | command_and_control | caution | stable | 0.88 | 3 | 4 | 3 |
| OSCO-CAP-0237 | office.addin.create | Create Addin | office | saas | caution | stable | 0.86 | 1 | 3 | 0 |
| OSCO-CAP-0238 | office.addin.delete | Delete Addin | office | saas | caution | stable | 0.86 | 1 | 3 | 0 |
| OSCO-CAP-0239 | office.addin.disable | Disable Addin | office | saas | caution | stable | 0.86 | 1 | 3 | 0 |
| OSCO-CAP-0240 | office.addin.execute | Execute Addin | office | saas | caution | stable | 0.86 | 1 | 3 | 0 |
| OSCO-CAP-0241 | powershell.command.constrain | Constrain Command | powershell | endpoint | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0242 | powershell.command.execute | Execute Command | powershell | endpoint | caution | stable | 0.86 | 1 | 1 | 3 |
| OSCO-CAP-0243 | powershell.command.import | Import Command | powershell | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0244 | powershell.command.inspect | Inspect Command | powershell | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0245 | privilege.context.delegate | Delegate Context | privilege | identity | destructive | stable | 0.80 | 6 | 4 | 1 |
| OSCO-CAP-0246 | privilege.context.drop | Drop Context | privilege | identity | destructive | stable | 0.80 | 6 | 4 | 0 |
| OSCO-CAP-0247 | privilege.context.escalate | Escalate Context | privilege | identity | destructive | stable | 0.80 | 6 | 4 | 2 |
| OSCO-CAP-0248 | privilege.context.inspect | Inspect Context | privilege | identity | destructive | stable | 0.80 | 6 | 4 | 0 |
| OSCO-CAP-0249 | process.argument.create | Create Argument | process | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0250 | process.argument.enumerate | Enumerate Argument | process | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0251 | process.argument.inject | Inject Argument | process | endpoint | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0252 | process.argument.modify | Modify Argument | process | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0326 | process.injection.dll | DLL Injection | process | defense_evasion | caution | stable | 0.95 | 1 | 1 | 3 |
| OSCO-CAP-0327 | process.injection.hollow | Process Hollowing | process | defense_evasion | caution | stable | 0.95 | 1 | 1 | 3 |
| OSCO-CAP-0321 | process.lsass.access | Access LSASS Process Memory | process | credential_access | caution | stable | 0.98 | 1 | 1 | 4 |
| OSCO-CAP-0253 | proxy.configuration.bypass | Bypass Configuration | proxy | network | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0254 | proxy.configuration.delete | Delete Configuration | proxy | network | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0255 | proxy.configuration.enforce | Enforce Configuration | proxy | network | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0256 | proxy.configuration.read | Read Configuration | proxy | network | caution | stable | 0.86 | 6 | 4 | 0 |
| OSCO-CAP-0257 | registry.hive.backup | Backup Hive | registry | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0258 | registry.hive.delete | Delete Hive | registry | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0259 | registry.hive.enumerate | Enumerate Hive | registry | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0260 | registry.key.set | Set Registry Key | registry | endpoint | caution | stable | 0.96 | 1 | 1 | 2 |
| OSCO-CAP-0324 | registry.run.persist | Persist via Registry Run Keys | registry | persistence | caution | stable | 0.98 | 1 | 1 | 4 |
| OSCO-CAP-0261 | response.containment.document | Document Containment | response | response | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0262 | response.containment.execute | Execute Containment | response | response | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0263 | response.containment.plan | Plan Containment | response | response | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0264 | response.containment.rollback | Rollback Containment | response | response | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0265 | rpc.binding.discover | Discover Binding | rpc | network | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0266 | rpc.binding.inspect | Inspect Binding | rpc | network | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0267 | rpc.binding.invoke | Invoke Binding | rpc | network | caution | stable | 0.86 | 5 | 3 | 1 |
| OSCO-CAP-0268 | rpc.binding.register | Register Binding | rpc | network | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0269 | scheduled_task.action.create | Create Action | scheduled_task | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0270 | scheduled_task.action.delete | Delete Action | scheduled_task | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0271 | scheduled_task.action.modify | Modify Action | scheduled_task | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0272 | service.binary.create | Create Binary | service | endpoint | caution | stable | 0.86 | 3 | 3 | 3 |
| OSCO-CAP-0273 | service.binary.delete | Delete Binary | service | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0274 | service.binary.modify | Modify Binary | service | endpoint | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0275 | service.binary.query | Query Binary | service | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0276 | smb.file.connect | Connect File | smb | network | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0277 | smb.file.disconnect | Disconnect File | smb | network | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0278 | smb.file.mount | Mount File | smb | network | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0279 | smb.file.read | Read File | smb | network | caution | stable | 0.86 | 3 | 3 | 1 |
| OSCO-CAP-0280 | telemetry.collector.disable | Disable Collector | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0281 | telemetry.collector.enable | Enable Collector | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0282 | telemetry.collector.query | Query Collector | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0283 | telemetry.collector.route | Route Collector | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0284 | telemetry.collector.transform | Transform Collector | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0285 | telemetry.pipeline.disable | Disable Pipeline | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0286 | telemetry.pipeline.enable | Enable Pipeline | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0287 | telemetry.pipeline.query | Query Pipeline | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0288 | telemetry.pipeline.route | Route Pipeline | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0289 | telemetry.pipeline.transform | Transform Pipeline | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0290 | telemetry.sink.disable | Disable Sink | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0291 | telemetry.sink.enable | Enable Sink | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0292 | telemetry.sink.query | Query Sink | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0293 | telemetry.sink.route | Route Sink | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0294 | telemetry.sink.transform | Transform Sink | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0295 | telemetry.stream.disable | Disable Stream | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0296 | telemetry.stream.enable | Enable Stream | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0297 | telemetry.stream.query | Query Stream | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0298 | telemetry.stream.route | Route Stream | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0299 | telemetry.stream.transform | Transform Stream | telemetry | telemetry | safe | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0300 | thread.context.create | Create Context | thread | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0301 | thread.context.inject | Inject Context | thread | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0302 | thread.context.inspect | Inspect Context | thread | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0303 | thread.context.resume | Resume Context | thread | endpoint | caution | stable | 0.86 | 3 | 3 | 0 |
| OSCO-CAP-0304 | token.access_token.exchange | Exchange Access Token | token | identity | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0305 | token.access_token.introspect | Introspect Access Token | token | identity | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0306 | token.access_token.issue | Issue Access Token | token | identity | caution | stable | 0.86 | 7 | 3 | 1 |
| OSCO-CAP-0307 | token.access_token.revoke | Revoke Access Token | token | identity | caution | stable | 0.86 | 7 | 3 | 0 |
| OSCO-CAP-0308 | validation.atomic.cleanup | Cleanup Atomic | validation | validation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0309 | validation.atomic.execute | Execute Atomic | validation | validation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0310 | validation.atomic.measure | Measure Atomic | validation | validation | caution | stable | 0.86 | 5 | 3 | 0 |
| OSCO-CAP-0311 | validation.persistence.endpoint.validate | Validate Endpoint Persistence | validation | validation | caution | stable | 0.90 | 3 | 4 | 1 |
| OSCO-CAP-0312 | virtualization.hypervisor.clone | Clone Hypervisor | virtualization | cloud | caution | stable | 0.86 | 3 | 2 | 0 |
| OSCO-CAP-0313 | virtualization.hypervisor.create | Create Hypervisor | virtualization | cloud | caution | stable | 0.86 | 3 | 2 | 0 |
| OSCO-CAP-0314 | virtualization.hypervisor.delete | Delete Hypervisor | virtualization | cloud | caution | stable | 0.86 | 3 | 2 | 0 |
| OSCO-CAP-0315 | virtualization.hypervisor.start | Start Hypervisor | virtualization | cloud | caution | stable | 0.86 | 3 | 2 | 0 |
| OSCO-CAP-0328 | windows.amsi.bypass | Bypass AMSI | windows | defense_evasion | caution | stable | 0.95 | 1 | 1 | 3 |
| OSCO-CAP-0323 | windows.defender.disable | Disable Windows Defender | windows | defense_evasion | caution | stable | 0.98 | 1 | 1 | 3 |
| OSCO-CAP-0331 | windows.lolbin.certutil | Abuse Certutil for Download or Decode | windows | defense_evasion | caution | stable | 0.95 | 1 | 1 | 4 |
| OSCO-CAP-0330 | windows.service.create | Create Windows Service for Persistence | windows | persistence | caution | stable | 0.97 | 1 | 1 | 4 |
| OSCO-CAP-0316 | windows.task.create | Create Scheduled Task | scheduled_task | endpoint | caution | stable | 0.97 | 1 | 1 | 2 |
| OSCO-CAP-0322 | windows.vss.delete | Delete Volume Shadow Copies | windows | impact | destructive | stable | 0.98 | 1 | 1 | 3 |
| OSCO-CAP-0317 | wmi.class.create | Create Class | wmi | endpoint | caution | stable | 0.86 | 1 | 1 | 1 |
| OSCO-CAP-0318 | wmi.class.delete | Delete Class | wmi | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0319 | wmi.class.modify | Modify Class | wmi | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0320 | wmi.class.query | Query Class | wmi | endpoint | caution | stable | 0.86 | 1 | 1 | 0 |
| OSCO-CAP-0325 | wmi.subscription.create | Create WMI Event Subscription | wmi | persistence | caution | stable | 0.97 | 1 | 1 | 4 |

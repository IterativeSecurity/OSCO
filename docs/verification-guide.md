# Verification Guide

Verification methods describe safe, controlled ways to exercise and confirm capability behavior.
They answer the question: "can we confirm this capability works as expected, without causing unintended harm?"

For field-level reference (types, defaults, required fields), see [Field Reference: VerificationMethod](field-reference.md#verificationmethod).

## Relationship to Discovery

Discovery confirms capability **support** (is it available here?).
Verification confirms capability **behavior** (does it work as expected?).
Both use separate metadata objects and serve distinct operational purposes.

See [Discovery Guide](discovery-guide.md) for discovery-specific guidance.

## Safety Flags

Every verification method declares four boolean safety flags. These gate automated execution in operational environments.

| Flag | Meaning |
|---|---|
| `supports_dry_run` | Can execute without committing state changes |
| `supports_safe_mode` | Can execute in a constrained mode with limited impact |
| `supports_cleanup` | Provides a defined post-execution cleanup path |
| `supports_rollback` | Can fully reverse execution state on failure or cancellation |

All flags default to `true`. Set a flag to `false` only when the capability genuinely cannot support that mode.
Do not set flags to `false` speculatively — it restricts automation unnecessarily.

## Verification Method Types

The `type` field describes the verification approach.

| Type | Description |
|---|---|
| `safe_execute` | Exercises the capability in a safe mode with cleanup support |
| `dry_run` | Simulates execution without committing state changes |
| `passive_observe` | Observes capability behavior without actively triggering it |
| `simulation` | Uses a simulation environment or emulation layer |
| `api_probe` | Calls an API to confirm behavior without side effects |

## Authoring Verification Methods

```json
{
  "method_id": "verify.windows.task.create",
  "type": "safe_execute",
  "description": "Create a scheduled task using schtasks.exe with a 1-second delay, then immediately delete it. Cleanup removes the task entry and verifies absence via Get-ScheduledTask.",
  "supports_dry_run": false,
  "supports_safe_mode": true,
  "supports_cleanup": true,
  "supports_rollback": true
}
```

## Verification Outcomes

A verification method should produce at minimum:
- A clear success/failure signal
- Notes on observed side effects
- Cleanup instructions or confirmation that cleanup ran
- Impact on the capability's `confidence` score when verification succeeds

If a verification produces unexpected evidence (e.g., artifacts that should not exist), escalate for review before marking the capability `stable`.

## Authoring Guidance

- Prefer non-destructive verification paths by default. A `caution` or `destructive` safety classification does not preclude safe verification — it means the underlying behavior is risky, not that verification must be risky.
- Clearly document required privileges and prerequisites in the `description` field.
- Verification methods should be repeatable: the same steps must produce the same outcome in the same environment.
- A capability with no verification methods is not `stable`. Promotion from `draft` to `stable` requires at least one verified or proven discovery method or verification method.

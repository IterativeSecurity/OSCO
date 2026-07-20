# Best Practices

## Capability Modeling

- **One behavior per capability.** If a single ID would need an "and" in its description, it covers two behaviors. Split it.
- **Implementation-neutral descriptions.** A description is wrong if it becomes false when run on a different provider. Vendor names, API versions, and product names belong in `execution_metadata`, not in `description`.
- **Precise IDs over broad ones.** Prefer `cloud.iam.role.create` over `cloud.iam.modify`. Specificity enables better mapping and coverage reasoning.
- **Stable IDs are permanent.** Never reuse, reassign, or rename a `stable_id`. Deprecate the old entry and create a new one if semantics must change.
- **Default `status` to `draft`.** Only promote to `stable` after review and at least one confirmed discovery or verification method.
- **Default `safety` to `caution`.** Only set `safe` if the capability is verifiably non-destructive across all listed platforms.

## Mappings

- **Use precise relation types.** `maps_to` is not a catch-all. If the external artifact is a detection rule, use `detects`. If it is a simulation test, use `validates`. See [Relation Types](relation-types.md).
- **Score confidence honestly.** `0.9+` means authoritative or machine-verified. Inferred or partial alignment is `0.5–0.69`. Do not round up.
- **Include `url` whenever available.** A URL makes a mapping verifiable. A mapping without a URL requires more reviewer trust.
- **Do not force a mapping.** A capability with no external mappings is valid. A forced low-confidence mapping adds noise without value.
- **Cover all three relation types for mature capabilities.** A mature capability should have `maps_to` (framework alignment), `detects` (detection coverage), and `validates` (simulation test) mappings. Missing `detects` or `validates` mappings indicate coverage gaps.

## Safety and Verification

- **All verification methods should support cleanup by default.** Set `supports_cleanup: false` only when genuinely impossible, not as a shortcut.
- **Document prerequisites in `description`.** A verification method that requires domain admin rights and says nothing about it is a safety hazard.
- **Separate detection and validation content from ontology identity.** `Detection` and `Validation` objects are references to external artifacts — they are not the detection logic or simulation procedure itself.
- **A `caution` capability can still have `safe` verification.** Safety classification applies to the behavior; verification safety flags apply to the test procedure. These are independent.

## Discovery

- **Start at `declared`, grow from there.** It is honest and correct to mark discovery state as `declared` when bootstrapping. Do not prematurely elevate to `verified` or `proven`.
- **Make discovery queries executable.** The `query` field should contain a literal command or query string that a human or system can run. Prose descriptions without a runnable query are less useful.
- **Discovery is not verification.** Discovering capability support does not mean the capability has been exercised. Use both metadata types.

## Repository Hygiene

- **Regenerate generated docs when source catalogs change.** Run `uv run scripts/generate_capability_table.py` and `uv run scripts/generate_component_docs_report.py --write` before submitting a PR that touches catalogs.
- **Run link validation before submitting.** `uv run scripts/check_markdown_links.py` catches broken references early.
- **Keep PRs focused.** A PR that adds a capability, updates a provider, modifies the schema, and refactors the CLI is hard to review. Split these concerns.
- **Write rationale in PR descriptions.** Mapping choices, confidence scores, and safety classifications are judgment calls. Explain the reasoning so reviewers can assess it.

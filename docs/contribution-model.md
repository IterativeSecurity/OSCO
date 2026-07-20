# Contribution Model

## Typical Contribution Flow

1. Open an issue describing the problem or proposal.
2. Implement focused changes in a branch.
3. Run local validation:
   - uv run osco/scripts_validate.py
   - uv run scripts/validate_ontology_taxonomy.py
   - uv run scripts/validate_mapping_frameworks.py
   - uv run scripts/validate_provider_registry.py
   - uv run pytest
   - uv run scripts/check_markdown_links.py
4. Regenerate generated docs when applicable:
   - uv run scripts/sync_ontology_domains.py
   - uv run scripts/generate_capability_table.py --catalog capability/catalog.json --output capability/README.md --title "Capability Registry"
   - uv run scripts/generate_capability_table.py --catalog capability/catalog.extended.json --output capability/README.extended.md --title "Capability Registry (Extended)"
   - uv run scripts/generate_component_docs_report.py --write
5. Submit a PR with rationale and relevant references.

## PR Review Expectations

- Clear scope and motivation
- Passing CI checks
- Backward-compatibility notes for schema/ontology-impacting changes
- Updated docs for user-visible behavior changes

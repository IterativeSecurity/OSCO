# Provider Authoring Guide

Providers represent implementation sources and link capabilities to real platforms.

## Where Provider Data Lives

- provider/providers.json
- Typed model: osco/models/core.py (Provider)

## Authoring Workflow

1. Define provider_id, name, and category.
2. Declare supported platforms.
3. Add a neutral technical description.
4. Populate supported domains/capability surfaces in supports.
5. Ensure referenced providers are used consistently by capabilities.

## Authoring Rules

- Keep provider metadata factual and implementation-oriented.
- Avoid embedding product marketing language.
- Do not turn provider entries into capability definitions.

## Validation

After provider changes, run:
- uv run pytest
- uv run scripts/check_markdown_links.py

# Contributing to OSCO

Thank you for contributing to the Open Security Capability Ontology.

OSCO is licensed under Apache-2.0 and welcomes contributions to capabilities, providers, mappings, documentation, and tooling.

## How to Report a Bug

Open an issue describing:
- What you expected to happen
- What actually happened
- Steps to reproduce, including relevant capability IDs or catalog entries
- Your Python version and OS

## How to Request a Feature or Capability

Open an issue describing:
- The capability or domain you want modeled
- The external framework(s) it maps to (ATT&CK, Sigma, OCSF, etc.)
- The platform(s) it applies to
- Any relevant references or prior art

## Development Setup

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```bash
git clone <repo-url>
cd osco
uv venv .venv
source .venv/bin/activate
uv pip install -e .[dev]
```

## Typical Contribution Flow

1. Open an issue for any non-trivial change.
2. Fork and create a focused branch.
3. Make changes following the [Capability Authoring Guide](docs/capability-authoring-guide.md) or [Provider Authoring Guide](docs/provider-authoring-guide.md) as applicable.
4. Run local validation:
   ```bash
   uv run osco/scripts_validate.py
   uv run pytest
   uv run scripts/check_markdown_links.py
   ```
5. Regenerate generated docs if you changed catalogs:
   ```bash
   uv run scripts/generate_capability_table.py --catalog capability/catalog.json --output capability/README.md --title "Capability Registry"
   uv run scripts/generate_component_docs_report.py --write
   ```
6. Submit a pull request with rationale and references.

## Quality Standards

- Capability IDs must follow the `domain.object.action` naming convention.
- Descriptions must be implementation-neutral (no vendor names, no product-specific language).
- Mappings must include `framework`, `external_id`, `external_name`, and a realistic `confidence`.
- Schema validation must pass (`uv run osco/scripts_validate.py`).
- All tests must pass (`uv run pytest`).
- All markdown links must resolve (`uv run scripts/check_markdown_links.py`).

## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

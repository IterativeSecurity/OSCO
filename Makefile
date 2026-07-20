.DEFAULT_GOAL := help
PYTHON := uv run

.PHONY: help all test validate generate build lint

help:
	@echo "OSCO build targets"
	@echo ""
	@echo "  make build      Build the gold capability catalog"
	@echo "  make generate   Regenerate all catalog.md and doc tables"
	@echo "  make validate   Run all data integrity validators"
	@echo "  make test       Run the test suite"
	@echo "  make lint       Run ruff linter"
	@echo "  make all        build + generate + validate + test"

all: build generate validate test

# ── Catalog ──────────────────────────────────────────────────────────────────

build:
	$(PYTHON) scripts/build_catalog.py

# ── Generators ───────────────────────────────────────────────────────────────

generate: generate-capabilities generate-discoveries generate-detections generate-component-docs

generate-capabilities:
	$(PYTHON) scripts/generate_capability_table.py
	$(PYTHON) scripts/generate_capability_table.py --extended

generate-discoveries:
	$(PYTHON) scripts/generate_discovery_readme.py

generate-detections:
	$(PYTHON) scripts/generate_detection_readme.py

generate-component-docs:
	$(PYTHON) scripts/generate_component_docs_report.py

# ── Validators ───────────────────────────────────────────────────────────────

validate: validate-mappings validate-ontology validate-providers validate-links

validate-mappings:
	$(PYTHON) scripts/validate_mapping_frameworks.py

validate-ontology:
	$(PYTHON) scripts/validate_ontology_taxonomy.py

validate-providers:
	$(PYTHON) scripts/validate_provider_registry.py

validate-links:
	$(PYTHON) scripts/check_markdown_links.py

# ── Tests ─────────────────────────────────────────────────────────────────────

test:
	$(PYTHON) pytest tests/ -q

test-verbose:
	$(PYTHON) pytest tests/ -v

# ── Lint ─────────────────────────────────────────────────────────────────────

lint:
	$(PYTHON) ruff check osco/ scripts/ tests/

lint-fix:
	$(PYTHON) ruff check --fix osco/ scripts/ tests/

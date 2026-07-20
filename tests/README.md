# Tests

This directory contains automated tests validating OSCO registry loading, data models, validation scripts, graph generation, and schema conformance.

## Running Tests

```bash
uv run pytest tests/ -v
```

Or run with coverage:

```bash
uv run pytest tests/ --cov=osco --cov=scripts
```

## Test Modules

### test_models.py
Pydantic model validation for all OSCO types:
- **SafetyClassification** enum (3 classifications: safe, caution, destructive)
- **DiscoveryState** enum (4 states: declared, observed, verified, proven)
- **MappingFramework** enum (26 frameworks: ATT&CK, Sigma, Velociraptor, etc.)
- **Platform** enum (cross-platform, cloud, Windows, Linux, macOS, etc.)
- **DiscoveryMethod** model with state and optional query fields
- **VerificationMethod** model with safe execution support flags
- **CapabilityMapping** model with framework references and confidence scoring
- **Detection**, **Validation**, **Provider**, and **Capability** models with full field validation
- **Tests**: 21 tests validating enum values, model construction, and field constraints

### test_validators.py
Validation script functionality (ontology, mapping frameworks):
- **OntologyTaxonomy**: Path extraction, capability ID validation
  - `iter_allowed_paths()`: Nested taxonomy structure parsing
  - `load_allowed_capabilities()`: YAML taxonomy loading
  - `load_capability_ids()`: Catalog parsing
  - `validate_catalog()`: Coverage checking (missing capability IDs)
  - **Tests**: 8 tests validating taxonomy structures and catalog validation
- **MappingFrameworkValidation**: Framework consistency
  - `load_frameworks_yaml()`: Registry loading
  - `load_frameworks_enum()`: Enum extraction
  - `extract_mapping_frameworks()`: Catalog framework references
  - **Tests**: 5 tests validating framework registry consistency

### test_registry_advanced.py
Advanced registry search, filtering, and data consistency:
- **RegistrySearch** (10 tests):
  - Search capabilities by name/description (case-insensitive)
  - List capabilities (>= 320) and providers (>= 16)
  - Bundle structure verification
  - Detection/validation data loading from bundle
- **RegistryConsistency** (6 tests):
  - Required fields in capabilities and providers
  - Unique IDs across all catalogs
  - Valid provider references in capabilities
  - Valid mapping frameworks in all records

### test_exporters.py
Graph building and export functionality:
- **GraphExports** (4 tests): JSON, GraphML, and Cypher export formats
  - Graph structure preservation (nodes, edges, attributes)
  - Output file generation and content validation
- **GraphBuilding** (8 tests):
  - Node and edge presence (> 0 of each)
  - Node kind classification (capability, provider)
  - Graph directedness verification
  - Reference preservation between registry and graph
- **GraphExportFormats** (1 test): All export formats work end-to-end

### test_graph.py
Original graph building test:
- Graph contains edges (> 0)

### test_registry.py
Original registry tests:
- Registry loads (>= 10 capabilities, >= 16 providers)
- Capability search for "persistence"

### test_schema.py
JSON Schema validation:
- All capabilities in catalog.json validate against jsonschema/capability.schema.json

## Coverage Summary

**Total Tests**: 74 (↑ from 4)
- Model validation: 21 tests
- Validator scripts: 13 tests
- Registry operations: 16 tests
- Graph building: 12 tests
- Original tests: 2 tests
- Schema validation: 1 test

**Coverage by component**:
- ✓ Pydantic models (all enums and model classes)
- ✓ Validation scripts (ontology taxonomy, mapping frameworks)
- ✓ Registry search and filtering
- ✓ Data consistency across catalogs
- ✓ Graph building and exports (JSON, GraphML, Cypher)
- ✓ Schema validation (JSON Schema conformance)

## Key Test Fixtures

- `registry`: Loads OSCORegistry with all catalogs
- `sample_graph`: Creates minimal test graph with capabilities and providers
- `built_graph`: Builds graph from loaded registry data

## CI Integration

Tests run on every push/PR via GitHub Actions. See [.github/workflows/quality-tests.yml](../.github/workflows/quality-tests.yml).

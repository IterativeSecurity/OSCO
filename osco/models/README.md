# Models Package

This package defines strongly typed Pydantic models and enums for OSCO core objects.

## Primary Files

- [core.py](core.py): object models, enums, and bundle container
- [__init__.py](__init__.py): export surface for model imports

## Core Model Types

`core.py` defines:

- `Capability`
- `Provider`
- `Detection`
- `Validation`
- `Evidence`
- `Telemetry`
- `CapabilityMapping`
- `DiscoveryMethod`
- `VerificationMethod`
- `ExecutionImplementation`
- `OSCOBundle`

## Key Enums

- `MappingFramework`
- `Platform`
- `SafetyClassification`
- `DiscoveryState`

## Notes

- These models are the canonical runtime type system for OSCO.
- JSON Schema and other schema artifacts should stay consistent with these models.

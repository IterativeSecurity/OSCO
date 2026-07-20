# Capability Authoring Guide

This guide explains how to add or update capabilities in capability/catalog.json.

## Authoring Workflow

1. Choose a semantic domain and action.
2. Define a stable, implementation-neutral capability_id.
3. Write concise name and description.
4. Set category, platforms, providers, safety, and confidence.
5. Add requirements, preconditions, and postconditions.
6. Add evidence and telemetry context where relevant.
7. Add discovery and verification metadata.
8. Add external mappings with relation and confidence.

## Minimum Quality Checklist

- capability_id follows naming conventions
- stable_id is unique within catalog
- description is vendor-neutral
- at least one provider is listed when known
- mapping entries include framework, external_id, and external_name
- schema and model validation pass

## Validation Commands

- uv run osco/scripts_validate.py
- uv run pytest

## Example

See examples/capability_example.yaml for a compact authoring example.

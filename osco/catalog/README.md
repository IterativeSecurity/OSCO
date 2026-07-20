# Catalog Package

This package contains the OSCO catalog build pipeline and curated knowledge base.

## Primary Files

- [builder.py](builder.py): builds a validated `OSCOBundle` from JSON catalog files
- [critical_capabilities.py](critical_capabilities.py): curated list of critical capability IDs
- [curated_mappings.py](curated_mappings.py): hand-curated capability-to-framework mappings

## Overview

The catalog package is responsible for loading, validating, and assembling the full OSCO capability catalog from on-disk JSON sources into a typed `OSCOBundle` object used by the CLI and exporters.

## Usage

```python
from osco.catalog import build_catalog

bundle = build_catalog()
print(len(bundle.capabilities))
```

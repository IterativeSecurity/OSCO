# Generators Package

This package contains catalog generation logic for producing markdown documentation from OSCO JSON data files.

## Primary Files

- [capabilities.py](capabilities.py): generates `capability/catalog.md` and `capability/catalog.extended.md`
- [detections.py](detections.py): generates `detection/catalog.md` with severity badges
- [discoveries.py](discoveries.py): generates `discovery/catalog.md` with multi-provider query support
- [common.py](common.py): shared utilities (auto-generated file header, write helpers)

## Overview

All generators follow the same pattern: read a JSON source, build a markdown table, and write the output with an auto-generated warning header. Scripts in `scripts/` are thin wrappers that call into this package.

## Usage

```python
from osco.generators import generate_capabilities, generate_detections, generate_discoveries

generate_capabilities()
generate_detections()
generate_discoveries()
```

Or via `make`:

```bash
make generate
```

# OSCO - Open Security Capability Ontology

A comprehensive, vendor-agnostic ontology for security capabilities, discoveries, and detections.

## Overview

OSCO provides a standardized framework for describing:

- **Security Capabilities** - What security functions can be performed
- **Discovery Methods** - How to detect the presence of capabilities
- **Detection Scenarios** - What to look for to identify threats or misconfigurations

## Quick Links

- [Vision & Goals](docs/vision.md) - Understand the project mission
- [Architecture](docs/architecture.md) - Learn the system design
- [Capability Catalog](capability/catalog.md) - Browse all capabilities
- [Discovery Methods](discovery/catalog.md) - See available discovery queries
- [Detection Scenarios](detection/catalog.md) - Review threat detections

## Key Features

✨ **Vendor Agnostic** - Support for multiple tools and platforms (AWS, Azure, GCP, etc.)

📊 **Comprehensive** - Over 1,000 capabilities with discovery and detection mappings

🔗 **Framework Aligned** - MITRE ATT&CK mapping for threat intelligence integration

📚 **Well Documented** - Guides for authoring capabilities, discoveries, and detections

🚀 **Community Driven** - Open contribution model for extending the ontology

## Getting Started

### For Users

1. Browse the [Capability Catalog](capability/catalog.md) to understand available security functions
2. Review [Discovery Methods](discovery/catalog.md) for techniques to detect capabilities
3. Check [Detection Scenarios](detection/catalog.md) for threat detection patterns

### For Contributors

1. Read the [Contribution Guide](CONTRIBUTING.md)
2. Check the [Capability Authoring Guide](docs/capability-authoring-guide.md)
3. Follow the [Best Practices](docs/best-practices.md)
4. Submit pull requests with conventional commits

## Data Organization

```
osco/
├── capability/           # Security capabilities registry
│   ├── catalog.json      # Full capability definitions
│   └── catalog.md        # Generated catalog documentation
├── discovery/            # Discovery methods registry
│   ├── discoveries.json  # Discovery definitions
│   └── catalog.md        # Generated discovery documentation
├── detection/            # Detection scenarios registry
│   ├── detections.json   # Detection definitions
│   └── catalog.md        # Generated detection documentation
├── mappings/             # Framework mappings (MITRE, etc.)
├── provider/             # Tool/platform provider definitions
└── validation/           # Validation rules and schemas
```

## Core Concepts

### Capability
A security function that can be performed (e.g., "List IAM roles", "Check Windows Event Logs")

### Discovery Method
A query or technique to determine if a capability is available (e.g., AWS CLI, PowerShell, osquery)

### Detection
A scenario or indicator that represents a security threat or misconfiguration

## Development

### Prerequisites

- Python 3.11+ (tested on 3.13)
- `uv` package manager v0.4.9+

### Setup

```bash
# Install dependencies
uv sync

# Run tests
make test

# Generate catalogs
make generate

# Validate schemas
make validate

# Build everything
make all
```

## Community

- **GitHub Issues** - Report bugs or request features
- **Discussions** - Ask questions and share ideas
- **Pull Requests** - Contribute code and documentation
- **Code of Conduct** - [Code of Conduct](CODE_OF_CONDUCT.md)

## License

This project is licensed under the [LICENSE](LICENSE) - see file for details.

## Security

For security issues, please see [SECURITY.md](SECURITY.md).

---

**Built with ❤️ by the Iterative Security team and community contributors**

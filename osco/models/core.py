from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class SafetyClassification(str, Enum):
    safe = "safe"
    caution = "caution"
    destructive = "destructive"


class DiscoveryState(str, Enum):
    declared = "declared"
    observed = "observed"
    verified = "verified"
    proven = "proven"


class MappingFramework(str, Enum):
    mitre_attack = "mitre_attack"
    mitre_car = "mitre_car"
    atomic_red_team = "atomic_red_team"
    velociraptor = "velociraptor"
    sigma = "sigma"
    yara = "yara"
    semgrep = "semgrep"
    event_maturity_matrix = "event_maturity_matrix"
    opentelemetry = "opentelemetry"
    openc2 = "openc2"
    openioc = "openioc"
    stix = "stix"
    taxii = "taxii"
    cve = "cve"
    cwe = "cwe"
    capec = "capec"
    cis_benchmarks = "cis_benchmarks"
    nist_800_53 = "nist_800_53"
    pci_dss = "pci_dss"
    iso_27001 = "iso_27001"
    microsoft_security_baselines = "microsoft_security_baselines"
    aws_security_hub = "aws_security_hub"
    google_scc = "google_scc"
    ocsf = "ocsf"
    ecs = "ecs"
    osquery = "osquery"


class Platform(str, Enum):
    windows = "windows"
    linux = "linux"
    macos = "macos"
    cloud = "cloud"
    saas = "saas"
    container = "container"
    network = "network"
    browser = "browser"
    database = "database"
    identity = "identity"
    cross_platform = "cross_platform"


class CapabilityMapping(BaseModel):
    framework: MappingFramework
    external_id: str = Field(..., min_length=1)
    external_name: str = Field(..., min_length=1)
    relation: str = Field(default="maps_to")
    confidence: float = Field(default=0.8, ge=0.0, le=1.0)
    url: str | None = None


class DiscoveryQuery(BaseModel):
    provider: str
    platform: str | None = None
    query: str
    notes: str | None = None


class DiscoveryMethod(BaseModel):
    method_id: str
    type: str
    state: DiscoveryState
    description: str
    query: str | None = None  # legacy single-query field; prefer queries[]
    queries: list[DiscoveryQuery] = Field(default_factory=list)


class VerificationMethod(BaseModel):
    method_id: str
    type: str
    description: str
    supports_dry_run: bool = True
    supports_safe_mode: bool = True
    supports_cleanup: bool = True
    supports_rollback: bool = True


class ExecutionImplementation(BaseModel):
    implementation_id: str
    implementation_type: str
    interface: str
    language: str | None = None
    artifact: str | None = None
    notes: str | None = None


class Evidence(BaseModel):
    evidence_id: str
    type: str
    description: str
    location: str | None = None


class Telemetry(BaseModel):
    telemetry_id: str
    source: str
    event_type: str
    description: str


class Detection(BaseModel):
    detection_id: str
    name: str
    description: str
    severity: str = "medium"  # critical, high, medium, low
    capability_ids: list[str] = Field(default_factory=list)
    data_sources: list[str] = Field(default_factory=list)
    platforms: list[Platform] = Field(default_factory=list)
    mappings: list[CapabilityMapping] = Field(default_factory=list)


class Validation(BaseModel):
    validation_id: str
    name: str
    description: str
    mappings: list[CapabilityMapping] = Field(default_factory=list)


class Provider(BaseModel):
    provider_id: str
    name: str
    category: str
    platforms: list[Platform]
    description: str
    homepage: str | None = None
    supports: list[str] = Field(default_factory=list)


class Capability(BaseModel):
    capability_id: str = Field(..., pattern=r"^[a-z0-9_]+(\.[a-z0-9_]+)+$")
    stable_id: str
    name: str
    description: str
    category: str
    domain: str
    platforms: list[Platform]
    providers: list[str] = Field(default_factory=list)
    version: str = "0.1.0"
    status: str = "draft"
    confidence: float = Field(default=0.7, ge=0.0, le=1.0)
    safety: SafetyClassification = SafetyClassification.caution
    parent_capability: str | None = None
    child_capabilities: list[str] = Field(default_factory=list)
    related_capabilities: list[str] = Field(default_factory=list)
    required_privileges: list[str] = Field(default_factory=list)
    required_software: list[str] = Field(default_factory=list)
    required_configuration: list[str] = Field(default_factory=list)
    required_dependencies: list[str] = Field(default_factory=list)
    preconditions: list[str] = Field(default_factory=list)
    postconditions: list[str] = Field(default_factory=list)
    parameters: dict[str, Any] = Field(default_factory=dict)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    evidence: list[Evidence] = Field(default_factory=list)
    produced_artifacts: list[str] = Field(default_factory=list)
    produced_telemetry: list[Telemetry] = Field(default_factory=list)
    consumed_telemetry: list[str] = Field(default_factory=list)
    cleanup_supported: bool = True
    verification_methods: list[VerificationMethod] = Field(default_factory=list)
    discovery_methods: list[DiscoveryMethod] = Field(default_factory=list)
    execution_metadata: list[ExecutionImplementation] = Field(default_factory=list)
    references: list[str] = Field(default_factory=list)
    mappings: list[CapabilityMapping] = Field(default_factory=list)


class OSCOBundle(BaseModel):
    ontology_version: str = "0.1.0"
    capabilities: list[Capability]
    providers: list[Provider]
    detections: list[Detection] = Field(default_factory=list)
    validations: list[Validation] = Field(default_factory=list)

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Callable
import json
import hashlib

@dataclass(frozen=True)
class HigherDimensionalSpec:
    degree: int
    window_spec: Any

class HigherDimensionalValuation:
    def cycle_space_dim(self, K: Any, d: int) -> int:
        raise NotImplementedError

    def local_cycle_span_dim(self, K: Any, d: int, window_spec: Any) -> int:
        raise NotImplementedError

    def residual_dim(self, K: Any, d: int, window_spec: Any) -> int:
        return self.cycle_space_dim(K, d) - self.local_cycle_span_dim(K, d, window_spec)

@dataclass(frozen=True)
class HigherDimensionalCertificate:
    degree: int
    signature: Mapping[str, Any]
    residual_dim: int

def build_higher_dimensional_certificate(
    K: Any,
    *,
    spec: HigherDimensionalSpec,
    signature_fn: Callable[[Any, int, Any], Mapping[str, Any]],
    valuation: HigherDimensionalValuation,
) -> HigherDimensionalCertificate:
    return HigherDimensionalCertificate(
        degree=spec.degree,
        signature=dict(signature_fn(K, spec.degree, spec.window_spec)),
        residual_dim=valuation.residual_dim(K, spec.degree, spec.window_spec),
    )

def certificate_to_dict(cert: HigherDimensionalCertificate) -> dict[str, Any]:
    return {
        "degree": cert.degree,
        "signature": dict(cert.signature),
        "residual_dim": cert.residual_dim,
    }

def certificate_to_json(cert: HigherDimensionalCertificate) -> str:
    return json.dumps(
        certificate_to_dict(cert),
        sort_keys=True,
        separators=(",", ":"),
    )

def certificate_sha256(cert: HigherDimensionalCertificate) -> str:
    return hashlib.sha256(certificate_to_json(cert).encode("utf-8")).hexdigest()

def validate_certificate_dict(obj: Mapping[str, Any]) -> None:
    if "degree" not in obj:
        raise ValueError("missing key: degree")
    if "signature" not in obj:
        raise ValueError("missing key: signature")
    if "residual_dim" not in obj:
        raise ValueError("missing key: residual_dim")
    if not isinstance(obj["degree"], int):
        raise TypeError("degree must be an int")
    if not isinstance(obj["signature"], dict):
        raise TypeError("signature must be a dict")
    if not isinstance(obj["residual_dim"], int):
        raise TypeError("residual_dim must be an int")

def verify_certificate(cert: HigherDimensionalCertificate, expected_sha256: str | None = None) -> dict[str, Any]:
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    actual = certificate_sha256(cert)
    if expected_sha256 is not None and actual != expected_sha256:
        raise ValueError("hash mismatch")
    return {"ok": True, "sha256": actual}

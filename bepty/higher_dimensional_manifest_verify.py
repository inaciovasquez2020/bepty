from __future__ import annotations

from typing import Any

from .higher_dimensional import certificate_sha256, validate_certificate_dict
from .higher_dimensional_manifest_io import read_higher_dimensional_manifest

def verify_higher_dimensional_manifest_obj(manifest: dict[str, Any]) -> dict[str, Any]:
    cert = manifest["certificate"]
    validate_certificate_dict(cert)
    actual = certificate_sha256(type("TmpCert", (), cert)()) if False else certificate_sha256_from_dict(cert)
    if manifest["sha256"] != actual:
        raise ValueError("manifest sha256 mismatch")
    return {"ok": True, "sha256": actual}

def certificate_sha256_from_dict(cert: dict[str, Any]) -> str:
    from .higher_dimensional import HigherDimensionalCertificate, certificate_sha256
    obj = HigherDimensionalCertificate(
        degree=cert["degree"],
        signature=dict(cert["signature"]),
        residual_dim=cert["residual_dim"],
    )
    return certificate_sha256(obj)

def verify_higher_dimensional_manifest_file(path: str) -> dict[str, Any]:
    return verify_higher_dimensional_manifest_obj(read_higher_dimensional_manifest(path))

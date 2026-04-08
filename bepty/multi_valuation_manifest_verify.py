from __future__ import annotations

from typing import Any

from .multi_valuation_hash import certificate_sha256
from .multi_valuation_manifest_io import read_manifest
from .multi_valuation_schema import validate_certificate_dict

def verify_manifest_obj(manifest: dict[str, Any]) -> dict[str, Any]:
    cert = manifest["certificate"]
    validate_certificate_dict(cert)
    actual = certificate_sha256(cert)
    if manifest["sha256"] != actual:
        raise ValueError("manifest sha256 mismatch")
    return {"ok": True, "sha256": actual}

def verify_manifest_file(path: str) -> dict[str, Any]:
    return verify_manifest_obj(read_manifest(path))

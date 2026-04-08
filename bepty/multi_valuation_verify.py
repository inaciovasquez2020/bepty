from __future__ import annotations

from .multi_valuation_codec import certificate_to_dict
from .multi_valuation_hash import certificate_sha256
from .multi_valuation_schema import validate_certificate_dict

def verify_certificate(cert, expected_sha256: str | None = None) -> dict:
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    actual = certificate_sha256(cert)
    if expected_sha256 is not None and actual != expected_sha256:
        raise ValueError("hash mismatch")
    return {"ok": True, "sha256": actual}

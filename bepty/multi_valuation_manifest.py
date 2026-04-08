from __future__ import annotations

from typing import Any, Callable, Mapping

from .multi_valuation_bundle import build_certificate
from .multi_valuation_codec import certificate_to_dict, certificate_to_json
from .multi_valuation_hash import certificate_sha256
from .multi_valuation_schema import validate_certificate_dict
from .valuation_registry import ValuationRegistry

def build_manifest(
    K: Any,
    window_spec: Any,
    *,
    signature_fn: Callable[[Any, Any], Mapping[str, Any]],
    registry: ValuationRegistry,
) -> dict:
    cert = build_certificate(
        K,
        window_spec,
        signature_fn=signature_fn,
        registry=registry,
    )
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    payload = certificate_to_json(cert)
    return {
        "certificate": obj,
        "sha256": certificate_sha256(cert),
        "json": payload,
    }

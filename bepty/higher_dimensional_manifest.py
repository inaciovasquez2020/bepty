from __future__ import annotations

from typing import Any, Callable, Mapping

from .higher_dimensional import (
    HigherDimensionalSpec,
    HigherDimensionalValuation,
    build_higher_dimensional_certificate,
    certificate_sha256,
    certificate_to_dict,
    certificate_to_json,
    validate_certificate_dict,
)

def build_higher_dimensional_manifest(
    K: Any,
    *,
    spec: HigherDimensionalSpec,
    signature_fn: Callable[[Any, int, Any], Mapping[str, Any]],
    valuation: HigherDimensionalValuation,
) -> dict[str, Any]:
    cert = build_higher_dimensional_certificate(
        K,
        spec=spec,
        signature_fn=signature_fn,
        valuation=valuation,
    )
    obj = certificate_to_dict(cert)
    validate_certificate_dict(obj)
    payload = certificate_to_json(cert)
    return {
        "certificate": obj,
        "sha256": certificate_sha256(cert),
        "json": payload,
    }

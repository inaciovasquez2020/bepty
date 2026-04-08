from __future__ import annotations

from typing import Any, Callable, Mapping

from .multi_valuation import MultiValuationCertificate, MultiValuationFactorization
from .valuation_registry import ValuationRegistry

def build_certificate(
    K: Any,
    window_spec: Any,
    *,
    signature_fn: Callable[[Any, Any], Mapping[str, Any]],
    registry: ValuationRegistry,
) -> MultiValuationCertificate:
    mv = MultiValuationFactorization(
        signature_fn=signature_fn,
        registry=registry,
    )
    return mv.certificate(K, window_spec)

from __future__ import annotations

from typing import Any, Callable, Mapping

from .multi_valuation_manifest import build_manifest
from .valuation_registry import ValuationRegistry

def build_unified_registry_manifest(
    K: Any,
    window_spec: Any,
    *,
    signature_fn: Callable[[Any, Any], Mapping[str, Any]],
    registry: ValuationRegistry,
) -> dict[str, Any]:
    return build_manifest(
        K,
        window_spec,
        signature_fn=signature_fn,
        registry=registry,
    )

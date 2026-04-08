from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping, Optional

from .valuation_registry import ValuationRegistry

@dataclass(frozen=True)
class MultiValuationCertificate:
    signature: Mapping[str, Any]
    valuations: Mapping[str, int]

class MultiValuationFactorization:
    def __init__(
        self,
        signature_fn: Callable[[Any, Any], Mapping[str, Any]],
        valuation_fns: Optional[Mapping[str, Callable[[Any, Any], int]]] = None,
        registry: Optional[ValuationRegistry] = None,
    ) -> None:
        self.signature_fn = signature_fn
        self.valuation_fns = dict(valuation_fns or {})
        self.registry = registry

    def certificate(self, K: Any, window_spec: Any) -> MultiValuationCertificate:
        valuations: Dict[str, int] = {
            name: fn(K, window_spec)
            for name, fn in self.valuation_fns.items()
        }
        if self.registry is not None:
            valuations.update(self.registry.evaluate_all(K))
        return MultiValuationCertificate(
            signature=dict(self.signature_fn(K, window_spec)),
            valuations=valuations,
        )

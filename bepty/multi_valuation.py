from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Mapping

@dataclass(frozen=True)
class MultiValuationCertificate:
    signature: Mapping[str, Any]
    valuations: Mapping[str, int]

class MultiValuationFactorization:
    def __init__(
        self,
        signature_fn: Callable[[Any, Any], Mapping[str, Any]],
        valuation_fns: Mapping[str, Callable[[Any, Any], int]],
    ) -> None:
        self.signature_fn = signature_fn
        self.valuation_fns = dict(valuation_fns)

    def certificate(self, K: Any, window_spec: Any) -> MultiValuationCertificate:
        return MultiValuationCertificate(
            signature=dict(self.signature_fn(K, window_spec)),
            valuations={
                name: fn(K, window_spec)
                for name, fn in self.valuation_fns.items()
            },
        )

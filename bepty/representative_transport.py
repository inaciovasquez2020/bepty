from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Callable, Dict, Hashable, Iterable, Mapping

Signature = Hashable
Valuation = Callable[[Any], int]
RepresentativeSelector = Callable[[Signature], Any]

@dataclass(frozen=True)
class TransportedValuation:
    name: str
    selector: RepresentativeSelector
    base_valuation: Valuation

    def induced_map(self, signatures: Iterable[Signature]) -> Dict[Signature, int]:
        return {sigma: int(self.base_valuation(self.selector(sigma))) for sigma in signatures}

    def evaluate_from_signature(self, sigma: Signature) -> int:
        return int(self.base_valuation(self.selector(sigma)))

def factorizes_via_representatives(
    objects: Iterable[Any],
    sigma_of: Callable[[Any], Signature],
    valuation: Valuation,
    selector: RepresentativeSelector,
) -> bool:
    seen: Dict[Signature, int] = {}
    for obj in objects:
        sigma = sigma_of(obj)
        value = int(valuation(obj))
        if sigma in seen and seen[sigma] != value:
            return False
        seen[sigma] = value
        if int(valuation(selector(sigma))) != value:
            return False
    return True

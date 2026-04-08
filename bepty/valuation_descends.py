from __future__ import annotations

from typing import Any, Callable, Iterable

def valuation_descends_to_signature_image(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuation: Callable[[Any], int],
) -> bool:
    constants = {}
    for K in objects:
        s = signature(K)
        v = valuation(K)
        if s in constants and constants[s] != v:
            return False
        constants[s] = v
    return True

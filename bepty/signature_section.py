from __future__ import annotations

from typing import Any, Callable, Iterable

def choose_signature_representatives(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
) -> dict[Any, Any]:
    reps = {}
    for K in objects:
        s = signature(K)
        if s not in reps:
            reps[s] = K
    return reps

def valuation_factors_via_representatives(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuation: Callable[[Any], int],
) -> bool:
    reps = choose_signature_representatives(objects, signature)
    for K in objects:
        s = signature(K)
        if valuation(K) != valuation(reps[s]):
            return False
    return True

def induced_signature_function(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuation: Callable[[Any], int],
) -> dict[Any, int]:
    reps = choose_signature_representatives(objects, signature)
    return {s: valuation(K) for s, K in reps.items()}

from __future__ import annotations

from typing import Any, Callable

def single_valuation_signature_complete(
    signature_of: Callable[[Any], Any],
    valuation: Callable[[Any], int],
    K1: Any,
    K2: Any,
) -> bool:
    return signature_of(K1) == signature_of(K2) and valuation(K1) == valuation(K2)

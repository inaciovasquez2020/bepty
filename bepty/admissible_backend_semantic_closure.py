from __future__ import annotations

from typing import Any, Callable, Iterable

def admissible_backend_semantic_closure(
    signature: Callable[[Any], Any],
    valuations: Iterable[Callable[[Any], int]],
    K1: Any,
    K2: Any,
) -> bool:
    return signature(K1) != signature(K2) or all(phi(K1) == phi(K2) for phi in valuations)

from __future__ import annotations

from typing import Any, Callable, Iterable

def joint_signature_complete(
    signature: Callable[[Any], Any],
    valuations: Iterable[Callable[[Any], int]],
    K1: Any,
    K2: Any,
) -> bool:
    if signature(K1) != signature(K2):
        return False
    return all(phi(K1) == phi(K2) for phi in valuations)

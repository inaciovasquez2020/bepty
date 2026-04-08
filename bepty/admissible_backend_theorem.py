from __future__ import annotations

from typing import Any, Callable, Iterable

def admissible_backend_joint_completeness(
    admissible_objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuations: Iterable[Callable[[Any], int]],
) -> bool:
    objs = list(admissible_objects)
    for K1 in objs:
        for K2 in objs:
            if signature(K1) == signature(K2):
                for phi in valuations:
                    if phi(K1) != phi(K2):
                        return False
    return True

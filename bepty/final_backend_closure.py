from __future__ import annotations

from typing import Any, Callable, Iterable

def final_backend_closure(
    concrete_objects: Iterable[Any],
    registered_objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuations: Iterable[Callable[[Any], int]],
) -> bool:
    concrete = list(concrete_objects)
    registered = list(registered_objects)

    concrete_image = {signature(K) for K in concrete}
    registered_image = {signature(K) for K in registered}
    if concrete_image != registered_image:
        return False

    for K1 in concrete:
        for K2 in concrete:
            if signature(K1) == signature(K2):
                for phi in valuations:
                    if phi(K1) != phi(K2):
                        return False
    return True

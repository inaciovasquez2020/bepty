from __future__ import annotations

from typing import Any, Callable, Iterable

def backend_signature_closure(
    concrete_objects: Iterable[Any],
    registered_objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuations: Iterable[Callable[[Any], int]],
) -> bool:
    concrete_list = list(concrete_objects)
    registered_list = list(registered_objects)

    concrete_image = {signature(K) for K in concrete_list}
    registered_image = {signature(K) for K in registered_list}
    if concrete_image != registered_image:
        return False

    for K1 in registered_list:
        for K2 in registered_list:
            if signature(K1) == signature(K2):
                for phi in valuations:
                    if phi(K1) != phi(K2):
                        return False
    return True

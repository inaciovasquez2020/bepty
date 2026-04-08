from __future__ import annotations

from typing import Any, Callable, Iterable

def every_admissible_fiber_has_registered_representative(
    all_objects: Iterable[Any],
    registered: Iterable[Any],
    signature: Callable[[Any], Any],
) -> bool:
    reg_sigs = {signature(K) for K in registered}
    return all(signature(K) in reg_sigs for K in all_objects)

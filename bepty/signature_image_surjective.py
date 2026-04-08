from __future__ import annotations

from typing import Any, Callable, Iterable

def signature_image_surjective_on_registered_family(
    concrete_objects: Iterable[Any],
    registered_objects: Iterable[Any],
    signature: Callable[[Any], Any],
) -> bool:
    concrete_image = {signature(K) for K in concrete_objects}
    registered_image = {signature(K) for K in registered_objects}
    return concrete_image == registered_image

from __future__ import annotations

from typing import Any, Callable, Iterable

def witness_family_generates_signature_fibers(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
    representatives: Iterable[Any],
) -> bool:
    rep_sigs = {signature(obj) for obj in representatives}
    return all(signature(obj) in rep_sigs for obj in objects)

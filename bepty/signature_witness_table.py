from __future__ import annotations

from typing import Any, Callable, Iterable

def build_signature_witness_table(
    objects: Iterable[Any],
    signature: Callable[[Any], Any],
    valuations: dict[str, Callable[[Any], int]],
) -> list[dict[str, Any]]:
    rows = []
    for obj in objects:
        rows.append(
            {
                "signature": signature(obj),
                "valuations": {name: phi(obj) for name, phi in valuations.items()},
            }
        )
    return rows

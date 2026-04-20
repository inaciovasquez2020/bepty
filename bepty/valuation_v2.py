from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable, List, Sequence


def _xor_rows_over_f2(rows: Sequence[Sequence[int]], src: int, dst: int) -> None:
    rows[dst][:] = [(a ^ b) for a, b in zip(rows[dst], rows[src])]


def rank_f2(matrix: Sequence[Sequence[int]]) -> int:
    rows: List[List[int]] = [list(map(lambda x: int(x) & 1, row)) for row in matrix if len(row) > 0]
    if not rows:
        return 0
    ncols = len(rows[0])
    r = 0
    for c in range(ncols):
        pivot = None
        for i in range(r, len(rows)):
            if rows[i][c]:
                pivot = i
                break
        if pivot is None:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c]:
                _xor_rows_over_f2(rows, r, i)
        r += 1
        if r == len(rows):
            break
    return r


def cycle_local_span_incidence_matrix_2(obj: Any) -> Sequence[Sequence[int]]:
    if hasattr(obj, "cycle_local_span_incidence_matrix_2"):
        return obj.cycle_local_span_incidence_matrix_2()
    if hasattr(obj, "M2"):
        return obj.M2()
    raise AttributeError("object must expose cycle_local_span_incidence_matrix_2() or M2()")


def LV2_rank(obj: Any) -> int:
    return rank_f2(cycle_local_span_incidence_matrix_2(obj))


@dataclass(frozen=True)
class Phi2:
    target_map: Callable[[int], Any]

    def __call__(self, value: int) -> Any:
        return self.target_map(value)


def V2(obj: Any, phi2: Phi2) -> Any:
    return phi2(LV2_rank(obj))


def LocalValuationD(obj: Any, d: int) -> int:
    if d != 2:
        raise ValueError("only d=2 is implemented in valuation_v2.LocalValuationD")
    return LV2_rank(obj)

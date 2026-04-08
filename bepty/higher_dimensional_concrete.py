from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .higher_dimensional import HigherDimensionalValuation

def _rref_rank_mod2(rows: Sequence[Sequence[int]]) -> int:
    mat = [list(int(x) & 1 for x in row) for row in rows]
    if not mat:
        return 0
    n_rows = len(mat)
    n_cols = len(mat[0]) if mat[0] else 0
    rank = 0
    pivot_row = 0
    for col in range(n_cols):
        pivot = None
        for r in range(pivot_row, n_rows):
            if mat[r][col] == 1:
                pivot = r
                break
        if pivot is None:
            continue
        mat[pivot_row], mat[pivot] = mat[pivot], mat[pivot_row]
        for r in range(n_rows):
            if r != pivot_row and mat[r][col] == 1:
                mat[r] = [(a ^ b) for a, b in zip(mat[r], mat[pivot_row])]
        rank += 1
        pivot_row += 1
        if pivot_row == n_rows:
            break
    return rank

def _nullity_mod2(rows: Sequence[Sequence[int]], n_cols: int) -> int:
    return n_cols - _rref_rank_mod2(rows)

@dataclass(frozen=True)
class MatrixComplex:
    boundary_d: Sequence[Sequence[int]]
    local_cycle_generators: Sequence[Sequence[int]]

class ConcreteHigherDimensionalValuation(HigherDimensionalValuation):
    def cycle_space_dim(self, K: MatrixComplex, d: int) -> int:
        if d < 0:
            raise ValueError("degree must be nonnegative")
        n_d_cells = len(K.boundary_d[0]) if K.boundary_d else len(K.local_cycle_generators[0]) if K.local_cycle_generators else 0
        return _nullity_mod2(K.boundary_d, n_d_cells)

    def local_cycle_span_dim(self, K: MatrixComplex, d: int, window_spec) -> int:
        if d < 0:
            raise ValueError("degree must be nonnegative")
        return _rref_rank_mod2(K.local_cycle_generators)

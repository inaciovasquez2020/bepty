from __future__ import annotations
from dataclasses import dataclass

from bepty.target_family import Graph, connected_components, cycle_rank


@dataclass(frozen=True)
class BEpTyValuation:
    component_gap: int
    cycle_rank_gap: int


def component_cycle_valuation(A: Graph, B: Graph) -> BEpTyValuation:
    return BEpTyValuation(
        component_gap=connected_components(B) - connected_components(A),
        cycle_rank_gap=cycle_rank(B) - cycle_rank(A),
    )


def first_betti_number(G: Graph) -> int:
    return cycle_rank(G)


def betti_gap_valuation(A: Graph, B: Graph) -> int:
    return first_betti_number(B) - first_betti_number(A)


def triangle_count(G: Graph) -> int:
    count = 0
    for a in range(G.n):
        for b in range(a + 1, G.n):
            if not G.has_edge(a, b):
                continue
            for c in range(b + 1, G.n):
                if G.has_edge(a, c) and G.has_edge(b, c):
                    count += 1
    return count


def triangle_gap_valuation(A: Graph, B: Graph) -> int:
    return triangle_count(B) - triangle_count(A)

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

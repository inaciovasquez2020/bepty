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

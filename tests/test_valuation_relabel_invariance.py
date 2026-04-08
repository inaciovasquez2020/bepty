from bepty.target_family import Graph, two_lift_pair_of_cycle
from bepty.valuations import component_cycle_valuation


def relabel_graph(G: Graph, perm: dict[int, int]) -> Graph:
    return Graph(
        n=G.n,
        edges=frozenset(
            (min(perm[u], perm[v]), max(perm[u], perm[v]))
            for (u, v) in G.edges
        ),
    )


def test_component_cycle_valuation_invariant_under_relabeling() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    perm = {i: (i + 3) % fam.plus.n for i in range(fam.plus.n)}
    plus_relab = relabel_graph(fam.plus, perm)
    minus_relab = relabel_graph(fam.minus, perm)

    v0 = component_cycle_valuation(fam.minus, fam.plus)
    v1 = component_cycle_valuation(minus_relab, plus_relab)

    assert v0 == v1

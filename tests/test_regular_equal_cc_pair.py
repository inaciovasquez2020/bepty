from bepty.target_family import connected_components, k33_graph, regular_equal_cc_pair, triangular_prism_graph


def test_regular_equal_cc_pair_basics() -> None:
    fam = regular_equal_cc_pair()

    assert fam.plus.n == fam.minus.n == 6
    assert len(fam.plus.edges) == len(fam.minus.edges) == 9
    assert connected_components(fam.plus) == connected_components(fam.minus) == 1
    assert sorted(fam.plus.degree(v) for v in range(fam.plus.n)) == [3] * 6
    assert sorted(fam.minus.degree(v) for v in range(fam.minus.n)) == [3] * 6


def test_named_regular_graph_builders() -> None:
    assert k33_graph().n == 6
    assert triangular_prism_graph().n == 6

from bepty.target_family import connected_components, regular_equal_cc_pair
from bepty.valuations import triangle_count, triangle_gap_valuation


def test_triangle_gap_separates_equal_cc_regular_pair() -> None:
    fam = regular_equal_cc_pair()

    assert connected_components(fam.plus) == connected_components(fam.minus) == 1
    assert triangle_count(fam.plus) == 0
    assert triangle_count(fam.minus) == 2
    assert triangle_gap_valuation(fam.minus, fam.plus) == -2


def test_actual_class_single_graph_baselines_match_on_regular_pair() -> None:
    fam = regular_equal_cc_pair()

    assert fam.plus.n == fam.minus.n
    assert len(fam.plus.edges) == len(fam.minus.edges)
    assert sorted(fam.plus.degree(v) for v in range(fam.plus.n)) == \
           sorted(fam.minus.degree(v) for v in range(fam.minus.n))
    assert connected_components(fam.plus) == connected_components(fam.minus)

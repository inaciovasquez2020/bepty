from bepty.target_family import connected_components, regular_equal_cc_pair
from bepty.valuations import betti_gap_valuation


def test_betti_gap_separates_equal_cc_regular_pair() -> None:
    fam = regular_equal_cc_pair()

    assert connected_components(fam.plus) == connected_components(fam.minus) == 1
    assert betti_gap_valuation(fam.minus, fam.plus) == 0

from bepty.target_family import two_lift_pair_of_cycle
from bepty.valuations import component_cycle_valuation


def test_component_cycle_valuation_separates_plus_minus() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    val = component_cycle_valuation(fam.minus, fam.plus)
    assert val.component_gap == 1
    assert val.cycle_rank_gap == 1

from bepty.target_family import connected_components, two_lift_pair_of_cycle
from bepty.valuations import component_cycle_valuation


def test_urf_tether_component_gap_implies_nonzero_bepty() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    I_cc = connected_components(fam.plus) - connected_components(fam.minus)
    beta = component_cycle_valuation(fam.minus, fam.plus)

    assert I_cc == 1
    assert I_cc != 0
    assert beta != type(beta)(0, 0)
    assert beta.component_gap == I_cc

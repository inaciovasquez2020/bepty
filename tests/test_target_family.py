from bepty.target_family import two_lift_pair_of_cycle, cycle_rank, connected_components


def test_two_lift_cycle_family_global_separation() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    assert connected_components(fam.plus) == 2
    assert connected_components(fam.minus) == 1
    assert cycle_rank(fam.plus) == 2
    assert cycle_rank(fam.minus) == 1


def test_two_lift_cycle_family_local_degree_match() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    plus_degrees = sorted(fam.plus.degree(v) for v in range(fam.plus.n))
    minus_degrees = sorted(fam.minus.degree(v) for v in range(fam.minus.n))
    assert plus_degrees == minus_degrees == [2] * 16

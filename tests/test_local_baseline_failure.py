from bepty.target_family import two_lift_pair_of_cycle


def test_degree_baseline_cannot_separate_plus_minus() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)
    plus_degrees = sorted(fam.plus.degree(v) for v in range(fam.plus.n))
    minus_degrees = sorted(fam.minus.degree(v) for v in range(fam.minus.n))
    assert plus_degrees == minus_degrees

from bepty.target_family import two_lift_pair_of_cycle


def vertex_count(G) -> int:
    return G.n


def edge_count(G) -> int:
    return len(G.edges)


def degree_multiset(G) -> list[int]:
    return sorted(G.degree(v) for v in range(G.n))


def test_compared_executable_class_fails_on_two_lift_pair() -> None:
    fam = two_lift_pair_of_cycle(8, twist_index=0)

    assert vertex_count(fam.minus) == vertex_count(fam.plus)
    assert edge_count(fam.minus) == edge_count(fam.plus)
    assert degree_multiset(fam.minus) == degree_multiset(fam.plus)

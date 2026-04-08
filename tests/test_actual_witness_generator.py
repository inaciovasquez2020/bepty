from collections import Counter
from examples.actual_witness_generator import Graph, theta_graph, dumbbell_graph


def rooted_ball_code(G, center, R):
    B = G.ball(center, R)
    verts = sorted(B.vertices)
    idx = {v: i for i, v in enumerate(verts)}
    edge_code = tuple(sorted((idx[u], idx[v]) for (u, v) in B.edges))
    center_code = idx[center]
    return (len(verts), edge_code, center_code)


def rooted_ball_histogram(G, R):
    return Counter(rooted_ball_code(G, v, R) for v in G.vertices)


def normalized_histogram(H):
    total = sum(H.values())
    return {k: H[k] / total for k in H}


def test_theta_and_dumbbell_have_same_beta1():
    assert theta_graph().cycle_rank() == 2
    assert dumbbell_graph().cycle_rank() == 2


def test_theta_and_dumbbell_have_same_radius_one_local_cycle_rank_entries():
    theta = theta_graph()
    dumbbell = dumbbell_graph()
    theta_profile = sorted(theta.ball(v, 1).cycle_rank() for v in theta.vertices)
    dumbbell_profile = sorted(dumbbell.ball(v, 1).cycle_rank() for v in dumbbell.vertices)
    assert theta_profile == [0] * len(theta_profile)
    assert dumbbell_profile == [0] * len(dumbbell_profile)


def test_theta_and_dumbbell_are_not_distinguished_merely_by_vertex_count_claim():
    theta = theta_graph()
    dumbbell = dumbbell_graph()
    assert len(theta.vertices) != len(dumbbell.vertices)


def test_theta_and_dumbbell_have_distinct_normalized_rooted_ball_type_histograms():
    theta = theta_graph()
    dumbbell = dumbbell_graph()
    Ht = normalized_histogram(rooted_ball_histogram(theta, 1))
    Hd = normalized_histogram(rooted_ball_histogram(dumbbell, 1))
    assert Ht != Hd

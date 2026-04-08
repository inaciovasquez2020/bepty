from examples.actual_witness_generator import theta_graph, dumbbell_graph
from examples.exact_sheaf_package_compare import (
    exact_sheaf_package_signature,
    normalized_rooted_ball_histogram,
)


def test_theta_and_dumbbell_do_not_have_equal_current_exact_sheaf_signature():
    G = theta_graph()
    H = dumbbell_graph()
    assert exact_sheaf_package_signature(G, 1) != exact_sheaf_package_signature(H, 1)


def test_theta_and_dumbbell_still_have_distinct_normalized_rooted_ball_histograms():
    G = theta_graph()
    H = dumbbell_graph()
    assert normalized_rooted_ball_histogram(G, 1) != normalized_rooted_ball_histogram(H, 1)

from examples.actual_witness_generator import theta_graph, dumbbell_graph, local_cycle_profile


def test_theta_and_dumbbell_have_same_beta1():
    assert theta_graph().cycle_rank() == 2
    assert dumbbell_graph().cycle_rank() == 2


def test_theta_and_dumbbell_have_distinct_radius_one_local_profiles():
    assert local_cycle_profile(theta_graph(), 1) != local_cycle_profile(dumbbell_graph(), 1)

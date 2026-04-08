from bepty.admissible_backend_theorem import admissible_backend_joint_completeness

def test_admissible_backend_joint_completeness_true_case():
    objs = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
        {"sig": ("a", 1), "v1": 3, "v2": 5},
    ]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    assert admissible_backend_joint_completeness(
        objs,
        signature=lambda K: K["sig"],
        valuations=valuations,
    ) is True

def test_admissible_backend_joint_completeness_false_case():
    objs = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("a", 1), "v1": 3, "v2": 8},
    ]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    assert admissible_backend_joint_completeness(
        objs,
        signature=lambda K: K["sig"],
        valuations=valuations,
    ) is False

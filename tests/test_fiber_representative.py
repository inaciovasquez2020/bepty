from bepty.fiber_representative import every_admissible_fiber_has_registered_representative

def test_every_admissible_fiber_has_registered_representative_true_case():
    all_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("a", 1)},
    ]
    registered = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert every_admissible_fiber_has_registered_representative(
        all_objects,
        registered,
        signature=lambda K: K["sig"],
    ) is True

def test_every_admissible_fiber_has_registered_representative_false_case():
    all_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("c", 3)},
    ]
    registered = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert every_admissible_fiber_has_registered_representative(
        all_objects,
        registered,
        signature=lambda K: K["sig"],
    ) is False

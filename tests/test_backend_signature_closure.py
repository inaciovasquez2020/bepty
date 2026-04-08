from bepty.backend_signature_closure import backend_signature_closure

def test_backend_signature_closure_true_case():
    concrete_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
        {"sig": ("a", 1), "v1": 3, "v2": 5},
    ]
    registered_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
    ]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    assert backend_signature_closure(
        concrete_objects,
        registered_objects,
        signature=lambda K: K["sig"],
        valuations=valuations,
    ) is True

def test_backend_signature_closure_false_on_image_gap():
    concrete_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("c", 3), "v1": 9, "v2": 11},
    ]
    registered_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
    ]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    assert backend_signature_closure(
        concrete_objects,
        registered_objects,
        signature=lambda K: K["sig"],
        valuations=valuations,
    ) is False

def test_backend_signature_closure_false_on_fiber_disagreement():
    concrete_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
    ]
    registered_objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("a", 1), "v1": 8, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
    ]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    assert backend_signature_closure(
        concrete_objects,
        registered_objects,
        signature=lambda K: K["sig"],
        valuations=valuations,
    ) is False

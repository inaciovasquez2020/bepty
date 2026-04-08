from bepty.signature_fiber_generation import witness_family_generates_signature_fibers

def test_witness_family_generates_signature_fibers_true_case():
    objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("a", 1)},
    ]
    representatives = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert witness_family_generates_signature_fibers(
        objects,
        signature=lambda K: K["sig"],
        representatives=representatives,
    ) is True

def test_witness_family_generates_signature_fibers_false_case():
    objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("c", 3)},
    ]
    representatives = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert witness_family_generates_signature_fibers(
        objects,
        signature=lambda K: K["sig"],
        representatives=representatives,
    ) is False

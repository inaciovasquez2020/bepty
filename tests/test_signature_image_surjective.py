from bepty.signature_image_surjective import signature_image_surjective_on_registered_family

def test_signature_image_surjective_on_registered_family_true_case():
    concrete_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("a", 1)},
    ]
    registered_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert signature_image_surjective_on_registered_family(
        concrete_objects,
        registered_objects,
        signature=lambda K: K["sig"],
    ) is True

def test_signature_image_surjective_on_registered_family_false_case():
    concrete_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
        {"sig": ("c", 3)},
    ]
    registered_objects = [
        {"sig": ("a", 1)},
        {"sig": ("b", 2)},
    ]
    assert signature_image_surjective_on_registered_family(
        concrete_objects,
        registered_objects,
        signature=lambda K: K["sig"],
    ) is False

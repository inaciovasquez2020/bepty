from bepty.valuation_descends import valuation_descends_to_signature_image

def test_valuation_descends_to_signature_image_true_case():
    objects = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("b", 2), "value": 4},
        {"sig": ("a", 1), "value": 3},
    ]
    assert valuation_descends_to_signature_image(
        objects,
        signature=lambda K: K["sig"],
        valuation=lambda K: K["value"],
    ) is True

def test_valuation_descends_to_signature_image_false_case():
    objects = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("a", 1), "value": 5},
    ]
    assert valuation_descends_to_signature_image(
        objects,
        signature=lambda K: K["sig"],
        valuation=lambda K: K["value"],
    ) is False

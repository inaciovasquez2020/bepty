from bepty.signature_section import (
    choose_signature_representatives,
    induced_signature_function,
    valuation_factors_via_representatives,
)

def test_choose_signature_representatives():
    objs = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("b", 2), "value": 4},
        {"sig": ("a", 1), "value": 3},
    ]
    reps = choose_signature_representatives(objs, signature=lambda K: K["sig"])
    assert reps == {
        ("a", 1): {"sig": ("a", 1), "value": 3},
        ("b", 2): {"sig": ("b", 2), "value": 4},
    }

def test_valuation_factors_via_representatives_true_case():
    objs = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("b", 2), "value": 4},
        {"sig": ("a", 1), "value": 3},
    ]
    assert valuation_factors_via_representatives(
        objs,
        signature=lambda K: K["sig"],
        valuation=lambda K: K["value"],
    ) is True

def test_valuation_factors_via_representatives_false_case():
    objs = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("a", 1), "value": 5},
    ]
    assert valuation_factors_via_representatives(
        objs,
        signature=lambda K: K["sig"],
        valuation=lambda K: K["value"],
    ) is False

def test_induced_signature_function():
    objs = [
        {"sig": ("a", 1), "value": 3},
        {"sig": ("b", 2), "value": 4},
        {"sig": ("a", 1), "value": 3},
    ]
    induced = induced_signature_function(
        objs,
        signature=lambda K: K["sig"],
        valuation=lambda K: K["value"],
    )
    assert induced == {
        ("a", 1): 3,
        ("b", 2): 4,
    }

from bepty.single_valuation_extractor import single_valuation_signature_complete

def test_single_valuation_signature_complete_true_case():
    signature_of = lambda K: K["sig"]
    valuation = lambda K: K["value"]
    K1 = {"sig": ("a", 1), "value": 3}
    K2 = {"sig": ("a", 1), "value": 3}
    assert single_valuation_signature_complete(signature_of, valuation, K1, K2) is True

def test_single_valuation_signature_complete_false_case():
    signature_of = lambda K: K["sig"]
    valuation = lambda K: K["value"]
    K1 = {"sig": ("a", 1), "value": 3}
    K2 = {"sig": ("a", 1), "value": 4}
    assert single_valuation_signature_complete(signature_of, valuation, K1, K2) is False

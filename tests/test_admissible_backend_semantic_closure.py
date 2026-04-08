from bepty.admissible_backend_semantic_closure import admissible_backend_semantic_closure

def test_admissible_backend_semantic_closure_true_same_signature_same_values():
    signature = lambda K: K["sig"]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    K1 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    K2 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    assert admissible_backend_semantic_closure(signature, valuations, K1, K2) is True

def test_admissible_backend_semantic_closure_true_different_signature():
    signature = lambda K: K["sig"]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    K1 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    K2 = {"sig": ("b", 2), "v1": 9, "v2": 8}
    assert admissible_backend_semantic_closure(signature, valuations, K1, K2) is True

def test_admissible_backend_semantic_closure_false_same_signature_disagreement():
    signature = lambda K: K["sig"]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    K1 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    K2 = {"sig": ("a", 1), "v1": 3, "v2": 8}
    assert admissible_backend_semantic_closure(signature, valuations, K1, K2) is False

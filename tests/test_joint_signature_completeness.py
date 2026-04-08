from bepty.joint_signature_completeness import joint_signature_complete

def test_joint_signature_complete_true_case():
    signature = lambda K: K["sig"]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    K1 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    K2 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    assert joint_signature_complete(signature, valuations, K1, K2) is True

def test_joint_signature_complete_false_case():
    signature = lambda K: K["sig"]
    valuations = [
        lambda K: K["v1"],
        lambda K: K["v2"],
    ]
    K1 = {"sig": ("a", 1), "v1": 3, "v2": 5}
    K2 = {"sig": ("a", 1), "v1": 3, "v2": 6}
    assert joint_signature_complete(signature, valuations, K1, K2) is False

from bepty.representative_transport import factorizes_via_representatives, TransportedValuation

def test_factorizes_via_representatives():
    objs = [
        {"sigma": ("a", 1), "value": 3},
        {"sigma": ("a", 1), "value": 3},
        {"sigma": ("b", 2), "value": 5},
    ]
    sigma_of = lambda x: x["sigma"]
    valuation = lambda x: x["value"]
    reps = {
        ("a", 1): {"sigma": ("a", 1), "value": 3},
        ("b", 2): {"sigma": ("b", 2), "value": 5},
    }
    selector = lambda s: reps[s]
    assert factorizes_via_representatives(objs, sigma_of, valuation, selector)

def test_induced_map():
    reps = {
        "x": {"value": 7},
        "y": {"value": 11},
    }
    tv = TransportedValuation(
        name="dim",
        selector=lambda s: reps[s],
        base_valuation=lambda x: x["value"],
    )
    assert tv.induced_map(["x", "y"]) == {"x": 7, "y": 11}
    assert tv.evaluate_from_signature("x") == 7

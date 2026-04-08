from bepty.valuation_factorization import valuation_factors_through_coordinate

def test_valuation_factors_through_coordinate_true_case():
    sigma_phi = lambda K: K["sigma_phi"]
    theta_phi = lambda s: (s["rank"], s["count"])
    G_phi = lambda t: t[0] + t[1]
    valuation = lambda K: K["value"]
    K = {"sigma_phi": {"rank": 2, "count": 3}, "value": 5}
    assert valuation_factors_through_coordinate(
        sigma_phi, theta_phi, G_phi, valuation, K
    ) is True

def test_valuation_factors_through_coordinate_false_case():
    sigma_phi = lambda K: K["sigma_phi"]
    theta_phi = lambda s: (s["rank"], s["count"])
    G_phi = lambda t: t[0] + t[1]
    valuation = lambda K: K["value"]
    K = {"sigma_phi": {"rank": 2, "count": 3}, "value": 6}
    assert valuation_factors_through_coordinate(
        sigma_phi, theta_phi, G_phi, valuation, K
    ) is False

from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_registry_evaluate_and_describe():
    reg = ValuationRegistry(
        {
            "phi_dim": ValuationSpec(
                name="phi_dim",
                degree=1,
                window="r2",
                evaluator=lambda K, W: 3,
            ),
            "phi_residue": ValuationSpec(
                name="phi_residue",
                degree=2,
                window="r3",
                evaluator=lambda K, W: 1,
            ),
        }
    )
    assert reg.evaluate_all(None) == {"phi_dim": 3, "phi_residue": 1}
    assert reg.describe() == {
        "phi_dim": {"degree": 1, "window": "r2"},
        "phi_residue": {"degree": 2, "window": "r3"},
    }

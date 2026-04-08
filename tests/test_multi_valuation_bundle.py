from bepty.multi_valuation_bundle import build_certificate
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_build_certificate_from_registry_bundle():
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
    cert = build_certificate(
        None,
        "rX",
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=reg,
    )
    assert cert.signature == {"cells": 4, "window": "rX"}
    assert cert.valuations == {"phi_dim": 3, "phi_residue": 1}

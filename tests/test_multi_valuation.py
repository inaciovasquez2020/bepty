from bepty.multi_valuation import MultiValuationFactorization
from bepty.valuation_registry import ValuationRegistry, ValuationSpec

def test_multi_valuation_certificate():
    mv = MultiValuationFactorization(
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        valuation_fns={
            "phi_dim": lambda K, W: 3,
            "phi_residue": lambda K, W: 1,
        },
    )
    cert = mv.certificate(None, "r2")
    assert cert.signature == {"cells": 4, "window": "r2"}
    assert cert.valuations == {"phi_dim": 3, "phi_residue": 1}

def test_multi_valuation_certificate_from_registry():
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
    mv = MultiValuationFactorization(
        signature_fn=lambda K, W: {"cells": 4, "window": W},
        registry=reg,
    )
    cert = mv.certificate(None, "rX")
    assert cert.signature == {"cells": 4, "window": "rX"}
    assert cert.valuations == {"phi_dim": 3, "phi_residue": 1}

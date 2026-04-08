from bepty.multi_valuation import MultiValuationFactorization

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

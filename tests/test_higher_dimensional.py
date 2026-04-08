import pytest

from bepty.higher_dimensional import (
    HigherDimensionalSpec,
    HigherDimensionalValuation,
    build_higher_dimensional_certificate,
    certificate_sha256,
    certificate_to_dict,
    certificate_to_json,
    validate_certificate_dict,
    verify_certificate,
)

class DummyValuation(HigherDimensionalValuation):
    def cycle_space_dim(self, K, d: int) -> int:
        return 7 + d

    def local_cycle_span_dim(self, K, d: int, window_spec) -> int:
        return 3

def test_build_certificate():
    spec = HigherDimensionalSpec(degree=2, window_spec="r3")
    cert = build_higher_dimensional_certificate(
        None,
        spec=spec,
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 5},
        valuation=DummyValuation(),
    )
    assert cert.degree == 2
    assert cert.signature == {"degree": 2, "window": "r3", "cells": 5}
    assert cert.residual_dim == 6

def test_codec_and_hash_and_verify():
    spec = HigherDimensionalSpec(degree=2, window_spec="r3")
    cert = build_higher_dimensional_certificate(
        None,
        spec=spec,
        signature_fn=lambda K, d, w: {"degree": d, "window": w, "cells": 5},
        valuation=DummyValuation(),
    )
    obj = certificate_to_dict(cert)
    assert obj == {
        "degree": 2,
        "signature": {"degree": 2, "window": "r3", "cells": 5},
        "residual_dim": 6,
    }
    assert certificate_to_json(cert) == '{"degree":2,"residual_dim":6,"signature":{"cells":5,"degree":2,"window":"r3"}}'
    expected = certificate_sha256(cert)
    assert verify_certificate(cert, expected) == {"ok": True, "sha256": expected}

def test_validate_rejects_bad_residual_dim():
    with pytest.raises(TypeError):
        validate_certificate_dict(
            {
                "degree": 2,
                "signature": {"degree": 2, "window": "r3"},
                "residual_dim": "6",
            }
        )

def test_verify_rejects_bad_hash():
    spec = HigherDimensionalSpec(degree=2, window_spec="r3")
    cert = build_higher_dimensional_certificate(
        None,
        spec=spec,
        signature_fn=lambda K, d, w: {"degree": d, "window": w},
        valuation=DummyValuation(),
    )
    with pytest.raises(ValueError):
        verify_certificate(cert, "0" * 64)

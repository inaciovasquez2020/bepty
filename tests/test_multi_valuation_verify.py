import pytest

from bepty.multi_valuation import MultiValuationCertificate
from bepty.multi_valuation_hash import certificate_sha256
from bepty.multi_valuation_verify import verify_certificate

def test_verify_certificate_accepts_valid_certificate():
    cert = MultiValuationCertificate(
        signature={"window": "r2", "cells": 4},
        valuations={"phi_dim": 3, "phi_residue": 1},
    )
    expected = certificate_sha256(cert)
    assert verify_certificate(cert, expected) == {"ok": True, "sha256": expected}

def test_verify_certificate_rejects_bad_hash():
    cert = MultiValuationCertificate(
        signature={"window": "r2", "cells": 4},
        valuations={"phi_dim": 3, "phi_residue": 1},
    )
    with pytest.raises(ValueError):
        verify_certificate(cert, "0" * 64)

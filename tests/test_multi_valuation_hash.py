import hashlib

from bepty.multi_valuation import MultiValuationCertificate
from bepty.multi_valuation_codec import certificate_to_json
from bepty.multi_valuation_hash import certificate_sha256

def test_certificate_sha256():
    cert = MultiValuationCertificate(
        signature={"window": "r2", "cells": 4},
        valuations={"phi_dim": 3, "phi_residue": 1},
    )
    expected = hashlib.sha256(certificate_to_json(cert).encode("utf-8")).hexdigest()
    assert certificate_sha256(cert) == expected

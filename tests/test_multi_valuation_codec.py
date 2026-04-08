from bepty.multi_valuation import MultiValuationCertificate
from bepty.multi_valuation_codec import certificate_to_dict, certificate_to_json

def test_certificate_codec():
    cert = MultiValuationCertificate(
        signature={"window": "r2", "cells": 4},
        valuations={"phi_dim": 3, "phi_residue": 1},
    )
    assert certificate_to_dict(cert) == {
        "signature": {"window": "r2", "cells": 4},
        "valuations": {"phi_dim": 3, "phi_residue": 1},
    }
    assert certificate_to_json(cert) == (
        '{"signature":{"cells":4,"window":"r2"},'
        '"valuations":{"phi_dim":3,"phi_residue":1}}'
    )

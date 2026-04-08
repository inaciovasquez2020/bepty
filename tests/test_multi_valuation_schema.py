import pytest

from bepty.multi_valuation_schema import validate_certificate_dict

def test_validate_certificate_dict_accepts_normal_form():
    validate_certificate_dict(
        {
            "signature": {"cells": 4, "window": "r2"},
            "valuations": {"phi_dim": 3, "phi_residue": 1},
        }
    )

def test_validate_certificate_dict_rejects_bad_valuation_value():
    with pytest.raises(TypeError):
        validate_certificate_dict(
            {
                "signature": {"cells": 4, "window": "r2"},
                "valuations": {"phi_dim": "3"},
            }
        )

import pytest

from bepty.bounded_search_negative_result import (
    build_manifest,
    certificate_sha256,
    certificate_to_dict,
    certificate_to_json,
    run_bounded_search,
    validate_certificate_dict,
    verify_certificate,
)

def test_run_bounded_search_negative_result():
    objs = [
        {"sig": ("a", 1), "value": 1},
        {"sig": ("b", 2), "value": 2},
        {"sig": ("a", 1), "value": 3},
    ]
    cert = run_bounded_search(
        objs,
        predicate=lambda K: K["value"] == 99,
        signature=lambda K: K["sig"],
        bound=3,
        search_name="no-hit",
    )
    assert cert.search_name == "no-hit"
    assert cert.bound == 3
    assert cert.explored == 3
    assert cert.found is False
    assert cert.witness is None
    assert cert.signature_image_size == 2

def test_run_bounded_search_positive_result():
    objs = [
        {"sig": ("a", 1), "value": 1},
        {"sig": ("b", 2), "value": 2},
        {"sig": ("c", 3), "value": 7},
    ]
    cert = run_bounded_search(
        objs,
        predicate=lambda K: K["value"] == 7,
        signature=lambda K: K["sig"],
        bound=5,
        search_name="hit",
    )
    assert cert.found is True
    assert cert.witness == {"sig": ("c", 3), "value": 7}
    assert cert.explored == 3
    assert cert.signature_image_size == 3

def test_codec_hash_verify_and_manifest():
    objs = [
        {"sig": ("a", 1), "value": 1},
        {"sig": ("b", 2), "value": 2},
    ]
    cert = run_bounded_search(
        objs,
        predicate=lambda K: K["value"] == 99,
        signature=lambda K: K["sig"],
        bound=2,
        search_name="no-hit",
    )
    obj = certificate_to_dict(cert)
    assert obj == {
        "search_name": "no-hit",
        "bound": 2,
        "explored": 2,
        "found": False,
        "witness": None,
        "signature_image_size": 2,
    }
    assert certificate_to_json(cert) == (
        '{"bound":2,"explored":2,"found":false,'
        '"search_name":"no-hit","signature_image_size":2,"witness":null}'
    )
    expected = certificate_sha256(cert)
    assert verify_certificate(cert, expected) == {"ok": True, "sha256": expected}
    manifest = build_manifest(cert)
    assert manifest["certificate"] == obj
    assert manifest["sha256"] == expected

def test_validate_rejects_bad_bound():
    with pytest.raises(TypeError):
        validate_certificate_dict(
            {
                "search_name": "x",
                "bound": "2",
                "explored": 2,
                "found": False,
                "witness": None,
                "signature_image_size": 1,
            }
        )

def test_verify_rejects_bad_hash():
    objs = [{"sig": ("a", 1), "value": 1}]
    cert = run_bounded_search(
        objs,
        predicate=lambda K: False,
        signature=lambda K: K["sig"],
        bound=1,
    )
    with pytest.raises(ValueError):
        verify_certificate(cert, "0" * 64)

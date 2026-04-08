from bepty.signature_witness_table import build_signature_witness_table

def test_build_signature_witness_table():
    objects = [
        {"sig": ("a", 1), "v1": 3, "v2": 5},
        {"sig": ("b", 2), "v1": 4, "v2": 7},
    ]
    table = build_signature_witness_table(
        objects,
        signature=lambda K: K["sig"],
        valuations={
            "v1": lambda K: K["v1"],
            "v2": lambda K: K["v2"],
        },
    )
    assert table == [
        {"signature": ("a", 1), "valuations": {"v1": 3, "v2": 5}},
        {"signature": ("b", 2), "valuations": {"v1": 4, "v2": 7}},
    ]

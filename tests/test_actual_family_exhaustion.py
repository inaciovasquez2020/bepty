import json
from itertools import product
from pathlib import Path

from bepty.exact_quotient import J
from bepty.intended_actual_class import (
    enumerate_intended_actual_objects,
    intended_are_isomorphic,
    reduction_R,
)
from bepty.valuation_v2 import Phi2, V2


def test_reduction_preserves_j_and_v2():
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    for x in enumerate_intended_actual_objects():
        rx = reduction_R(x)
        assert J(x) == J(rx)
        assert V2(x, phi2) == V2(rx, phi2)
        assert x.iso_tag == rx.iso_tag


def test_global_nonrecoverability_on_intended_actual_class():
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    objs = list(enumerate_intended_actual_objects())
    for x, y in product(objs, objs):
        if J(x) == J(y) and V2(x, phi2) != V2(y, phi2):
            assert not intended_are_isomorphic(x, y)


def test_exhaustion_artifact_present():
    payload = json.loads(Path("artifacts/bepty_actual_witness/exhaustion_check.json").read_text())
    assert payload["status"] == "PROVED-FOR-INTENDED-CLASS"
    assert payload["lemma"] == "Actual-Family Exhaustion Lemma"

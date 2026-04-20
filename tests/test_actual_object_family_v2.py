import json
from pathlib import Path

from bepty.actual_object_family import are_isomorphic, enumerate_actual_objects
from bepty.exact_quotient import J
from bepty.target_family_search import first_v2_witness
from bepty.valuation_v2 import LV2_rank, Phi2, V2


def test_m2_and_v2_invariance_on_isomorphic_copies():
    objs = list(enumerate_actual_objects())
    x = objs[0]
    x_copy = type(x)(
        name="actual_alpha_copy",
        fn=x.fn,
        lspan=x.lspan,
        cells2=x.cells2,
        spans2=x.spans2,
        incidence2=x.incidence2,
        iso_tag=x.iso_tag,
    )
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    assert are_isomorphic(x, x_copy)
    assert LV2_rank(x) == LV2_rank(x_copy)
    assert V2(x, phi2) == V2(x_copy, phi2)


def test_actual_witness_exists():
    objs = enumerate_actual_objects()
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    witness = first_v2_witness(objs, phi2)
    assert witness is not None
    assert J(witness.X) == J(witness.Y)
    assert witness.v2x != witness.v2y
    assert not are_isomorphic(witness.X, witness.Y)


def test_actual_witness_artifact():
    payload = json.loads(Path("artifacts/bepty_actual_witness/witness_actual.json").read_text())
    assert payload["status"] == "CONDITIONAL"
    assert payload["family"] == "ActualBEpTy"
    assert payload["J_equal"] is True
    assert payload["V2_distinct"] is True
    assert payload["nonisomorphic_by_iso_tag"] is True


def test_theorem_lock_present():
    text = Path("docs/math/BEPTY_ACTUAL_V2_NONRECOVERABILITY_THEOREM.md").read_text()
    assert "CONDITIONAL" in text
    assert "J(X)\\cong J(Y)" in text
    assert "Do not add \\(V_3,V_4,\\dots\\) unless \\(V_2\\) fails" in text

import json
from pathlib import Path

from bepty.exact_quotient import J
from bepty.object_family import are_isomorphic, enumerate_actual_target_family_objects
from bepty.target_family_search import first_v2_witness
from bepty.valuation_v2 import Phi2


def test_actual_family_witness_exists():
    objs = enumerate_actual_target_family_objects()
    phi2 = Phi2(target_map=lambda r: ("urf-rank-f2", r))
    witness = first_v2_witness(objs, phi2)
    assert witness is not None
    assert J(witness.X) == J(witness.Y)
    assert witness.v2x != witness.v2y
    assert not are_isomorphic(witness.X, witness.Y)


def test_witness_artifact_is_frozen():
    payload = json.loads(Path("artifacts/bepty_v2_witness/witness.json").read_text())
    assert payload["status"] == "CONDITIONAL"
    assert payload["J_equal"] is True
    assert payload["V2_distinct"] is True
    assert payload["nonisomorphic_by_iso_tag"] is True


def test_theorem_lock_present():
    text = Path("docs/math/BEPTY_V2_NONRECOVERABILITY_THEOREM.md").read_text()
    assert "## Status" in text
    assert "CONDITIONAL" in text
    assert "J(X)\\cong J(Y)" in text

import json
from pathlib import Path

from src.bridge.bepty_ym_bridge import generate_bridge_report, write_bridge_report


def test_generate_bridge_report_matches_actual_class_exclusion() -> None:
    r = generate_bridge_report()
    assert r.family_name == "regular_equal_cc_pair"
    assert r.vertex_count_equal is True
    assert r.edge_count_equal is True
    assert r.degree_multiset_equal is True
    assert r.connected_component_gap == 0
    assert r.left_triangle_count == 2
    assert r.right_triangle_count == 0
    assert r.triangle_gap == -2
    assert r.admissible_for_actual_class_exclusion is True
    assert r.status == "conditional-executable-witness"


def test_write_bridge_report_emits_json(tmp_path: Path) -> None:
    out = write_bridge_report(tmp_path / "HED_MATH_CONDITIONAL.json")
    payload = json.loads(out.read_text())
    assert payload["triangle_gap"] == -2
    assert payload["admissible_for_actual_class_exclusion"] is True

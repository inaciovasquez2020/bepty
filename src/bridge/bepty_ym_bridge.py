from __future__ import annotations
from dataclasses import dataclass, asdict
from pathlib import Path
import json

from bepty.target_family import regular_equal_cc_pair
from bepty.valuations import triangle_gap_valuation, triangle_count


@dataclass(frozen=True)
class BEpTyBridgeReport:
    family_name: str
    left_name: str
    right_name: str
    vertex_count_equal: bool
    edge_count_equal: bool
    degree_multiset_equal: bool
    connected_component_gap: int
    left_triangle_count: int
    right_triangle_count: int
    triangle_gap: int
    admissible_for_actual_class_exclusion: bool
    target_lemma: str
    status: str


def generate_bridge_report() -> BEpTyBridgeReport:
    fam = regular_equal_cc_pair()
    left = fam.minus
    right = fam.plus

    left_deg = sorted(left.degree(v) for v in range(left.n))
    right_deg = sorted(right.degree(v) for v in range(right.n))

    left_tri = triangle_count(left)
    right_tri = triangle_count(right)
    tri_gap = triangle_gap_valuation(left, right)

    report = BEpTyBridgeReport(
        family_name="regular_equal_cc_pair",
        left_name="triangular_prism",
        right_name="k33",
        vertex_count_equal=(left.n == right.n),
        edge_count_equal=(len(left.edges) == len(right.edges)),
        degree_multiset_equal=(left_deg == right_deg),
        connected_component_gap=0,
        left_triangle_count=left_tri,
        right_triangle_count=right_tri,
        triangle_gap=tri_gap,
        admissible_for_actual_class_exclusion=(
            left.n == right.n
            and len(left.edges) == len(right.edges)
            and left_deg == right_deg
            and tri_gap != 0
        ),
        target_lemma="Spectral Contraction Lemma bridge placeholder",
        status="conditional-executable-witness",
    )
    return report


def write_bridge_report(path: str | Path) -> Path:
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    report = generate_bridge_report()
    out.write_text(json.dumps(asdict(report), indent=2, sort_keys=True) + "\n")
    return out


if __name__ == "__main__":
    path = write_bridge_report("artifacts/HED_MATH_CONDITIONAL.json")
    print(path)

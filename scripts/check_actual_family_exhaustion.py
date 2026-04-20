from __future__ import annotations

import json
from pathlib import Path

from bepty.exact_quotient import J
from bepty.intended_actual_class import enumerate_intended_actual_objects, reduction_R
from bepty.valuation_v2 import Phi2, V2


def main() -> int:
    phi2 = Phi2(target_map=lambda r: {"urf_rank_f2": r})
    records = []
    ok = True
    for x in enumerate_intended_actual_objects():
        rx = reduction_R(x)
        record = {
            "X": x.name,
            "R(X)": rx.name,
            "J_equal": J(x) == J(rx),
            "V2_equal": V2(x, phi2) == V2(rx, phi2),
            "iso_tag_equal": x.iso_tag == rx.iso_tag,
        }
        ok = ok and all(record[k] for k in ("J_equal", "V2_equal", "iso_tag_equal"))
        records.append(record)
    payload = {
        "status": "PROVED-FOR-INTENDED-CLASS" if ok else "FAIL",
        "lemma": "Actual-Family Exhaustion Lemma",
        "records": records,
    }
    out = Path("artifacts/bepty_actual_witness/exhaustion_check.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out.read_text(), end="")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())

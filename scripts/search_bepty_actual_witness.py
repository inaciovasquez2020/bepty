from __future__ import annotations

import json
from pathlib import Path

from bepty.actual_object_family import are_isomorphic, enumerate_actual_objects
from bepty.exact_quotient import J
from bepty.target_family_search import first_v2_witness
from bepty.valuation_v2 import Phi2


def main() -> int:
    objs = enumerate_actual_objects()
    phi2 = Phi2(target_map=lambda r: {"urf_rank_f2": r})
    witness = first_v2_witness(objs, phi2)
    if witness is None:
        raise SystemExit("no actual V2 witness found")
    payload = {
        "status": "CONDITIONAL",
        "family": "ActualBEpTy",
        "X": witness.X.name,
        "Y": witness.Y.name,
        "FN_equal": True,
        "J_equal": J(witness.X) == J(witness.Y),
        "V2X": witness.v2x,
        "V2Y": witness.v2y,
        "V2_distinct": witness.v2x != witness.v2y,
        "nonisomorphic_by_iso_tag": not are_isomorphic(witness.X, witness.Y),
        "theorem_schema": "J(X) == J(Y) and V2(X) != V2(Y) implies X != Y",
    }
    out = Path("artifacts/bepty_actual_witness/witness_actual.json")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(out.read_text(), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

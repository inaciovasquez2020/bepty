#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(".")

REQUIRED_FILES = [
    "docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md",
    "docs/math/BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02.md",
    "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
    "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
    "docs/status/BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02.md",
    "artifacts/bepty_high_girth_local_v33/witness.json",
    "artifacts/bepty_v33_finite_normalization/compatibility_reduction.json",
    "artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json",
    "artifacts/bepty_n_dege_normalized_closure_lock/status_lock_certificate.json",
]


def require_file(path):
    p = ROOT / path
    if not p.exists():
        raise AssertionError(f"missing required file: {path}")
    return p


def require_text(path, tokens):
    s = require_file(path).read_text()
    for token in tokens:
        if token not in s:
            raise AssertionError(f"missing token in {path}: {token}")
    return s


def require_json_status(path, status="PASS"):
    data = json.loads(require_file(path).read_text())
    if data.get("status") != status:
        raise AssertionError(f"{path} status is not {status}")
    return data


def main():
    for path in REQUIRED_FILES:
        require_file(path)

    require_text(
        "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
        [
            "Status: N_DEGE_NORMALIZED CLOSURE LOCK",
            "does not assert unrestricted BEpTy closure",
            "does not assert normalizer-independence",
        ],
    )

    require_text(
        "docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md",
        [
            "Status: PROPOSED CLOSURE PACKET",
            "v_{33}(G_m)=1",
            "v_{33}(H_m)=0",
        ],
    )

    require_text(
        "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
        [
            "Status: EXPLICIT NORMALIZER PACKET",
            "N_{\\deg E}(X)=\\mathcal E_{\\deg}(X)",
            "v_{33}(N_{\\deg E}(X))=v_{33}(X)",
        ],
    )

    require_text(
        "docs/status/BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02.md",
        [
            "Status: FRONTIER_OPEN",
            "remaining obstruction is unrestricted normalizer-independence",
            "\\forall N\\in\\mathsf{AdmNorm}_{\\mathrm{BEpTy}}",
            "This does not assert unrestricted BEpTy closure unless normalizer-independence is proved.",
            "This does not promote \\(N_{\\deg E}\\)-normalized closure to unrestricted closure.",
            "Unrestricted closure requires a theorem about all admissible BEpTy normalizers.",
            "If admissible normalizers are unconstrained, unrestricted normalizer-independence is false.",
            "N_0(X)=\\varnothing",
            "v_{33}(N_0(G_m))\\ne v_{33}(G_m)",
        ],
    )

    witness = require_json_status("artifacts/bepty_high_girth_local_v33/witness.json")
    reduction = require_json_status("artifacts/bepty_v33_finite_normalization/compatibility_reduction.json")
    normalizer = require_json_status("artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json")
    lock = require_json_status("artifacts/bepty_n_dege_normalized_closure_lock/status_lock_certificate.json")

    if witness.get("corrected_ball_bound") != "girth(G) > 2R + 1":
        raise AssertionError("high-girth corrected ball bound not locked")

    if "degree-labeled edge-incidence multiset preservation implies v33 preservation" not in reduction.get("proved_reduction", ""):
        raise AssertionError("v33 compatibility reduction not locked")

    if normalizer.get("theorem") != "v33(N_degE(X)) = v33(X)":
        raise AssertionError("N_degE theorem not locked")

    if lock.get("classification") != "N_DEGE_NORMALIZED_CLOSURE_ONLY":
        raise AssertionError("N_degE-normalized closure-only classification not locked")

    out = {
        "status": "FRONTIER_OPEN",
        "frontier": "BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02",
        "current_closure": "N_DEGE_NORMALIZED_CLOSURE_ONLY",
        "remaining_obstruction": "normalizer-independence / unrestricted BEpTy closure",
        "missing_theorem": "forall admissible BEpTy normalizers N, v33(N(X)) = v33(X)",
        "sufficient_theorem": "forall admissible BEpTy normalizers N, E_deg(N(X)) = E_deg(X)",
        "conditional_refutation": "If admissible normalizers are unconstrained, the constant empty normalizer refutes unrestricted normalizer-independence.",
        "not_claimed": [
            "unrestricted BEpTy closure",
            "normalizer-independence",
            "all finite-normalization maps preserve E_deg",
        ],
    }

    path = ROOT / "artifacts/bepty_normalizer_independence_frontier/status.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy normalizer-independence frontier verification: PASS")


if __name__ == "__main__":
    main()

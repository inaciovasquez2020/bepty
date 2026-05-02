#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(".")


REQUIRED_FILES = [
    "docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md",
    "docs/math/BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02.md",
    "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
    "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
    "artifacts/bepty_high_girth_local_v33/witness.json",
    "artifacts/bepty_v33_finite_normalization/compatibility_reduction.json",
    "artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json",
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


def require_json(path, expected_status="PASS"):
    data = json.loads(require_file(path).read_text())
    if data.get("status") != expected_status:
        raise AssertionError(f"{path} status is not {expected_status}")
    return data


def main():
    for path in REQUIRED_FILES:
        require_file(path)

    require_text(
        "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
        [
            "Status: N_DEGE_NORMALIZED CLOSURE LOCK",
            "N_{\\deg E}(X)=\\mathcal E_{\\deg}(X)",
            "v_{33}(N_{\\deg E}(X))=v_{33}(X)",
            "v_{33}(G_m)=1,\\qquad v_{33}(H_m)=0",
            "does not assert unrestricted BEpTy closure",
            "does not assert normalizer-independence",
            "remaining open object is unrestricted BEpTy closure",
        ],
    )

    require_text(
        "docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md",
        [
            "Status: PROPOSED CLOSURE PACKET",
            "girth}(G)>2R+1",
            "v_{33}",
            "{#V,#E,L_{\\deg},I_{cc}}",
        ],
    )

    require_text(
        "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
        [
            "Status: EXPLICIT NORMALIZER PACKET",
            "N_{\\deg E}(X)=\\mathcal E_{\\deg}(X)",
            "v_{33}(N_{\\deg E}(X))=v_{33}(X)",
            "does not assert unrestricted BEpTy closure",
        ],
    )

    witness = require_json("artifacts/bepty_high_girth_local_v33/witness.json")
    normalizer = require_json("artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json")
    reduction = require_json("artifacts/bepty_v33_finite_normalization/compatibility_reduction.json")

    if witness.get("corrected_ball_bound") != "girth(G) > 2R + 1":
        raise AssertionError("corrected ball bound is not locked")

    if normalizer.get("theorem") != "v33(N_degE(X)) = v33(X)":
        raise AssertionError("normalizer theorem is not locked")

    if "degree-labeled edge-incidence multiset preservation implies v33 preservation" not in reduction.get("proved_reduction", ""):
        raise AssertionError("compatibility reduction is not locked")

    out = {
        "status": "PASS",
        "lock": "BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02",
        "classification": "N_DEGE_NORMALIZED_CLOSURE_ONLY",
        "closed_relative_to": "N_degE(X) = degree-labeled edge-incidence multiset",
        "not_claimed": [
            "unrestricted BEpTy closure",
            "normalizer-independence",
            "all finite-normalization maps preserve E_deg",
        ],
    }

    path = ROOT / "artifacts/bepty_n_dege_normalized_closure_lock/status_lock_certificate.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy N_degE-normalized closure lock verification: PASS")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import json
from pathlib import Path


ROOT = Path(".")

REQUIRED_FILES = [
    "docs/status/BEPTY_FINAL_STATUS_INDEX_2026_05_02.md",
    "docs/math/BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02.md",
    "docs/math/BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02.md",
    "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
    "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
    "docs/status/BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02.md",
    "docs/math/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_2026_05_02.md",
    "docs/status/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_STATUS_2026_05_02.md",
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


def main():
    for path in REQUIRED_FILES:
        require_file(path)

    require_text(
        "docs/status/BEPTY_FINAL_STATUS_INDEX_2026_05_02.md",
        [
            "Status: FINAL STATUS INDEX",
            "N_{\\deg E}\\text{-NORMALIZED CLOSURE ONLY}",
            "High-girth local \\(v_{33}\\) separating packet",
            "Finite-normalization compatibility reduction",
            "Explicit degree-edge normalizer \\(N_{\\deg E}\\)",
            "\\(N_{\\deg E}\\)-normalized closure lock",
            "Normalizer-independence frontier lock",
            "Normalizer Dichotomy / Maximality lock",
            "v_{33}(N_{\\deg E}(X))=v_{33}(X)",
            "v_{33}(G_m)=1,\\qquad v_{33}(H_m)=0",
            "\\mathsf{AdmNorm}_{\\mathrm{BEpTy}}\\subseteq\\mathsf{AdmNorm}_{v33}",
            "This does not assert unrestricted BEpTy closure.",
            "This does not assert normalizer-independence.",
            "This does not declare \\(\\mathsf{AdmNorm}_{v33}\\) as a foundational BEpTy axiom.",
            "This does not promote beyond \\(N_{\\deg E}\\)-normalized closure.",
        ],
    )

    require_text(
        "docs/status/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_STATUS_2026_05_02.md",
        [
            "Status: NORMALIZER_DICHOTOMY_MAXIMALITY_LOCK",
            "This certifies maximality of the current \\(N_{\\deg E}\\)-normalized closure status under the existing repository assumptions.",
        ],
    )

    out = {
        "status": "PASS",
        "classification": "FINAL_STATUS_INDEX_LOCK",
        "repository_status": "N_DEGE_NORMALIZED_CLOSURE_ONLY",
        "locked_chain": [
            "high-girth local v33 separating packet",
            "finite-normalization compatibility reduction",
            "explicit degree-edge normalizer N_degE",
            "N_degE-normalized closure lock",
            "normalizer-independence frontier lock",
            "normalizer dichotomy maximality lock",
        ],
        "future_promotion_requires": "AdmNorm_BEpTy subset AdmNorm_v33",
        "not_claimed": [
            "unrestricted BEpTy closure",
            "normalizer-independence",
            "AdmNorm_v33 declared as foundational BEpTy axiom",
            "promotion beyond N_degE-normalized closure",
        ],
    }

    path = ROOT / "artifacts/bepty_final_status_index/final_status_index_certificate.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy final status index verification: PASS")


if __name__ == "__main__":
    main()

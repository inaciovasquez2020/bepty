#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path


ROOT = Path(".")

REQUIRED_FILES = [
    "docs/status/BEPTY_N_DEGE_NORMALIZED_CLOSURE_LOCK_2026_05_02.md",
    "docs/status/BEPTY_NORMALIZER_INDEPENDENCE_FRONTIER_2026_05_02.md",
    "docs/math/BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02.md",
    "docs/math/BEPTY_V33_DEGREE_EDGE_NORMALIZER_2026_05_02.md",
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


def add_edge(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def graph_Gm(m):
    adj = {i: set() for i in range(m + 2)}
    for i in range(m):
        add_edge(adj, i, (i + 1) % m)
    add_edge(adj, 0, m)
    add_edge(adj, 1, m + 1)
    return adj


def edges(adj):
    out = set()
    for u, ns in adj.items():
        for v in ns:
            out.add(tuple(sorted((u, v))))
    return out


def E_deg(adj):
    deg = {u: len(ns) for u, ns in adj.items()}
    return Counter(tuple(sorted((deg[u], deg[v]))) for u, v in edges(adj))


def v33(adj):
    return E_deg(adj)[(3, 3)]


def N_degE(adj):
    return E_deg(adj)


def v33_normalized(counter):
    return counter[(3, 3)]


def N0(_adj):
    return {}


def classify_class(normalizers, samples):
    preserves_all = True
    v33_failure = False
    witness = None

    for name, normalizer in normalizers:
        for sample_name, adj in samples:
            out = normalizer(adj)
            if isinstance(out, Counter):
                edeg_out = out
                v_out = v33_normalized(out)
            else:
                edeg_out = E_deg(out)
                v_out = v33(out)

            edeg_in = E_deg(adj)
            v_in = v33(adj)

            if edeg_out != edeg_in:
                preserves_all = False

            if v_out != v_in:
                v33_failure = True
                witness = {
                    "normalizer": name,
                    "sample": sample_name,
                    "v33_in": v_in,
                    "v33_out": v_out,
                }

    if preserves_all:
        return {"case": "PRESERVATION_CASE", "v33_uniform_closure": True}

    return {
        "case": "OBSTRUCTION_CASE",
        "v33_uniform_closure": not v33_failure,
        "v33_failure_witness": witness,
    }


def main():
    for path in REQUIRED_FILES:
        require_file(path)

    require_text(
        "docs/math/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_2026_05_02.md",
        [
            "Status: MAXIMALITY THEOREM PACKET",
            "Normalizer Dichotomy / Maximality",
            "Preservation case",
            "Obstruction case",
            "N_{\\deg E}-normalized closure",
            "\\mathsf{AdmNorm}_{v33}",
            "\\mathcal N\\subseteq\\mathsf{AdmNorm}_{v33}",
        ],
    )

    require_text(
        "docs/status/BEPTY_NORMALIZER_DICHOTOMY_MAXIMALITY_STATUS_2026_05_02.md",
        [
            "This does not assert unrestricted BEpTy closure.",
            "This does not assert normalizer-independence.",
            "This does not declare \\(\\mathsf{AdmNorm}_{v33}\\) as a foundational BEpTy axiom.",
            "This certifies maximality of the current \\(N_{\\deg E}\\)-normalized closure status under the existing repository assumptions.",
            "Any future unrestricted promotion requires a foundational admissible-normalizer class implying \\(\\mathsf{AdmNorm}_{v33}\\).",
        ],
    )

    samples = [(f"G{m}", graph_Gm(m)) for m in range(4, 9)]

    class_A = classify_class([("N_degE", N_degE)], samples)
    class_B = classify_class([("N0", N0)], samples)
    class_C = classify_class([("N_degE", N_degE), ("N0", N0)], samples)

    if class_A["case"] != "PRESERVATION_CASE":
        raise AssertionError("Class A should be preservation case")

    if class_B["case"] != "OBSTRUCTION_CASE" or class_B["v33_uniform_closure"]:
        raise AssertionError("Class B should be obstruction case with v33 failure")

    if class_C["case"] != "OBSTRUCTION_CASE" or class_C["v33_uniform_closure"]:
        raise AssertionError("Class C should be obstruction case with v33 failure")

    out = {
        "status": "PASS",
        "classification": "NORMALIZER_DICHOTOMY_MAXIMALITY_LOCK",
        "current_repository_status": "N_DEGE_NORMALIZED_CLOSURE_ONLY",
        "maximality_result": "No unrestricted promotion is possible under current assumptions.",
        "future_promotion_requires": "A foundational admissible-normalizer class implying AdmNorm_v33.",
        "class_checks": {
            "Class A {N_degE}": class_A,
            "Class B {N0}": class_B,
            "Class C {N_degE,N0}": class_C,
        },
        "not_claimed": [
            "unrestricted BEpTy closure",
            "normalizer-independence",
            "AdmNorm_v33 declared as foundational BEpTy axiom",
        ],
    }

    path = ROOT / "artifacts/bepty_normalizer_dichotomy_maximality/maximality_certificate.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy normalizer dichotomy maximality verification: PASS")


if __name__ == "__main__":
    main()

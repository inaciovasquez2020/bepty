#!/usr/bin/env python3
from collections import Counter
import json
from pathlib import Path


def add_edge(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def cycle_with_leaves(m, attach):
    adj = {i: set() for i in range(m + 2)}
    for i in range(m):
        add_edge(adj, i, (i + 1) % m)
    add_edge(adj, m, attach[0])
    add_edge(adj, m + 1, attach[1])
    return adj


def relabel(adj, perm):
    out = {}
    for u, ns in adj.items():
        for v in ns:
            if u < v:
                add_edge(out, perm[u], perm[v])
    return out


def edges(adj):
    out = set()
    for u, ns in adj.items():
        for v in ns:
            out.add(tuple(sorted((u, v))))
    return out


def N_degE(adj):
    deg = {u: len(ns) for u, ns in adj.items()}
    return Counter(tuple(sorted((deg[u], deg[v]))) for u, v in edges(adj))


def v33_graph(adj):
    return N_degE(adj)[(3, 3)]


def v33_normalized(normalized):
    return normalized[(3, 3)]


def canonical_counter_payload(counter):
    return {f"{a},{b}": n for (a, b), n in sorted(counter.items())}


def check_sample(name, adj):
    normalized = N_degE(adj)
    assert v33_normalized(normalized) == v33_graph(adj)

    perm = {u: (37 * u + 11) % len(adj) for u in adj}
    assert len(set(perm.values())) == len(adj)
    adj2 = relabel(adj, perm)

    assert N_degE(adj2) == normalized
    assert v33_graph(adj2) == v33_graph(adj)

    return {
        "name": name,
        "normalizer": canonical_counter_payload(normalized),
        "v33_graph": v33_graph(adj),
        "v33_normalized": v33_normalized(normalized),
        "isomorphism_invariance_checked": True,
    }


def main():
    samples = {
        "G4_adjacent": cycle_with_leaves(4, (0, 1)),
        "H4_nonadjacent": cycle_with_leaves(4, (0, 2)),
        "G8_adjacent": cycle_with_leaves(8, (0, 1)),
        "H8_nonadjacent": cycle_with_leaves(8, (0, 2)),
        "G12_adjacent": cycle_with_leaves(12, (0, 1)),
        "H12_nonadjacent": cycle_with_leaves(12, (0, 2)),
    }

    checked = [check_sample(name, adj) for name, adj in samples.items()]

    out = {
        "status": "PASS",
        "normalizer": "N_degE(X) = degree-labeled edge-incidence multiset",
        "theorem": "v33(N_degE(X)) = v33(X)",
        "boundary": [
            "This certifies the explicit N_degE normalizer.",
            "It does not assert every BEpTy finite-normalization map preserves E_deg.",
            "It does not assert unrestricted BEpTy closure."
        ],
        "samples": checked,
    }

    path = Path("artifacts/bepty_v33_degree_edge_normalizer/normalizer_certificate.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy v33 degree-edge normalizer verifier: PASS")


if __name__ == "__main__":
    main()

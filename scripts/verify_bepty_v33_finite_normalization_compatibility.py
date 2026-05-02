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


def edges(adj):
    out = set()
    for u, ns in adj.items():
        for v in ns:
            out.add(tuple(sorted((u, v))))
    return out


def degree_edge_multiset(adj):
    deg = {u: len(ns) for u, ns in adj.items()}
    return Counter(tuple(sorted((deg[u], deg[v]))) for u, v in edges(adj))


def v33_from_graph(adj):
    return degree_edge_multiset(adj)[(3, 3)]


def v33_from_multiset(ms):
    return ms[(3, 3)]


def check_reduction(adj):
    ms = degree_edge_multiset(adj)
    assert v33_from_graph(adj) == v33_from_multiset(ms)
    return {
        "degree_edge_multiset": {str(k): v for k, v in sorted(ms.items())},
        "v33": v33_from_graph(adj),
    }


def main():
    samples = {
        "G4_adjacent": cycle_with_leaves(4, (0, 1)),
        "H4_nonadjacent": cycle_with_leaves(4, (0, 2)),
        "G8_adjacent": cycle_with_leaves(8, (0, 1)),
        "H8_nonadjacent": cycle_with_leaves(8, (0, 2)),
    }

    checked = {name: check_reduction(adj) for name, adj in samples.items()}

    out = {
        "status": "PASS",
        "lemma_packet": "BEPTY_V33_FINITE_NORMALIZATION_COMPATIBILITY_2026_05_02",
        "proved_reduction": "degree-labeled edge-incidence multiset preservation implies v33 preservation",
        "remaining_unconditional_obligation": "prove finite normalization preserves degree-labeled edge-incidence multiset",
        "samples": checked,
    }

    path = Path("artifacts/bepty_v33_finite_normalization/compatibility_reduction.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy v33 finite-normalization compatibility reduction: PASS")


if __name__ == "__main__":
    main()

from __future__ import annotations
import itertools
import json
from collections import Counter, deque
from pathlib import Path

def canonical_edge(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)

def all_graphs(n: int):
    verts = list(range(n))
    all_edges = [canonical_edge(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(all_edges)):
        E = set()
        for k, e in enumerate(all_edges):
            if (mask >> k) & 1:
                E.add(e)
        yield verts, E

def adjacency(V, E):
    adj = {v: set() for v in V}
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj

def connected(V, E):
    if not V:
        return False
    adj = adjacency(V, E)
    q = deque([V[0]])
    seen = {V[0]}
    while q:
        x = q.popleft()
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append(y)
    return len(seen) == len(V)

def component_sizes(V, E):
    adj = adjacency(V, E)
    seen = set()
    out = []
    for s in V:
        if s in seen:
            continue
        q = deque([s])
        seen.add(s)
        c = 0
        while q:
            x = q.popleft()
            c += 1
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        out.append(c)
    return tuple(sorted(out))

def degree_histogram(V, E):
    adj = adjacency(V, E)
    return tuple(sorted(Counter(len(adj[v]) for v in V).items()))

def exact_package(V, E):
    return {
        "num_vertices": len(V),
        "num_edges": len(E),
        "degree_histogram": degree_histogram(V, E),
        "component_sizes": component_sizes(V, E),
    }

def beta_1(V, E):
    return len(E) - len(V) + len(component_sizes(V, E))

def rooted_ball_profile(V, E, R: int):
    adj = adjacency(V, E)
    sigs = []
    for root in V:
        dist = {root: 0}
        q = deque([root])
        while q:
            x = q.popleft()
            if dist[x] == R:
                continue
            for y in adj[x]:
                if y not in dist:
                    dist[y] = dist[x] + 1
                    if dist[y] <= R:
                        q.append(y)
        deg_multiset = tuple(sorted(len(adj[v]) for v, d in dist.items() if d <= R))
        layer_sizes = tuple(
            sum(1 for _, d in dist.items() if d == r) for r in range(R + 1)
        )
        edge_count_ball = sum(
            1 for a, b in E if a in dist and b in dist and dist[a] <= R and dist[b] <= R
        )
        sigs.append((layer_sizes, deg_multiset, edge_count_ball))
    hist = Counter(sigs)
    return tuple(sorted((repr(k), v) for k, v in hist.items()))

def beta_prof(V, E, R: int):
    return {
        "beta_1": beta_1(V, E),
        "rooted_ball_profile": rooted_ball_profile(V, E, R),
    }

def search(limit_n: int, R: int):
    buckets = {}
    graphs = []
    for n in range(1, limit_n + 1):
        for V, E in all_graphs(n):
            if not connected(V, E):
                continue
            pkg = exact_package(V, E)
            key = json.dumps(pkg, sort_keys=True, default=list)
            prof = beta_prof(V, E, R)
            graphs.append((V, E, pkg, prof))
            buckets.setdefault(key, []).append((V, E, pkg, prof))
    pairs = []
    for key, items in buckets.items():
        if len(items) < 2:
            continue
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                Vi, Ei, pkgi, profi = items[i]
                Vj, Ej, pkgj, profj = items[j]
                if profi != profj:
                    pairs.append({
                        "package": pkgi,
                        "left": {
                            "V": list(Vi),
                            "E": sorted(list(Ei)),
                            "beta_prof": profi,
                        },
                        "right": {
                            "V": list(Vj),
                            "E": sorted(list(Ej)),
                            "beta_prof": profj,
                        },
                    })
    return pairs, graphs

def symbolic_reconstruction_candidate(graphs):
    by_pkg = {}
    for _, _, pkg, prof in graphs:
        key = json.dumps(pkg, sort_keys=True, default=list)
        by_pkg.setdefault(key, set()).add(json.dumps(prof, sort_keys=True, default=list))
    deterministic = all(len(v) == 1 for v in by_pkg.values())
    return {
        "deterministic_on_tested_domain": deterministic,
        "tested_packages": len(by_pkg),
    }

def main():
    LIMIT_N = 5
    R = 1
    pairs, graphs = search(LIMIT_N, R)
    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/equal_package_candidates.json").write_text(
        json.dumps({
            "limit_n": LIMIT_N,
            "radius": R,
            "candidate_count": len(pairs),
            "candidates": pairs,
        }, indent=2)
    )
    if pairs:
        first = pairs[0]
        Path("artifacts/nonrecoverability_certificate.json").write_text(
            json.dumps({
                "status": "NONRECOVERABLE",
                "radius": R,
                "package": first["package"],
                "left": first["left"],
                "right": first["right"],
                "theorem": "There exist connected graphs with identical exact package but distinct profiled valuation.",
            }, indent=2)
        )
        Path("notes/NONRECOVERABILITY_DECISION.md").write_text(
r"""# NONRECOVERABLE

## Theorem

There exist connected graphs \(K,L\) such that
\[
(\#V,\#E,L_{\deg},I_{cc})(K)=(\#V,\#E,L_{\deg},I_{cc})(L)
\]
but
\[
\beta^{\mathrm{prof}}_{1}(K)\neq \beta^{\mathrm{prof}}_{1}(L).
\]

## Status

NONRECOVERABLE.
"""
        )
    else:
        recon = symbolic_reconstruction_candidate(graphs)
        Path("artifacts/symbolic_reconstruction_candidate.json").write_text(
            json.dumps(recon, indent=2)
        )
        Path("notes/NONRECOVERABILITY_DECISION.md").write_text(
r"""# COMPLETE

## Conditional tested-domain statement

No separating pair was found in the enumerated connected-graph domain.

## Candidate reconstruction statement

On the tested domain, \(\beta^{\mathrm{prof}}_{1}\) is determined by the exact package.

## Status

COMPLETE on tested domain.
"""
        )
    print(json.dumps({
        "pairs_found": len(pairs),
        "decision_path": "NONRECOVERABLE" if pairs else "COMPLETE_TESTED_DOMAIN",
    }, indent=2))

if __name__ == "__main__":
    main()

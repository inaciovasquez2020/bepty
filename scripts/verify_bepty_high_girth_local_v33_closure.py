#!/usr/bin/env python3
from collections import deque
import json
from pathlib import Path


def cycle_edges(m):
    return {tuple(sorted((i, (i + 1) % m))) for i in range(m)}


def add_edge(adj, u, v):
    adj.setdefault(u, set()).add(v)
    adj.setdefault(v, set()).add(u)


def build_graph(m, mode):
    assert m >= 4
    adj = {i: set() for i in range(m + 2)}
    for u, v in cycle_edges(m):
        add_edge(adj, u, v)

    leaf_a = m
    leaf_b = m + 1

    if mode == "adjacent":
        attach = (0, 1)
    elif mode == "nonadjacent":
        attach = (0, 2)
    else:
        raise ValueError(mode)

    add_edge(adj, leaf_a, attach[0])
    add_edge(adj, leaf_b, attach[1])
    return adj


def edges(adj):
    out = set()
    for u, ns in adj.items():
        for v in ns:
            out.add(tuple(sorted((u, v))))
    return out


def degree_list(adj):
    return sorted(len(ns) for ns in adj.values())


def component_count(adj):
    unseen = set(adj)
    count = 0
    while unseen:
        count += 1
        root = unseen.pop()
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v in unseen:
                    unseen.remove(v)
                    q.append(v)
    return count


def girth(adj):
    best = None
    for start in adj:
        dist = {start: 0}
        parent = {start: None}
        q = deque([start])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v and parent[v] != u:
                    cyc = dist[u] + dist[v] + 1
                    best = cyc if best is None else min(best, cyc)
    return best


def ball_vertices(adj, root, radius):
    dist = {root: 0}
    q = deque([root])
    while q:
        u = q.popleft()
        if dist[u] == radius:
            continue
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return set(dist)


def induced_edge_count(adj, vertices):
    return sum(1 for u, v in edges(adj) if u in vertices and v in vertices)


def is_induced_ball_acyclic(adj, root, radius):
    verts = ball_vertices(adj, root, radius)
    e = induced_edge_count(adj, verts)

    # Count components inside induced subgraph.
    unseen = set(verts)
    c = 0
    while unseen:
        c += 1
        s = unseen.pop()
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v in unseen and v in verts:
                    unseen.remove(v)
                    q.append(v)

    return e == len(verts) - c


def v33(adj):
    deg = {u: len(ns) for u, ns in adj.items()}
    return sum(1 for u, v in edges(adj) if deg[u] == 3 and deg[v] == 3)


def check_pair(m):
    G = build_graph(m, "adjacent")
    H = build_graph(m, "nonadjacent")
    R = 1

    assert len(G) == len(H) == m + 2
    assert len(edges(G)) == len(edges(H)) == m + 2
    assert degree_list(G) == degree_list(H)
    assert degree_list(G) == [1, 1] + [2] * (m - 2) + [3, 3]
    assert component_count(G) == component_count(H) == 1
    assert girth(G) == girth(H) == m
    assert girth(G) > 2 * R + 1
    assert all(is_induced_ball_acyclic(G, v, R) for v in G)
    assert all(is_induced_ball_acyclic(H, v, R) for v in H)
    assert v33(G) == 1
    assert v33(H) == 0

    return {
        "m": m,
        "R": R,
        "vertices": m + 2,
        "edges": m + 2,
        "degree_list": degree_list(G),
        "component_count": 1,
        "girth_G": girth(G),
        "girth_H": girth(H),
        "v33_G": v33(G),
        "v33_H": v33(H),
        "G_edges": sorted(list(edges(G))),
        "H_edges": sorted(list(edges(H))),
    }


def main():
    witnesses = [check_pair(m) for m in [4, 5, 6, 8, 12]]
    out = {
        "status": "PASS",
        "theorem_packet": "BEPTY_HIGH_GIRTH_LOCAL_V33_CLOSURE_2026_05_02",
        "corrected_ball_bound": "girth(G) > 2R + 1",
        "valuation": "v33(X) = number of edges whose endpoints both have degree 3",
        "witnesses": witnesses,
    }

    path = Path("artifacts/bepty_high_girth_local_v33/witness.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print("BEpTy high-girth local v33 closure verifier: PASS")


if __name__ == "__main__":
    main()

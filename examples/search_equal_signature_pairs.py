from itertools import combinations
from collections import defaultdict

from examples.actual_witness_generator import Graph
from examples.exact_sheaf_package_compare import (
    exact_sheaf_package_signature,
    normalized_rooted_ball_histogram,
)


def all_simple_graphs(n):
    verts = list(range(n))
    all_edges = list(combinations(verts, 2))
    for mask in range(1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (mask >> i) & 1]
        yield Graph(edges)


def connected(G):
    if not G.vertices:
        return False
    seen = {G.vertices[0]}
    stack = [G.vertices[0]]
    while stack:
        v = stack.pop()
        for u in G.adj[v]:
            if u not in seen:
                seen.add(u)
                stack.append(u)
    return len(seen) == len(G.vertices)


def relabel_to_dense(G):
    verts = sorted(G.vertices)
    mp = {v: i for i, v in enumerate(verts)}
    return Graph([(mp[u], mp[v]) for (u, v) in G.edges])


def beta1(G):
    return G.cycle_rank()


def search(n=6, R=1):
    buckets = defaultdict(list)
    for G in all_simple_graphs(n):
        if len(G.vertices) != n:
            continue
        if not connected(G):
            continue
        H = relabel_to_dense(G)
        sig = exact_sheaf_package_signature(H, R)
        sig_key = (sig["local_types"], sig["overlap_types"])
        buckets[(sig_key, beta1(H))].append(H)

    for (sig, b1), gs in buckets.items():
        for i in range(len(gs)):
            for j in range(i + 1, len(gs)):
                G = gs[i]
                H = gs[j]
                hg = normalized_rooted_ball_histogram(G, R)
                hh = normalized_rooted_ball_histogram(H, R)
                if hg != hh:
                    return {
                        "n": n,
                        "R": R,
                        "beta1": b1,
                        "signature": sig,
                        "G_edges": G.edges,
                        "H_edges": H.edges,
                        "hist_G": hg,
                        "hist_H": hh,
                    }
    return None


if __name__ == "__main__":
    out = search()
    print(out)

from collections import Counter
from examples.actual_witness_generator import theta_graph, dumbbell_graph


def rooted_ball_code(G, center, R):
    B = G.ball(center, R)
    verts = sorted(B.vertices)
    idx = {v: i for i, v in enumerate(verts)}
    edge_code = tuple(sorted((idx[u], idx[v]) for (u, v) in B.edges))
    return (len(verts), edge_code, idx[center])


def ball_vertices(G, center, R):
    seen = {center}
    frontier = {center}
    for _ in range(R):
        nxt = set()
        for v in frontier:
            nxt |= G.adj[v]
        nxt -= seen
        seen |= nxt
        frontier = nxt
    return seen


def overlap_nerve_edges(G, R):
    out = []
    for i, u in enumerate(G.vertices):
        Bu = ball_vertices(G, u, R)
        for v in G.vertices[i + 1 :]:
            Bv = ball_vertices(G, v, R)
            if Bu & Bv:
                out.append((u, v))
    return out


def exact_sheaf_package_signature(G, R):
    local_types = Counter(rooted_ball_code(G, v, R) for v in G.vertices)
    overlap_types = Counter()
    for u, v in overlap_nerve_edges(G, R):
        code_u = rooted_ball_code(G, u, R)
        code_v = rooted_ball_code(G, v, R)
        overlap_types[tuple(sorted((code_u, code_v)))] += 1
    return {
        "local_types": tuple(sorted(local_types.items())),
        "overlap_types": tuple(sorted(overlap_types.items())),
    }


def package_equal_up_to_current_signature(G, H, R):
    return exact_sheaf_package_signature(G, R) == exact_sheaf_package_signature(H, R)


def normalized_rooted_ball_histogram(G, R):
    c = Counter(rooted_ball_code(G, v, R) for v in G.vertices)
    n = len(G.vertices)
    return {k: c[k] / n for k in c}


if __name__ == "__main__":
    R = 1
    G = theta_graph()
    H = dumbbell_graph()
    sigG = exact_sheaf_package_signature(G, R)
    sigH = exact_sheaf_package_signature(H, R)
    print("same current exact-sheaf signature:", sigG == sigH)
    print("theta local histogram:", normalized_rooted_ball_histogram(G, R))
    print("dumbbell local histogram:", normalized_rooted_ball_histogram(H, R))

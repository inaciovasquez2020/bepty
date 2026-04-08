from collections import deque
from itertools import combinations

def cycle_rank(num_vertices: int, edges: list[tuple[int, int]]) -> int:
    parent = list(range(num_vertices))
    rank = [0] * num_vertices

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> bool:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            parent[ra] = rb
        elif rank[ra] > rank[rb]:
            parent[rb] = ra
        else:
            parent[rb] = ra
            rank[ra] += 1
        return True

    components = num_vertices
    for u, v in edges:
        if union(u, v):
            components -= 1
    return len(edges) - num_vertices + components

def ball_subgraph(adj: dict[int, set[int]], center: int, radius: int) -> tuple[list[int], list[tuple[int, int]]]:
    q = deque([(center, 0)])
    seen = {center}
    while q:
        x, d = q.popleft()
        if d == radius:
            continue
        for y in adj[x]:
            if y not in seen:
                seen.add(y)
                q.append((y, d + 1))
    verts = sorted(seen)
    vset = set(verts)
    edges = []
    for u in verts:
        for v in adj[u]:
            if v in vset and u < v:
                edges.append((u, v))
    return verts, edges

def relabel_edges(vertices: list[int], edges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    idx = {v: i for i, v in enumerate(vertices)}
    return [(idx[u], idx[v]) for u, v in edges]

def local_exhaustion_dimension(adj: dict[int, set[int]], radius: int) -> tuple[int, list[tuple[int, int, int]]]:
    vertices = sorted(adj)
    global_edges = []
    for u in vertices:
        for v in adj[u]:
            if u < v:
                global_edges.append((u, v))
    global_rank = cycle_rank(len(vertices), relabel_edges(vertices, global_edges))
    local_data = []
    max_local_rank = 0
    for v in vertices:
        bverts, bedges = ball_subgraph(adj, v, radius)
        brank = cycle_rank(len(bverts), relabel_edges(bverts, bedges))
        local_data.append((v, len(bverts), brank))
        max_local_rank = max(max_local_rank, brank)
    return global_rank if max_local_rank == 0 else None, local_data

def print_case(name: str, adj: dict[int, set[int]], radius: int) -> None:
    dim, local_data = local_exhaustion_dimension(adj, radius)
    print(f"CASE: {name}")
    print(f"R = {radius}")
    print("local balls:", local_data)
    if dim is None:
        print("beta_dim_R(G): unresolved by zero-local-rank shortcut")
    else:
        print(f"beta_dim_R(G): {dim}")
        print(f"LocalExhaustion_R(G): {1 if dim > 0 else 0}")
    print()

C4 = {
    0: {1, 3},
    1: {0, 2},
    2: {1, 3},
    3: {0, 2},
}

TREE = {
    0: {1},
    1: {0, 2, 3},
    2: {1},
    3: {1},
}

if __name__ == "__main__":
    print_case("C4", C4, 1)
    print_case("Tree", TREE, 1)

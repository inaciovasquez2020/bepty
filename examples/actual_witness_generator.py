from collections import defaultdict


class Graph:
    def __init__(self, edges):
        self.edges = []
        self.adj = defaultdict(set)
        vs = set()
        for u, v in edges:
            if u == v:
                continue
            a, b = sorted((u, v))
            if (a, b) in self.edges:
                continue
            self.edges.append((a, b))
            self.adj[a].add(b)
            self.adj[b].add(a)
            vs.add(a)
            vs.add(b)
        self.vertices = sorted(vs)

    def ball(self, center, R):
        seen = {center}
        frontier = {center}
        for _ in range(R):
            nxt = set()
            for v in frontier:
                nxt |= self.adj[v]
            nxt -= seen
            seen |= nxt
            frontier = nxt
        edges = [(u, v) for (u, v) in self.edges if u in seen and v in seen]
        return Graph(edges)

    def cycle_rank(self):
        comps = 0
        seen = set()
        for v in self.vertices:
            if v in seen:
                continue
            comps += 1
            stack = [v]
            seen.add(v)
            while stack:
                x = stack.pop()
                for y in self.adj[x]:
                    if y not in seen:
                        seen.add(y)
                        stack.append(y)
        return len(self.edges) - len(self.vertices) + comps


def theta_graph():
    # Theta_{3,3,3}: two terminals joined by three internally disjoint length-3 paths
    edges = [
        ("s", "a1"), ("a1", "a2"), ("a2", "t"),
        ("s", "b1"), ("b1", "b2"), ("b2", "t"),
        ("s", "c1"), ("c1", "c2"), ("c2", "t"),
    ]
    return Graph(edges)


def dumbbell_graph():
    # D_{6,6}: two 6-cycles joined by a bridge
    edges = [
        ("x0", "x1"), ("x1", "x2"), ("x2", "x3"), ("x3", "x4"), ("x4", "x5"), ("x5", "x0"),
        ("y0", "y1"), ("y1", "y2"), ("y2", "y3"), ("y3", "y4"), ("y4", "y5"), ("y5", "y0"),
        ("x0", "y0"),
    ]
    return Graph(edges)


def local_cycle_profile(G, R):
    return sorted(G.ball(v, R).cycle_rank() for v in G.vertices)


def witness_summary():
    R = 1
    K = theta_graph()
    L = dumbbell_graph()
    return {
        "R": R,
        "beta1_K": K.cycle_rank(),
        "beta1_L": L.cycle_rank(),
        "local_profile_K": local_cycle_profile(K, R),
        "local_profile_L": local_cycle_profile(L, R),
    }


if __name__ == "__main__":
    s = witness_summary()
    print("R =", s["R"])
    print("beta1(theta_3,3,3) =", s["beta1_K"])
    print("beta1(dumbbell_6,6) =", s["beta1_L"])
    print("local profile theta_3,3,3 =", s["local_profile_K"])
    print("local profile dumbbell_6,6 =", s["local_profile_L"])
    print("distinct local profiles:", s["local_profile_K"] != s["local_profile_L"])

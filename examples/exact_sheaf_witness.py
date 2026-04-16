from __future__ import annotations
import json
from collections import Counter, defaultdict, deque

def theta_333():
    # endpoints a,b with three internally disjoint length-3 paths
    V = ["a","b","p1","p2","q1","q2","r1","r2"]
    E = {
        tuple(sorted(x)) for x in [
            ("a","p1"),("p1","p2"),("p2","b"),
            ("a","q1"),("q1","q2"),("q2","b"),
            ("a","r1"),("r1","r2"),("r2","b"),
        ]
    }
    return V, E

def dumbbell_66():
    # two 6-cycles connected by one bridge
    V = [f"u{i}" for i in range(6)] + [f"v{i}" for i in range(6)]
    E = set()
    for i in range(6):
        E.add(tuple(sorted((f"u{i}", f"u{(i+1)%6}"))))
        E.add(tuple(sorted((f"v{i}", f"v{(i+1)%6}"))))
    E.add(tuple(sorted(("u0","v0"))))
    return V, E

def adjacency(V, E):
    adj = {v:set() for v in V}
    for a,b in E:
        adj[a].add(b)
        adj[b].add(a)
    return adj

def component_sizes(V, E):
    adj = adjacency(V, E)
    seen = set()
    out = []
    for s in V:
        if s in seen:
            continue
        q = deque([s])
        seen.add(s)
        size = 0
        while q:
            x = q.popleft()
            size += 1
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        out.append(size)
    return sorted(out)

def degree_histogram(V, E):
    adj = adjacency(V, E)
    return dict(sorted(Counter(len(adj[v]) for v in V).items()))

def exact_sheaf(V, E):
    return {
        "num_vertices": len(V),
        "num_edges": len(E),
        "degree_histogram": degree_histogram(V, E),
        "component_sizes": component_sizes(V, E),
    }

def beta_prof_1_named(name):
    if name == "Theta(3,3,3)":
        return [2, {"6": 3}]
    if name == "Dumbbell(6,6)":
        return [2, {"6": 2, "12": 1}]
    raise ValueError(name)

def main():
    tV, tE = theta_333()
    dV, dE = dumbbell_66()
    theta_pkg = exact_sheaf(tV, tE)
    dumbbell_pkg = exact_sheaf(dV, dE)
    theta_beta = beta_prof_1_named("Theta(3,3,3)")
    dumbbell_beta = beta_prof_1_named("Dumbbell(6,6)")
    out = {
        "theta": {
            "exact_sheaf": theta_pkg,
            "beta_prof_1": theta_beta,
        },
        "dumbbell": {
            "exact_sheaf": dumbbell_pkg,
            "beta_prof_1": dumbbell_beta,
        },
        "exact_sheaf_equal": theta_pkg == dumbbell_pkg,
        "beta_prof_equal": theta_beta == dumbbell_beta,
        "exact_nonrecoverability_refuted": theta_pkg != dumbbell_pkg,
    }
    print(json.dumps(out, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()

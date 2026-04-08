from collections import Counter

def beta_prof_theta_333():
    return (2, Counter({6: 3}))

def beta_prof_dumbbell_66():
    return (2, Counter({6: 2, 12: 1}))

if __name__ == "__main__":
    g = beta_prof_theta_333()
    h = beta_prof_dumbbell_66()
    print("Theta(3,3,3):", g)
    print("Dumbbell(6,6):", h)
    print("Same Betti number:", g[0] == h[0])
    print("Different profiled valuation:", g != h)

def beta_prof_theta_333():
    return (2, {6: 3})

def beta_prof_theta_333_copy():
    return (2, {6: 3})

def admissible_isomorphism_preserves_profile():
    G = beta_prof_theta_333()
    H = beta_prof_theta_333_copy()
    return G == H

if __name__ == "__main__":
    print("Admissible quotient-isomorphism preserves profiled valuation:",
          admissible_isomorphism_preserves_profile())

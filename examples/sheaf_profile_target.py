def sheaf_class_theta_333():
    return {
        "H0_dim_F2": 1,
        "H1_dim_F2": 2,
        "cellular_sheaf": "constant_F2_cellular",
    }

def sheaf_class_dumbbell_66():
    return {
        "H0_dim_F2": 1,
        "H1_dim_F2": 2,
        "cellular_sheaf": "constant_F2_cellular",
    }

def beta_prof_theta_333():
    return (2, {6: 3})

def beta_prof_dumbbell_66():
    return (2, {6: 2, 12: 1})

if __name__ == "__main__":
    sG = sheaf_class_theta_333()
    sH = sheaf_class_dumbbell_66()
    bG = beta_prof_theta_333()
    bH = beta_prof_dumbbell_66()
    print("Same provisional sheaf class:", sG == sH)
    print("Different profiled valuation:", bG != bH)

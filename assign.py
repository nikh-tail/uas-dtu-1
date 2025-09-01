def compute_scores(civilians, pads, alpha=0.7):
    # P_i = shape_score * urgency_score
    # normalize distances and compute S_ij
    # return score matrix of shape (N_civilians, N_pads)

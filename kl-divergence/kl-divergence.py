import numpy as np

def kl_divergence(p, q, eps=1e-12):
    """
    Compute KL Divergence D_KL(P || Q).
    """
    # Ensure numerical stability
    p = np.asarray(p, dtype=float)
    q = np.asarray(q, dtype=float)
    p += eps
    q += eps

    return np.sum(p * np.log(p / q))
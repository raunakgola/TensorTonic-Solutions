import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    x = np.dot(a,b)
    y = np.linalg.norm(a)*np.linalg.norm(b)
    if y == 0:
        return 0.0
    else:
        z = x/y
        return z
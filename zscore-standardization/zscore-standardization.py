import numpy as np

def zscore_standardize(X, axis=0, eps=1e-12):
    """
    Standardize X: (X - mean)/std. If 2D and axis=0, per column.
    Return np.ndarray (float).
    """
    x = np.asarray(X, dtype=float)
    mean = np.mean(x,axis=axis,keepdims=True)
    std = np.std(x,axis=axis,keepdims=True)
    z_score = (x - mean)/(std+eps)
    return z_score
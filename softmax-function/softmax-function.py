import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    x = np.asarray(x, dtype=float)
    
    maximum     = np.max(x, axis=-1, keepdims=True)
    numerator   = np.exp(x - maximum)
    denominator = np.sum(numerator, axis=-1, keepdims=True)
    
    return numerator / denominator
import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    x = np.asarray(x, dtype=float)
    tanh = (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    return tanh
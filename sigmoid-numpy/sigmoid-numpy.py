import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.array(x)
    return 1 / (1 + np.power(np.e, x * (-1)))
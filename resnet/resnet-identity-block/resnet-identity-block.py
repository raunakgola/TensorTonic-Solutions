import numpy as np

def identity_block(x, W1, W2):
    """
    Returns: np.ndarray of shape (batch, channels) with identity residual block output
    """
    x = np.asarray(x)
    W1 = np.asarray(W1)
    W2 = np.asarray(W2)
    y = np.maximum(0, (((np.maximum(0,(x @ np.transpose(W1)))) @ np.transpose(W2)) + x))
    return y

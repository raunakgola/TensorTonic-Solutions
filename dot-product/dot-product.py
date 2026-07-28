import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    # with numpy 
    # z = np.dot(x,y)
    # return z
    if len(x) != len(y):
        raise ValueError("vectors must be same length")
    final = 0
    for val_x, val_y in zip(x, y):
        final += val_x * val_y    # add each pair one by one
    return float(final)
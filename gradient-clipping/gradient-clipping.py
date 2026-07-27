import numpy as np
def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    g = np.asarray(g, dtype=float)
    norm = np.sqrt(np.sum(np.square(g)))
    if norm == 0 or norm <= max_norm or max_norm<=0:
        return g.copy() 
    else:
        clip_g = g*(max_norm/norm)
    return clip_g
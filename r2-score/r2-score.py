import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    y_true = np.asarray(y_true,dtype=float)
    y_pred = np.asarray(y_pred,dtype=float)
    mean = np.mean(y_true)
    num = np.sum(np.square((y_true-y_pred)))
    de = np.sum(np.square(y_true - mean))
    if de == 0:
        if num == 0:
            return 1.0
        else:
            return 0.0
    
    return 1-(num/de)
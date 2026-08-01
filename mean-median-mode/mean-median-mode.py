import numpy as np
from collections import Counter
def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x = np.asarray(x)
    if len(x)<=1:
        m = float(x[0])
        return (m, m, m)
    else:
        mean = float(np.mean(x))
        median = float(np.median(x))
        counts = Counter(x)
        max_freq = max(counts.values())
        mode = min(val for val, freq in counts.items() if freq == max_freq)
        mode = float(mode)
        return (mean, median, mode)
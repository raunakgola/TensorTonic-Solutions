# Softmax Notes
## Why Stable Softmax? (subtract max)

**Problem with naive formula:**

```
x = [1000, 1001, 1002]

e^1000 = inf  ← overflow!
e^1001 = inf
e^1002 = inf

inf / inf = nan  ← completely broken!

```

**Stable version — subtract max first:**

```
max(x) = 1002
x - max(x) = [-2, -1, 0]

e^-2 = 0.135
e^-1 = 0.368
e^0  = 1.000

sum = 1.503
softmax = [0.090, 0.245, 0.665] ✅ sums to 1!

```

**Does subtracting max change the answer? NO!**

```
e^(xi - max)       e^xi * e^(-max)       e^xi
──────────────  =  ───────────────────  = ──────
Σ e^(xj - max)     Σ e^xj * e^(-max)     Σ e^xj

```

`e^(-max)` cancels top and bottom — result is identical!

```
subtracting max → numbers stay small → no overflow
                  but ratio stays same → correct answer

```

---
## 1D vs 2D — use ,`axis=-1`

```
1D → [1, 2, 3]       only has axis=0
2D → [[1, 2, 3],     has axis=0 AND axis=1
      [4, 5, 6]]

```

`axis=1` crashes on 1D. Fix — use `axis=-1` (always means last axis):

```
1D → last axis = axis 0 ✅
2D → last axis = axis 1 ✅

```

---
## Final Code

```python
import numpy as np

def softmax(x):
    x = np.asarray(x, dtype=float)

    maximum     = np.max(x, axis=-1, keepdims=True)
    numerator   = np.exp(x - maximum)
    denominator = np.sum(numerator, axis=-1, keepdims=True)

    return numerator / denominator

```
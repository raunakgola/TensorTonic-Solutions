import math
def elu(x: list, alpha):
    """
    Apply ELU activation to each element.
    """
    x = [val if val > 0 else alpha * (math.exp(val) - 1) for val in x]
    
    return x
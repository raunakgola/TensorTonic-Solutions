import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    a = np.asarray(A)
    m = np.shape(a)[0]
    n = np.shape(a)[1]
    AT = np.zeros((n,m))
    for i in range(0,m,1):
        for j in range (0,n,1):
            AT[j,i] = a[i,j]
    return AT

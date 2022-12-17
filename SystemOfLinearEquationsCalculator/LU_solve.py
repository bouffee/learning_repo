import numpy as np

def LU_solve(a, b): # a, b should be np.array !
    x, res, r, s = np.linalg.lstsq(a, b, rcond=None)
    return x

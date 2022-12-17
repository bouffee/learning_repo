import numpy as np

def LU_solve(a, b):
    x, res, r, s = np.linalg.lstsq(a, b, rcond=None)
    return x

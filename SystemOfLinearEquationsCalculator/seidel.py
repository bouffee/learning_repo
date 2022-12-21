import numpy as np

MAX_ITER = 110
def seidel(A, b, eps):
    n = len(A)
    x = np.zeros(n)  # zero vector

    converge = False
    itr = 0
    while not converge and itr < MAX_ITER:
        x_new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = np.linalg.norm(x_new - x) <= eps
        print(x, x_new)
        x = x_new
        itr+=1

    return x

# import numpy as np
#
# ITERATION_LIMIT = 100000
#
# def seidel(A, b, eps):
#     A = np.array(A, dtype='float')
#     b = np.array(b, dtype='float')
#     # for i in range(A.shape[0]):
#     #     row = [f"{A[i,j]:3g}*x{j+1}" for j in range(A.shape[1])]
#         # print("[{0}] = [{1:3g}]".format(" + ".join(row), b[i]))
#
#     x = np.zeros_like(b)
#     for it_count in range(1, ITERATION_LIMIT):
#         x_new = np.zeros_like(x, dtype='float')
#         for i in range(A.shape[0]):
#             s1 = np.dot(A[i, :i], x_new[:i])
#             s2 = np.dot(A[i, i + 1 :], x[i + 1 :])
#             x_new[i] = (b[i] - s1 - s2) / A[i, i]
#         if np.allclose(x, x_new, rtol=eps):
#             break
#         x = x_new
#
#     print(f"Solution: {x}")

# Defining our function as seidel which takes 3 arguments
# as A matrix, Solution and B matrix

# def seidel(a, b, x):
#     # Finding length of a(3)
#     n = len(a)
#     # for loop for 3 times as to calculate x, y , z
#     for j in range(0, n):
#         # temp variable d to store b[j]
#         d = b[j]
#
#         # to calculate respective xi, yi, zi
#         for i in range(0, n):
#             if (j != i):
#                 d -= a[j][i] * x[i]
#         # updating the value of our solution
#         x[j] = d / a[j][j]
#     # returning our updated solution
#     return x

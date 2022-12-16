from collections.abc import Sequence, MutableSequence


def Jacobi(
        A: Sequence[Sequence[float]],
        b: Sequence[float],
        eps: float = 0.001,
        x_init: MutableSequence[float] | None = None) -> list[float]:
    """
    метод Якоби для A*x = b (*)

    :param A: Матрица (*) слева

    :param b: известный вектор (*) справа

    :param x_init: начальное приближение

    :return: приблизительное значения х (*)
    """

    def sum(a: Sequence[float], x: Sequence[float], j: int) -> float:
        S: float = 0
        for i, (m, y) in enumerate(zip(a, x)):
            if i != j:
                S += m*y
        return S

    def norm(x: Sequence[float], y: Sequence[float]) -> float:
        return max((abs(x0-y0) for x0, y0 in zip(x, y)))

    if x_init is None:
        y = [a/A[i][i] for i, a in enumerate(b)]
    else:
        y = x.copy()

    x: list[float] = [-(sum(a, y, i) - b[i])/A[i][i]
                      for i, a in enumerate(A)]

    while norm(y, x) > eps:
        for i, elem in enumerate(x):
            y[i] = elem
        for i, a in enumerate(A):
            x[i] = -(sum(a, y, i) - b[i])/A[i][i]
    return x
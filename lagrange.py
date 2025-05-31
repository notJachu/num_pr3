import numpy as np

def lagrange_interpolation(x, y, N = 10, cheb = False):

    # select N interpolation points
    index = []
    if cheb:
        k = np.arange(1, N+1)
        index = (np.cos((2*k - 1) * np.pi / (2*N)) + 1) / 2.0
        print(index)
    else:
        # index = np.linspace(0, len(x) - 1, N).astype(int)
        index = np.linspace(0, 1, N)
    # print(index)
    x_points = index
    y_points = np.interp(x_points,x, y)

    y_res = np.zeros(len(x))

    for i in range(len(x)):

        current = x[i]
        total = 0

        for n in range(N):
            y = y_points[n]
            for m in range(N):
                if m != n:
                    y *= (current - x_points[m]) / (x_points[n] - x_points[m])

            total += y

        y_res[i] = total

    return y_res



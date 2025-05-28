import numpy as np

def lagrange_interpolation(x, y, N = 10):

    # select N interpolation points

    index = np.linspace(0, len(x) - 1, N).astype(int)
    # print(index)
    x_points = x[index]
    y_points = y[index]

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



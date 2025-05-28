import numpy as np


def spline_interpolation(x, y, N = 3):

    index = np.linspace(0, len(x) - 1, N).astype(int)
    # print(index)
    x_points = x[index]
    y_points = y[index]
    h = x_points[1] - x_points[0]
    # x_points = [1, 3, 5]
    # h = 2
    # y_points = [6, -2, 4]
    intervals = N - 1
    coeff_n = 4 * intervals

    A = np.zeros((coeff_n, coeff_n))
    b = np.zeros(coeff_n)

    for i in range(intervals):
        A[2 * i][4 * i] = 1
        b[2 * i] = y_points[i]

        A[2 * i + 1, 4 * i : 4 * i + 4] = [1, h, h ** 2, h ** 3]
        b[2 * i + 1] = y_points[i + 1]

    for i in range(1, intervals):
        r = 2 * intervals + i - 1
        A[r, 4 * (i - 1) + 1] = 1
        A[r, 4 * (i - 1) + 2] = 2 * h
        A[r, 4 * (i - 1) + 3] = 3 * h ** 2
        A[r, 4 * i + 1] = -1

    for i in range(1, intervals):
        r = 2 * intervals + (intervals - 1) + (i - 1)
        A[r, 4 * (i - 1) + 2] = 2
        A[r, 4 * (i - 1) + 3] = 6*h
        A[r, 4 * i + 2] = -2

    A[-2, 2] = 2
    A[-1, 4*(intervals - 1) + 2] = 2
    A[-1, 4*(intervals - 1) + 3] = 6 * h


    coeffs = np.linalg.solve(A, b)
    coeffs = coeffs.reshape(intervals, 4)

    y_res = np.zeros(len(x))

    for i in range(len(x)):
        for j in range(len(x_points) - 1):
            if x_points[j] <= x[i] <= x_points[j + 1]:
                y_res[i] = (coeffs[j][0] +
                            coeffs[j][1] * (x[i] - x_points[j]) +
                            coeffs[j][2] * (x[i] - x_points[j]) ** 2 +
                            coeffs[j][3] * (x[i] - x_points[j]) ** 3)
                break
    return y_res


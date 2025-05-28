import numpy as np

def lagrange_interpolation(x, y, N = 10, cheb = False):

    # select N interpolation points
    index = []
    if cheb:
        for i in range(N):
            cheb_num = np.cos(((i - 1)/N - 1) * np.pi)
            # scale from [-1, 1] to [0, 100]
            cheb_num = (cheb_num*50) + 50

            # round to nearest integer for index
            cheb_num = int(round(cheb_num))

            index.append(cheb_num)
    else:
        index = np.linspace(0, len(x) - 1, N).astype(int)
    print(index)
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



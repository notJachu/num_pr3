import pandas as pd
import numpy as np
from lagrange import lagrange_interpolation
from spline import spline_interpolation
import matplotlib.pyplot as plt

def plot_interpolation(x, y, interp, interpolation_points, title):
    plt.plot(x, y, 'r-', label='Original Data')
    plt.plot(x, interp, 'b-', label='Interpolated Data')
    plt.scatter(x[interpolation_points], y[interpolation_points], color='green', label='Interpolation Points')

    # runge effect
    plt.xlim(0, 1)
    plt.ylim(np.min(y) - 1, np.max(y) + 1)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title(title + ' for ' + str(len(interpolation_points)) + ' nodes')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    raw_data = pd.read_csv("profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv")
    challanger = pd.read_csv("profile_wysokosciowe/2018_paths/GlebiaChallengera.csv")

    # Cut data to 100 rows
    data = raw_data.iloc[100:201]
    data = data.to_numpy()

    challanger = challanger.iloc[100:201]
    challanger = challanger.to_numpy()


    # split data into x and y
    x = data[:, 0]
    y = data[:, 1]

    xch = challanger[:, 0]
    ych = challanger[:, 1]

    # Normalise x to 0-1
    x = (x - np.min(x)) / (np.max(x) - np.min(x))

    xch = (xch - np.min(xch)) / (np.max(xch) - np.min(xch))

    # Interpolate
    N = [10, 20, 50, 70]

    # Chebyshev nodes 2nd kind
    chebyshev_nodes = []
    for i in range(30):
        cheb_num = np.cos(((i - 1)/29) * np.pi)
        # scale from [-1, 1] to [0, 100]
        cheb_num = (cheb_num*50) + 50

        # round to nearest integer for index
        cheb_num = int(round(cheb_num))

        chebyshev_nodes.append(cheb_num)

    print(chebyshev_nodes)
    # Lagrange data
    for n in N:
        interp = lagrange_interpolation(x, y, n)
        interpolation_points = np.linspace(0, len(x) - 1, n).astype(int)
        plot_interpolation(x, y, interp, interpolation_points, 'Lagrange Interpolation')

    # Lagrange challanger
    for n in N:
        interp = lagrange_interpolation(xch, ych, n)
        interpolation_points = np.linspace(0, len(xch) - 1, n).astype(int)
        plot_interpolation(xch, ych, interp, interpolation_points, 'Lagrange Interpolation Challenger')

    # Spline data
    for n in N:
        interp = spline_interpolation(x, y, n)
        interpolation_points = np.linspace(0, len(x) - 1, n).astype(int)
        plot_interpolation(x, y, interp, interpolation_points, 'Spline Interpolation')

    # Spline challanger
    for n in N:
        interp = spline_interpolation(xch, ych, n)
        interpolation_points = np.linspace(0, len(xch) - 1, n).astype(int)
        plot_interpolation(xch, ych, interp, interpolation_points, 'Spline Interpolation Challenger')




if __name__ == "__main__":
    main()
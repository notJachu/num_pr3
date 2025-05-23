import pandas as pd
import numpy as np
from lagrange import lagrange_interpolation
import matplotlib.pyplot as plt

def main():
    raw_data = pd.read_csv("profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv")

    # Cut data to 100 rows
    data = raw_data.iloc[100:201]
    data = data.to_numpy()

    # split data into x and y
    x = data[:, 0]
    y = data[:, 1]

    # Normalise x to 0-1
    x = (x - np.min(x)) / (np.max(x) - np.min(x))

    print(x)

    # print(y)

    # Interpolate
    N = 30
    interp = lagrange_interpolation(x, y, N)
    interpolation_points = np.linspace(0, len(x) - 1, N).astype(int)



    plt.plot(x, y, 'r-', label='Original Data')
    plt.plot(x, interp, 'b-', label='Interpolated Data')
    plt.scatter(x[interpolation_points], y[interpolation_points], color='green', label='Interpolation Points')

    # runge efect
    plt.xlim(0, 1)
    plt.ylim(np.min(y) - 1, np.max(y) + 1)

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Lagrange Interpolation')
    plt.legend()
    plt.grid()
    plt.show()



if __name__ == "__main__":
    main()
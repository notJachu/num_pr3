import pandas as pd
import numpy as np

def main():
    raw_data = pd.read_csv("profile_wysokosciowe/2018_paths/SpacerniakGdansk.csv")

    # Cut data to 100 rows
    data = raw_data.iloc[100:201]
    data = data.to_numpy()

    # split data into x and y
    x = data[:, 0]
    y = data[:, 1]

    # Normalise y to 0-1
    y = (y - np.min(y)) / (np.max(y) - np.min(y))

    print(y)





if __name__ == "__main__":
    main()
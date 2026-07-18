import pandas as pd
import numpy as np

def get_frequency_table(iterable):
    uniques, counts = np.unique(iterable, return_counts=True)
    relative_freq = counts / counts.sum()
    return pd.DataFrame({
        'x': uniques,
        'f': counts,
        'r': relative_freq,
        'F': counts.cumsum(),
        'R': relative_freq.cumsum()
    })


if __name__ == '__main__':
    observations = ['A', 'A', 'B', 'A', 'C', 'C', 'A', 'B', 'B', 'C', 'A', 'C']
    table = get_frequency_table(observations)
    print(table)

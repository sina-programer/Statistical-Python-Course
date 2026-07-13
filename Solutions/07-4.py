import numpy as np

def loop(sequence):
    result = []
    for i in range(len(sequence)-1):
        result.append((sequence[i]+sequence[i+1])/2)
    return result

def vectorized(sequence):
    return np.add(sequence[1:], sequence[:-1]) / 2


if __name__ == '__main__':
    series = [10, 12, 12, 13, 15, 20]
    print(series)
    print(loop(series))
    print(vectorized(series))

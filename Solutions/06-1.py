nan = float('nan')

def arithmetic(series):
    n = s = 0
    for x in series:
        s += x
        n += 1

    if n == 0:
        return nan
    return s / n

def geometric(series):
    p, n = 1, 0
    for x in series:
        if x <= 0:
            continue
        p *= x
        n += 1
    
    if n == 0:
        return nan
    return p ** (1/n)

def harmonic(series):
    n, s = 0, 0
    for x in series:
        if x == 0:
            continue
        s += (1 / x)
        n += 1

    if n == 0:
        return nan
    return n / s

def weighted(series, weights=None):
    if weights is None:
        weights = [1] * len(series)

    sx, sw = 0, 0
    for x, w in zip(series, weights):
        sx += w*x
        sw += w

    if sw == 0:
        return nan
    return sx / sw

functions = [arithmetic, geometric, harmonic, weighted]


if __name__ == '__main__':
    import random

    N = 100
    X = [random.randint(1, 10) for _ in range(N)]
    for f in functions:
        print(f.__name__ + ':', f(X))

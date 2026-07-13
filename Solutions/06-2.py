from statistics import stdev
import random
import time

def mean(series):
    n, s = 0, 0
    for x in series:
        s += x
        n += 1
    return s / n

def var(series):
    avg = mean(series)  # sum(series) / len(series)
    s, n = 0, 0
    for x in series:
        s += (x - avg) ** 2
        n += 1
    return s / n

def std(series):
    return var(series) ** 0.5


if __name__ == '__main__':
    N = 10_000
    X = [random.random()+1 for _ in range(N)]

    t1 = time.time()
    s1 = stdev(X)
    t2 = time.time()
    s2 = std(X)
    t3 = time.time()

    dt1 = t2 - t1
    dt2 = t3 - t2

    print('statistics function  :', dt1, 's')
    print('manuall implementaion:', dt2, 's')

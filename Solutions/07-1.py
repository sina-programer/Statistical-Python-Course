import numpy as np

points = [5, 10, 20, 50, 100, 200, 500, 1_000, 10_000, 50_000, 100_000, 500_000]
last_point = 1
last_sum = 0

for point in sorted(points):
    t = np.arange(last_point, point)
    s = np.sum(1 / np.square(t))

    last_point = point
    last_sum += s

    print('{:_}\t: {}'.format(point, last_sum))

print('(PI^2)/6:', np.square(np.pi)/6)

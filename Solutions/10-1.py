from matplotlib import pyplot as plt
import numpy as np

# P(X > s+t | X>s) = P(X > t)

N = 100_000
mean = 2
lam = 1 / mean
delta = 1
U = np.random.random(N)
X = -np.log(U) / lam

grid = np.quantile(X, np.arange(1, 100)/100)
Y = X[X > delta]
P1 = [
    np.mean(Y > t+delta)
    for t in grid
]
P2 = [
    np.mean(X > t)
    for t in grid
]

plt.scatter(P1, P2)
plt.xlabel('P(X > t+{0} | X>{0})'.format(delta))
plt.ylabel('P(X > t)')
plt.grid()
plt.show()

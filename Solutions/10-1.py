import numpy as np

# P(X > a+b | X>a) = P(X > b)

N = 100_000
mean = 2
a = 1
b = 2

U = np.random.random(N)
X = -np.log(U) * mean

p1 = np.mean(X > b)
p2 = np.mean(X[X>a] > a+b)

print(p1)
print(p2)

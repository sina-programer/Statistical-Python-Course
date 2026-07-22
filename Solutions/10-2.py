import numpy as np

N = 100_000

X = np.random.random(N)
Y = np.random.random(N)
R = np.sqrt((X-0.5)**2 + (Y-0.5)**2)
mask = R <= 0.5
pi = 4 * np.mean(mask)
print(pi)

from matplotlib import pyplot as plt
import numpy as np

def likelihood(p):
    s = np.sum(X)
    return p**s * (1-p)**(N-s)

P = 0.5
N = 20
X = np.where(np.random.random(N) <= P, 1, 0)
Pbar = np.mean(X)

span = np.linspace(0, 1, 101)
# L = list(map(likelihood, span))
L = likelihood(span)
L_max = np.max(L)

plt.plot(span, L)
plt.vlines(P, 0, L_max, colors='red', linestyles='solid', label='parameter')
plt.vlines(Pbar, 0, L_max, colors='red', linestyles='dashed', label='estimate')
plt.legend()
plt.show()

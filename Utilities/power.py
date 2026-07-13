from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

n = 10
s0 = stats.binom(n, 0.75)
s1 = stats.binom(n, 0.25)

t = np.arange(n+1)
alpha = s0.cdf(t)
power = s1.cdf(t)
beta = 1 - power

plt.plot(t, alpha, label='I')
plt.plot(t, beta, label='II')
plt.legend()
plt.show()

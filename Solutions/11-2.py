from matplotlib import pyplot as plt
from scipy import stats
import numpy as np

N = 10_000  # n.o. observations
K = 1000  # n.o. samples

X = np.random.random((N, K))
Xbar = X.mean(axis=1)

sample_mean = np.mean(Xbar)
sample_std = np.std(Xbar)

dist = stats.norm(sample_mean, sample_std)
span = np.linspace(np.min(Xbar), np.max(Xbar), 100)
prob = dist.pdf(span)

plt.hist(Xbar, bins=100, density=True)
plt.plot(span, prob, color='red')
plt.show()

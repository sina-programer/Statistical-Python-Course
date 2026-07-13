from matplotlib import pyplot as plt
import numpy as np

n = 10

##means = np.random.random((n, 1000)).mean(axis=0)
##plt.hist(means, bins=100, density=True)
##print(np.mean(means))
##print(np.var(means))

arr = np.random.random(n)
means_bts = [np.random.choice(arr, n, replace=True).mean() for _ in range(1000)]
plt.hist(means_bts, bins=100, density=True, alpha=0.7)
print(np.mean(means_bts))
print(np.var(means_bts))

plt.show()

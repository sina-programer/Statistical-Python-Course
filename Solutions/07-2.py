import numpy as np
import random

N = 1000  # population size
K = 10  # number of samples
P = 0.5  # proportion for sampling

population = []
for _ in range(N):
    if random.random() < 0.5:
        population.append(0)
    else:
        population.append(1)

true_mean = np.mean(population)
sample_means = []
print(true_mean)

for _ in range(K):
    sample = random.sample(population, int(N*P))
    sample_means.append(np.mean(sample))

print(np.mean(sample_means))
print(np.round(sample_means, 2))

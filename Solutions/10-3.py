import numpy as np
import math

N = 100_000


print('\nSimulating a flush (5 same card)')

exact_p1 = 4 * math.comb(13, 5) / math.comb(52, 5)
print('Exact Probability:', exact_p1)

cards = ['A', 'B', 'C', 'D'] * 13
count1 = 0
for _ in range(N):
    deck = np.random.choice(cards, 5, replace=False)
    if len(set(deck)) == 1:
        count1 += 1

p1 = count1 / N
print('Estimated Probability:', p1)


print('\nSimulating 10 tosses exceeding 30')

A = np.random.randint(1, 7, size=(N, 10))
S = np.sum(A, axis=1)
p2 = np.mean(S >= 30)
print(p2)


print('\nSimulating product of two uniform numbers less than 0.5')

U1 = np.random.random(N)
U2 = np.random.random(N)
U = U1 * U2
p3 = np.mean(U <= 0.5)
print(p3)

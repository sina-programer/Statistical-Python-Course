X = [1, 2, 3, 4, 5]
S = []

for i in range(len(X)):
    k = i+1
    cum_mean = sum(X[:k]) / k

    vi = 0
    for j in range(k):
        vi += (X[j] - cum_mean) ** 2

    S.append((vi/k) ** 0.5)

print(S)

total = 6 ** 3
count = 0

die = range(1, 7)
for a in die:
    for b in die:
        for c in die:
            s = a + b + c
            if s >= 12:
                count += 1

probability = count / total
print(probability)

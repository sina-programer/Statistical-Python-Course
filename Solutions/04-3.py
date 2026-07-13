digits = list(input('Enter an integer: '))

uniques = []
for i in range(len(digits)):
    digit = int(digits[i])
    if digit not in uniques:
        uniques.append(digit)

uniques = tuple(uniques)
print(uniques)

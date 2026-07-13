x = abs(int(input('Enter a number: ')))
maximum = -float('inf')
length = 0

while x>0:
    d, m = divmod(x, 10)
    if m > maximum:
        maximum = m
    length += 1
    x = d

print('Maximum Digit:', maximum)
print('Number of Digits:', length)

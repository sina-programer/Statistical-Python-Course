n = int(input('Enter n: '))
a, b = 0, 1

while n>0:
    print(a)
    a, b = b, b+a
    n -= 1

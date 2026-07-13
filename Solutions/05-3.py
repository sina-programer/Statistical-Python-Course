def fib(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, b+a
        n -= 1
    return a


for i in range(10):
    print(i, fib(i))

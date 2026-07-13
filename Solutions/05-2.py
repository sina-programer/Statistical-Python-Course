def is_prime(n):
    if n<2:
        return False
    for k in range(2, n):
        if n%k == 0:
            return False
    return True

def is_prime_efficient(n):
    if n < 2 or n%2 == 0:
        return False

    for k in range(3, int(n**0.5)+1, 2):
        if n % k == 0:
            return False

    return True


for x in range(100):
    if is_prime(x):
        print(x)

def collatz(n):
    if n%2 == 0:
        return n//2
    return 3*n + 1

def path(n):
    history = []
    while n > 1:
        history.append(n)
        n = collatz(n)
    return history


if __name__ == "__main__":
    from matplotlib import pyplot as plt

    n = 9  # int(input())
    p = path(n)
    plt.plot(p)
    plt.show()

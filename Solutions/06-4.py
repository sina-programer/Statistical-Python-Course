import random

def shuffle(iterable):
    iterable = list(iterable)
    output = []
    n = len(iterable)
    for i in range(n):
        idx = random.randint(0, n-i-1)
        output.append(iterable.pop(idx))
    return output


if __name__ == '__main__':
    nums = list(range(5))
    print(nums)
    print(shuffle(nums))

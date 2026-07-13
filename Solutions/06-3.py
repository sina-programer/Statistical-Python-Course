def sum_of_digits(x):
    if x < 10:
        return x

    s = 0
    while x > 0:
        d, m = divmod(x, 10)
        s += m
        x = d

    return sum_of_digits(s)


if __name__ == '__main__':
    print(sum_of_digits(99))

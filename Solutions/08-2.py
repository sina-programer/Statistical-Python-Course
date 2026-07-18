from statistics import sumprod

def expectation(rv: dict):
    return sumprod(rv.keys(), rv.values())

def variance(rv: dict):
    E = expectation(rv)
    E2 = expectation({x**2: p for x, p in rv.items()})
    return E2 - E**2


if __name__ == '__main__':
    random_variable = {0: 0.25, 1: 0.5, 2: 0.25}
    print('Random Variable:', random_variable)
    print('Expectation:', expectation(random_variable))
    print('Variance:', variance(random_variable))

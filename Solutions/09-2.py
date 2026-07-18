def f(n):
    numerator = 1
    a = 365 - n + 1
    while a <= 365:
        numerator *= a
        a += 1
    return 1 - numerator / (365**n)


if __name__ == '__main__':
    from matplotlib import pyplot as plt
    import numpy as np

    span = list(range(1, 100))
    probs = list(map(f, span))
    plt.plot(span, probs, label='probs')

    threshold = 0.5
    k = int(np.take(span, np.where(np.greater_equal(probs, threshold))[0]).min())
    # k = span[np.where(np.greater_equal(probs, threshold))[0][0]]
    # k = span[np.argmin(np.less_equal(probs, threshold))]
    # k = np.where(np.greater_equal(probs, threshold), span, span[-1]+1).min()
    print('with {} people, the probability of observing same birth days exceeds {}'.format(k, threshold))
    plt.hlines(threshold, span[0], span[-1], linestyles='dotted', colors='black', alpha=0.5, label='threshold')
    plt.vlines(k, 0, 1, linestyles='dashed', colors='red', label='k')

    plt.legend()
    plt.show()

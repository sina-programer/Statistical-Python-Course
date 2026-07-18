def barplot(dictionary, n=10):
    max_key_length = max(map(len, dictionary.keys()))
    sum_values = sum(dictionary.values())
    for key, value in dictionary.items():
        ratio = value / sum_values
        print("{:<{}} |{:<{}}| {:.2%}".format(key, max_key_length, '#'*int(ratio*n), n, ratio))
        # print(key.ljust(max_key_length), '|'+('#'*int(ratio*n)).ljust(n)+'|', round(ratio, 4)*100, '%')


if __name__ == '__main__':
    quota = {
        'A': 1,
        'B': 3,
        'C': 6
    }

    barplot(quota)

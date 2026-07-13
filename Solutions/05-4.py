def min_(iterable):
    floor = float('inf')
    for x in iterable:
        if x < floor:
            floor = x
    return floor

def sum_(iterable):
    summation = 0
    for x in iterable:
        summation += x
    return summation

def zip_(a, b):
    result = []
    for i in range(min(len(a), len(b))):
        result.append((a[i], b[i]))
    return result

def sorted_(iterable):
    '''bubble sort'''
    output = iterable.copy()
    n = len(iterable)
    for i in range(n):
        for j in range(i+1, n):
            if output[i] > output[j]:
                output[i], output[j] = output[j], output[i]
    return output

def reversed_(iterable):
    output = []
    n = len(iterable)
    for i in range(n):
        output.append(iterable[n-i-1])
    return output

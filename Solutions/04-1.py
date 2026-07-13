n = int(input('Enter n: '))

numbers = []
for i in range(n):
    xi = float(input('Enter {}th number: '.format(i+1)))
    numbers.append(xi)

mean = sum(numbers) / n

var = 0
for i in range(n):
    var += (numbers[i] - mean) ** 2
var /= n

std = var ** 0.5

queue = []
for i in range(n):
    si = (numbers[i] - mean) / std
    queue.append(str(round(si, 2)))
print(', '.join(queue))

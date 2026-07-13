flag = True
n = 0
s = 0

while flag:
    x = float(input('Enter a number: '))
    if x == 0:
        flag = False
    else:
        n += 1
        s += x

if n == 0:
    print('You should enter at least one number!')
else:
    mean = s / n
    print(mean)

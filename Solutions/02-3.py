score = float(input('Enter your score: '))

# first method
if score<0 or score>20:
    print('invalid')
elif score < 10:
    print('low')
elif score < 15:
    print('good')
else:
    print('great')

# second method
if 0 <= score < 10:
    print('low')
elif 10 <= score < 15:
    print('good')
elif 15 <= score <= 20:
    print('great')
else:
    print('invalid')

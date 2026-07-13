hours = int(input('Enter hours: '))

if hours < 0:
    print('Negative hours is invalid')

else:
    hours = hours % 24
    converted = hours % 12

    if converted == 0:
        converted = 12

    if hours < 12:
        period = 'AM'
    else:
        period = 'PM'

    print(converted, period)

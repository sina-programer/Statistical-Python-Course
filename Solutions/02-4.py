a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

is_triangle = a+b > c and a+c > b and b+c > a
is_right_angle = (
    (a**2 == b**2+c**2)
    or (b**2 == a**2+c**2)
    or (c**2 == a**2+b**2)
)

if is_triangle:
    print('Triangle')

    if is_right_angle:
        print('Right-Angle')

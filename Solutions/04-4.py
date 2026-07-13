people = [
    {
        'name': 'A',
        'age': 20
    },
    {
        'name': 'B',
        'age': 18
    },
    {
        'name': 'C',
        'age': 21
    },
]

n = len(people)
ages = []
for i in range(n):
    person = people[i]
    ages.append(person['age'])

i = j = n//2
if n%2 == 0:
    j = i + 1
ages_sorted = sorted(ages)
median = (ages_sorted[i] + ages_sorted[j]) / 2
print('Median:', median)

counter = 0
for i in range(n):
    if ages[i] < 18:
        counter += 1
print('Number of under 18s:', counter)

max_age = max(ages)
print('name(s) with maximum age of {}:'.format(max_age))
for i in range(n):
    if people[i]['age'] == max_age:
        print(people[i]['name'])

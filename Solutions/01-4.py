t = 155  # seconds

h = t // 3600
t = t % 3600

m = t // 60
t = t % 60

s = t

print(h, 'hours,', m, 'minutes and', s, 'seconds')

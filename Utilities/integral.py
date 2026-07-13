from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def f(x):
    return np.square(x)

a, b, step = 0, 2, 0.1
s = np.arange(a, b+step, step)
x = np.linspace(a, b, 101)
y = f(x)

plt.plot(x, y)
plt.bar(s, f(s), width=step*0.9, alpha=0.5, color='#ee4b66')

plt.savefig('integral.png', transparent=True)
plt.show()

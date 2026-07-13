from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

n = 100
a, b = 5, 2
X = np.random.random(n) * 2
E = np.random.randn(n)
Y = a + b*X**2 + E

span = np.linspace(np.min(X), np.max(X), 100)
plt.plot(span, a+b*span**2, c='#ee4b66')
plt.scatter(X, Y)

plt.savefig('s1.png', transparent=True)
plt.show()

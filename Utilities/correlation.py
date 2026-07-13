from matplotlib import pyplot as plt
from functools import partial
import pandas as pd
import numpy as np

plt.rcParams['mathtext.default'] = 'regular'
COLOR = '#ee4b66'

n = 50
E = np.random.randn(n)
X = np.random.random(n) * 2
span = np.linspace(np.min(X), np.max(X), 100)

fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(8, 7))

f1 = np.poly1d([2, 5])
Y1 = f1(X) + 1.4*E
axes[0, 0].plot(span, f1(span), c=COLOR)
axes[0, 0].scatter(X, Y1)
axes[0, 0].set_title(r'$\rho={:.3f}$'.format(np.corrcoef(X, Y1)[0, 1]))

f2 = np.poly1d([-1, 2])
Y2 = f2(X) + 0.25*E
axes[0, 1].plot(span, f2(span), c=COLOR)
axes[0, 1].scatter(X, Y2)
axes[0, 1].set_title(r'$\rho={:.3f}$'.format(np.corrcoef(X, Y2)[0, 1]))

Y3 = np.random.random(n)
f3 = np.poly1d(np.polyfit(X, Y3, 1))
axes[1, 0].plot(span, f3(span), c=COLOR)
axes[1, 0].scatter(X, Y3)
axes[1, 0].set_title(r'$\rho={:.3f}$'.format(np.corrcoef(X, Y3)[0, 1]))

X4 = X - 1
f4 = np.square
Y4 = f4(X4) + 0.4*E
axes[1, 1].plot(span-1, f4(span-1), c=COLOR)
axes[1, 1].scatter(X4, Y4)
axes[1, 1].set_title(r'$\rho={:.3f}$'.format(np.corrcoef(X4, Y4)[0, 1]))

fig.tight_layout()
plt.savefig('corr.png', transparent=True)
plt.show()

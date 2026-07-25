from scipy import stats
import numpy as np

n = 30
variance = 1
x = stats.norm(0, np.sqrt(variance / n))
xbar = 0.4

for alpha in [0.05, 0.01]:
    lower, upper = x.interval(1 - alpha)
    is_typical = lower <= xbar <= upper
    print('at alpha={} the observed sample mean of {}, {} typical.'.format(alpha, xbar, 'IS' if is_typical else 'IS NOT'))

print('NOTE: if observed value IS typical it means the hypothetical distribution can not be rejected.')

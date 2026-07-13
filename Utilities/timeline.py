from matplotlib import pyplot as plt
import numpy as np

session = 1

plt.rcParams['ytick.major.left'] = False
plt.rcParams['xtick.major.bottom'] = False

plt.rcParams['axes.spines.left'] = False
plt.rcParams['axes.spines.right'] = False
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.bottom'] = False

text_props = {
    'verticalalignment': 'center',
    'horizontalalignment': 'center',
    'fontsize': 20
}

phenomenon = {
    1: ['install', 'print', 'arithmetic', 'variable', 'naming', 'constant', 'comment', 'delete', 'string operations', 'data', 'scales'],
    2: ['scripting', 'built-in functions', 'data types', 'comparison', 'logical operators', 'input', 'condition', 'enumerate', 'combination', 'set'],
    3: ['loop', 'block', 'index', 'method', 'frequency table', 'central tendency', 'dispersion'],
    4: ['notebook', 'dir/help', 'iterable', 'iterable functions', 'membership', 'identity', 'interruption', 'linear transformation', 'standardization', 'scaling'],
    5: ['range', 'iterative loop', 'loop management', 'function', 'quantile', 'box plot', 'outlier detection'],
    6: ['library', 'standard libraries', 'thrid-party libraries', 'arithmetic mean', 'geometric mean', 'harmonic mean', 'weighted mean'],
    7: ['population & sample', 'concept of probability', 'probability theory', 'conditional probability', 'numpy arrays', 'vector operations'],
    8: ['random variable', 'probability function', 'CDF', 'expectation', 'variance', 'joint distribution', 'random sample', 'tabular data', 'pandas', 'read/write'],
    9: ['relation', 'covariance', 'correlation', 'bar plot', 'pie chart', 'scatter plot', 'line plot', 'histogram', 'box plot', 'q-q plot', 'grouping'],
    10: ['statistical distribution', 'bernoulli / binominal', 'hyper geometric', 'poisson', 'negative binomial', 'uniform', 'exponential', 'normal', 'inverse transform', 'simulation'],
    11: ['central limit theorem', 'inferential statistics', 'statistic', 'estimator', 'MLE', 'confidence interval', 'mean diff CI'],
    12: ['hypothesis testing', 'statistical errors', 'critical region', 'p-value', 'linear relation', 'correlation test', 'linear regression']
}[session]

k = len(phenomenon)
L = np.arange(k)
X = np.arange(k)
Y = np.zeros(k)
E = np.ones(k)
S = np.where(X%2==0, 1, -1)
eps = E / 6
P = Y + (E+eps)*S

plt.figure(figsize=(17, 8))

plt.errorbar(X, Y, yerr=E, lolims=X%2==0, uplims=X%2==1, c='#ee4b66')
for i, phenomena in enumerate(phenomenon):
    plt.text(X[i], P[i], phenomena, **text_props)
    # plt.text(X[i], Y[i]-S[i]*eps[i], L[i], **text_props, color='darkblue', backgroundcolor='cyan')

# plt.ylim(np.min(P*1.25), np.max(P*1.25))
plt.tight_layout()
plt.savefig('timeline.png', transparent=True)
plt.show()

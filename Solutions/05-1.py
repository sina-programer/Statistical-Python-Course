def quantile(series, p):
    if p<0 or p>1:
        return float('nan')
    X = sorted(series)
    n = len(series)
    k = (n+1) * p
    r = int(k // 1)
    w = k - r
    return w * X[r] + (1-w) * X[r-1]

def mask_outliers(series, k=1.5):
    q1 = quantile(series, 0.25)
    q3 = quantile(series, 0.75)
    iqr = q3 - q1
    lower = q1 - k*iqr
    upper = q3 + k*iqr
    mask = []
    for x in series:
        mask.append((x<lower) or (x>upper))
    return mask

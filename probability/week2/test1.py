from scipy.stats import poisson

mu = 2
rv = poisson(mu)

less_5_sum = sum([rv.pmf(k) for k in range(6)])

print(1 - less_5_sum)

percentile = rv.ppf(0.95)

print(percentile)

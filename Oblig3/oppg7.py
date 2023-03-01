import numpy as np
from scipy import stats as stats
from matplotlib import pyplot as plt

val = float(input("Skriv inn ønsket λt: \n"))
l = int(input("Skriv inn øvre grense: \n"))

x = np.arange(0, l+1, 1)
p1 = stats.poisson.pmf(x, mu=val)
p2 = stats.poisson.pmf(x, mu=val+20)
p3 = stats.poisson.pmf(x, mu=val+40)

plt.plot(x, p1)
plt.plot(x, p2)
plt.plot(x, p3)
plt.show()
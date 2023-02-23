import numpy as np
from scipy import stats as stats
from matplotlib import pyplot as plt

x = np.arange(720, 801, 1)


plt.plot(stats.norm.pdf(x, 760, 10))
plt.title("Normalfordeling")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.xticks(np.arange(0, 81, 10), np.arange(720, 801, 10))
plt.show()
import random as rand
from matplotlib import pyplot as plt
import numpy as np

i = int(input("Skriv in ønsket antall omganger: "))
j = int(input("Skriv in ønsket antall kast pr omgang: "))
results = []
avg_results = []

for x in range(i):
    print(x)
    result = 0
    for y in range(j):
        result += rand.randint(1,6)

    results.append(result)
    avg_results.append(result/j)

#print(results, "\n", avg_results)

# Fikse antall bins - 30 stk
bin_range = np.arange(min(avg_results), max(avg_results) + 0.05, 0.05)
plt.hist(avg_results, bins=bin_range)
plt.show()
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

plt.hist(avg_results, bins=30, edgecolor="black", linewidth=0.5)
plt.show()
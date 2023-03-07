import math
import random as rand
from matplotlib import pyplot as plt
import numpy as np

i = int(input("Skriv in ønsket antall omganger: "))
j = int(input("Skriv in ønsket antall kast pr omgang: "))
results = []
avg_results = []
sum_of_avg = 0
diff = []
for x in range(i):
    result = 0
    for y in range(j):
        result += rand.randint(1,6)

    results.append(result)
    avg_results.append(result / j)
    diff.append(math.pow(result, 2) - math.pow((result / j), 2))

total_avg = (sum(avg_results) / i)

var = (sum(diff) / (i - 1))
sd = math.sqrt(var)

print(results)
print(avg_results)
print("Gjennomsnittet av hele utvalget: ", total_avg)
print(diff)
print("Utvalgsvarians: ", var)
print("Utvalgsstandardavvik: ", sd)


#print(results, "\n", avg_results)

# Fikse antall bins - 30 stk
#bin_range = np.arange(min(avg_results), max(avg_results) + 0.05, 0.05)
#plt.hist(avg_results, bins=bin_range)
#plt.show()
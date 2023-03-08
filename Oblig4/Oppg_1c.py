import math
import random as rand
from matplotlib import pyplot as plt
import numpy as np

n = int(input("Skriv in ønsket antall omganger: "))
k = int(input("Skriv in ønsket antall kast pr omgang: "))
results = []
avg_results = []
sum_of_avg = 0
S2_sum = 0

for omgang in range(n):
    result = 0
    for kast in range(k):
        result += rand.randint(1,6)

    results.append(result)
    avg_results.append(result / k)

total_avg = np.mean(avg_results)

utvalgsstandardavvik = np.std(avg_results)

print("Resultater: ", results)
print("Gjennomsnitt pr omgang: ", avg_results)
print("Gjennomsnittet av hele utvalget: ", total_avg)
print("Utvalgsstandardavvik: ", utvalgsstandardavvik)

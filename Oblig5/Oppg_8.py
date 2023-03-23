from matplotlib import pyplot as plt
from scipy import stats
import pandas as pd
import numpy as np
import math

measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

b_weights = []
h_weights = []

for row in measurements:
    b_weights.append(row[1])
    h_weights.append(row[2])

# a)
plt.scatter(b_weights, h_weights)
plt.xlabel("Kroppsvekt (kg)")
plt.ylabel("Hjertevekt (g)")
plt.show()

# b)
reg_line = stats.linregress(b_weights, h_weights)
beta_hat = reg_line.slope
stderr = reg_line.stderr

print(f"Ligningen for linjen: y={round(reg_line.intercept, 4)}+{round(beta_hat, 4)}x")
print(f"Standardfeilen for estimatoren β er {round(stderr, 4)}")

# d)
x = float(input("Skriv inn en vekt(i kg): "))

# Regner ut alfa, n, antall frihetsgrader og middelvedi av b_weights
alpha = 0.05
n = len(b_weights)
dof = n - 2
x_mean = np.mean(b_weights)

SS_E = 0
for row in measurements:
    SS_E += math.pow((row[2] - reg_line.intercept - beta_hat * row[1]), 2)

s2 = SS_E / dof
s = math.sqrt(s2)

expected_h_weight = reg_line.intercept + beta_hat * x
t_statistic = stats.t.ppf(1 - alpha / 2, dof)
ci_limit = t_statistic * s * math.sqrt((1/n) + math.pow(((x - x_mean) / (s / stderr)), 2))

print(f"Konfidensintervallet for hjertevekt når kroppsvekten er {x} er: {round(expected_h_weight, 1)} +- { round(ci_limit, 1)}")

# e)
pi_limit = t_statistic * s * math.sqrt(1 + (1/n) + math.pow(((x - x_mean) / (s / stderr)), 2))

print(f"Prediksjonsintervallet for hjertevekt når kroppsvekten er {x} er: {round(expected_h_weight, 1)} +- {round(pi_limit, 1)}")



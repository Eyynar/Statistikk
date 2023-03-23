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

#plt.scatter(b_weights, h_weights)
#plt.show()

reg_lin = stats.linregress(b_weights, h_weights)

beta_hat = reg_lin.slope

print(f"Ligningen for linjen: y={round(reg_lin.intercept, 4)}+{round(beta_hat, 4)}x")
print(f"Standardfeilen for estimatoren β er {round(reg_lin.stderr, 4)}")

x = float(input("Skriv inn en vekt(i kg): "))

alpha = 0.05
dof = len(b_weights) - 2
variance = np.var(b_weights)

expected_h_weight = reg_lin.intercept + beta_hat * x

t_statistic = stats.t.ppf(1 - alpha / 2, dof)


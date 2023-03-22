from matplotlib import pyplot as plt
from scipy import stats
import pandas as pd

measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

b_weights = []
h_weights = []

for row in measurements:
    b_weights.append(row[1])
    h_weights.append(row[2])

#plt.scatter(b_weights, h_weights)
#plt.show()

reg_lin = stats.linregress(b_weights, h_weights)
print(f"Ligningen for linjen: y={round(reg_lin.intercept, 4)}+{round(reg_lin.slope, 4)}x")
print(f"Standardfeilen for estimatoren β er {round(reg_lin.stderr, 4)}")

y = float(input())

    
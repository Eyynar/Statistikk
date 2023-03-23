from scipy import stats
import pandas as pd

measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

b_weights = []
h_weights = []

for row in measurements:
    b_weights.append(row[1])
    h_weights.append(row[2])

r = stats.pearsonr(b_weights, h_weights)

print(f"Korrelasjonskoeffisienten mellom datasettene er: {round(r[0], 3)}")

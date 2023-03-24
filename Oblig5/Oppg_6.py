from scipy import stats
import pandas as pd

# Leser inn data fra csv-filen
measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

# Lager to lister som inneholder kroppsvekt og hjertevekt
b_weights = []
h_weights = []
for row in measurements:
    b_weights.append(row[1])
    h_weights.append(row[2])

# Finner korrelasjonskoeffisienten mellom datasettene
r = stats.pearsonr(b_weights, h_weights)

print(f"Korrelasjonskoeffisienten mellom datasettene er: {round(r[0], 3)}")

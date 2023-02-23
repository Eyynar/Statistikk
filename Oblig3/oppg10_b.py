import numpy as np
from scipy import stats

i = int(input("Skriv inn ønsket vekt: \n"))
x = np.arange(720, 801, 1)

print(f"Sannsynligheten for at brødet veier mer enn {i} gram: {1 - (stats.norm.cdf(x, 760, 10))[i-720]}")

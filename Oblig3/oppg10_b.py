import numpy as np
from scipy import stats

i = int(input("Skriv inn ønsket vekt: \n"))

print(f"Sannsynligheten for at brødet veier mer enn {i} gram: {1 - (stats.norm.cdf(i, 760, 10))}")

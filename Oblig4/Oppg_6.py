import numpy as np
import math
from scipy import stats

data = np.genfromtxt("maalinger.csv", delimiter=",")

alfa = (100 - int(input("Skriv inn ønsket konfidensintervall i prosent: "))) / 100
n = len(data)
dof = n - 1
s2 = np.var(data, ddof=1)

chi1 = stats.chi2.ppf(1 - alfa / 2, dof)
nedre_grense = math.sqrt((dof * s2) / chi1)

chi2 = stats.chi2.ppf((alfa / 2), dof)
ovre_grense = math.sqrt((dof * s2) / chi2)

print(f"Punktestimat for standardavvik: {np.std(data, ddof=1)}")
print(f"konfidensintervall: [{nedre_grense}, {ovre_grense}]")



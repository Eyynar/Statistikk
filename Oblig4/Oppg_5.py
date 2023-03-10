import math
from scipy import stats

n = int(input("Skriv inn utvalgets størrelse: "))
X = int(input("Skriv inn antall i favør for hendelsen: "))

KI_prosent = int(input("Skriv inn ønsket konfidensintervall i prosent: "))

p_hatt = (X / n)
alfa_2 = (100 - KI_prosent) / 200

if n * p_hatt * (1 - p_hatt) < 5:
    print("Med disse tallene er ikke forutsetningen oppfylt,")
    exit()

else:
    z = abs(stats.norm.ppf((alfa_2)))
    differanse = z * math.sqrt((p_hatt * (1 - p_hatt)) / n)
    print(f"Følgende er et {KI_prosent}% KI for tallene du tastet inn: \n[{p_hatt - differanse}, {p_hatt + differanse}]")

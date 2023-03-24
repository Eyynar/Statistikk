from scipy import stats
import pandas as pd

# Importerer data fra csv-filen "katters_vekt.csv"
measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

# Lager en liste med bare kroppsvektene til kattene
weights = []
for row in measurements:
    weights.append(row[1])

# Henter inn ønsket signifikansnivå og forventningsverdi fra bruker
alfa = float(input("Skriv inn ønsket signifikansnivå: "))
my_0 = float(input("Skriv inn forventningsverdi: "))

# Finner kritisk verdi og p-verdien til t-testen
t_statistic, p_value = stats.ttest_1samp(a=weights, popmean=my_0, alternative="greater")

# Regner ut antall frihetsgrader og finner t-kvantil
dof = len(weights) - 1
t_quantile = stats.t.ppf(1-alfa, dof)

# Bruker if-sjekk for å sjekke om H0 skal forkastes eller ikke
if t_statistic >= t_quantile:
    print(f"Siden t={round(t_statistic, 3)} >= t_alfa, v={round(t_quantile, 3)} forkaster vi H0 på signifikansnivå alfa={alfa}")

else:
    print(f"Siden t={t_statistic} < t_alfa, v={t_quantile} forkaster vi ikke H0 på signifikansnivå alfa={alfa}")

# Printer ut p-verdien
print(f"P-verdi: {round(p_value, 4)}")

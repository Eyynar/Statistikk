from scipy import stats

# Henter inn ønsket signifikansnivå
alpha = float(input("Skriv inn ønsket signifikansnivå: "))

# Binomial test med n=74, k=11 og p=0.05
test = stats.binomtest(11, n=74, p=0.05, alternative="greater")

# Bruker if-test for å sjekke om P-verdien er mindre eller større enn alfa, og skriver ut resultatet av testen
if test.pvalue <= alpha:
    print(f"Siden P={round(test.pvalue, 4)} <= alpha={alpha} forkaster vi H0 på signifikansnivå alfa=0.1")
else:
    print(f"Siden P={round(test.pvalue, 4)} >= alpha={alpha} forkaster vi ikke H0 på signifikansnivå alfa=0.1")




from scipy import stats
import numpy as np


# Oppgave a
print(f"Oppgave a:\nP(X=3): {round(stats.hypergeom.pmf(3, 64, 14, 8), 4)}\n"
      f"P(X<=3): {round(stats.hypergeom.cdf(3, 64, 14, 8), 4)}\n\n")


# Oppgave b
print(f"Oppgave b:\nP(X=3): {round(stats.binom.pmf(3, 8, (14/64)), 4)}\n"
      f"P(X<=3): {round(stats.binom.cdf(3, 8, (14/64)), 4)}\n\n")


# Oppgave c
print(f"Oppgave c:\nP(Y=3): {round(stats.hypergeom.pmf(3, 640, 140, 8), 4)}\n"
      f"P(Y<=3): {round(stats.hypergeom.cdf(3, 640, 140, 8), 4)}\n\n")


# Oppgave d
print(f"Oppgave d:\nP(Y=3): {round(stats.binom.pmf(3, 8, (140/640)), 4)}\n"
      f"P(Y<=3): {round(stats.binom.cdf(3, 8, (140/640)), 4)}\n\n")

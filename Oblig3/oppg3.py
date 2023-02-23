from scipy import stats
import numpy as np


# Oppgave a
print(f"Oppgave a:\nP(X=3): {stats.hypergeom.pmf(3, 64, 14, 8)}\n"
      f"P(X<=3): {stats.hypergeom.cdf(3, 64, 14, 8)}\n\n")


# Oppgave b
bin_pmf = stats.binom.pmf((np.arange(65)), 8, (14/64))

print(f"Oppgave b:\nP(X=3): {bin_pmf[3]}\n"
      f"P(X<=3): {stats.binom.cdf(3, 8, (14/64))}\n\n")


# Oppgave c
print(f"Oppgave c:\nP(Y=3): {stats.hypergeom.pmf(3, 640, 140, 8)}\n"
      f"P(Y<=3): {stats.hypergeom.cdf(3, 640, 140, 8)}\n\n")


# Oppgave d
bin_pmf = stats.binom.pmf((np.arange(641)), 8, (140/640))

print(f"Oppgave d:\nP(Y=3): {bin_pmf[3]}\n"
      f"P(Y<=3): {stats.binom.cdf(3, 8, (140/640))}\n\n")

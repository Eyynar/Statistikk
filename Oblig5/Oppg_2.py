from scipy import stats

# Finner p-verdien til t-verdien 3.53, med 9 frihetsgrader
p_verdi = stats.t.sf(3.53, 9)

print(f"P-verdien er {round(p_verdi, 4)}")

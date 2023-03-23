from scipy import stats
import numpy as np

p_verdi = stats.t.sf(3.53, 9)

print(f"P-verdien er {round(p_verdi, 4)}")

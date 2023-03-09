from scipy import stats
import numpy as np

data = [15, 17, 18, 14, 19, 16, 17, 15, 19, 13]

n = len(data)
dof = n - 1
X = np.mean(data)


#t_verdi = stats.t.ppf(0.05, dof)
p_verdi = stats.t.sf(3.53, dof)

#print(t_verdi)
print(p_verdi)
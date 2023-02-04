import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt

n = int(input("Skriv inn antall forsøk(som et heltall): \n"))
p = float(input("Skriv inn sannsynligheten for forsøket(med . ): \n"))

number_list = np.arange(n+1)

pmf = st.binom.pmf(number_list, n, p)
cdf = st.binom.cdf(number_list, n, p)
print(pmf)
print(cdf)

y_points1 = pmf
y_points2 = cdf

plt.plot(y_points1)
plt.plot(y_points2)
plt.show()

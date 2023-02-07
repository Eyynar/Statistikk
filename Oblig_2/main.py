import numpy as np
from scipy import stats as st
import matplotlib.pyplot as plt

n = int(input("Skriv inn antall forsøk(som et heltall): \n"))
p = float(input("Skriv inn sannsynligheten for forsøket(med . ): \n"))

number_list = np.arange(n+1)

plt.bar(number_list, st.binom.pmf(number_list, n, p))
plt.step(number_list, st.binom.cdf(number_list, n, p))
plt.show()

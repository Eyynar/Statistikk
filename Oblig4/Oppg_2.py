from statsmodels.graphics.gofplots import qqplot
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

measurements = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

weight = []
h_weight = []


for i in range(len(measurements)):
    weight.append(float(measurements[i][1]))
    h_weight.append(float(measurements[i][2]))

np_weight = np.array(weight)
np_h_weight = np.array(h_weight)

qqplot(np_weight, fit=True, line="s").suptitle("Kattenes vekt")
plt.show()

qqplot(np_h_weight, fit=True, line="s").suptitle("Hjertenes vekt")
plt.show()


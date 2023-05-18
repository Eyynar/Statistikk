import numpy as np
import pandas as pd

data = pd.read_csv('Leselyst.csv', quotechar=';', skipinitialspace=True).values
print(data)

np.mean
np.var
np.std
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

# Linear regression of data from katters_vekt.csv
# The data is from a study of the relationship between the weight of a cat and the weight of its heart.

# Read data from csv file
data = pd.read_csv('katters_vekt.csv', quotechar=',', skipinitialspace=True).values

# Extract the weights of the cats and the weights of the hearts
cat_weights = []
heart_weights = []

for row in data:
    cat_weights.append(row[1])
    heart_weights.append(row[2])

# Plot the data
plt.scatter(cat_weights, heart_weights)
plt.xlabel('Cat weight (kg)')
plt.ylabel('Heart weight (g)')
# plt.show()

# Perform linear regression
reg_lin = stats.linregress(cat_weights, heart_weights)

# Print the equation of the line
print(f"The equation of the line is: y={round(reg_lin.intercept, 4)}+{round(reg_lin.slope, 4)}x")

# Print the standard error of the estimator
print(f"The standard error of the estimator is {round(reg_lin.stderr, 4)}")

# Predict the weight of the heart of a cat with a weight of 3.5 kg
x = 2.1
alpha = 0.05
dof = len(cat_weights) - 2
variance = np.var(cat_weights)

# Return a confidence interval for the expected weight of a heart, given the weight of a cat.
expected_heart_weight = reg_lin.intercept + reg_lin.slope * x
t_statistic = stats.t.ppf(1 - alpha / 2, dof)

print(expected_heart_weight - t_statistic * math.sqrt(variance / len(cat_weights)), expected_heart_weight + t_statistic * math.sqrt(variance / len(cat_weights)))

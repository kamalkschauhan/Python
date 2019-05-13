import pandas as pd
print("\n")
print("Panda Series")

x = pd.Series([6,3,4,6])

print (x)

import numpy as np
print("\n")
print("Panda DataFrame")

df = pd.DataFrame(np.random.randn(14,3))

print (df)
print (df.describe())
# print (df[2].hist(bins=50))
print ("\n")
# print (df.hist(bins=50))

# import matplotlib as mpl
import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib import colors
# from matplotlib.ticker import PercentFormatter
# print (df[2].hist(bins=50))

x = np.random.normal(size = 1000)
# plt.hist(x, density=True, bins=30)
plt.hist(df[0], density=True, bins=30)
plt.ylabel('Probability');
plt.show()
# %matplotlib inline


df2 = pd.read_csv("report.csv")
print (df2.head())

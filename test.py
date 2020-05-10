import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



IrisData = pd.read_csv('IRIS.csv')

sns.set()
g = sns.lmplot(x="petal_length", y = "petal_width", hue = "species", height = 5, data=IrisData)
g.set_axis_labels("Petal length (mm)", "Petal width (mm)")
plt.show()
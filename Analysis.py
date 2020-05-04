import pandas
import numpy as np
import seaborn as sns
import matplotlib as plt


IrisData = pandas.read_csv('IRIS.csv')

# print(IrisData)
# this has output the full 150 instances of the data set to the terminal. 

# to provide an analysis of the information within the text, we are going to extract the following from the data: 
# Head of the data, tail of the data, describe of all the data contained. 

# a = IrisData.head
# print(a(10))
# this will provide a cursory glance at he material from the first 10 rows of data.

# d = IrisData.tail
# print(d(10))
# This will provide a cursory glance at he material from the last 10 rows of data.

# b = IrisData.describe
# print(b())
# this has printed to the terminal the overall description of the data set

# c = (IrisData.groupby('species').size())
# print(c)
# this will allow us to view the individual names of each iris

df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["sepal_length"])
plt.title('Compare of the three Sepal Lengths')
plt.xlabel('Difference in the Species')
plt.ylabel('Sepal Length')
plt.show()
plt.savefig()


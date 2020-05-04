import pandas
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


IrisData = pandas.read_csv('IRIS.csv')
# print(IrisData)
# this has output the full 150 instances of the data set to the terminal. 

# to provide an analysis of the information within the text, we are going to extract the following from the data: 
# Head of the data, tail of the data, describe of all the data contained. 

# a = IrisData.head
# print(a(10))
# this will provide a cursory glance at the material from the first 10 rows of data.

# d = IrisData.tail
# print(d(10))
# This will provide a cursory glance at the material from the last 10 rows of data.

# b = IrisData.describe
# print(b())
# this has printed to the terminal the overall description of the data set

# c = (IrisData.groupby('species').size())
# print(c)
# this will allow us to view the individual names of each iris

# df = sns.load_dataset('iris')
# sns.boxplot(x = df["species"], y = df["sepal_length"])
# plt.title('Compare of the three Sepal Lengths')
# plt.xlabel('Difference in the Species')
# plt.ylabel('Sepal Length')
# plt.show()
# plt.savefig()
# this will allow us to see the first sbox plot of all three species based on sepal length. 

# df = sns.load_dataset('iris')
# sns.boxplot(x = df["species"], y = df["sepal_width"])
# plt.title('Compare of the three Sepal Widths')
# plt.xlabel('Difference in the Species')
# plt.ylabel('Sepal Width')
# plt.show()


#df = sns.load_dataset('iris')
#sns.boxplot(x = df["species"], y = df["petal_length"])
#plt.title('Compare the three Petal Lengths')
#plt.xlabel('Difference in the Species')
#plt.ylabel('Petal Length')
#plt.show()


df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["petal_width"])
plt.title('Compare the three Petal Widths')
plt.xlabel('Difference in the Species')
plt.ylabel('Petal Width')
plt.show()
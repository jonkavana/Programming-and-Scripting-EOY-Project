import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def AppendToFile(content):
    file = open("Output.txt", "a")
    file.write(content)
    file.close()

IrisData = pd.read_csv('IRIS.csv')
# print(IrisData.values)
# print(IrisData)
# AppendToFile(str(IrisData))
# this has output the full 150 instances of the data set to the terminal. 

# to provide an analysis of the information within the text, we are going to extract the following from the data: 
# Head of the data, tail of the data, describe of all the data contained. 

#a = IrisData.head(10)
#print(a(10))
# AppendToFile(str(a))
# this will provide a cursory glance at the material from the first 10 rows of data.

# d = IrisData.tail
# print(d(10))
# This will provide a cursory glance at the material from the last 10 rows of data.

# b = IrisData.describe
# print(b())
# AppendToFile(str(b()))
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

#df = sns.load_dataset('iris')
#sns.boxplot(x = df["species"], y = df["petal_width"])
#plt.title('Compare the three Petal Widths')
#plt.xlabel('Difference in the Species')
#plt.ylabel('Petal Width')
#plt.show()

# plt.figure(figsize = (6, 5)) 
# SepalHist = IrisData["sepal_length"] 

# plt.hist(SepalHist, bins = 20, color = "green") 
# plt.title("Sepal Length in cm") 
# plt.xlabel("Sepal_Length_cm") 
# plt.ylabel("Count")
# plt.savefig("SepalHist.png")
# This as a code will print a hist of the sepal length

plt.figure(figsize = (10, 10))
plt.scatter(IrisData["sepal_length"], IrisData["sepal_width"])
plt.show()
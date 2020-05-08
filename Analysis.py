import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# We need to create a function to append each variable in our analysis into a single text file, so we call on this to do so.
def AppendToFile(content):
    file = open("Output.txt", "a")
    file.write(content)
    file.close()

# the following will print to the terminal screen the contents of the file in full in a grided view.
IrisData = pd.read_csv('IRIS.csv')
#print(IrisData)
#AppendToFile(str(IrisData))

# To provide an analysis of the information within the text, we are going to extract the following from the data: 
# An array of the data, Head of the data, tail of the data, description of the data contained. 

# the following will return all values for each instance in an array format.
#print(IrisData.values)
#AppendToFile(str(IrisData.values))

# this will provide a cursory glance at the material from the first 10 rows of data.
#a = IrisData.head(10)
#print(a)
#AppendToFile(str(a))

# This will provide a cursory glance at the material from the last 10 rows of data.
#b = IrisData.tail(10)
#print(b)
#AppendToFile(str(b))

# this has printed to the terminal the overall description of the data set
#c = IrisData.describe
#print(c())
#AppendToFile(str(c()))

# this will allow us to view the individual names of each Iris
#d = (IrisData.groupby('species').size())
#print(d)
#AppendToFile(str(d))


# Visual Ouput has been created from this point onwards.

# This will allow us to see the first box plot of all three species based on sepal length
df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["sepal_length"])
plt.title('Comparision of the three Sepal Lengths')
plt.xlabel('Difference in the Species')
plt.ylabel('Sepal Length')
plt.show()
plt.savefig("Images-from-Analysis/SepalLengthComparison.png")

# this will allow us to see the first box plot of all three species based on sepal width
# df = sns.load_dataset('iris')
# sns.boxplot(x = df["species"], y = df["sepal_width"])
# plt.title('Compare of the three Sepal Widths')
# plt.xlabel('Difference in the Species')
# plt.ylabel('Sepal Width')
# plt.show()
#plt.savefig("Images-from-Analysis/Test")

# this will allow us to see the first box plot of all three species based on petal length
#df = sns.load_dataset('iris')
#sns.boxplot(x = df["species"], y = df["petal_length"])
#plt.title('Compare the three Petal Lengths')
#plt.xlabel('Difference in the Species')
#plt.ylabel('Petal Length')
#plt.show()
#plt.savefig("Images-from-Analysis/Test")

# this will allow us to see the first box plot of all three species based on petal width
#df = sns.load_dataset('iris')
#sns.boxplot(x = df["species"], y = df["petal_width"])
#plt.title('Compare the three Petal Widths')
#plt.xlabel('Difference in the Species')
#plt.ylabel('Petal Width')
#plt.show()
#plt.savefig("Images-from-Analysis/Test")

# plt.figure(figsize = (6, 5)) 
# SepalHist = IrisData["sepal_length"] 

# plt.hist(SepalHist, bins = 20, color = "green") 
# plt.title("Sepal Length in cm") 
# plt.xlabel("Sepal_Length_cm") 
# plt.ylabel("Count")
# plt.savefig("SepalHist.png")
# This as a code will print a hist of the sepal length

#plt.figure(figsize = (10, 10))
#plt.scatter(IrisData["sepal_length"], IrisData["sepal_width"])
#plt.show()
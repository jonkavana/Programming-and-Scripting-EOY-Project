import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# We need to create a function to append each variable in our analysis into a single text file, so we call on this to do so.
def AppendToFile(content):
    file = open("Output.txt", "a")
    file.write(content)
    file.close()

# The following will print to the terminal screen the contents of the file in full in a grided view.
IrisData = pd.read_csv('IRIS.csv')
print(IrisData)
AppendToFile(str(IrisData))

# To provide an analysis of the information within the text, we are going to extract the following from the data: 
# An array of the data, Head of the data, tail of the data, description of the data contained. 

# The following will return all values for each instance in an array format.
print(IrisData.values)
AppendToFile(str(IrisData.values))

# This will provide a cursory glance at the material from the first 10 rows of data.
a = IrisData.head(10)
print(a)
AppendToFile(str(a))

# This will provide a cursory glance at the material from the last 10 rows of data.
b = IrisData.tail(10)
print(b)
AppendToFile(str(b))

# This has printed to the terminal the overall description of the data set
c = IrisData.describe
print(c())
AppendToFile(str(c()))

# This will allow us to view the individual names of each Iris
d = (IrisData.groupby('species').size())
print(d)
AppendToFile(str(d))


# Visual Ouput has been created from this point onwards.

# This will allow us to see the first box plot of all three species based on sepal length
df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["sepal_length"])
plt.title('Comparison of the three Sepal Lengths')
plt.xlabel('Difference in the Species')
plt.ylabel('Sepal Length')
plt.show()

# this will allow us to see the first box plot of all three species based on sepal width
df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["sepal_width"])
plt.title('Comparison of the three Sepal Widths')
plt.xlabel('Difference in the Species')
plt.ylabel('Sepal Width')
plt.show()

# This will allow us to see the first box plot of all three species based on petal length
df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["petal_length"])
plt.title('Comparison of the three Petal Lengths')
plt.xlabel('Difference in the Species')
plt.ylabel('Petal Length')
plt.show()

# This will allow us to see the first box plot of all three species based on petal width
df = sns.load_dataset('iris')
sns.boxplot(x = df["species"], y = df["petal_width"])
plt.title('Comparison of the three Petal Widths')
plt.xlabel('Difference in the Species')
plt.ylabel('Petal Width')
plt.show()

# The following code is in relation to the histogram requirements of the project.
# We are going to the create a histogram relationshop between our four attributes, the sepal length & width, as well as the petal length & width.

# This as a code will print a hist of the sepal length
plt.figure(figsize = (6, 5)) 
SepalLengthHist = IrisData["sepal_length"] 
plt.hist(SepalHist, bins = 20, color = "green") 
plt.title("Sepal Length in cm") 
plt.xlabel("Sepal_Length_cm") 
plt.ylabel("Count")
plt.savefig("SepalLengthHist.png")

plt.figure(figsize = (6, 5)) 
SepalWidthHist = IrisData["sepal_width"] 
plt.hist(SepalHist, bins = 20, color = "blue") 
plt.title("Sepal Width in cm") 
plt.xlabel("Sepal_Width_cm") 
plt.ylabel("Count")
plt.savefig("SepalWidthHist.png")

plt.figure(figsize = (6, 5)) 
PetalWidthHist = IrisData["petal_width"] 
plt.hist(SepalHist, bins = 20, color = "red") 
plt.title("Petal Width in cm") 
plt.xlabel("Petal_Width_cm") 
plt.ylabel("Count")
plt.savefig("PetalWidthHist.png")

plt.figure(figsize = (6, 5)) 
PetalLengthHist = IrisData["petal_length"] 
plt.hist(SepalHist, bins = 20, color = "magenta") 
plt.title("Petal Length in cm") 
plt.xlabel("Petal_Length_cm") 
plt.ylabel("Count")
plt.savefig("PetalLengthHist.png")


# The following code is in relation to the scatterplot requirements of the project.
# We are going to display the attributes against one another, as well as display the permutations of these instances using the seaborn library.

plt.scatter(IrisData["sepal_length"], IrisData["sepal_width"])
plt.title("sepal length versus sepal width")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()

plt.scatter(IrisData["petal_length"], IrisData["petal_width"])
plt.title("petal length versus petal width")
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()

sns.pairplot(IrisData, hue="species")
plt.show()
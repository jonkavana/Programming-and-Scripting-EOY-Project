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

z = IrisData.describe
print(z())


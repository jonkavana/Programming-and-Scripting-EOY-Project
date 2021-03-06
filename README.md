# An Analysis of Fishers Iris Dataset

## Ronald Fisher & the Iris DataSet

According to the [Encyclopaedia Brittanica](https://www.britannica.com/biography/Ronald-Aylmer-Fisher "Encyclopaedia Brittanica") Sir Ronald Fisher was a British statistician, commonly known for his development of statistical procedures. Fisher graduated from Cambridge in 1912, being awarded a B.A. in Astronomy, which amongst other aspects, focused on the mathematical components of the discipline.


In 1936 he published the work that we are analysing in this project entitled "The use of multiple measurements in taxonomic problems", retrieved from [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). It was only upon reading the paper and researching it further that it became clear that the dataset is sometimes refered to as the Anderson dataset. According to Fisher himself, as per [Wiley Online Library](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"), Dr. Anderson is the man who performed all of the physical recording of the measurements on the Iris species. It was Fisher who performed the analysis on these individual instances.


Before undertaking any detailed primary or secondary analysis, there are some high level observations that can be taken from the material ahead of time. According to the [UCI](http://archive.ics.uci.edu/ml/datasets/Iris "UCI") there are a number of aspects to be highlighted by the reserach undertaken by Fisher. This extends to features such as characteristics, instances and attributes. It is in this review that the claim of four attributes is to be found. This may be true for the areas of machine learning, upon reading from other sources of material, and for the purposes of this research, based on observing the data, there are actually five. This is the case according to the dataset review by [Arshid Aslam Baba](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "Arshid Aslam Baba"). This fifth attribute is the Iris genus, the collection of all Iris sub-species. Below is a high-level view of this information.

|Characteristics| Instances| Attributes|
|---------------|----------|-----------|
| Multivariate  |    150   |     5     | 

According to the [UCI](http://archive.ics.uci.edu/ml/datasets/Iris "UCI"), the dataset itself is a multivariate dataset. In this context and with respect to data, multivariate analysis in datasets refers to the number of variables that are under examination. According to [ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis "ScienceDirect") it is the experimentation of multiple measurements on an experimental unit, for which the relationship between the units are important. This is the scientific component within the name of the paper, where multiple measurements are explicitly referenced.

In terms of the Taxonomy, this is of importance as Fisher was experimenting on data in relation to the Iris. The Iris, as stated previously is the genus, or collective term for similar plants, for this colllective. More specifically the sub sections, or Species, are the Setosa, Virginica and Versicolor. This will be dealt with in the later stages of this analysis.

The five attributes, or variables, highlighted on the site Kaggle by [Arshid Aslam Baba](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "Arshid Aslam Baba") are detailed in the list below. The first four attributes are the measurements taken from the 150 instances recorded, with the fifth being the class of Iris.

These are listed as: 
 - Sepal Length
 - Sepal Width
 - Petal Length
 - Petal Width
 - Classs (Species)

Sepal, by way of distinction to a petal, is the outermost part of the Iris flower according to [Biology Dictionary](https://biologydictionary.net/sepal/ "Biology Dictionary"). These are important attributes to focus on, as they allow for a clear pattern for distinguishing between the different types of Iris. The variances of size as detailed by Fisher too, will show a distinguishing trend between the sepal and petal.

Fisher sought to apply this discipline to taxonomy by way of measuring the difference in Iris Flowers. Approaching it with his background in mathematics, his work also harnassed the concept of "linear functions of the measurements by which the populations are best discriminate" as deatiled in [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library").

Taxonomy, according to [Merriam-Webster](https://www.merriam-webster.com/dictionary/taxonomy "Merriam-Webster") is the "general principles of scientific classification" as they apply to flowers. We can see that this is the highest point at which the two disciplines are merging, mathematical concepts and the classification of flowers. 

### Praise for the Literature

To fully appreciate the paper, there is a requirement to have an understanding for the reoccuring language within it. In this case, in relation to the terms  'species' and 'genus'. Genus is the collective term for similar plants, according to the [National Gardening Association](https://garden.org/courseweb/course1/week3/page3.htm "NGA"). The term species, can only refer to the name of the specific plant within the genus per the same source. 

The measurements taken by Dr. Anderson and subsequently analysed by Fisher, within this dataset are unambiguous and are distinctive to each species and the elements of its composition. This transparancy is so crucial as it allows for less and less scrutiny of the datas validity.

From a mathematical perspective, there is a logical sequence of events that Fisher has portrayed in the linear dimensions and how they are structuerd. That there are four different measurements, each with their own place in the formula is a positive movement as it caters for each of the attributes of Sepal Length & Width, as well as Petal Length & Width. 

Because of the ananlysis that Fisher performed, according to [Towards Science](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 "Towards Science"), the discriminant function was successful in performing its function. That is, to successfully distinguish between the three species.

One of the greaest pieces of praise that can be said of this paper is its longevity and adaptability to new areas of study, which will be spoken about in greater detail later on in the scetion titled "The Iris Dataset in modern literature". 

### Criticism of the literature

As mentioned previously in this analysis, there are three specific species that have been detailed in the collection. However, as detailed under the 'Arithmetical Procedure' there are only two of the three that have been acknowledged. According to the 'Arithmetical Procedure' section of the paper, there were only two species taken from the Iris. These were the Iris Setosa and the Iris Versicolor. This has been done without any mention of the Iris Virginica whatsoever, despite it being detailed in the abstract of this widely cited paper.

Without any mention of this third species, the Iris Viriginica, it is detailed as a piece of information in a table under 'Arithmetical Procedure'section. This was a confusing element to stumble across as there is no mention of it until we read the table. ONce this table ends, the Iris Virginica is dropped again from the mathematical analysis in Table 2 "Observed means for two species and their difference (cm)". 

Furthermore, there is no mention of why there is a third species as part of this paper until we reach a much later stage of the paper. This is only done once all mathematic foundations are in place. That there is no mention of the Iris Virginica outside of this table, serves the paper poorly in my opinion. There is no purpose or intended relevance to be garnered. There is also no apparent significance attached to the rationale provided by the author as to its ommission. 

It is at the point, in the 'Applications to the theory of Allopolyploidy' that we discover that the first two species were measured within the same natural colony. We discover that the third was taken from somewhere else by Dr. Anderson. There has been a significant amount of mathematical preparation and calculation completed before this detail is revealed. Fisher does address this issue, eventually, with an acknowledgement of stating that it may 'disturb the mean and their variabilities' as per [Wiley Online Library](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). To me, this is not a minor oversight as it introduces an opaque view of the experimentation. 

In relation to the layout of the mathematical components, there are some concerns too. These layout peculiarities are quite conflicting and feel overlooked from the perspective of Fisher. He states "For reasons to be discussed later we shall estimate the variance of a single plant by dividing 1085.5522 by 95", retrieved from [Wiley Online Library](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). This, I feel is neither a benefit to the reader, or a point that guides us to the material for review at a later point.

### The Iris Dataset in modern literature

If you type 'Iris Dataset analysis' into a web browser, and scrape through enough of the sites returned, a common theme to be returned is in the area of Machine Learning. Machine Learning, according to [Expert System](https://expertsystem.com/machine-learning-definition/ "Expert System") is an application of artificial intelligence, by which systems learn from all experience that is stored in data, regardless of the format, without being explicitly being told to do so. According to [MIT](https://www.technologyreview.com/2018/11/17/103781/what-is-machine-learning-we-drew-you-another-flowchart/ "MIT") it is this development of machine learning algorithms that is powering the development behind the likes of Twitter, YouTube and Facebook. 

The Iris Dataset, has been used with the Support Vector Machine (SVM) by Ritvik Raj, in order to extract greater meaning. According to [Ritvik Raj](https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/ "Ritvik Raj") to test against the algorithm to extract value and makes for a fascinating read in his area of study. 

Having discovered that the SVM model was the most accurate within his experimentation Raj ran it against the test dataset using the following code: 

        knn = KNeighborsClassifier()
        knn.fit(X_train, Y_train)
        predictions = knn.predict(X_validation)
        print(accuracy_score(Y_validation, predictions))
        print(confusion_matrix(Y_validation, predictions))
        print(classification_report(Y_validation, predictions))

This produced an accuracy result of 91%, whilst a confusion matrix using the sklearn library highlights that there are areas that can be worked on to further improve the accuracy.

In the area of machine learning, there is a model known as Gradient Boosting. Gradient boosting is used in the classification of data, according to [Cindy Wang](https://blogs.sas.com/content/sgf/2018/03/29/play-with-classification-of-iris-data-using-gradient-boosting/ "Cindy Wang"). Wang provides an introductory overview of visual data mining as well as a machine learning product being utiliised, whilst leveraging Fisher's dataset to show its capability. Within this report there is no code shared, but visuals of the output can be viewed.

The dataset has also successfully been used in the area of neural networking. Neural Networking as defined by [Pathmind](https://pathmind.com/wiki/neural-network#define "Pathmind") is an algorithm that is mapped however loosely on the brain. The purpose of neural networking is to develop and recognize patterns. It is also used to cluster and aid with the classification process, per the same source. We can see that the Fisher Dataset has been used in this area based on the work of [David Joy](https://www.kaggle.com/azzion/iris-data-set-classification-using-neural-network/execution "David Joy") and the scripts that he has posted to [Kaggle](https://www.kaggle.com/ "Kaggle"). 

Below we can see a snippet of the code extracted from the script:

        tf.reset_default_graph()
        (n_x, m) = X_train_flatten.shape       # shape of X                    
        n_y = Y_train_flatten.shape[0]         # shape of Y
        X, Y = create_placeholders(n_x,n_y)    # creating placeholder 
        tf.set_random_seed(42)

This code is being used to display the value for the five attributes in the dataset. Where we see the "X_train_flatten.shape", this represents the Sepal Length & Width, as well as the Petal Length & Width. In relation to the "Y_train_flatten.shape", this is the representation of the Species.


## Analysis of the data from Python

**Overview of the Dataset**
![Overview of the dataset](Images-from-Analysis/Describe.PNG)

The information above has been extracted from the iris dataset. There are four variables that are to be analysed, namely "Sepal Length", "Sepal Width", "Petal Length", "Petal Width". 
        
        c = IrisData.describe

We can see that there is a considerable difference in the mean between the Sepal Length and the Petal Length. This logically stands to reason, as previously mentioned, the Sepal is the outer cover of the plant, so it would cover more surface area. 

**Species in the Dataset**

![Seperating the Iris by Species](Images-from-Analysis/Species.PNG)

One of the most important aspects of the data, is that it is comprised of the Iris Genus. This is the collective term used when there are similar flowers in a set. The image above is an extraction of the individual species. to demonstrate how far we have come from the collection of this data, we need to remmember that Fisher himself acknowledged the difficulty in being able to accurately capture the differences within the Iris genus. With this in mind, we ahve been able to extract the types of the species.
To extract the information from the data, we run the following code:

        d = (IrisData.groupby('species').size())

 
**Comparison of the three Sepal Lengths**
![Sepal Length comparison between the three Iris Types](Images-from-Analysis/SepalLength.png)

As we can see in the image above, there is a considerable difference in the distribution in three tyes of species in relation to the sepal length. We can see that the greatest delta is between the Setosa and the Virginica, with the span of the Setosa box being more narrow than that of the Virginica. It's an important reminder to be conscience of that the Sepal is the outer leaf on the Iris plant. One can determine that the size of the length of the Virginica in comparison to the Setosa is considerably larger.

**Comparison of the three Sepal Widths**
![Sepal Width comparison between the three Iris Types](Images-from-Analysis/SepalWidth.png)

It is clear to see that there are a number of differences in relation to Sepal Width, with a role reversal to be seen between the Setosa and the Virginica. Based on the divisional line between the setosa, there is a majority of the instances captured where the width exceeds the average. One can determine that the size of the width of the Setosa in comparison to the Virginica is larger, in the context of its sepal.

**Comparison of the three Petal Lengths**
![Petal Length comparison between the three Iris Types](Images-from-Analysis/PetalLength.png)

In terms of what we can see in relation to the length of the petal the Virginica is considerably longer relative to both the Setosa and the Versicolor. The span of measurements for the Setosa is is very acute. There is not much in the difference across the 50 instances captured. The Iris versicolor, the third flower in the iris dataset, having been seperately captured, is closer still to the Iris Virgininca.   

**Comparison of the three Petal Widths**
![Sepal Width comparison between the three Iris Types](Images-from-Analysis/PetalWidth.png)

Finally, we have the comparison between the three different petal widths. The Virginica again has shown to be the widest, with also the widest span of measured petals across the 50 instances. The setosa being the least wide when determining the size of the petals. 

**Pairplot graph**
![All four attributes in a matrix](Images-from-Analysis/seaborn.png)

We can also see in the image above, which was created using the [Python Basics](https://pythonbasics.org/seaborn-pairplot/ "Seaborn Pairplot Examples"), the relationships that are possible between these attributes. It is marked out in a four by four matrix format with all the permutations of the four attributes. Where, in the grid, there is an overlpa of the attributes, i.e. a Petal Length versus Petal Length, we are shown a distribution of the values based on the species.

In order to create the above, we have used the following code:

        sns.pairplot(IrisData, hue="species")



Fisher, writing in the Section "The analogy of partial regression", speaks of the analysis of the variance on portions of each species accountable by linear regression. To put this in a graphical representation, we have the two following displays. 

**Lmplot graph**
![Sepal Length plotted against Sepal Width](Images-from-Analysis/LinearRegression.png)

As we can see from the image above, we have a simple plotting of the sepal length against the sepal width for all three species as called out in the legend. The graph very simply demonstrates the difference in the relationships between each sepacies and these components. This has been represented by a scatter plot of the data.  Within each species, we can see that there is a corresponding line that runs from bottom left to top right, within the structure of the data for its respective species. This is the linear regression line that attempts to plot the relationship beteen the two variables, as detailed on the x and y axes.

**Lmplot graph**
![Petal Length plotted against Petal Width](Images-from-Analysis/LinearRegression2.png)


In the same manner as the description above, there is a relationship between the petal length and the petal width for each of the three species. This has the same characterisitics as the image that came before it, except that the trajectory for the line demonstrating linear regression, will be different because of the recorded values being different. 

As detailed above, this is the code to be used to return the imagery.


        g = sns.lmplot(x="petal_length", y = "petal_width", hue = "species", height = 5, data=IrisData)


## Conclusion

It is probably the most important takeaway from the paper itself, that Fisher highlights the difficulty in seperating out the difference between the Iris Virginica and the Iris Versicolor. The inability to distinguish the two apart can not be based solely, he says, "on these four measurements of a single flower taken on a plant growing wild." [Fisher, 1936](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Fisher") . That Fisher himself has recorded this opinion in the paper is signiifcant.

One of the biggest takeaways from this dataset is its' ability to stand above scrutiny over such a period of time. The dataset has been adapted from a research into distinguishing species in the world of taxonomy, to being an important milestone in data clustering, as well Machine Learning amongst other areas of study.  

It is a testament to the quality of the research that more than eighty years later, the mathematical principles that Fisher recorded are still in use and being applied to new areas of research. 

## Runbook for Iris Python Code
According to the website [Stepshot](https://stepshot.net/how-to-create-a-runbook/ "Stepshot") there are some key callouts that needs to be adhered to when creating a runbook. Given the scale of our analysis, we may not need to hit on every marker, but nevertheless, we will try to provide as much structure as possible for readability purposes. 

 - Overview of Process
 - Required Software
 - Data Import Source
 - How to run the program from end to end. 

### Overview of the process

When undertaking analysis for the first time, it is important to note that there are documentations that can be scanned through if any difficulty is experiecned, such as"A Whirlwind Tour of Python" as retrieved [O'Reilly Publications](https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf "pdf of the material").  

### Required Software

There is a requirement to download and install the Anaconda package to your computer. you will need to have access to Visual Studio code or a programem similar to it to undetake the analysis. Once these installations have been completed, the user can then proceed to using the software. 

### Data Import Source

The source of the dataset is taken from the following website source, as hosted on Kaggle. 

[Arshid Aslam Baba](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "Arshid Aslam Baba") has a copy of the file containing the data within this link. This csv file will need to be read into the python programme.

### How to run the programme from end to end

#### Data Analysis on the Dataset

Import the following libraries to your python programme:

        import pandas
        import numpy as np
        import seaborn as sns
        import matplotlib.pyplot as plt

These libraries are required to perform the anlaysis form end to end.

To read the csv file, we apply the following code in place.

        IrisData = pd.read_csv('IRIS.csv')
        print(IrisData)
        
This will provide a simple text display to the terminal with each row and column displayed. 

We are required to produce a text file for the variables that are produced in our analysis, so we create a function that will append the data to the text file that we are calling 'Output.txt'.

        def AppendToFile(content):
        file = open("Output.txt", "a")
        file.write(content)
        file.close()

The analysis that we are pulling from the data will take two formats. The first will be in the traditional tabular format, the second will be in visual, thanks to some of the libraries that we have imported.
We are going to take extract an overview of the data and pull it into an array format, as well as a snapshot of the head and tail of the data. We are also going to extract an overview from a number of viewpoints, such as min, max, standard deviation, as well as a view of the data from each Species within the set. 


The following will return all values for each instance in an array format.
        
        print(IrisData.values)
        AppendToFile(str(IrisData.values))

This will provide a cursory glance at the material from the first 10 rows of data. Note too that the first line returned is called line 0. This is the case as the formatting allows the first piece of data to be in position 0.
        
        a = IrisData.head(10)
        print(a)
        AppendToFile(str(a))

This will provide a cursory glance at the material from the last 10 rows of data.
        
        b = IrisData.tail(10)
        print(b)
        AppendToFile(str(b))

This will print to the terminal the overall description of the dataset. We will see this information categorised as:

- Count
- Mean
- Standard Deviation
- Minimum Value
- value at 25% of sample
- value at 50% of sample
- value at 75% of sample
- Maximum Value
        
        c = IrisData.describe
        print(c())
        AppendToFile(str(c()))

This will allow us to view the individual names of each Iris flower.
        
        d = (IrisData.groupby('species').size())
        print(d)
        AppendToFile(str(d))

All of these lines are individally run and are then subsequently appended to our 'Output.txt' file.

#### Visualising the data

We are going to use some of the functionality that is part of the libraries that we have imported from matplotlib as well as the seaborn library. 
As we have seen in our analysis in the previous section of the text, there are some requirements for this project to be considered. From a visualisation perspective, we need to be able to run a histogram as well as a scatter plot.
The full work breakdown structure is detailed at the end of this file under the heading Project Management Overview. 

If we take the following code, this will allow us to see the first box plot of all three species based on sepal length
        
        df = sns.load_dataset('iris')
        sns.boxplot(x = df["species"], y = df["sepal_length"])
        plt.title('Comparison of the three Sepal Lengths')
        plt.xlabel('Difference in the Species')
        plt.ylabel('Sepal Length')
        plt.show()

This will allow us to see the first box plot of all three species based on sepal width

        df = sns.load_dataset('iris')
        sns.boxplot(x = df["species"], y = df["sepal_width"])
        plt.title('Comparison of the three Sepal Widths')
        plt.xlabel('Difference in the Species')
        plt.ylabel('Sepal Width')
        plt.show()

This will allow us to see the first box plot of all three species based on petal length

        df = sns.load_dataset('iris')
        sns.boxplot(x = df["species"], y = df["petal_length"])
        plt.title('Comparison of the three Petal Lengths')
        plt.xlabel('Difference in the Species')
        plt.ylabel('Petal Length')
        plt.show()

This will allow us to see the first box plot of all three species based on petal width
        
        df = sns.load_dataset('iris')
        sns.boxplot(x = df["species"], y = df["petal_width"])
        plt.title('Comparison of the three Petal Widths')
        plt.xlabel('Difference in the Species')
        plt.ylabel('Petal Width')
        plt.show()

The following code is in relation to the histogram requirements of the project.
We are going to the create a histogram relationship between our four attributes, the sepal length & width, as well as the petal length & width.

This as a code will print a histogram of the sepal length

        plt.figure(figsize = (6, 5)) 
        SepalLengthHist = IrisData["sepal_length"] 
        plt.hist(SepalLengthHist, bins = 20, color = "green") 
        plt.title("Sepal Length in cm") 
        plt.xlabel("Sepal_Length_cm") 
        plt.ylabel("Count")
        plt.savefig("SepalLengthHist.png") 
        # Please note that this line can be introdcued if there is a need to save each image created. It can be replicated across the remaining histograms.

This as a code will print a histogram of the sepal width

        plt.figure(figsize = (6, 5)) 
        SepalWidthHist = IrisData["sepal_width"] 
        plt.hist(SepalWidthHist, bins = 20, color = "blue") 
        plt.title("Sepal Width in cm") 
        plt.xlabel("Sepal_Width_cm") 
        plt.ylabel("Count")


This as a code will print a histogram of the petal width

        plt.figure(figsize = (6, 5)) 
        PetalWidthHist = IrisData["petal_width"] 
        plt.hist(PetalWidthHist, bins = 20, color = "red") 
        plt.title("Petal Width in cm") 
        plt.xlabel("Petal_Width_cm") 
        plt.ylabel("Count")
 

This as a code will print a histogram of the petal length

        plt.figure(figsize = (6, 5)) 
        PetalLengthHist = IrisData["petal_length"] 
        plt.hist(PetalLengthHist, bins = 20, color = "magenta") 
        plt.title("Petal Length in cm") 
        plt.xlabel("Petal_Length_cm") 
        plt.ylabel("Count")
 

The following code is in relation to the scatterplot requirements of the project.
We are going to display the attributes against one another, as well as display the permutations of these instances using the seaborn library.

This will return the sepal length versus sepal width graph.

        plt.scatter(IrisData["sepal_length"], IrisData["sepal_width"])
        plt.title("sepal length versus sepal width")
        plt.xlabel("sepal length")
        plt.ylabel("sepal width")
        plt.show()

This will return the Petal Length versus Petal width graph.

        plt.scatter(IrisData["petal_length"], IrisData["petal_width"])
        plt.title("petal length versus petal width")
        plt.xlabel("sepal length")
        plt.ylabel("sepal width")
        plt.show()

This will return a pairplot of all permutations in one graphic, as detailed in the ananlysis section of this project.

        sns.pairplot(IrisData, hue="species")
        plt.show()

To demonstrate some of the linear functions in the dateset, leveraging the functionality of seaborn. 

        sns.set()
        g = sns.lmplot(x="sepal_length", y = "sepal_width", hue = "species", height = 5, data=IrisData)
        # pairing sepal length against its width, for all species.
        g.set_axis_labels("Sepal length (mm)", "Sepal width (mm)")
        plt.show()

        sns.set()
        g = sns.lmplot(x="petal_length", y = "petal_width", hue = "species", height = 5, data=IrisData)
        # pairing sepal length against its width, for all species.
        g.set_axis_labels("Petal length (mm)", "Petal width (mm)")
        plt.show()

These will produce very clear and concise visuals of the dataset, as we macth up the sepal length against sepal width, as well as petal length and petal width. These linear regression models were created based from research of the code detailed on the [Seaborn Library](https://seaborn.pydata.org/examples/multiple_regression.html "Seaborn")

This concludes the runbook.


## Bibliography

For a full list of the refernces, please see below as well as the Project2020Bibliography.txt file, where the structure aligns to the APA styleguide.
Failing that, there is a word document version that is available to view in the repository.  



#### Markdown Research:

Article Title: Getting Started. An overview of MarkDown, how it works, and what you can do with it. 
Website Title: www.markdown.org
URL          : https://www.markdownguide.org/getting-started/

Article Title: Mastering Markdown
Website Title: www.guides.github.com
URL          : https://guides.github.com/features/mastering-markdown/

Article Title: How to write a readme.md file? 
Website Title: www.medum.com
URL          : https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f

Article Title: Markdown:Syntax 
Website Title: www.daringfireball.com
URL          : https://daringfireball.net/projects/markdown/syntax#overview

Article Title: Basic Syntax
Website Title: https://www.markdownguide.org
URL          : https://www.markdownguide.org/basic-syntax/

#### Fishers Dataset: 

Article Title: Iris Flower Dataset used for multi-class classification
Website Title: www.Kaggle.com
URL          : https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv


Article Title: The use of multiple measurements in Taxonomic Problems 
Website Title: https://onlinelibrary.wiley.com
URL          : https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x

Article Title: Taxonomy
Website Title: https://www.merriam-webster.com
URL          : https://www.merriam-webster.com/dictionary/taxonomy

Article Title: Sir Ronald Aylmer Fisher - British Geneticist And Statistician
Website Title: https://www.britannica.com
URL          : https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Article Title: Multivariate Analysis
Website Title: https://www.sciencedirect.com
URL          : https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis

Article Title: The Iris Dataset -  A Little Bit of History and Biology
Website Title: https://towardsdatascience.com
URL          : https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5

Article Title: Iris Data Set
Website Title: http://archive.ics.uci.edu
URL          : http://archive.ics.uci.edu/ml/datasets/Iris

Article Title: Sepal Definition
Website Title: https://biologydictionary.net
URL          : https://biologydictionary.net/sepal/

Article Title: National Gardening Association
Website Title: https://garden.org
URL          : https://garden.org/courseweb/course1/week3/page3.htm

#### Applications to Modern Literature: 

Article Title: Iris Dataset Analysis (Python)
Website Title: https://rajritvikblog.wordpress.com
URL          : https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/

Article Title: Play with classification of Iris data using gradient boosting
Website Title: https://blogs.sas.com
URL          : https://blogs.sas.com/content/sgf/2018/03/29/play-with-classification-of-iris-data-using-gradient-boosting/

Article Title: Iris Data Set Classification using Neural Network
Website Title: https://www.kaggle.com
URL          : https://www.kaggle.com/azzion/iris-data-set-classification-using-neural-network/execution

Article Title: Kaggle 
Website Title: https://www.kaggle.com/ 
URL          : https://www.kaggle.com/

Article Title: What is Machine Learning?
Website Title: https://www.technologyreview.com
URL          : https://www.technologyreview.com/2018/11/17/103781/what-is-machine-learning-we-drew-you-another-flowchart/

Article Title: A Beginner's Guide to Neural Networks and Deep Learning
Website Title: https://pathmind.com
URL          : https://pathmind.com/wiki/neural-network#define

Article Title: What is machine learning? a definition
Website Title: https://expertsystem.com/
URL          : https://expertsystem.com/machine-learning-definition/


#### Analysis of the data from Python:

Article Title: Boxplot Demo
Website Title: https://matplotlib.org/
URL          : https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py

Article Title: Seaborn plots not showing up
Website Title: https://stackoverflow.com
URL          : https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up

Article Title: Multiple Linear Regression
Website Title: https://seaborn.pydata.org/
URL          : https://seaborn.pydata.org/examples/multiple_regression.html

Article Title: Project 2018 Iris
Website Title: https://github.com/
URL          : https://github.com/RitRa/Project2018-iris/blob/master/README.md

Article Title: Fishers Iris Data set
Website Title: https://github.com/
URL          : https://github.com/deniscarr/Fishers-Iris-dataset-project/blob/master/README.txt

Article Title: Basic Analysis of the Iris Data set Using Python
Website Title: https://medium.com/
URL          : https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342

Article Title: 3.1. Statistics in Python
Website Title: http://scipy-lectures.org/
URL          : http://scipy-lectures.org/packages/statistics/index.html

Article Title: Seaborn Plots not showing up
Website Title: https://stackoverflow.com
URL          : https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up

Article Title: Boxplot demo
Website Title: https://matplotlib.org/
URL          : https://matplotlib.org/3.1.1/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py

Article Title: Python Histogram Plotting: NumPy, Matplotlib, Pandas & Seaborn
Website Title: https://realpython.com
URL          : https://realpython.com/python-histograms/


#### Skills / Knowledge Gap:

Article Title: Managing your work on GitHub
Website Title: https://help.github.com
URL          : https://help.github.com/en/github/managing-your-work-on-github

Article Title: How to Create a Runbook that Rocks? Automatically is the Best Way
Website Title: https://stepshot.net
URL          : https://stepshot.net/how-to-create-a-runbook/

Article Title: Fishers Iris Data Set Project
Website Title: https://github.com/
URL          : https://github.com/deniscarr/Fishers-Iris-dataset-project/blob/master/README.txt


#### Runbook Material / Support Documentation:

Article Title: A Whirlwind Tour of Python
Website Title: www.oreilly.com
URL          : https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf


### Project Management Overview.txt
This will act as a log of the project from commencement to cessation. The intent with this project will be to review the problem set and to detail a work breakdown structure. Within each breakdown, there is going to be smaller units of activity that need to be completed, and at this stage they will be shown in the structure of:
        
        Section 'X'
                Activity '1'
                        Task '1.1'
                                Sub-Task '1.1.1'

This is the intended approach of the project, but it will be reviesed on an iterative basis as the project develops. There will be updates communicated via the commit command when work is being saved to the repository. The first breakdown will be in relation to the problem set that has been detailed on the GMIT Site. For a copy of this brief, there is a pdf copy available in this repository for review. This document is intended as a complimentary document to the expected outcomes of the project. On reading the information that is contained in the project there are a number of areas that need to be reviewed. 

The status of completed will only be detailed once the sub-task or other nested activities are completed within the rolled up view.

Project Breakdown:

        Section A) Fishers Data Set
                1) Find a dataset that contains the original clean copy of the dataset. - completed
                        1.1) Dataset has been found - completed
                        1.2) Test to read in csv file - completed
                        1.3) Analysis - completed
                                1.3.1) reference to Section B Task 6 - completed
                2) Perform a research of the dataset and why it is under analysis - completed
                        2.1) review of fisher biography - completed
                        2.2) review of the paper and its conclusions - completed
                        2.3) praise for the set - completed
                        2.4) criticism of the set - completed
                        2.5) Conclusion of the paper with analysis - completed
                        2.6) its link to the data analysis performed today. - completed
                
        Section B) Expected Output:
                4) Research from the information about Fishers dataset are to be commited to the READ.md file - completed.
                        4.1) This file in its entirety will need to be added into the read.md file, upon completion of project and before communicating the git hub repository url. - completed
                5) Download the data - completed
                        5.1) Add it to the repository - completed
                                5.1.1) Reference to Section A - 1). - completed
                6) Write an analysis called analysis.py, which contains:
                        6.1) Output of each variable to a single text file - completed
                        6.2) Saves a histogram of each variable of png file type - completed
                        6.3) Outputs a scatter plot of each pair of variables.- completed
                        6.4) Prepare all of the above as if were to be presented - completed
                                6.4.1) To be contained in the git hub repository, specifically in relation to the code. - completed 

        Section C) Minimum Acceptance standards breakdown per file to be submitted:
                7) README
                        7.1) Summary of the dataset as well as the investigations into it. - completed
                        7.2) Runbook of how to run the code from start to finish. - completed
                                7.2.1) Full list of the library that has been used to be added into the runbook. - completed
                                7.2.2) Data Import - completed
                                7.2.3) How to run the programme from start to finish -completed 
                        7.3) Fill list of references for all sources for all aspects of the project. - completed
                                7.3.1) to ensure cmpliance, bibliography in txt, md as well as docx file added. - completed
                8) Python Script - completed
                9) Summary Text File - completed

        Section D) Skills / Knowledge Gap:
                10) Overview of git and how to structure a project file / folder -  completed
                11) Review of the standards and principles that are considered best practise for a markdown file - completed. 
                        11.1) Review of the pseudo styling as spoken about it in the video. - completed
                        11.2) Open up the read.md file in a text editor and test to see how changes in the indentation will look once the y have been pused to github repository. - completed
                12) Need to review how to display pdf in VS Code or remove file. - completed
                13) What is a high level overview of a runbok for running the code aspect of the analysis. - completed
                14) Referencing of the information to be structured - completed
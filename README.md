# An Analysis of Fishers Iris Data set

## Ronald Fisher & his Iris data set

According to the [Encyclopaedia Brittanica](https://www.britannica.com/biography/Ronald-Aylmer-Fisher "Encyclopaedia Brittanica") Sir Ronald Fisher was a British statistician,  commonly known for his development of statistical procedures. Fisher graduated from Cambridge in 1912, being awarded a B.A. in astronomy, which amongst other aspects, focused on the mathematical components of the discipline.


In 1936, he published, the work that we are analysing in this poject entitled "The use of multiple measurements in taxonomic problems", retrieved from [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library").

 However, it was only upon reading the paper and researching it further that it had become clear that the data set is sometimes refered to as the Ansderson data set. According to Fisher himserlf, [Wiley Online Library]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library") Dr. Anderson is the man who performed all of the recording of the measurements on the Iris species. It was Fisher who performed the analysis on these individual instances.


Before undertaking any detailed primary or secondary analysis,there are some high level observations that can be taken from the material ahead of time. 

According to the [UCI](http://archive.ics.uci.edu/ml/datasets/Iris "UCI") there are a number of aspects to be highlighted by the reserach undertaken by Fisher, such as characteristics, instances and attributes. It is in this review that the claim of four attributes is to be found. From reading other material and for the purposes of this research, based on observing the date, there are actually five. This is also the case according to the data set review by [MathNerd](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "MathNerd"). This fifth attribute is the Iris genus, the collection of all Iris sub-species. Below is a table of a very high level view of this information.

|Characteristics| Instances| Attributes|
|---------------|----------|-----------|
| Multivariate  |    150   |     5     | 

According to UCI, the data set itself is a multivariate data set.I this context and with respect to data, multivariate analysis in data sets refers to the number of variables that are under examination. According to [ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis "ScienceDirect") it is the experimentation of multiple measurements on an experimental unit, for which the relationship between the units are important. This is the scientific component to the name of the paper, where multiple meaasurements are explicitly referenced.

In terms of the Taxonomy, this is of importnace as Fisher was experimenting on data, where there the Iris is the colllective, and specific sub sect of this is the Setosa, Virginica and Versicolor. This will be dealt with in the later stages of this analysis.

The five attributes highlighted on the site Kaggle by[MathNerd](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "MathNerd"). The first four attributes are the measurements taken from the 150 instances recorded, with the fifth being the type of Iris.

These are listed as: 
 - Sepal Length
 - Sepal Width
 - Petal Length
 - Petal Width
 - Classs (Species)

Sepal, by way of distinction to a petal, is the outermost part of the Iris flower according [Biology Dictionary](https://biologydictionary.net/sepal/ "Biology Dictionary"). This is important attriubtes to focus on, as they allow for a clear pattern for distinguishing between the different types of Iris. The variances of size as detailed by Fisher too, will show a distinguishing trend between the sepal and petal.

Fisher declared that he had taken inspiration from research of the anatomy and physiology. This inlcuded reviews of the developement of the mandible (lower jaw) by Mr. E. Smith as well as the cranial measurements compiledby Mildred Barnard. 


Fisher sought to apply this discipline to taxonomy [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library") by way of measuring the difference in Iris Flowers. Approaching it with his background in mathematics, his work also harnassed the concept of "linear funcitons of the measurements by which the populations are best discriminate". 

Taxonomy, according to [Merriam-Webster](https://www.merriam-webster.com/dictionary/taxonomy "Merriam-Webster") is the "general principles of scientific classification" as they apply to flowers. We can see that this is the highest point at which the two disciplines are merging, mathematical concepts and the classification of flowers. 

## Praise for the Literature

### An Overview to the Iris Data Set
To fully appreciate the paper, there is a requirement have an understanding for the reoccuring language within the paper, namely 'specied'and 'genus'.
According to the National Gardening Association, the term species, can only refer to the name of the specific plant within the genus. Genus is the collective term for similar plants, according to the [National Gardening Association](https://garden.org/courseweb/course1/week3/page3.htm "NGA")

The measurements taken by Anderson and subsequently analysed by Fisher, within this dataset are unambiguous and are distinctive to each species. This unambiguous factor is so crucial as it allows for less and less scrutiny of the data.

From a mathematical perspective, there is a logical sequence of events that Fisher has portrayed in the linear dimensions and how they are structuerd formulically. That there are four different measurements, each with their own place in the formula is a positive movement as it caters for each of the attributes of Speal Length & Width, as well as Petal Length & Width. 

According to the 'Arithmetical Procedure' aspect of the paper, there were only two species taken from the first set of Iris, that is the Iris Setosa and the Iris Versicolor.
The third Iris, is not taken from the same colony, the scope of the research appears to be focused on the first 100 instances before widening the lens to include the versicolor.

Because of the ananlysis that Fisher performed, according to [Towards Science](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5 "Towards Science"), the discriminant funciton was successful in performing its function. That is, successfully distinguish between the three species.

## Criticism of the literature

### An overview to the Iris Data set
As mentioned previously in this analysis, from the outset that there are two specific species that have been collected, as detailed under the 'Arithmetical Procedure'. Without any mention of the third species, we are now introduced to a variation in the genus, the Iris Viriginica. This can be quite a confusing element to stumble across as there is no mention of it until we read the table.

Furthermore, there is no mention of why there is a third species as part of this paper until we reach a much later stage of the paper. This is only done once all mathematic foundations are in place. That there is no mention of the Iris Virginica outside of this table, serves the paper, with no purpose or intended relevance to be seen. There is also no rationale provided by the author as to its ommission. 


It is at this point, in the 'Applications to the theory of Allopolyploidy' that we discover that the first two species were measured within the same natural colony, and the third was taken from somewhere else by the Dr Anderson. 

There has been a significant amount of mathematical preparation and calculation been completed before this reveal. 

Fisher does address this issue, eventually, with an acknowledgement of stating that it may 'disturb the mean and their variabilities' [Wiley Online Library]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). 

### Issues with the Mathematical Structure

There are some concerns, however, to the lay reader, such as me, that are quite conflicitng and overlooked.

Fisher states "For reasons to be discussed later we shall estimate the variance of a single plant by dividing 1085.5522 by 95", from [Wiley Online Library]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). This I feel is neither a benefit to the reader, or a point that is clearly referecend at a later date. If a reader of this paper does not have a basic understanding of the mathematics, it adds unnecessary confusion where it is not required.



## Conclusion

It is probably the most important takeaway from the paper itself, that Fisher highlights the difficulty in seperating out the difference between the Iris Virginica and the Iris Versicolor. The inability to distnguish the two apart can not be based solely, he says, "on these four measurements of a single flower taken on a plant growing wild." [Fisher, 1936]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Fisher") . That fisher himself has recorded this opinion in the paper is signiifcant.

One of the my biggest takeaways from this data set is its ability to stand above scrutiny over such a period of time. THe data set has adapted from a research into distinguishing species in the world of taxonomy, to being an important milestone in data clustering, as well Machine Learning. 

It is a testament to the quality of the research that more than eighty years later, the mathematical principles that Fisher recorded are still in use and being applied to new areas of research. 

### How has the Iris Data Set been adapted to modern literature

Upon  starting this research into the Fisher Iris Data Set, one of the common links to be returned was in the area of Machine Learning. Machine Learning, according to [MIT](https://www.technologyreview.com/2018/11/17/103781/what-is-machine-learning-we-drew-you-another-flowchart/ "MIT") is the process of taking data as well as machine learned algorithms and using the two of them together to find and apply patterns in the data. 

The Iris Data Set, has been used with the Support Vector Machine by Ritvik Raj, in order to extract meaning. According to [Ritvik Raj](https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/ "Ritvik Raj") to test against the algorithm to extract value and makes for fascinating read in this area of study.

In the area of machine learnign, there is a model known as Gradient Boosting. it is used in teh classfification of data, according to [Cindy Wang](https://blogs.sas.com/content/sgf/2018/03/29/play-with-classification-of-iris-data-using-gradient-boosting/ "Cindy Wang") on the SAS blog forum. It is, according to Wang, a introductory overview of visual data mining as well as maine learning product being leveraged, whilst using Fisher's data set to show its capability.

The data set has also successfully been used in the area of neural networking. Neural Networking as defined by [Pathmind](https://pathmind.com/wiki/neural-network#define "Pathmind") is an algorithm that is mapped, however loosely on the brain. The purpose of neeural networking to develop and recognize patterns. It is alos used to cluster and aid with the classification, per the same source. We can see that the Fisher Data Set has been used in this area based on the work of [David Joy](https://www.kaggle.com/azzion/iris-data-set-classification-using-neural-network/execution "David Joy") and the scripts that he has posted to [Kaggle](https://www.kaggle.com/ "Kaggle").


## Further research to be conducted
distinguishable on te non linear branching component
linear discriminant model - needs to be reviewed.
cluster analysis
pivot to machine learning 



# Runbook for Iris Python Code
According to the website [Stepshot](https://stepshot.net/how-to-create-a-runbook/ "Stepshot") there are some key callouts that needs to be adhered to when creating a runbook. Given the scale of our analysis, we may need to hit on every marker, but nevertheless, we will try to provide as much structure as possible for readability purposes. 

 - Overview of Process
 - Software to be downloaded / required
 - Data Import Source
 - How to run the program from end to end. 




# Bibliography

## **Markdown Research**:

Rview of how to format a markdown file: https://www.markdownguide.org/getting-started/

Markdown Syntax: https://guides.github.com/features/mastering-markdown/

Information on the relationship between markdown and visual studio code: https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f

Primary SUpport link: https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f


Further syntax information: https://daringfireball.net/projects/markdown/syntax#overview
further information link: https://guides.github.com/features/mastering-markdown/


## **Fishers DataSet**: 

I retrieved the link for my data set from [Kaggle](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "Kaggle")


Kaggle data set file location : https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv
Wiley Online Library: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x

taxonomy definiton https://www.merriam-webster.com/dictionary/taxonomy

Biography of Fisher: https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Multivariate explanation https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis

Review of the Iris Data Set https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5


## Applications to wider ##

SVM Analysis - https://rajritvikblog.wordpress.com/2017/06/29/iris-dataset-analysis-python/
SAS - https://blogs.sas.com/content/sgf/2018/03/29/play-with-classification-of-iris-data-using-gradient-boosting/
David JOy - https://www.kaggle.com/azzion/iris-data-set-classification-using-neural-network/execution
Kaggle -m https://www.kaggle.com/


## **Skills / Knowledge Gap**

As reference material for how to structure a project for use in git, i have utilised teh following documentaiton : 
https://help.github.com/en/github/managing-your-work-on-github

Performing a Runbook checklist https://stepshot.net/how-to-create-a-runbook/



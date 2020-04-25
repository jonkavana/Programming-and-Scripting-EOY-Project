The aim of this project is to provide an analytical oversight of Fisher's Iris data set

# Analysis of Fishers Iris Data set

## Overview of the Paper and its author

According to the [Encyclopaedia Brittanica](https://www.britannica.com/biography/Ronald-Aylmer-Fisher "Encyclopaedia Brittanica") Sir Ronald Fisher was a British statistician, most commonly known for his development of statistical procedures. Fisher graduated from Cambridge in 1912, being awarded a B.A. in astronomy, which amongst other aspeccts, focused on the mathematical components of the discipline.


In 1936, he published, what would become one of his most cited works, entitled "The use of multiple measurements in taxonomic problems", retrieved from [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). 


Before undertaking any detailed primary or secondary analysis,there are some high level observations that can be taken from the material ahead of time. 

According to the website [UCI](http://archive.ics.uci.edu/ml/datasets/Iris "UCI") there are a number of aspects highlighted by the reserach undertaken by Fisher, suhc as characteristics, instances and attributes. It is in the review that the claim of four attributes are to be found, but for the purposes of this research, based on observing the date, there are five. This is also the case according to the data set review by [MathNerd](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "MathNerd)).

|Characteristics| Instances| Attributes|
|---------------|----------|-----------|
| Multivariate  |    150   |     5     | 

According to UCI, the data set itself is a multivariate data set. Multivariate analysis in data sets refers to the number of variables that are under examination. According to [ScienceDirect](https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis "ScienceDirect") it is the experimentation of multiple measurements on an experimental unit, for which the relationship between the units are important. This is of importnace as Fisher was experimenting on data, where there the Iris is the colllective, and specific sub sect of this is the Setosa, Virginica and Versicolor. This will be dealt with in the later stages of this analysis.

There are also four attributes highlighted by site. The four attributes are the measurements taken from the 150 instances recorded. These are listed as: 
 - Sepal Length
 - Sepal Width
 - Petal Length
 - Petal Width
 - Classs (Species)

Sepal, by way of distinction to a petal, is the outermost part of the Iris flower. Whereas in the structure of the Iris, the petal is to be found inside the flower, according [Biology Dictionary](https://biologydictionary.net/sepal/ "Biology Dictionary"). These are important attriubtes to focus on, as they allow for a clear pattern for distinguishing between the different types of Iris.

Fisher took inspiration from research of the anatomy and physiology. This inlcued reviews of the developement of the mandible (lower jaw) by Mr. E. Smith as well as the cranial measurement by Mildred Barnard. 


Fisher sought to apply this concept to taxonomy [Wiley Online Library](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library") by way of measuring teh difference in Iris Flowers. Approaching it with his background in mathematics in focus, his work also harnassed the concept of "linear funcitons of the measurements by which the populations are best discriminate". 

Taxonomy, according to [Merriam-Webster](https://www.merriam-webster.com/dictionary/taxonomy "Merriam-Webster") is the "general principles of scientific classification" as they apply to flowers. We can see that this is the highest point at which the two disciplines are merging, mathematical concepts and the classification of flowers. 

## Praise for the Literature

### An Introduction to the Iris Data Set
According to the National Gardening Association, the term species, only refers to the name of the specific plant within the genus. Genus is the collective term for similar plants, according to the [National Gardening Association](https://garden.org/courseweb/course1/week3/page3.htm "NGA")

To this point, the measurements that have been taken within for ths dataset are unambiguous and are distinctive to each species. From the outset there are two specific callouts of the Iris Setosa and the Iris versicolor. 

From a mathematical perspective, there is a logical sequence of events that Fisher has portrayed in the linear dimensions and how they are structuerd formulically. That there are four different measurements, each with their own place in the formula. 

According to the 'Arithmetical Procedure' aspect of the paper, there were only two species taken from the first set of Iris, that is the Iris Setosa and the Iris Versicolor.
The third Iris, is not taken from the same colony, the scope of the research appears to be focused on the first 100 instances before widening the lens to include the versicolor.

## Criticism of the literature

### Introduciton to the Iris FLower
As mentioned previously in this analysis, Fisher has mentioned from the outset that there are two specific species that have been collected, as detailed under the 'Arithmetical Procedure'. Without any mention of the third species, we are now introduced to a variation in the genus, the Iris Viriginica. This can be quite a confusing element to stumble across as there is no mentino of it until we read the table. 

Furthermore, there is no mention of why there is a third species as part of this paper until we reach a mcuh later stage of the paper, when all mathematic foundation is in place. That there is no mention of the Iris Virginica outside of this table, it is poorly served, with no purpose or intended relevance to be seen.


It is at this point, in the 'Applications to the theory of Allopolyploidy' that we discover that the first two species were measured within the same natural colony, and the third was taken from somewhere else. 

Fisher does address this issue with an acknowledgement of stating that it may 'disturb the mean and their variabilities' [Wiley Online Library]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Wiley Online Library"). 

### Issues with the Mathematical Structure

There are some concerns however, to the lay reader, such as me, that are quite conflicitng and overlooked. Fisher states "For reasons to be discussed later we shall estimate the variance of a single plant by dividing 1085.5522 by 95", which is neither a benefit to the reader, or a point that is clearly referecend at a later date. If a reader of this paper does not have a basic understanding of third level mathematics, it would quite a confusing paper, in my opinon.



## Conclusion

It is probably the most important takeaway from the paper itself, that Fisher highlights the difficulty in seperating out the difference between the Iris Virginica and the Iris Versicolor. The inability to distnguish the two apart can not be based solely, he says, "on these four measurements of a single flower taken on a plant growing wild." [Fisher, 1936]( https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Fisher") .


## How has the Iris Data Set been adapted to modern literature

distinguishable on te non linear branching component
linear discriminant model - needs to be reviewed.
cluster analysis
pivot to machine learning 

I retrieved the link for my data set from [Kaggle](https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv "Kaggle")


As part of this project we are seeking to understand and appreciate what is that researchers are drawn to this data set






# Runbook for Iris Python Code



# Bibliography

## **Markdown Research**:

Rview of how to format a markdown file: https://www.markdownguide.org/getting-started/

Markdown Syntax: https://guides.github.com/features/mastering-markdown/

Information on the relationship between markdown and visual studio code: https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f

Primary SUpport link: https://medium.com/@saumya.ranjan/how-to-write-a-readme-md-file-markdown-file-20cb7cbcd6f


Further syntax information: https://daringfireball.net/projects/markdown/syntax#overview
further information link: https://guides.github.com/features/mastering-markdown/


## **Fishers DataSet**: 

Kaggle data set file location : https://www.kaggle.com/arshid/iris-flower-dataset#IRIS.csv
Wiley Online Library: https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1469-1809.1936.tb02137.x

taxonomy definiton https://www.merriam-webster.com/dictionary/taxonomy

Biography of Fisher: https://www.britannica.com/biography/Ronald-Aylmer-Fisher

Multivariate explanation https://www.sciencedirect.com/topics/medicine-and-dentistry/multivariate-analysis

## **Skills / Knowledge Gap**

As reference material for how to structure a project for use in git, i have utilised teh following documentaiton : 
https://help.github.com/en/github/managing-your-work-on-github


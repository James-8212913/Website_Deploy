title: Regression Basics
description: A basic summary of regression
publication:
authour: James
image:


This article sits squarely in the Statistics and Modelling (Building a Product - Analyse) area in the Data Science process. It is after you have gathered and wrangled your Data, you likely have an understanding of the summary statistics, some trends within the Data and you are at the point of beginning to build a model in an effort to make some kind of prediction. During this article we will consider what regression is, when to use it and how to interpret the results.

### What Regression is

Regression is defined by the Macquarie Dictionary as the act of going back; return; backward movement. The Oxford dictionary of Statistics defines Regression as...  The origins of the term in a statistical sense can be traced to a geneticist in the late 1800's; Francis Galton, in 1889 published an article that demonstrated how every characteristic of an individual is inherited by their offspring, but on *average* to a lesser degree. This can be thought of as regressing (going back) to the average - regression towards mediocrity. The **Galton Universal Regression Law** was later confirmed by Karl Pearson.

Regression can assist us in two ways - it can help us to summarise the Data (descriptive statistics) in addition to make probabilistic forecasts (inferential statistics).

At its heart Regression is the identification of a relationship between two features of an observation, ideally we can use one (or more) of the features to make some kind of prediction about a dependant feature. It seeks to answer questions along the lines of - Is feature *A* related to *B*, if so, what is the relationship and can this be used to predict *B* as feature *A* changes. This is ostensibly the beginning of the prediction *'magic'*.

Regression is generally classified as supervised Machine Learning(ML) - it seeks to take messy(real world) Data and model it with a mathematical function. Regression models are usually developed from a training set of Data where a Regression Equation is built. This equation denotes the relationship between the features - *A* and *B*, it seeks to approximate the trend of the Data. It infers a trend that future predictions can be based on. The quality of the 'fit' to the Data offers some kind of insight as to the quality of any possible future prediction - how good the model is.

**Note** Different regression techniques can be used for both continuous and categorical Data and offer different outcomes.

#### When to use which form of regression

There are several different kinds of regression. The choice around which one to use is a critical skill for any Data Scientist. To better understand how the different kinds of regression fit into the Machine Learning process a general guide is in the figure below.

[Image 1](!regression_flowchart)



- Linear Regression
	- Multiple Linear Regression
- Logistic Regression
	-

##### Linear Regression

Linear Regression is in the form of $$ p(x) = ax +b $$.

In this equation $$ p(x) $$ is the linear function where $$ x $$ is the co-efficient/ gradient, $$ a $$ and $$ b $$ are the two variables from the existing Data set. Imagine that we are training our model $$ p(x) $$ based on the features of $$ a $$ and $$ b $$ from each observation in the Data set. The more Data we have generally the better the model fit will be.

##### Logistic Regression

Logistic Regression is in the form of $$


### When to use it


### What the findings could mean

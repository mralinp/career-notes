# Machine Learning

## Popular machine learning algorithms

- [K Nearest Neighbor (KNN)](#k-nearest-neighbor-knn)
- [Linear Regression](#linear-regression)
- [Logistic Regression](#logistic-regression)
- [Naive Bayes](#naive-bayes)

### K Nearest Neighbor (KNN)

K-Nearest Neighbors is a popular algorithm used in supervised learning for classification and regression tasks. It's a non-parametric and lazy learning algorithm, meaning it doesn't make any assumptions about the underlying data distribution and it doesn't learn a model explicitly during training, but rather memorizes the training instances.

Here's how it works:

- Training Phase: In the training phase, KNN simply stores the entire dataset. It doesn't do any further processing or computation.

- Prediction Phase: When you want to make a prediction for a new data point, KNN looks at the K closest data points (neighbors) to that point in the feature space. For classification tasks, it takes a majority vote among the labels of these neighbors to assign a label to the new data point. For regression tasks, it takes the average of the values of these neighbors to predict a continuous value.

The "$K$" in KNN refers to the number of neighbors that are considered when making a prediction. It's a hyperparameter that needs to be specified by the user.

KNN is simple to understand and implement, but it can be computationally expensive, especially for large datasets, since it needs to compute distances between the new data point and all training data points during prediction. Additionally, choosing the right value for K can significantly impact the performance of the algorithm.

### Linear Regression

Linear regression is a statistical method used for modeling the relationship between a dependent variable and one or more independent variables. It assumes that there is a linear relationship between the independent variables (predictors) and the dependent variable (outcome).

Here's how linear regression works:

- Simple Linear Regression: In simple linear regression, there is only one independent variable. The relationship between the independent variable $X$ and the dependent variable $Y$ is modeled using a straight line equation:

- $Y=\beta_0+\beta_1X+\epsilon$
    $Y$ is the dependent variable.
    $X$ is the independent variable.
    $\beta_0$​ is the intercept, the value of $Y$ when $X=0$.
    $\beta_1$​ is the slope, which represents the change in $Y$ for a one-unit change in $X$.
    $\epsilon$ is the error term, representing the difference between the observed and predicted values of $Y$.

- Multiple Linear Regression: In multiple linear regression, there are two or more independent variables. The relationship between the independent variables $(X_1,X_2,…,X_n)$​ and the dependent variable $Y$ is modeled using a linear equation:

- $Y=\beta_0+\beta_1X_1+\beta_2X_2+…+\beta_nX_n+\epsilon$
  - $\beta_0$​ is the intercept.
  - $\beta_1,\beta_2,…,\beta_n$​ are the coefficients for the independent variables.
  - $X_1,X_2,…,X_n$​ are the independent variables.
  - $\epsilon$ is the error term.

The goal of linear regression is to estimate the coefficients $(\beta_1,\beta_2,…,\beta_n)$ that minimize the sum of squared differences between the observed and predicted values of the dependent variable. This is typically done using the method of least squares.

Linear regression is widely used in various fields for predicting and modeling relationships between variables, understanding the impact of predictors on the outcome, and making forecasts. 


# Logestic Regression
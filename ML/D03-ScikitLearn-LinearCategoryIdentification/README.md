# D03 - scikit-learn Classification Basics (Logistic / Softmax Regression)
*ML / D03-ScikitLearn-LinearCategoryIdentification*

This folder continues the [D02-ScikitLearn-LinearRegression](../D02-ScikitLearn-LinearRegression) module, but now the target is a **category** instead of a number.

We reuse many ideas from linear regression (features, `X`/`y`, `train_test_split`, `fit`/`predict`, preprocessing with `ColumnTransformer` and `Pipeline`) and add what changes when the output is a class label.

## Course Goals

In this module, we will learn:

1. Why predicting a category is a different problem from predicting a number
2. How the sigmoid function turns a linear score into a probability (logistic regression)
3. How softmax regression generalizes logistic regression to more than two classes
4. How to configure `LogisticRegression` and read its learned parameters
5. How to preprocess a real, messy dataset (categorical columns, blank values, mixed magnitudes) for classification
6. How to evaluate a classifier with accuracy, precision, recall, F1, and confusion matrices, instead of MAE/R^2
7. How to apply everything to a real project: predicting customer churn

## Lessons

1. [01-logistic-regression-overview.md](./01-logistic-regression-overview.md)
   A first end-to-end walkthrough of training and testing a logistic regression model in scikit-learn, plus the idea behind softmax regression for multi-class problems
2. [02-logistic-regression-parameters.md](./02-logistic-regression-parameters.md)
   A guided look at the main `LogisticRegression` parameters (`C`, `penalty`, `solver`, `multi_class`, `class_weight`) and when changing them matters
3. [03-classification-data-preprocess.md](./03-classification-data-preprocess.md)
   A deliberate repeat of the linear regression preprocessing lesson (categorical values, dates, differently scaled numeric columns) applied to a classification target, plus what is different for classification
4. [04-classification-metrics.md](./04-classification-metrics.md)
   How to read a confusion matrix and compute accuracy, precision, recall, and F1-score, and why accuracy alone is misleading on imbalanced data
5. [05-logistic-regression-practice.md](./05-logistic-regression-practice.md)
   A guided class project using the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) to predict which customers will churn

More lessons can be added later as the course grows.

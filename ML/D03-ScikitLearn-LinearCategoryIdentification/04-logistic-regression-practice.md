*ML / D03-ScikitLearn-LinearCategoryIdentification*

Make use of the data
https://www.kaggle.com/datasets/blastchar/telco-customer-churn

Build a logistic regression model to predict whether a customer will churn (`Churn` column), based on the other columns.

Evaluate how accurate the model is. Accuracy alone is not enough here, since churn is imbalanced (most customers do not churn) — also report precision, recall, F1-score, and the confusion matrix for the `Churn = Yes` class.

Consider the following questions:

1. `TotalCharges` looks numeric but may be stored as text, and can contain blank values for brand-new customers with `tenure = 0`. How do you detect this, and how do you handle it?

2. There are many categorical columns (`gender`, `Partner`, `Dependents`, `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `Contract`, `PaymentMethod`, and more). How should each be encoded? Are any of them ordinal (have a natural order) rather than purely categorical?

3. `tenure`, `MonthlyCharges`, and `TotalCharges` have different magnitudes. How can we reconcile this, and why does it matter for `LogisticRegression` specifically, beyond why it mattered for linear regression?

4. `customerID` is a unique identifier for each row. Should this be used as a model feature? Why or why not?

5. The target classes are imbalanced (roughly `27%` churn vs `73%` no churn).
   5.a How does this affect a plain accuracy score?
   5.b What does `class_weight="balanced"` change about training?
   5.c Between precision and recall, which one matters more if the business goal is "catch as many at-risk customers as possible, even with some false alarms"? Which matters more if the goal is "only flag customers we're quite confident will actually churn"?

6. Some columns like `OnlineSecurity`, `OnlineBackup`, `TechSupport`, `StreamingTV`, and `StreamingMovies` have a third value like `"No internet service"` in addition to `"Yes"`/`"No"`. Does this need special handling, or does one-hot encoding handle it naturally?

7. **Bonus (softmax regression):** Instead of predicting `Churn`, pick a multi-category column such as `Contract` (`Month-to-month` / `One year` / `Two year`) or `PaymentMethod` as the target, and train a multinomial `LogisticRegression` model to predict it from the remaining columns.
   7.a Compare `multi_class="ovr"` versus `multi_class="multinomial"` on this target. Do the predictions differ?
   7.b Which evaluation metrics from Lesson 1/2 still apply directly, and which need to be adapted for more than two classes (for example, a confusion matrix now has more than 2x2 cells)?

## Test Validation Data Split
Basic principle: Testing Data must be after Validation Data. Validation Data must be after Training Data.

1. Make 15% as the testing data
2. For validation data we use the following thresholds to make folds
  - 10%
  - 15%
  - 20%
  - 25%

For each fixed NN model do following experiment:

1. For each validation data fold

- Training
- Selecting the snapshot of best validation
- Store the checkpoint into a file named NN-\<hyperparameter\>-\<validation_percent\>.cpt

2. Combine all best result from validation data

- Calculate the mean of mean percentage loss
- Calculate the std of mean percentage loss
- Record the result by creating an empty file with name NN-\<hyperparameter\>-\<mean\>-\<std\>.rcd


Adjust NN model to be 

- Two layer MVP, namely just one hidden layer and one output layer
- Adjust the size of the hidden layer, pick a reasonable range for trials.
- For each model Repeat the step 2
- Pick the best model whose mean + std is smallest.
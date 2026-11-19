# A01 - Training Question Format
*AIO / A01-TrainingQuestionFormat*

This folder covers how USAAIO trained-model (open-ended) problems are structured, submitted and graded, using Sample Problem 5 as the running example.

## Course Goals

In this module, we will learn:

1. The official USAAIO submission rules for trained-model problems, what the provided cheat sheet does and does not cover, and the contest restriction: no Google, no AI, only the cheat sheet and Colab IntelliSense
2. The standard training SOP (RAW DATA → Pandas → Feature Engineering → NumPy → Training → Save Model) and its mirror inference SOP, and how to get a minimum submission passing Self-check
3. Hand-written feature engineering with `StandardScaler` and `OneHotEncoder`, and the rule of fitting and saving preprocessors in training but loading them in validation and testing
4. A four-stage tuning routine: lock a test set, compare plans with K-fold or multi-seed validation (mean and variance), check once on test, then train the final model on all data

## Lessons

1. [01-usaaio-trained-model-rules-and-cheat-sheet.md](./01-usaaio-trained-model-rules-and-cheat-sheet.md)
   Summary of the official guideline (file architecture, 5-step roadmap, how grading works) and the Save & Load cheat sheet, plus what must be memorized
2. [02-training-and-inference-sop.md](./02-training-and-inference-sop.md)
   The two mirror-image pipelines, a core template for both notebooks, and a minimum hands-on with no feature engineering ([Sample problem 5 Solution Minimum](./AIO_Sample_Problem/Sample%20problem%205%20Solution%20Minimum/))
3. [03-feature-engineering-scaler-and-onehot.md](./03-feature-engineering-scaler-and-onehot.md)
   Why we skip `ColumnTransformer`, how `StandardScaler` and `OneHotEncoder` work, the `training` flag pattern for persisting and loading preprocessors, and the full hands-on ([Sample problem 5 Solution JohnChen](./AIO_Sample_Problem/Sample%20problem%205%20Solution%20JohnChen/))
4. [04-model-tuning-with-k-fold-validation.md](./04-model-tuning-with-k-fold-validation.md)
   Hold-out test set, K-fold and seed-list validation with mean and std, refitting on train + validation, what to do when test accuracy is surprisingly bad, and the final all-data model

## Sample Problem Materials

- [Sample problem 5 Original](./AIO_Sample_Problem/Sample%20problem%205%20Original/): the official starter notebooks
- [Sample problem 5 Solution Minimum](./AIO_Sample_Problem/Sample%20problem%205%20Solution%20Minimum/): JSON → Pandas → NumPy → LinearRegression, no feature engineering (val MSE ≈ 0.477)
- [Sample problem 5 Solution JohnChen](./AIO_Sample_Problem/Sample%20problem%205%20Solution%20JohnChen/): adds `x^2`, `positive`, StandardScaler and OneHotEncoder (val MSE ≈ 0.388)

More lessons can be added later as the course grows.

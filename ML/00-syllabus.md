# ML Syllabus
*ML*

A 23-week machine learning syllabus for high school students, built around scikit-learn
and real datasets. Each unit opens with a **hands-on project** — training a model on real
data and seeing what it gets right and wrong — before opening up the **underlying math**
that explains why it worked. Concepts are motivated by a working model first, then made
precise second, rather than the other way around.


## Unit 1: Data Foundations — Working with Real Tables (Week 1)

**Core Focus:** A single fast tour of NumPy and pandas syntax, just enough to load and
manipulate a real CSV — deep fluency comes later, built up across every project that
follows.
**Module:** [D01-Dataframe](D01-Dataframe)

- Week 1: NumPy arrays (shapes, indexing, vectorized ops) → pandas `Series`/`DataFrame` →
  selecting with `loc`/`iloc`/boolean filters → cleaning, deriving columns, and `groupby`,
  taught back-to-back as one connected walkthrough on a real table.

**Essential Question:** How do we turn a spreadsheet into something a computer can compute
with?

## Unit 2: Predicting Numbers — Linear Regression (Weeks 2–5)

**Core Focus:** One session of `LinearRegression` syntax, then three full sessions turning
a working-but-mediocre model into a genuinely good one.
**Module:** [D02-ScikitLearn-LinearRegression](D02-ScikitLearn-LinearRegression)
**Project:** Predicting Walmart weekly sales from historical data (`project_henry`).

- Week 2 (syntax): Train/predict/evaluate walkthrough (`train_test_split`, `fit`,
  `predict`), what the main parameters control, preprocessing categorical/date/differently
  -scaled columns with `ColumnTransformer`/`Pipeline`, and MAE/$R^2$ as grading tools — all
  in one session, using a small toy dataset.
- Weeks 3–5 (project): Apply it for real on Walmart sales. Visualize the data to find what
  actually drives sales, notice what the first naive model gets wrong, engineer and test
  new features, and iterate until the model is defensibly good — not just runnable.

**Essential Question:** What does it mean for a computer to learn the "best" line through
a cloud of points?

## Unit 3: Predicting Categories — Classification (Weeks 6–9)

**Core Focus:** One session covering everything that changes when the target becomes a
label instead of a number, then two project sessions — shorter than Unit 2's because the
data workflow itself (splitting, preprocessing, iterating) is no longer new.
**Module:** [D03-ScikitLearn-LinearCategoryIdentification](D03-ScikitLearn-LinearCategoryIdentification)
**Project:** Predicting customer churn on the
[Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn).

- Week 6 (syntax): Sigmoid → `LogisticRegression` end-to-end → softmax for multi-class →
  key parameters (`C`, `penalty`, `solver`, `class_weight`) → confusion matrix, accuracy,
  precision, recall, $F_1$ — one connected session.
- Weeks 7–9 (project): Predict churn on real, messy data. The new work here is specific to
  classification: handling class imbalance, deciding whether precision or recall matters
  more for a churn business case, and reading a confusion matrix instead of a residual plot.

**Essential Question:** How does a model decide between "yes" and "no," and how do we know
if it's right?


## Unit 4: Feature Engineering — Giving the Model Better Inputs (Weeks 10–12)

**Core Focus:** One session on the transformer contract, then two sessions pushing the
Unit 2 Walmart model further with real engineered features — the payoff for building it,
not a new project from scratch.
**Module:** [D05-ScikitLearn-FeatureEngineering](D05-ScikitLearn-FeatureEngineering)

- Week 10 (syntax): `fit`/`transform`/`fit_transform` by hand → writing a custom
  transformer → why unscaled `PolynomialFeatures` breaks a model at degree 5 — one session.
- Weeks 11–12 (project): Return to the Walmart sales model. Add `FourierFeatures` for the
  yearly sales cycle and `GroupInteraction` for per-store coefficients, and measure whether
  they actually beat the Unit 2 baseline — real feature engineering means some ideas fail.

**Essential Question:** When the model isn't wrong but the inputs are, how do we reshape
data so the pattern becomes learnable?

## Unit 5: Regularization — Controlling Overfitting (Weeks 13–14)

**Core Focus:** One session watching a model overfit on purpose, one session fixing it —
directly on the now feature-rich Walmart model from Unit 5, which is exactly complex enough
to overfit.
**Module:** *Planned* — `D06-Regularization` (builds on `ML/lib/multi_alpha_ridge.py`,
a custom per-column Ridge estimator already in the shared library).

- Week 13 (syntax): Overfitting vs. underfitting via training-vs-test error as complexity
  grows, then the Ridge (L2) penalty and what it changes about fitted coefficients.
- Week 14 (project): Apply `RidgePerColumn` to the Unit 5 engineered-feature model; tune
  $\alpha$ per feature by comparing validation error, and confirm it beats the unregularized
  version on held-out data.

**Essential Question:** Why does a model that fits the training data perfectly sometimes
make worse predictions than one that fits it a little worse?

## Unit 6: Model Evaluation — Trusting a Score (Week 15)

**Core Focus:** A single session that revisits the Walmart and churn models already built
and asks: how much do we actually trust these numbers? Applied retroactively, not a new
project.
**Module:** *Planned* — `D07-ModelEvaluation`.

- Week 15: Why one train/test split can mislead (re-split the same data, watch the score
  move) → $k$-fold cross-validation → train/validation/test structure and avoiding leakage
  during hyperparameter search — one session, run against Unit 2/3/6 models directly.

**Essential Question:** How do we know a model will work on data it has never seen, not
just the one test set we happened to pick?

## Unit 7: Tree-Based Models — Decision Trees & Random Forests (Weeks 16–18)

**Core Focus:** One session of tree syntax and theory, then two project sessions applying
trees to the churn dataset and asking whether they actually beat the Unit 3 logistic
baseline.
**Module:** *Planned* — `D08-TreeModels`.

- Week 16 (syntax): A single decision tree trained and read → Gini impurity/information
  gain → overfitting in deep trees and `max_depth` → random forests as variance reduction
  through averaging — one session.
- Weeks 17–19 (project): Apply trees and forests to the churn dataset from Unit 3, tune
  depth/`n_estimators`, compare feature importances against the logistic regression
  coefficients, and decide which model actually deserves to ship.

**Essential Question:** How can a model learn "if-then" rules instead of a straight line,
and why do many weak trees beat one strong one?

## Unit 8: Neural Networks — Learning Nonlinear Patterns (Weeks 19–21)

**Core Focus:** Train a working neural network in the first session before touching
backpropagation, treating it as the natural next step after logistic regression (one
neuron) rather than a totally new topic.
**Module:** *Planned* — `D09-NeuralNetworks`.

- Week 20 (syntax): Train `MLPClassifier` on a familiar dataset and compare it to Unit 3's
  logistic regression, then open it up — layers, weights, activation functions as stacked
  sigmoid/softmax units, and gradient descent/backpropagation as "how the weights get
  updated," explained as an extension of ideas already known, not new math.
- Weeks 21–23 (project): Handwritten digit recognition (`sklearn.datasets.load_digits`,
  or MNIST) — images as arrays ties back to Unit 1. Tune hidden-layer sizes, watch it
  overfit and apply Unit 6 regularization instincts, and compare against a tree-based
  baseline from Unit 8.

**Essential Question:** How does stacking many simple linear decisions let a model learn
patterns no single line, sigmoid, or tree split could capture on its own?

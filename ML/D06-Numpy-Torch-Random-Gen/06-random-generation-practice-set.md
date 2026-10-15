# Practice Set: Random Generation and Fake Training Data
*ML / D06-Numpy-Torch-Random-Gen*

Write every task twice unless a task names one library: once with NumPy and once
with PyTorch. Use a local generator and put the seed in one visible variable.

For every generated object, print or assert its shape.

## Problem 1: Shape Warm-Up

With seed `2026`, generate:

1. a `(4, 5)` uniform array/tensor on $[0,1)$;
2. a `(2, 3, 4)` standard-normal array/tensor;
3. 100 integers from `10` through `19`, inclusive; and
4. a `(50, 2)` array/tensor uniform on $[-3,7)$.

Check all shapes and confirm that every bounded value lies in its requested
interval.

## Problem 2: Reproducibility

Create two separate generators with seed `99`. Draw five standard-normal values
from each and verify that they match. Then draw five more values from the first
generator and verify that this new draw does not match its first draw.

Explain in one sentence why both observations are expected.

## Problem 3: Match the Distribution to the Story

Generate 10,000 observations for each story:

1. a fair six-sided die;
2. whether an email is opened when the open probability is `0.32`;
3. the number of website errors per day when the average is `2.4`;
4. measurement error with mean `0` and standard deviation `0.05`;
5. waiting time when events occur at a rate of `4` per hour; and
6. a value equally likely to be anywhere from `20` up to but not including `35`.

Report the sample mean for each and compare it with the theoretical mean.

## Problem 4: Mixed Feature Matrix

Generate 2,000 fake customers with these four features:

- age: integer uniform from 18 through 80;
- annual income: lognormal;
- monthly support contacts: Poisson with mean `1.5`;
- subscribed: Bernoulli with probability `0.40`.

Combine the features into an `X` matrix with shape `(2000, 4)`. Print summary
statistics for each column. Explain one disadvantage of storing all four
columns in one numeric matrix.

## Problem 5: Weighted Categories

Generate 5,000 plan IDs using these probabilities:

| Plan ID | Probability |
|---|---:|
| 0 | 0.50 |
| 1 | 0.35 |
| 2 | 0.15 |

Count the realized proportion of each plan. Assert that the probabilities sum
to `1.0` before sampling.

## Problem 6: Shuffle Without Breaking Pairs

Create:

```python
X = np.arange(60).reshape(20, 3)
y = X.sum(axis=1)
```

Shuffle the rows. Use an assertion to prove that every shuffled target remains
paired with the correct row. Repeat in PyTorch.

## Problem 7: Linear Regression Data

Generate 1,500 rows with five standard-normal features. Use

$$
w=
\begin{bmatrix}
2\\
-1\\
0.5\\
3\\
-2.5
\end{bmatrix},
\qquad b=4,
$$

and

$$
y=Xw+b+\varepsilon,
\qquad
\varepsilon\sim\mathcal{N}(0,0.7^2).
$$

Requirements:

- store `signal` and `noise` separately;
- assert the final shapes;
- report the sample mean and standard deviation of `noise`; and
- split the result into 80% training and 20% test data using one permutation.

## Problem 8: Broadcasting Bug Hunt

Predict the shape of `y_bad` before running this code:

```python
X = torch.randn(100, 3)
w = torch.randn(3, 1)
signal = X @ w
noise = torch.randn(100)
y_bad = signal + noise
```

Explain why that shape occurs and repair the code in two different ways.

## Problem 9: Nonlinear Regression Data

Generate two features uniformly from $[-2,2)$. Define

$$
y=1.5x_1^2-2\sin(x_2)+0.8x_1x_2+\varepsilon,
\qquad
\varepsilon\sim\mathcal{N}(0,0.25^2).
$$

Create 3,000 observations. Compare the variance of the signal with the variance
of the noise.

## Problem 10: Binary Classification Data

Generate 2,000 rows with three standard-normal features. Choose your own fixed
weights and intercept, then:

1. compute logits;
2. apply sigmoid;
3. draw Bernoulli labels;
4. assert every probability is in `[0, 1]`;
5. report the positive-class proportion; and
6. compare random labels with deterministic labels made by thresholding at `0.5`.

## Problem 11: Controlled Corruption

Starting with the classification data from Problem 10, make three separate
training datasets:

1. one with 10% of labels flipped;
2. one with 5% of feature cells missing; and
3. one with 2% of rows changed into feature outliers.

Keep the test set clean. Record Boolean masks so you can report exactly how many
labels, cells, or rows were changed.

## Problem 12: Distribution Shift Investigation

Create a training set with 1,500 rows and a test set with 500 rows. Each row
has five independent features. Generate the features from different
distributions:

$$
X_{\text{train},j}\sim\mathcal{N}(0,1)
$$

and

$$
X_{\text{test},j}\sim\mathcal{N}(1.5,1.8^2),
\qquad j=1,\ldots,5.
$$

For both sets, generate the scalar target with the *same* linear data-generating
process:

$$
w=
\begin{bmatrix}
2\\
-1\\
0.5\\
3\\
-2.5
\end{bmatrix},
\qquad b=4,
\qquad
y=Xw+b+\varepsilon,
\qquad \varepsilon\sim\mathcal{N}(0,0.7^2).
$$

Thus `y_train` has shape `(1500,)` (or `(1500, 1)`) and `y_test` has shape
`(500,)` (or `(500, 1)`), with one target value per feature row.

1. Generate `X_train`, `X_test`, `y_train`, and `y_test` according to the
   distributions above. Assert their shapes.
2. Compute and compare the feature-wise means and standard deviations of
   `X_train` and `X_test`.
3. Fit a linear regression model on `(X_train, y_train)`.
4. Evaluate the model on `(X_test, y_test)` and report test RMSE and $R^2$.
5. Did the test metrics change relative to a no-shift test set? Explain that
   the conditional relationship $y\mid X$ (the weights, intercept, and noise
   distribution) stayed fixed, while the marginal feature distribution $P(X)$
   changed.

## Extension Challenges

1. Write reusable `make_regression_data` and `make_classification_data`
   functions with seeds as arguments.
2. Generate ten datasets from ten seeds and compare the resulting metric rather
   than trusting one lucky split.
3. Make regression noise heavy-tailed by using a Student's $t$ distribution.
4. Build a three-class target using softmax and categorical sampling.
5. Use a PyTorch `DataLoader` to produce shuffled mini-batches from your tensor
   dataset.

## Reflection Questions

1. What is the difference between a shape and a distribution?
2. Why is `scale=variance` wrong for a normal sampler?
3. Why should $X$ and $y$ use the same permutation?
4. How does increasing noise change what a model can learn?
5. Why is thresholding a probability different from sampling a Bernoulli label?
6. Why should intentional training-data corruption usually leave test data clean?
7. What can synthetic data prove, and what can it not prove?


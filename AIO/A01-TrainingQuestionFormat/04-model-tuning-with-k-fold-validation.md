# Lesson 4: Model Tuning with K-Fold and Multi-Seed Validation
*AIO / A01-TrainingQuestionFormat*

[Lesson 3](./03-feature-engineering-scaler-and-onehot.md) gave us one working pipeline. Real problems offer many plans (different features, different hyperparameters), and this lesson shows the four-stage routine for choosing between them without fooling yourself: **lock a test set, compare plans on several validation splits, check once on test, then train the final model on everything.**

## 1. Why One Validation Split Is Not Enough

A single `train_test_split` gives a single validation score. That score is partly the plan's quality and partly **luck of the split**. If plan A scores $0.39$ and plan B scores $0.38$ on one split, a different `random_state` can flip the order.

Worse, every time you look at the validation score and adjust something, the plan slowly adapts to **that** validation set. That is overfitting to the validation data, and it is why we keep a separate test set that no decision ever sees.

| Data | Used for | Looked at how often |
|---|---|---|
| **Train** | Fitting the model and preprocessors | Every run |
| **Validation** | Comparing plans | Many times |
| **Test** | One honest check of the chosen plan | **Once** |

![Four horizontal bars showing the four tuning stages. Stage 1 splits the data into an 80 percent train and validation block and a 20 percent locked test block. Stage 2 shows a 5-fold layout where each of five rows highlights a different fifth of the 80 percent block as the validation fold, with a note to report the mean and standard deviation per plan. Stage 3 retrains the chosen plan on all of the 80 percent block and scores the test block exactly once. Stage 4 trains on 100 percent of the provided data and writes model.joblib, scaler.joblib and onehot.joblib.](./images/model-tuning-four-stages.svg)

## 2. Stage 1: Split Off the Test Data and Leave It Untouched

Do this **first**, once, before any experiment:

```python
from sklearn.model_selection import train_test_split

x_train_val, x_test, y_train_val, y_test = train_test_split(
    x_raw, y_raw, test_size=0.2, random_state=42)
```

Rules for the test block:

- Never pass it to `fit` of anything (model **or** preprocessor).
- Never look at its score while choosing between plans.
- Keep the same `random_state` for the whole session so the test rows never change.

From now on, "the data" means `x_train_val`, `y_train_val`.

## 3. Stage 2: Compare Plans on Several Validation Splits

A **plan** is one complete choice: feature engineering recipe + model + hyperparameters. To compare plan A with plan B, score each on **many different validation sections of the same data** and look at the **mean** and the **spread**.

### 3.1 The rigorous way: K-fold cross validation

Cut the data into $k$ equal parts (folds), for example $k = 5$. In round $i$, fold $i$ (20%) is validation and the other four folds are training. Every row is used for validation exactly once.

$$
\text{CV score} = \frac{1}{k}\sum_{i=1}^{k} \text{MSE}_i
$$

```python
from sklearn.model_selection import KFold

kf = KFold(n_splits=5, shuffle=True, random_state=0)
for train_idx, val_idx in kf.split(x_train_val):
    x_tr, x_va = x_train_val.iloc[train_idx], x_train_val.iloc[val_idx]
    y_tr, y_va = y_train_val.iloc[train_idx], y_train_val.iloc[val_idx]
    ...  # fit on x_tr, score on x_va
```

### 3.2 The simple way: a list of random seeds

`KFold` is not on the cheat sheet, but `train_test_split` is. Repeat the split with different `random_state` values:

```python
for seed in [0, 1, 2, 3, 4]:
    x_tr, x_va, y_tr, y_va = train_test_split(
        x_train_val, y_train_val, test_size=0.2, random_state=seed)
    ...  # fit on x_tr, score on x_va
```

Validation sets from different seeds can overlap, so this is slightly less tidy than K-fold. For choosing between plans it is good enough, and it needs nothing new to memorize.

### 3.3 Read the mean **and** the standard deviation

Record one score per round, then summarize:

```python
scores = np.array(scores)
print(f"mean = {scores.mean():.4f}, std = {scores.std():.4f}")
```

| Plan | Mean MSE | Std | Reading |
|---|---|---|---|
| A | 0.40 | 0.01 | Stable. Gives similar results on any split. |
| B | 0.38 | 0.12 | Better on average but erratic. On some splits it is far worse. |

A large std means the result depends heavily on which rows landed in training. That is a typical **symptom of overfitting** (or of a plan too sensitive to a few rows). Prefer the plan whose mean is good **and** whose std is small. If two means differ by less than about one std, treat them as a tie and take the simpler plan.

## 4. Core Template: Score One Plan Over Many Seeds

```python
def score_plan(x_all, y_all, feature_fn, make_model, seeds):
  scores = []
  for seed in seeds:
    x_tr, x_va, y_tr, y_va = train_test_split(
        x_all, y_all, test_size=0.2, random_state=seed)

    x_tr = feature_fn(x_tr.copy(), training=True).to_numpy()
    x_va = feature_fn(x_va.copy(), training=False).to_numpy()

    model = make_model()
    model.fit(x_tr, y_tr.to_numpy())
    pred = model.predict(x_va)
    scores.append(mean_squared_error(y_va.to_numpy(), pred))
  return np.array(scores)
```

Notes:

- The preprocessors are **re-fit inside every round** on that round's training rows (`training=True`), then reused on validation (`training=False`). Fitting them once on all data before the loop would leak validation information ([Lesson 3, Section 5](./03-feature-engineering-scaler-and-onehot.md#5-the-golden-rule-fit-and-save-in-training-load-in-validation-and-testing)).
- Pass `x_tr.copy()` because `add_columns` in Lesson 3 modifies its input in place.
- Each round overwrites `scaler.joblib` and `onehot.joblib`. That is fine during tuning, but it means **the files on disk after tuning are not the final ones**. Stage 4 recreates them.
- Use the **same seeds** for every plan so they are compared on identical splits.

```python
seeds = [0, 1, 2, 3, 4]
a = score_plan(x_train_val, y_train_val, feature_fn_a, lambda: LinearRegression(), seeds)
b = score_plan(x_train_val, y_train_val, feature_fn_b, lambda: LinearRegression(), seeds)
print("A", a.mean(), a.std())
print("B", b.mean(), b.std())
```

## 5. Stage 3: Train on All Train + Validation Data and Check on Test

Once a plan is chosen, stop comparing. Train it on **all** of `x_train_val` (no more validation holdout), then score the test block **once**.

Simplest code change: reuse the same split call but make validation tiny, so almost everything trains:

```python
x_tr, x_va, y_tr, y_va = train_test_split(
    x_train_val, y_train_val, test_size=0.001, random_state=0)   # tiny validation, almost all rows train
```

Then apply the same pipeline to the test block with `training=False`:

```python
x_te = feature_fn(x_test.copy(), training=False).to_numpy()
test_mse = mean_squared_error(y_test.to_numpy(), model.predict(x_te))
```

**Expected result:** test MSE close to the Stage 2 mean, within about one or two std. A gap of that size is just noise.

### 5.1 What if the test score is surprisingly bad?

Do not panic and do not immediately start tuning on the test score. Work through these in order, cheapest first:

1. **Look for a bug before blaming the model.** Most "surprising" gaps are pipeline mistakes:
   - Test features built with `training=True` (re-fit on test) or with stale `.joblib` files from an old run.
   - Column order or column count differs from training. Print `x_te.shape` and the column names next to the training ones.
   - NaNs from a missing `index=x.index` (Lesson 3, Section 7). Run `np.isnan(x_te).sum()`.
   - `x_test` and `y_test` accidentally shuffled apart.
2. **Check that the gap is real.** Compare to the Stage 2 std. If the test MSE is within about $2\times$ std of the mean, it is noise, especially with a small test block. Repeat Stage 3 with a few different seeds of the first split to see the spread.
3. **Look for leakage that made validation too optimistic.** Preprocessors fit on all data before splitting, duplicate rows that landed in both train and validation, or a feature computed from the target.
4. **Look for distribution shift.** Compare ranges, means and category counts of `x_train_val` and `x_test`. If the data is time-ordered or grouped, a random split is not representative, so split by time or group instead.
5. **Treat it as overfitting.** The plan fits the train + validation rows too specifically. Go back to Stage 2 and choose a simpler plan or a more regularized one: fewer or lower-degree features, a smaller tree depth, a larger `alpha`, more training data. Prefer the low-std candidate that you passed over earlier.
6. **If both validation and test are bad, it is underfitting.** Add informative features or a more flexible model.

After step 5 or 6 you have used the test score to guide a decision, so that test block is **no longer untouched**. Be honest about it: when the data is plentiful, redo Stage 1 with a new `random_state` to get a fresh test block. When data is scarce, accept that the test score is now a slightly optimistic estimate, and do not repeat this cycle many times.

## 6. Stage 4: Train the Final Model on Everything

Keep the plan and hyperparameters fixed and train on **all** rows the question provides (train + validation + test):

```python
x_all = feature_fn(x_raw.copy(), training=True).to_numpy()   # fit + dump scaler/onehot on ALL rows
model = make_model()
model.fit(x_all, y_raw.to_numpy())
joblib.dump(model, "model.joblib")
```

Why it is safe: you already measured how this plan behaves on unseen data (Stages 2 and 3), and more rows almost always help. Why it is last: after this, no unseen data remains, so any score you print is a training score.

Checklist before zipping:

- [ ] `model.joblib`, `scaler.joblib`, `onehot.joblib` were all written by **this** final run, not by a tuning round.
- [ ] `submission.py` contains the same feature functions and `predict` uses `training=False`.
- [ ] Self-check ([Lesson 2](./02-training-and-inference-sop.md)) passes with the new ZIP.

## 7. Class Practice 1: Compare Two Plans on Sample Problem 5

Goal: decide between Plan A (raw `x` only, as in Lesson 2) and Plan B (with `x^2`, `positive`, scaler and one-hot, as in Lesson 3), using the four-stage routine.

Starting files: [Sample problem 5 Solution JohnChen](./AIO_Sample_Problem/Sample%20problem%205%20Solution%20JohnChen/) (has both pipelines).

**Step 1.** Split off 20% as test with `random_state=42`. Do not use it again until Step 4.

**Step 2.** Write `score_plan` (Section 4). Write `feature_fn_a` (returns `x[["x"]]`) and `feature_fn_b` (Lesson 3's `feature_eng`). Score both with seeds `[0, 1, 2, 3, 4]` and print mean and std.

**Step 3.** Pick the winner. Apply the tie rule (Section 3.3) if the means are close.

**Step 4.** Retrain the winner on all of `x_train_val` (Section 5), score the test block, and compare with the Stage 2 mean.

**Step 5.** Train the final model on all provided rows (Section 6), then run Self-check.

**Done when** you can state, for each plan, `mean ± std`, and the test MSE of the winner, and explain in one sentence why the test MSE does or does not match.

<details>
<summary>Solution</summary>

```python
def feature_fn_a(x):                      # wrapper with the same signature
  return x[["x"]]

def fa(x, training=True): return feature_fn_a(x)
fb = feature_eng                           # Lesson 3

seeds = [0, 1, 2, 3, 4]
a = score_plan(x_train_val, y_train_val, fa, lambda: LinearRegression(), seeds)
b = score_plan(x_train_val, y_train_val, fb, lambda: LinearRegression(), seeds)
print(f"A: {a.mean():.3f} +- {a.std():.3f}")
print(f"B: {b.mean():.3f} +- {b.std():.3f}")
```

Typical outcome: Plan A has mean near $0.48$, Plan B near $0.39$, and both stds are small compared with the $0.09$ gap, so Plan B wins clearly. Test MSE for Plan B should land near $0.39$ too. The exact numbers depend on the split, so judge by the **relationship** (gap versus std), not by matching digits.

If your Plan B test MSE is much worse, go through Section 5.1 in order. The most common cause here is a test block transformed with `training=True`.

</details>

## 8. Common Mistakes

### 8.1 Choosing a plan by looking at the test score
Then the test block is just another validation block. Decide with Stage 2 only.

### 8.2 Comparing plans on different splits
Plan A on seed 0 versus plan B on seed 7 mixes plan quality with split luck. Use identical seeds.

### 8.3 Reporting only the mean
Two plans with the same mean are not equal if one has ten times the std.

### 8.4 Fitting preprocessors before the split
`StandardScaler().fit(x_all)` before the loop leaks validation rows into the scaler. Fit inside each round.

### 8.5 Submitting stale preprocessor files
Tuning rounds overwrite `scaler.joblib` and `onehot.joblib`. Re-run Stage 4 last, then download.

### 8.6 Tuning forever
Every extra comparison adds a little overfitting to the validation data. Set a small list of candidate plans up front, and stop.

## Key Takeaways

- Four stages: **lock test → compare plans on many validation splits → refit on train + validation and check test once → final fit on all data**.
- Compare plans on identical splits (K-fold, or a seed list), and read **mean and std**. A large std signals overfitting or instability.
- Re-fit preprocessors inside each round; never on validation or test.
- A bad test score means "debug first": pipeline bug, noise, leakage, shift, then overfitting or underfitting, in that order.
- The final model uses every row provided, and its `.joblib` files must come from that last run.

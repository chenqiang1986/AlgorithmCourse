# Lesson 4: Classification Metrics
*ML / D03-ScikitLearn-LinearCategoryIdentification*

This lesson covers how to read whether a classification model is actually good: the confusion matrix, precision, recall, and accuracy.

We already computed `accuracy_score` and `confusion_matrix` in [Lesson 1](./01-logistic-regression-overview.md), but only printed them without explaining what the numbers mean, or when accuracy alone is misleading. This lesson fills that gap before we apply it to a real, imbalanced dataset in [Lesson 5](./05-logistic-regression-practice.md).

## 1. Why Accuracy Alone Is Not Enough

Imagine a churn dataset where `8` out of `10` customers do **not** churn, and only `2` actually churn.

A lazy model that always predicts `"No"` (never churns) would score:

```text
accuracy = 8 correct / 10 total = 80%
```

That sounds good, but this model is useless — it never catches a single real churner. It just happens to be right most of the time because "No" is the majority class.

This is why classification needs more than one number. We need metrics that describe performance **per class**, not just overall.

## 2. The Confusion Matrix

A confusion matrix is a table that breaks predictions down by what was actually true versus what the model predicted.

For a binary target (`"No"` / `"Yes"`), it looks like this:

```text
                     Predicted: No     Predicted: Yes
Actual: No           TN                 FP
Actual: Yes           FN                 TP
```

- rows = the real answer
- columns = what the model guessed
- the diagonal (`TN`, `TP`) is where the model got it right
- the off-diagonal (`FP`, `FN`) is where the model got it wrong

## 3. The Four Outcomes: TP, TN, FP, FN

Pick one class to call the **positive** class (here, `"Yes"`, churn) and the other the **negative** class (`"No"`, no churn). Then every prediction falls into one of four buckets:

- **True Positive (TP)**: actually `Yes`, predicted `Yes` — correctly caught
- **True Negative (TN)**: actually `No`, predicted `No` — correctly cleared
- **False Positive (FP)**: actually `No`, predicted `Yes` — a false alarm
- **False Negative (FN)**: actually `Yes`, predicted `No` — a miss

`False Positive` and `False Negative` are named after what the *prediction* claimed, not the true answer: a false positive is a prediction of "positive" that turned out to be false.

## 4. Reading a Confusion Matrix in scikit-learn

```python
from sklearn.metrics import confusion_matrix

y_true = ["No", "No", "No", "No", "No", "No", "No", "No", "Yes", "Yes"]
y_pred = ["No", "No", "No", "No", "No", "No", "Yes", "Yes", "No", "Yes"]

cm = confusion_matrix(y_true, y_pred, labels=["No", "Yes"])
print(cm)
```

Output:

```text
[[6 2]
 [1 1]]
```

Reading it with `labels=["No", "Yes"]`:

- row 0 (`No`), column 0 (`No`) = `6` → `TN`
- row 0 (`No`), column 1 (`Yes`) = `2` → `FP`
- row 1 (`Yes`), column 0 (`No`) = `1` → `FN`
- row 1 (`Yes`), column 1 (`Yes`) = `1` → `TP`

Passing `labels=["No", "Yes"]` explicitly matters: without it, `confusion_matrix` orders classes alphabetically/numerically on its own, which is easy to misread if you assume a different order.

## 5. Accuracy: The Overall Score

$$\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}$$

Using the numbers above (`TP=1, TN=6, FP=2, FN=1`):

$$\text{Accuracy} = \frac{1 + 6}{1 + 6 + 2 + 1} = \frac{7}{10} = 0.7$$

Accuracy answers: *"out of everything, how much did we get right?"* It treats every class equally, which is exactly the problem when classes are imbalanced (Section 1).

## 6. Precision: Normalize the Confusion Matrix by Column

Accuracy (Section 5) normalizes the *entire* matrix by the grand total. Precision and recall instead normalize just one slice of it at a time — precision normalizes by **column**.

Take a column of the confusion matrix — everyone the model predicted into that class — and divide each cell by the column's total:

```text
                     Predicted: No     Predicted: Yes
Actual: No           TN                 FP
Actual: Yes           FN                 TP
                     ---------------    ---------------
column total:         TN + FN            FP + TP
```

Dividing the `Predicted: Yes` column by its total gives **precision for the positive class**:

$$\text{Precision}_{\text{Yes}} = \frac{TP}{TP + FP} = \frac{1}{1 + 2} = 0.333$$

Nothing about that operation is specific to `Yes` — the exact same division, applied to the `Predicted: No` column, gives **precision for the negative class**:

$$\text{Precision}_{\text{No}} = \frac{TN}{TN + FN} = \frac{6}{6 + 1} = 0.857$$

Either way, precision answers: *"of everyone we predicted into this class, how many actually belong there?"* Low precision for a class means a lot of false alarms for that class. "Precision" with no qualifier usually means precision for whichever class you called positive, but every column of the matrix has its own precision.

## 7. Recall: Normalize the Confusion Matrix by Row

Recall is the mirror image: normalize by **row** instead of column.

Take a row of the confusion matrix — everyone who actually belongs to that class — and divide each cell by the row's total:

```text
                     Predicted: No     Predicted: Yes     row total
Actual: No           TN                 FP                 TN + FP
Actual: Yes           FN                 TP                 FN + TP
```

Dividing the `Actual: Yes` row by its total gives **recall for the positive class**:

$$\text{Recall}_{\text{Yes}} = \frac{TP}{TP + FN} = \frac{1}{1 + 1} = 0.5$$

The same division applied to the `Actual: No` row gives **recall for the negative class**, sometimes called **specificity**:

$$\text{Recall}_{\text{No}} = \frac{TN}{TN + FP} = \frac{6}{6 + 2} = 0.75$$

Recall (also called **sensitivity** or **true positive rate** for the positive class) answers: *"of everyone who actually belongs to this class, how many did we correctly find?"* Low recall for a class means we are missing real members of it.

So the whole trick is: **precision normalizes columns, recall normalizes rows.** That is also why they rarely agree — precision (`0.333` for `Yes`) and recall (`0.5` for `Yes`) come from the same matrix but slice it in perpendicular directions, so a single "percent correct" cannot capture both at once. It is also why the idea generalizes past two classes for free: with $k$ classes, class $i$'s precision is just diagonal cell $i$ divided by column $i$'s total, and its recall is diagonal cell $i$ divided by row $i$'s total — no extra machinery needed (more on this in Section 13).

## 8. Precision vs Recall: The Tradeoff

These two metrics pull in different directions, and the right balance depends on the cost of each type of mistake:

- a model that predicts `Yes` (churn) very freely: catches almost every real churner (**high recall**), but also raises lots of false alarms (**low precision**)
- a model that only predicts `Yes` when very confident: rarely wrong when it does say `Yes` (**high precision**), but misses many real churners who looked borderline (**low recall**)

Which one matters more is a business decision, not a math decision:

- "catch as many at-risk customers as possible, even with some false alarms" → prioritize **recall**
- "only flag customers we're quite confident will actually churn" → prioritize **precision**

We revisit this exact question with a real dataset in [Lesson 5](./05-logistic-regression-practice.md).

## 9. F1-Score: Combining Precision and Recall

Sometimes you want one number that balances both. The **F1-score** is the harmonic mean of precision and recall:

$$F_1 = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}$$

$$F_1 = 2 \times \frac{0.333 \times 0.5}{0.333 + 0.5} = 0.4$$

F1 is low when *either* precision or recall is low — a model cannot get a good F1-score just by favoring one and ignoring the other. Use it when you want a single balanced score instead of eyeballing precision and recall separately.

## 10. Full Example Code

`confusion_matrix` has a `normalize` argument that does the column/row division from Sections 6-7 for us: `normalize="pred"` divides by column totals (precision), `normalize="true"` divides by row totals (recall). That means precision and recall never need their own function calls — they are just the confusion matrix, normalized a different way.

```python
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from sklearn.model_selection import train_test_split

study_hours = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
passed = [0, 0, 0, 0, 1, 0, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    study_hours, passed, test_size=0.4, random_state=42, stratify=passed
)

model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("Counts:\n", confusion_matrix(y_test, y_pred, labels=[0, 1]))
print("Precision per class (normalize='pred'):\n", confusion_matrix(y_test, y_pred, labels=[0, 1], normalize="pred").round(3))
print("Recall per class (normalize='true'):\n", confusion_matrix(y_test, y_pred, labels=[0, 1], normalize="true").round(3))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("F1:", f1_score(y_test, y_pred))
```

## 11. Reading Example: Computing Metrics by Hand, Then Checking with scikit-learn

Take the same `y_true`/`y_pred` from Section 4:

```python
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score

y_true = ["No", "No", "No", "No", "No", "No", "No", "No", "Yes", "Yes"]
y_pred = ["No", "No", "No", "No", "No", "No", "Yes", "Yes", "No", "Yes"]
labels = ["No", "Yes"]

print(confusion_matrix(y_true, y_pred, labels=labels))
print(confusion_matrix(y_true, y_pred, labels=labels, normalize="pred").round(3))
print(confusion_matrix(y_true, y_pred, labels=labels, normalize="true").round(3))
print("Accuracy:", accuracy_score(y_true, y_pred))
print("F1:", f1_score(y_true, y_pred, pos_label="Yes"))
```

Output:

```text
[[6 2]
 [1 1]]
[[0.857 0.667]
 [0.143 0.333]]
[[0.75 0.25]
 [0.5  0.5 ]]
Accuracy: 0.7
F1: 0.4
```

The diagonal of the `normalize="pred"` matrix *is* precision for each class, and the diagonal of the `normalize="true"` matrix *is* recall for each class — read off `[1][1]` (the `Yes`/`Yes` cell) from each: `0.333` matches $\text{Precision}_{\text{Yes}}$ from Section 6, and `0.5` matches $\text{Recall}_{\text{Yes}}$ from Section 7, exactly. The other diagonal cell, `[0][0]` (the `No`/`No` cell), gives the negative-class versions: `0.857` is $\text{Precision}_{\text{No}}$, `0.75` is $\text{Recall}_{\text{No}}$. No separate `precision_score`/`recall_score` calls were needed — both metrics, for both classes, come straight out of `confusion_matrix` by changing `normalize`.

The non-obvious detail: `f1_score` still needed `pos_label="Yes"` because the target is text, not `0`/`1`. If the target had been encoded to `0`/`1` first (as in [Lesson 3](./03-classification-data-preprocess.md#6-the-target-is-different-encoding-y)), `pos_label=1` is the default and can be omitted.

## 12. `classification_report`: All Metrics at Once

Computing precision, recall, and F1 one call at a time gets repetitive. `classification_report` prints all of them, for every class, at once:

```python
from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred, labels=["No", "Yes"]))
```

```text
              precision    recall  f1-score   support

          No       0.86      0.75      0.80         8
         Yes       0.33      0.50      0.40         2

    accuracy                           0.70        10
   macro avg       0.60      0.62      0.60        10
weighted avg       0.75      0.70      0.72        10
```

`support` is how many real examples of that class were in `y_true`. `macro avg` treats both classes equally regardless of size; `weighted avg` weights each class by its `support`. On imbalanced data, the minority class's row (here `Yes`) is usually the one that matters most, even though it barely moves the `weighted avg`.

## 13. Common Beginner Questions

### Which class should be "positive"?

Whichever class you actually care about detecting. For churn, that is `Yes` (a customer leaving) — missing a real churner (a false negative) is usually more costly to the business than a false alarm.

### Is a confusion matrix only for two classes?

No. With $k$ classes it becomes a $k \times k$ table, with the correct predictions still on the diagonal. Precision and recall are still computed the same way as Sections 6-7, just repeated per class: class $i$'s precision is diagonal cell $i$ divided by column $i$'s total, and its recall is diagonal cell $i$ divided by row $i$'s total.

### Why did `accuracy` look fine in Section 1 but the model still seemed bad?

Because `80%` accuracy came from a model that predicted the majority class every time. Precision and recall on the minority class exposed that it was not actually learning anything.

## 14. Common Mistakes

### Mistake 1: Reading the confusion matrix with the wrong orientation

Rows and columns can be swapped depending on the library or the order `labels=` was passed in. Always check which axis is "actual" and which is "predicted" rather than assuming.

### Mistake 2: Trusting accuracy on imbalanced data

As shown in Section 1, a model can reach high accuracy while completely failing the minority class. Always look at precision/recall/confusion matrix alongside accuracy, especially when class sizes are uneven — this comes up directly with the Telco churn dataset in [Lesson 5](./05-logistic-regression-practice.md).

### Mistake 3: Forgetting `labels=` when reading precision/recall off a normalized matrix

Since precision and recall come from `confusion_matrix(..., normalize=...)` rather than `precision_score`/`recall_score`, there is no `pos_label` to set — but `labels=` still decides which row/column belongs to which class. Skip it, and scikit-learn falls back to alphabetical/numeric order, making it easy to read the wrong diagonal cell as "the positive class". `f1_score` still defaults to treating `1` as positive, so it still needs `pos_label="Yes"` on a text target, or the target encoded to `0`/`1` first as shown in [Lesson 3](./03-classification-data-preprocess.md#6-the-target-is-different-encoding-y).

### Mistake 4: Mixing up precision and recall

A memory aid: **precision** is about the predictions you *made* ("of what I said was `Yes`, how much was right?"); **recall** is about the positives that *exist* ("of everyone who was really `Yes`, how much did I find?").

## 15. Class Practice

### Practice 1

Given this confusion matrix for a spam filter (`"spam"` is the positive class):

```text
                     Predicted: not spam   Predicted: spam
Actual: not spam      90                    10
Actual: spam            5                    15
```

Compute, by hand:

1. accuracy
2. precision and recall for `spam` (normalize the `spam` column, then the `spam` row)
3. precision and recall for `not spam` (normalize the `not spam` column, then the `not spam` row)
4. F1-score for `spam`

Then explain in one sentence why accuracy alone looks better than the `spam` precision/recall/F1 numbers here.

### Practice 2

Using the code from Section 10:

1. change `passed` to a more imbalanced target, for example `[0, 0, 0, 0, 0, 0, 0, 0, 1, 1]`
2. re-run the script and compare accuracy, precision, and recall to the original version
3. print `classification_report(y_test, y_pred)` and identify the `support` for each class
4. explain which metric changed the most, and why

## 16. Key Takeaways

- accuracy alone can hide a model that fails on the minority class, especially on imbalanced data
- a confusion matrix breaks predictions into `TP`, `TN`, `FP`, `FN` — pass `labels=` explicitly so the orientation is unambiguous
- **precision** = normalize the confusion matrix by column: of everyone predicted into a class, how many actually belong there — $\text{Precision}_{\text{Yes}} = \frac{TP}{TP+FP}$, and the same division on the other column gives $\text{Precision}_{\text{No}}$
- **recall** = normalize the confusion matrix by row: of everyone who actually belongs to a class, how many were found — $\text{Recall}_{\text{Yes}} = \frac{TP}{TP+FN}$, and the same division on the other row gives $\text{Recall}_{\text{No}}$ (specificity)
- **accuracy** = of everything, how many were correct: $\frac{TP+TN}{TP+TN+FP+FN}$
- **F1-score** balances precision and recall into one number, and stays low if either one is low
- `classification_report` prints precision/recall/F1/support for every class in one call
- which of precision or recall matters more depends on the real-world cost of false positives versus false negatives

Next, [Lesson 5](./05-logistic-regression-practice.md) puts all of this to work on a real, imbalanced dataset: predicting customer churn.

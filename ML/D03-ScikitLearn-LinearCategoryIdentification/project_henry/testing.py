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
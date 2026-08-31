import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "sleep_hours": [8, 8, 7, 7, 6, 6, 5, 5],
    "exam_score": [50, 54, 60, 64, 71, 75, 81, 87]
})

X = df[["study_hours", "sleep_hours"]]
y = df["exam_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

model = LinearRegression(
    
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
y_pred_train = model.predict(X_train)

print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)
print("Predictions:", y_pred)
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R^2:", r2_score(y_test, y_pred))

print("Predictions:", y_pred_train)
print("MAE:", mean_absolute_error(y_train, y_pred_train))
print("R^2:", r2_score(y_train, y_pred_train))
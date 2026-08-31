import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "study_hours": [2, 4, 3, 6, 8, 5, 7, 9],
    "practice_questions": [20, 50, 35, 80, 120, 65, 100, 140],
    "course_type": ["online", "offline", "online", "offline", "offline", "online", "online", "offline"],
    "exam_date": [
        "2026-01-10", "2026-01-12", "2026-01-18", "2026-02-01",
        "2026-02-10", "2026-02-12", "2026-03-01", "2026-03-08"
    ],
    "final_score": [55, 63, 60, 74, 85, 70, 81, 90]
})

# Step 1: convert raw dates
df["exam_date"] = pd.to_datetime(df["exam_date"])

# Step 2: create date features
df["exam_month"] = df["exam_date"].dt.month
df["exam_dayofweek"] = df["exam_date"].dt.dayofweek
df["days_since_start"] = (df["exam_date"] - df["exam_date"].min()).dt.days

# Step 3: choose features and target
X = df[[
    "study_hours",
    "practice_questions",
    "course_type",
    "exam_month",
    "exam_dayofweek",
    "days_since_start"
]]
y = df["final_score"]

# Step 4: split first
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Step 5: tell sklearn which columns need which preprocessing
numeric_features = [
    "study_hours",
    "practice_questions",
    "exam_month",
    "exam_dayofweek",
    "days_since_start"
]
categorical_features = ["course_type"]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
    ]
)

# Step 6: combine preprocessing and model into one pipeline
model = Pipeline(
    steps=[
        ("preprocess", preprocessor),
        ("regressor", LinearRegression())
    ]
)

# Step 7: fit on training data only
model.fit(X_train, y_train)

# Step 8: predict on test data
y_pred = model.predict(X_test)

print(y_pred)
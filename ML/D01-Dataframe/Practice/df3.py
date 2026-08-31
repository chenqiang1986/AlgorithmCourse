import pandas as pd

df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek"],
    "science": [85, None, 92, 88],
    "history": [78, 81, None, 90]
})

print(df.isna().sum())

df["science"] = df["science"].fillna(df["science"].mean())
df["history"] = df["history"].fillna(0)

df["total"] = df["science"] + df["history"]

print(df)
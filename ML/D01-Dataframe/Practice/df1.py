import pandas as pd

df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek", "Eva"],
    "math": [91, 78, 88, 95, 73],
    "english": [84, 81, 90, 89, 76]
})

df["average"] = (df["math"] + df["english"]) / 2

df["passed"] = df["average"] >= 80

print(df[["student", "average"]])

print(df[df["math"] >= 90]["student"])

print(df)
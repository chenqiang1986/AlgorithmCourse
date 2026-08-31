import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Amy", "Brian", "Chloe", "Derek"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 4],
    "math": [91, 78, 95]
})

joined = students.merge(scores, on = "student_id", how = "left")

print(joined)

print(joined[joined["math"].isna()]["name"])
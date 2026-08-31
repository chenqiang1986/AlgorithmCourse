import pandas as pd

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ann", "Ben", "Cara", "Dan"]
})

scores = pd.DataFrame({
    "student_id": [1, 2, 3],
    "math": [82, 94, 88]
})

merged = students.merge(scores, on="student_id", how="left")
print(merged)
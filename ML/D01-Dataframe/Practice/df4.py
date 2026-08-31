import pandas as pd

df = pd.DataFrame({
    "student": ["Amy", "Brian", "Chloe", "Derek", "Eva", "Felix"],
    "club": ["music", "robotics", "music", "robotics", "music", "robotics"],
    "grade": [10, 10, 11, 11, 10, 11],
    "score": [82, 94, 88, 91, 79, 85]
})

clubgroup = df.groupby("club")

print(clubgroup["score"].mean())

print(clubgroup["student"].count())

gradegroup = df.groupby("grade")

print(gradegroup["score"].count())

print(gradegroup["score"].mean())

print(gradegroup["score"].max())
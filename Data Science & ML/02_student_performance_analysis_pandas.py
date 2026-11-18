# Student performance analysis using pandas.
# Install dependency: pip install pandas

import pandas as pd

data = {
    "Name": ["Asha", "Rohan", "Kabir", "Sara", "Dev", "Ira"],
    "Maths": [88, 67, 91, 76, 54, 95],
    "Python": [92, 72, 89, 81, 60, 98],
    "Physics": [79, 65, 84, 73, 58, 90]
}

df = pd.DataFrame(data)

subjects = ["Maths", "Python", "Physics"]
df["Total"] = df[subjects].sum(axis=1)
df["Average"] = df[subjects].mean(axis=1)
df["Result"] = df["Average"].apply(
    lambda score: "Pass" if score >= 40 else "Fail"
)

print("\\nStudent records:")
print(df)

print("\\nClass average in each subject:")
print(df[subjects].mean())

print("\\nTop performer:")
top_student = df.loc[df["Average"].idxmax()]
print(top_student[["Name", "Average", "Result"]])

print("\\nStudents with average above 80:")
print(df[df["Average"] > 80][["Name", "Average"]])

print("\\nSorted student ranking:")
print(df.sort_values("Average", ascending=False)[
    ["Name", "Total", "Average", "Result"]
])

df.to_csv("student_performance_report.csv", index=False)
print("\\nSaved student_performance_report.csv")

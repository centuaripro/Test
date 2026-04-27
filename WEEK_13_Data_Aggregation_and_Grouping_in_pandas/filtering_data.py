
import pandas as pd

from utils.students_record_utils import load_student_records

# Boolean Indexing 
students_df = load_student_records("files/students_record.csv")

math_high_performers = students_df[students_df["math_score"]> 90]

print(math_high_performers)

print("\n")
print("="*56)
print("\n")

# Filter for students who scored above 85 in maths and 75 in science

science_high_performers = students_df[
    (students_df["math_score"] > 85) & (students_df["science_score"] >95)
]

print(science_high_performers)

print("\n")
print("="*56)
print("\n")

# Filter for students who excel in either maths(above 90) or English(above 90)

math_or_english = students_df[
    (students_df["math_score"]> 90) |
    (students_df["science_score"] > 90)
]

print(math_or_english)

print("\n")
print("="*56)
print("\n")

# 2 Query Indexing(using SQL-Like syntax)
results = students_df.query("math_score >= 80 and english_score > 90 and grade_level == 10")
print("Query Result")
print(results)

print("\n")
print("="*56)
print("\n")

# 3 Filter() method- used to filter rows or columns based on their labels not content

filtered_cols = students_df.filter(like = "mat", axis = 1)
print(filtered_cols)

print("\n")
print("="*56)
print("\n")

# 4 isin () method
# Take for example, we are looking for students with last name "Hernandez"

filtered_students = students_df[students_df["last_name"].isin(["Hernandez", "Thomas", "Taylor"])]

print(filtered_students)

# 5 .loc[] Assessor (label-based)

filtered_df = students_df.loc[students_df["history_score"] > 80, ["student_id", "first_name", "history_score"]]

print(filtered_df)

# 6 .iloc[] Assessor (label-based)

filtered_df = students_df.loc[students_df["history_score"] > 80, [0, 1, 9]]

print(filtered_df)


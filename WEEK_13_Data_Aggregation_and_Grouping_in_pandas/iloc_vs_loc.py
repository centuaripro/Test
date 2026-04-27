
# The difference between the loc and the iloc functions is that the loc function selects rows using row labels whereas the iloc function selcets rows using their index position (starting from 0)

from utils.students_record_utils import load_student_records

students_df = load_student_records("files/students_record.csv")

#students_df.set_index("last_name", inplace = True)

#print(students_df.loc["Hernandez"])

print(students_df.iloc[0:4])

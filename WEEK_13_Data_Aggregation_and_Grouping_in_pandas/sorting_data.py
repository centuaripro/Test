
import pandas as pd

from WEEK_13_Data_Aggregation_and_Grouping_in_pandas.utils.students_record_utils import load_student_records

def main():
    """ Main EntryPoint """

    students_df = load_student_records("files/students_record.csv")

    # sort mathematics score from highest to lowest -single column art
    sorted_by_math = students_df.sort_values("math_score", ascending = False)

    print("Top math students:")
    print(sorted_by_math[["student_id", "first_name", "last_name", "math_score"]])

    print("\n")
    print("="*50)

    # sort class level, the mathematics score- multiple column sort
    sorted_multi = students_df.sort_values(["grade_level","math_score"], ascending=[True, False])
    print("\nSorted by class level, then mathematics score")
    print(sorted_multi)

    print("\n")
    print("="*50)

if __name__ == "__main__":
    main()

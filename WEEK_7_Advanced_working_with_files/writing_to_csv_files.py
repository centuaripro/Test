
import csv
from pprint import pprint

# Sample data

dataset = [
    #["Name", Score", "Grade"]
    ["Alice", 90, "A"],
    ["Bob",85, "B"],
    ["Mike",73,"C"],
    ["Harrison",97,"A"],
    ["Florence",61,"D"],
]

def write_to_csv(list_data):
    # Assuming the headers were not defined
    headers = ["Name", "Score", "Grade"]
    _data = [headers] + list_data

    # Write to the CSV file

    with open("files/students_grades.csv","w", newline = '') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(_data)
    

print("Done writing to 'students_grade.csv'")

def write_to_csv_dict(list_data):
    students = []

    for items in list_data:

        pprint(students)
        name = items[0]
        score = items[1]
        grade = items[2]

        students.append({
            "Name":name,
            "Score":score,
            "Grade":grade
        })

        with open("files/students_grades_dict.csv","w", newline = '') as file:
            writer = csv.DictWriter(file, fieldnames= ["Name", "Score",  "Grade"])
            writer.writeheader() # First write the header row
            writer.writerows(students)
        

write_to_csv(dataset)        
write_to_csv_dict(dataset)

# A dictionary is a data structure used to store data values in key value pairs
# Values in a dictionary can be of any data type
# Keys must be strings
# A dictionary is an ordered collection(from version 3.17) which is changable/ mutable and ordered.
# Does not allow duplicates
from pprint import pprint

student_a = {
    "first_name": "Chris",
    "last_name": "Idakwo",
    "age":20,
    "height": 1.65,
    "gender": "male",
    "registered": "True",
    "skills": []
}

# pprint(student_a)

# create dictionary using dict() constructor

student_b = dict(
    first_name = "Chris",
    last_name=  "Idakwo",
    age = 26,
    height = 1.9,
    gender = "Male"
)

print("="*50)
pprint(student_a)
print("="*50)
pprint(student_b)





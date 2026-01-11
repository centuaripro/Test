
# Ask the teacher for the number of students
# For each student:
# Ask for the students's name
# Ask for their test score
# Check if each score is valid ( between 0 and 100)
# Calculate the average of all scores
# Tell the teacher:
# Who passed ( score >= 60)
# who failed (score  < 60)
# The class average
# The highest and lowest scores



print("")
print("==================================")
print("""
    Student Grades Tracker Project
    Author: Ekpjoka Chris Idokwo
    Description: A program that tracks students grades, calculates average
 """)
print("=======================================")
print("")

# step 1 
# Ask for the number of students

num_students = int(input("How many studnets to you want to grade?"))

# Initialize all necessary variables for calculation
total_score = 0
passed_students = []
failed_students = []

for num in range(num_students):
    print(f"\n --- student {num + 1 } ---")

    # Get the student name
    student_name = input("Enter student name:")

    # Get and validate student score

    student_score = float(input(f"Enter score for {student_name}"))

    while student_score < 0 or student_score > 100:
        print("Invlaid score! Please enter a score between 0 and 100")
        student_score = float(input(f"Enter score for {student_name}"))
    
    print("score recorded!")

    total_score = total_score + student_score
    print("The total score is",total_score)

    # Check if student pssed or failed

    if student_score >= 60:
        passed_students.append((student_name, student_score))
    else:
        failed_students.append((student_name, student_score))

class_average = total_score/num_students
print("Class average", class_average)


print("\n" + "="*50)
print("GRADE REPORT")
print("="*50)

print("\nSTUDENTS WHO PASSED:")
for student in passed_students:
    print(f"  - {student[0]}: {student[1]}")


print("\n STUDENTS WHO FAILED:")
for student in failed_students:
    print(f"  - {student[0]}: {student[1]}")



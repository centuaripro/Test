
# inputs student name, student grade
# outouts average grade, pass or fail, summary

print("="*50)
print("" * 10 + "STUDENT TRACKER")
print("="*50)


num_students = int(input("How many students? "))

names = []
scores = []



for i in range(num_students):
    name = input(f"Enter student name: ")

    score = float(input(f"Enter student's score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score! Enter a number between 0 and 100.")
        score = float(input(f"Enter student's score (0-100): "))

    names.append(name)
    scores.append(score)

 # calculate average   
if num_students > 0:
    average = sum(scores)/len(scores)
    print("Average score:" , average)
else:
    average = 0

# pass/fail

for i in range(len(scores)):
    
    if scores[i] >= 60 and scores[i] <=100:
        print(names[i], ":", scores[i], "PASS")
    elif scores[i] >=0 and scores[i] < 60:
        print(names[i], ":", scores[i], "FAIL")

# Summary
print(names)
print(scores)
print("Highest score:" , max(scores))
print("Lowest score:" , min(scores))

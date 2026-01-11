state = "Kaduna"

print(state)
print(type(state))

print("")
print("------------------------------")
print("")

# Length of a string
print("****** String Length ******")
print("")
print(len("Kaduna"))

country = "Nigeria"

print("")
print("------------------------------")
print("")

# Transform to Lower case
print("****** Lower Case ******")
print("")
print(country.lower())

print("")
print("------------------------------")
print("")

# Transform to Uppercase
print("****** UpperCase ******")
print("")
print(country.upper())

print("")
print("------------------------------")
print("")

# Transform to Titlecase
event_name = "uefa champions league" 

print("****** TitleCase ******")
print("")
print(event_name.title())

age = "9089"
print(age.isnumeric ())


is_student = False
print("is_student", type(is_student))

print("====================")

# names = None
# print(bool(names))



greeting = "Hello, good morning"
print(greeting[3:5])

print(greeting[::-1])

# Strip
print("****** Strip ******")

username = " chris.idakwo@gmail.com "
print("Username", username)
print("Username", username.strip("  "))
print("-/user@gmail.com&-".strip("-&/"))

# lstrip removes leading character from the left hand side of the string 
print("Username", username.lstrip("  "))

# rstrip removes trailing character from the right hand side of the string
print("Username", username.strip("  "))

# String Concatenation
print("****** String Concatenation ******")

first_name = "John"
last_name = "Doe"
score = 80

full_name = first_name + " " + last_name
print("full name", full_name) 

# print out John Doe scored 80 out of 100
print(first_name + " " + last_name + " " "scored" + " " ,str(score) + " " "out of 180")

# print out John Doe scored 80 out of 100
sentence = (first_name + " " + last_name + "scored" + str(score) + "out of 180")


print("")
print("------------------------------")
print("")


# String formatting
print("****** string formating ******")
sentence_f = f"{first_name} {last_name} scored {score} out of 100"
print(sentence_f)

sentence_fa = "{fname} {lname} scored {sc} out of 100 for this session".format(
    fname=first_name, lname=last_name, sc= score
)
print(sentence_fa)

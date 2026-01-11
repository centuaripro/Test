
print("")
print("===============================")
print("password length check")
print("===============================")
print("")

# password = input("Enter a password: ")

# # Rules
# # At least one Uppercase Letter
# # At least one Lowercase Letter
# # 8 characters minimum

# min_len = len(password) >= 8
# has_uppercase = password.lower() != password
# has_lowercase = password.upper() != password

# print("Has ~ 8 characters", min_len)
# print("Has upper case", has_uppercase)
# print("Has lower case", has_lowercase)

# if min_len and has_uppercase and has_lowercase:
#     print('Welcome to Dev and Design!')
# else:
#     print("Your password is not secure enough")


print("")
print("")
print("===============================")
print("Grade Classification")
print("===============================")
print("")

# Take a score and convert to a grade letter, rsanging from A to F
# Where A is for scores between 85 and 100
# B is for scores between 70 and 85
# C is for scores between 55 and 70
# D is for scores between 45 and 55
# E is for scores between 30 and 45
# F is for scores below 30 ( 0 and 30)

score = input("Enter a score (0 10 100): ")

if score.isnumeric():
    score = int(score)

    if score >= 85 and score <= 100:
        print("Grade is A")
    elif score >= 70 and score < 85:
        print("Grade is B")
    elif score >= 55 and score < 70:
        print('Grade is C')
    elif score >=45 and score < 55:
        print(:Grade is D)
    elif score >=30 and score < 45:
        print("Grade is E")
    elif score >=0 and score < 30:
        print("Grade is F")
    print("Score: ", score)
else:
    print("Enter a valid number (0 to 100): ")




 





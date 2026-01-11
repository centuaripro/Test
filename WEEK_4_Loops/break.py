
# without loop control

# for num in range(1,10001):
#     guess = int(input("Guess the number: "))
#     if guess == 42:
#         found = True
#         print("Correct you gave found the number 42!")
    
#     if not found:
#         print("Try again!")


# with loop control

for num in range(1,10001):
    if num > 20:
        break 

    if num % 2 == 0:
        print(num)



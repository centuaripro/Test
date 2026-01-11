
name= input("Enter your name: ")
times = input("How many number of greetings? ")

if times.isnumeric():
    for i in range(int(times)):
        print(f"Hello {name}")
else:
    print("Enter a valid number")

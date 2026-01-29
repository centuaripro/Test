
file_path = "files/greeting.txt"
with open(file_path, "w") as file:
    file.write("Hello, this is a new line entry in a new file!\n")
    file.write("Hello, this is another new line\n")
    file.write("Now I am just having fun!\n")
    file.write("\n\n")
    file.write("="*80)
    file.write("\n\n")

    #Write multiple lines

    names = ["John Gospel", "Bisi Ade", "Mary Thomas","Tech World"]

    # Option 1 Introduce a new line character to each name in the list using a for loop

    newNames = []
    for name in names:
        if name != "Tech World":
            newNames.append(f"{name}\n")
    

    # option 2 Introduce a new line character for each namne in the list using a list comprehension

    newNames = [f"{name}\n"  for name in names]
    file.writelines(newNames)
        




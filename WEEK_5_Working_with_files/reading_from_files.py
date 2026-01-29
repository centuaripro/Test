
#Relative path

path_file = "files/example.txt"
with open(path_file, "r") as file:
    for line in file:
        print(line)

    # print("")

    # Reset the pointer back to the first line
    file.seek(0)

    content= file.read()
    for line in content.split("\n"):
        print(line)


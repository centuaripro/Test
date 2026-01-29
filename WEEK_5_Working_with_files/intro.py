
# Step 1- Opening and reading a file
# file = open("files/Sample - Superstore.csv","r")
# content = file.read()
# file.close()

# print(content)

# Absolute path - path to the file on on your laptop/ cloud

# Relative path  - path to the file python relative to the file importing it



# Step 2- Using 'with' statement ( best practice)
with open("files/Sample - Superstore.csv","r") as file:
    # Read header
    header = file.readline().strip()
    print("Columns:", header)

    for line in file:
        print(line.strip())
        print("="*20)
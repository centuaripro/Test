
import os
from pprint import pprint

# File and directory operations 
# process management
# Environmental variables
# Path Manipulation

cwd = os.getcwd()
print("\nMy current working directory is:")
print(cwd)
print("")

cwd_content = os.listdir()
print(cwd_content)
print("")

# cwd_content.sort()
# pprint(cwd_content)

exists = os.path.exists("example.txt")
if os.path.exists("C:\\Users\\HP\\Documents\\SOURCE CODE\\WEEK_7_Advanced_working_with_files\\example.txt"):
    print("example.txt found!")
else:
    print("Cannot find example.txt!")

if not os.path.exists("Sample Directory"):
    # Navigate into the directory and create a new file
    pass
else:
    # Create the new folder first
    pass

if os.path.exists("Sample path") is False:
    # Boolean expression has to be true for the code in the if block to run
    os.mkdir("Sample path")

# Create directory with try/except block
# try/catch
try:
    os.mkdir("Sample path")
    print("Sample path directory created!")
except FileExistsError:
    print("An error occured! Check to seee the directory does not exist.")

print("")
data_file = os.path.join('data', 'students', 'grades.txt')
full_path = os.path.abspath(data_file)
print(f"Absolute path: {full_path}")
print(data_file)
      





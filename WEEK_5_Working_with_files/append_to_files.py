
from datetime import datetime

file_path = "files/log.txt"

# add content to the end of an existing file
with open(file_path, "w") as file:
    file.write("New Entry:" + str(datetime.now()) + "\n")


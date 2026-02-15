
import csv

FILENAME = "files\house_prices.csv"

def read_csv_file(file_path):
    """"Read the content of a csv file using the python in-built CSV module"""

    with open(file_path,"r") as file:
        # The first thing you do in order to raed the content of a CSV file is to instantiate/create
        # a new instance of the CVS reader
        csv_reader = csv.reader(file)

        print("\nROWS IN DATA FILE")
        print("")
        for row in csv_reader:
            print(row) # list of values
            print("")
            
def read_csv_file_dict(file_path):

    with open(file_path, "r") as file:
        csv_reader = csv.DictReader(file)
        print("\nROWS IN DATA FILE")
        print("")
        for row in csv_reader:
            print(row) # row is a dictionary{column name: value}
            print("")


read_csv_file(FILENAME)
print("\n==============================n")
read_csv_file_dict(FILENAME)

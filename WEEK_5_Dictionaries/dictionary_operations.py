
# Adding new items to a dictionary

from pprint import pprint


person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets":{"dog": "Freida" , "cat": "sox"},
    "kids":["Joe", "Martha", "Sarah"]
}

if "first_name" in person:
    print("found the key: first_name")

pprint(person)

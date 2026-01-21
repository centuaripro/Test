
# get()  method

from pprint import pprint
print("")
print("")
print("===============================")
print("get () method")
print("===============================")
print("")

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets":{"dog": "Freida" , "cat": "sox"},
    "kids":["Joe", "Martha", "Sarah"]
}
print("\n")
print("first name (with get() method):", person.get("first_name"))
print("first name (without method):", person["first_name"])

print("\n")

print("")
print("")
print("===============================")
print("clear ( method)")
print("===============================")
print("")


person_b = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 50,
    "pets":{"dog": "Freida" , "cat": "sox"},
    "kids":["Joe", "Martha", "Sarah"]
}

person_b.clear()
pprint(person_b)

print("")
print("")
print("===============================")
print("copy() creates a shallow/copy of the dictionary")
print("===============================")
print("")

person_a = person.copy()
pprint(person)
print("")
pprint(person)
print("")

print("")
print("")
print("===============================")
print("items() - returns a list containing a tuple of each key value pair")
print("===============================")
print("")

pprint(person.items())

print("")
print("")
print("===============================")
print("values() - returns a list of all th values in the dictionary")
print("===============================")
print("")

pprint(person.values())
print("")

print("")
print("")
print("===============================")
print("keys() - returns a list of all th values in the dictionary")
print("===============================")
print("")

pprint(person.keys())
print("")

print("")
print("")
print("===============================")
print("pop() - removes the element with the specified key and returns the value")
print("===============================")
print("")

last_name = person.pop("last_name")
print("The last name is ", last_name)
pprint(person)
print("")
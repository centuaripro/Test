
# Patter 1: Filter

# Template

# results = []
# for item in []:
#     if condition:
#         results.append(item)

# Example Set: Find Expensive transactions

import csv

expensive_transactions = []
_transactions = None

with open("customer_transactions.csv") as file:
    _transactions = csv.DictReader(file)

    for transaction in _transactions:
        transaction["Purchase_Amount"] = float(transaction["Purchase_Amount"])

        if transaction["Purchase_Amount"]> 100:

            expensive_transactions.append(transaction)


# Pattern 2: Aggregate

# Template:

# total = 0

# for item in collection:
#     total = item.get("field") + total

# result = total/count

total_revenue = 0

for transaction in _transactions:
    total_revenue = total_revenue + float(transaction["Purchase_Amount"])

# Alternative appraich using a list  comprehension and the sum() function
transaction_revenue = sum([float(transaction["Purchase_Amount"]) for transction in _transactions])

average = total_revenue/len(list(_transactions))

# Pattern 3; Groupby

# Template

# groups = {}

# for item in collection:
#     key = item[field]
#     if key not in groups:
#         groups[key] = [] # = 0, = {}

#     groups[key].append(item)

# Example : Group transactions by category

transactions_by_categories = {}

for transaction in _transactions:
    category = transaction["Product_Category"]

    if category in transactions_by_categories:
        transactions_by_categories[category].append(transaction)

    else:
        transactions_by_categories[category] = 0


# Pattern 4: min/max
# Most often, the output of a min/max operation is numeric- either an integer or a float. However, sometimes it could be a date

# Example: Find the most valuable transaction

most_valuable_transaction = list(_transactions)[0]

for transaction in list(_transactions)[1:]:
    if transaction["Purchase_Amount"]> most_valuable_transaction["Purchase_Amount"]:
        most_valuable_transaction = transaction

# Patter 5: Transform
# filter + transform operation
# Example: Create a list of email addresses for vip customers only (assume there is a customer category column in the dataset
 
emails = []

for transaction in _transactions:
    if transaction["Group"] is "VIP":
        if transaction["Email"] not in emails:
            emails.append(transaction["Email"])

emails = set()
for transaction in _transactions:
    if transaction["Group"] is "VIP":
            emails.add(transaction["Email"])

# Extract Customer Names

customer_names = set()

for transaction in _transactions:
    customer_names.add(transaction["Customer_Name"])

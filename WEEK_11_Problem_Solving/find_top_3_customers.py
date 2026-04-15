
# Understand
# Input
# Output
# Pattern
# Skeleton
# Implement

def get_total_spent_amt(data):
    return data[1]
    

# Problem: find the top 3 customers based on total spent
from pprint import pprint
def find_top_3_customers(transactions):
    # Step 1 Group by customer and sum spending
    customer_totals = {}

    for transaction in transactions:
        # Extract customer name and purchase amount
        customer_id = transaction["Customer_Name"]
        purchase_amt = float(transaction["Purchase_Amount"])
                                   
        # TODO Recursively add the purchase amount for each customer
        if customer_id not in customer_totals:
            customer_totals[customer_id] = purchase_amt
        else:
            customer_totals[customer_id] += purchase_amt

    # Step 2   Convert to list and sort
    # TODO: Create a list of (ID, total) tuples
    # TODO: Sort by total in descending order

    top_customers = []

    for(customer_id, total_spent) in customer_totals.items():
        top_customers.append((customer_id, total_spent))

    top_customers.sort(key=get_total_spent_amt, reverse =True)
    top_customers = top_customers[:3] 

    # A one line implementation of the preceeding code

    # top_customers = sorted(customer_totals.items(), key =get_total_spent_amt, reverse = True)[:3]


    result = " | ".join([f"{cust[0]} - ${cust[1]:.1f}" for cust in top_customers])

    return result

    #pprint(customer_totals)

def main():
    import csv

    with open("files/customer_transactions.csv") as file:
        reader = csv.DictReader(file)

        transactions = []
        for item in reader:
            item["Purchase_Amount"] = float(item["Purchase_Amount"])
            transactions.append(item)

        result = find_top_3_customers(transactions)
        print(result)

main()
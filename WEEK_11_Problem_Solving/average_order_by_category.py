
# Understand
# Input
# Output
# Pattern
# Skeleton
# Implement
    

# Problem: Calculate the average order value by product categories

# 1. Understanding the problem set

# average order value = total sales amount/ total number of orders

from pprint import pprint

def average_order_by_category(orders):
    #step 1 Group by category, track the sum and count values for each category

    category_totals = {}
    category_counts = {}
    for order in orders:
        #  Get the category name and purchase amount
        category_name = order["Product_Category"]
        purchase_amt = order["Purchase_Amount"]

        # Recursively increment to total increement the count by (1).
        if category_name not in category_totals:
            category_totals[category_name] = purchase_amt
        else:
            category_totals[category_name] += purchase_amt

        if category_name not in category_counts:
            category_counts[category_name] = 1
        else:
            category_counts[category_name] += 1
        

    # Calculate the averages
    # Introduce a new variable to keep track of average value
    category_averages = {}

    # Loop through the category_totals, get the category name, the total order value
    #   Use the category name to retrieve the count/occurences

    for(category,total) in category_totals.items():
        count = category_counts[category]

    # Calculate the average using the total order value
        category_averages[category] = total/count

    print("")
    pprint(f"{'Product Category':<24} {'Avg Order Value(USD)':<8}")
    print("-"*60)

    for (cat, avg) in category_totals.items():
        print(f"{cat:<24} {avg:<8}")

    

    


def main():

    import csv

    with open("files/customer_transactions.csv") as file:
        reader = csv.DictReader(file)

        transactions = []
        for item in reader:
            item["Purchase_Amount"] = float(item["Purchase_Amount"])
            transactions.append(item)

        average_order_by_category(transactions)
        # print(result)

main()

import csv
from pprint import pprint
def load_transaction_data(filename):
    """Load sales data from CSV file"""
    transactions = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Convert numeric fields
                row['Purchase_Amount'] = float(row['Purchase_Amount'])
                transactions.append(row)
                
                
        
        return transactions
    
    except FileNotFoundError:
        print(f"Error: {filename} not found")
        return []
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

def build_customer_profiles(transactions):
    """
    Pattern: GroupBy Pattern
    """
    customer_profiles = {}
    for tx in transactions:
        customer_id = tx["Customer_ID"]

        if customer_id not in customer_profiles:
            customer_profiles[customer_id] = {
                "id": tx["Customer_ID"],
                "name": tx["Customer_Name"],
                "email": tx["Email"],
                "signup_date": tx["Signup_Date"],
                "transactions": [],
                "total_transactions":0,
                "total_spent": 0
                }
        customer_profiles["transactions"].append(tx)
        customer_profiles["total_spent"] += tx["Purchase_Amount"]
        

    return customer_profiles

def display_customer_summary(customer_profiles):

    # 1. Tota Unique customers
    total_unique_customers = len(customer_profiles.keys())

    

    # 2. Avearge transaction (count) per customer
    customer_transactions = []
    for profile in customer_profiles.values():
        customer_transactions.append(len(profile["transactions"]))
    
    avg_transactions = sum(customer_transactions)/ total_unique_customers
        
    # Alternative method for implememnting the preceeding code which is the average transaction per customer
    # total_transactions = sum([len(p["transactions"] for p in customer_profiles.values)])
    # avg_transactions = total_transactions/ unique_customer_count

    # 3. Average Spend per customer
    customer_total_spend = []

    for profile in customer_profiles.values():
        customer_total_spend.append(profile["total_spend"])

    avg_clv = sum(customer_total_spend) / total_unique_customers

    # Alternative method for implememnting the preceeding code which is the average spend per customer
    # total_spend = sum([len(p["total_spend"] for p in customer_profiles.values)])
    # avg_clv = total_spent/ unique_customer_count

    # 4. Most valuable customer

    mvp_customer = max(customer_profiles.values(), key = lambda x: x["total_spent"])

    return {
        "total_customers": total_unique_customers,
        "avg_tx_count_per_customer": avg_transactions,
        "avg_spend_per-customer": avg_clv,
        "mvp_customer": mvp_customer,
    }


    
    
def main():
    transactions = load_transaction_data("files/customer_transactions.csv")
    customer_profiles = build_customer_profiles(transactions)
    customer_summary = display_customer_summary(customer_profiles)

if __name__ == "__main__":
    main()
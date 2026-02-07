# Positional Vs Key word Arguments

def create_customer_profile(name, age, city, purchases):
    """ Create a Customer Profile Summary"""
    print(f"\nCustomer: {name}")
    print(f"Age: {age}")
    print(f"Location: {city}")
    print(f"Total Purchases: {purchases}")

    # In positional arguments,order matters
create_customer_profile("Alice", 28, "Newyork", 15)

# However in Keyword arguments, order do not matter.

create_customer_profile(city="Lagos", name="Bob, purchases=8, age=15")

# You can also mix positional arguments and key word arguments. However, when you do, positional arguments must come first
create_customer_profile("chris", 28, city="Owerri", purchases=10)
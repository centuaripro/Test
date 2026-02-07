
# What is scope?
# scope where python "see" your variable

# 1. Global Scope(The Living Room)
# Variables at the main level- everybody can see them.

# This is Global - created outside any function, class etc.

customer_name = " Alice"

def greet():
    # Inside this function, we can see the global variable
    print(f"Hello, {customer_name}")

greet() # works Prints: Hello,Alice
print(customer_name) # works Prints: Alice

# 1. local Scope(The Bedroom)
# Variables created inside a function can only beseen by that function

def calculate_tax():
    # The variable "tax_rate" is LOCAL and only exists inside the function calculate_tax
    tax_rate = 0.08
    return tax_rate * 100

print(calculate_tax()) # Works, Prints: 8.0
try: 
    print(tax_rate) # Error! Cant see tax_rate outside of the "calculate_tax" function
except:
    print("Cannot see tax_rate outside of the calculate_tax function")


# ------------------------------------------------
# READING GLOBAL VARIABLE
# ------------------------------------------------

discount_rate = 0.10

def calculate_discount(price):
    discount = price * discount_rate
    return discount
print(calculate_discount(800))

# ------------------------------------------------
# REASSIGNING GLOBAL VARIABLE
# ------------------------------------------------

def calculate_total_a(price):
    discount_rate = 0.13 # re-assigned the value of discount_rate
    discount = price * discount

    # Here the value of 'discount_rate' has been temporarily re-assigned (within the function) to a new value
    # However, the initialvalue of the variable remains the same outside of the function.

    print("What is discount rate?", discount_rate)

    return price - discount

# ------------------------------------------------
# MODIFYING GLOBAL VARIABLE
# ------------------------------------------------

def calculate_total_b(price):
    global discount_rate

    # Cant modify global variables in this manner(within a function)
    # except the case where teh global keyword is used(just like above) to notify python that the variable
    # referenced from the global scope
    # Any change/modification made to the value of the variable at this point will also be reflecetd  at the global scope
    discount_rate = discount_rate + 0.02
    discount = price * discount_rate

    # print("What is discount rate 1?", discount_rate)

    return price - discount
calculate_total_b(800)

# print(calculate_total(800))
# print("What is discount rate 2?", discount_rate)







def calculate_discount_rate(price, discount_rate=0.10):
    """Calculate Price afetr Discount"""
    discount_amount= price * discount_rate
    net_amount= price - discount_amount
    return net_amount

    print("What is the value of the discount_rate", discount_rate)


# When you call a function with a default parameter, its legal/okay to not provide an argument in place of the parameter
amount= calculate_discount_rate(850)



print("Amount:", amount)

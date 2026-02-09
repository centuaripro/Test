
from pprint import pprint
petshop = {
    "animals": {
        "dogs": {"Labrador": 3, "Beagle": 2, "Poodle": 1, "Mastiff": 5},
        "cats": {"Persian": 2, "Siamese": 1, "Maine Coon": 2},
        "fish": {"Goldfish": 12, "Angelfish": 5, "Betta": 3},
        "birds": {"Parakeet": 4, "Canary": 3, "Cockatiel": 7}
    },
    "supplies": {
        "food": {"Dog Food": 20, "Cat Food": 9, "Fish Food": 25},
        "toys": {"Dog Toys": 30, "Cat Toys": 20},
        "habitats": {"Aquariums": 5, "Cat Trees": 8, "Dog Beds": 7}
    },
}
def get_category(stock_categories):
    category = input(f"Enter the category ({",".join(stock_categories)}:")

    while not(category in stock_categories):
        print("")
        category = input(f"Invalid category. Choose from the options {",".join(stock_categories)}:")
   
    return category

def get_sub_category(stock_sub_categories):
    # Ask the user to select from the avialble subcategories in our inventory stock
    # TODO: Take home. Introduce validation just the 'get category()' function
    return input("Select from the available sub-categories: "+", ".join (stock_sub_categories))

def get_selected_product(stock_products):
    
    # Ask the user to select the stock they want from our inventory
    return input(f"What product do you want? ({",".join(stock_products.keys())}):")

def get_requested_qty(stock_qty):   
    # Ask the user to provide the quantity they want to buy, while also displayiong the available qauntity
    requested_qty = int(input(f"\nHow many do you want? (Available Qty:{stock_qty})? "))

    # Ensure that the quantity requested by the user is not more than waht is available in the stock
    while requested_qty>stock_qty:
        requested_qty = int(input(f"Sorry we only have {stock_qty} in stock:"))
    return requested_qty
        
def get_low_stock_supplies(supplies):
    """"Returns a list of products that are low in stock (<10 qty). 
    Each product entry is a dictionary.
    """
    ## Task 2

    #Create a shopping list of supplies that are low in stock (fewer than 10)

    # Approach 1
    low_stock_products =[]

    supplies = petshop["supplies"]

    for(subcategory,products) in supplies.items():
        for product, qty in products.items():
            if qty < 10:
                low_stock_products.append(product)

    print(low_stock_products)

    # Approach 2

    shopping_list =[
        item
        for products in supplies.values()
        for item, qty in products.items()
        if qty < 10
    ]

    print(shopping_list)

def get_most_varied_product(animals):
    # Docstring for get_most_varied_products
    
    ### Task 3

    # Find which animal type has the most variety. 
    # Variety in this case means the animal with the most headcount and number of breeds.


    max_variety = 0
    most_varied_animal = None


    for sub_category, breeds in animals.items():
        num_of_breeds = len(breeds.keys())
        head_count = sum(breeds.values())

        variety = num_of_breeds + head_count

        if variety > max_variety:
            max_variety = variety
            most_varied_animal = sub_category

        
    return {
        "product": most_varied_animal,
        "variety_count": max_variety
    }

def main():
    """Entry point into the application"""
    print("\n")
    print("="*60)
    print("PETSHOP INVENTORY")
    print("="*60)
    print("\n")

    stock_categories = petshop.keys()
    category = get_category(stock_categories)

    stock_sub_categories = petshop[category].keys()
    sub_category = get_sub_category(stock_sub_categories)

    # Get the products and their quantity for the selceted sub_category
    stock_products = petshop[category][sub_category]

    selected_product = get_selected_product(stock_products)

    # Get the inventory stock quantity for the product selected
    stock_qty = petshop[category][sub_category][selected_product]

    requested_qty = get_requested_qty(stock_qty)

    

    # Reduce the requested quantity from what is available in stock
    petshop[category][sub_category][selected_product] = stock_qty - requested_qty

    print("")

    print("\n")
    low_stock_supplies = get_low_stock_supplies(petshop["supplies"])

    print("="*30)
    print("Low-stock_products")
    print("="*30)
    print("Low_stock_supplies")

    print("\n")
    most_varied_product = get_most_varied_product(petshop["animals"])
    print("="*30)
    print("Most-varied product")
    print("="*30)
    pprint(most_varied_product)

    
    

main()
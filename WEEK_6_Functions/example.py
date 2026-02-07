
def calculate_average(sales_data):
    """Calculate average of sales values"""
    total_sales_value = 0
    total_sales_count = 0

    for sale in sales_data:
        total_sales_value += sale
        total_sales_count += 1
    
    average = total_sales_value/ total_sales_count
    return average

north_sales = [1200, 850, 210, 1450, 980]
south_sales = [1500, 920, 1800, 1100, 2200 ]
east_sales = [1100, 1300, 950, 1700, 1200 ]

print(f"North Average: ${calculate_average(north_sales)}")
print(f"South Average: ${calculate_average(south_sales)}")
print(f"East Average: ${calculate_average(east_sales)}")

print("\n\n")
def calculate_average_alt(sales_data,region):
    """Calculate average of sales values"""
    total_sales_value = 0
    total_sales_count = 0

    for sale in sales_data:
        total_sales_value += sale
        total_sales_count += 1
    
    average = total_sales_value/ total_sales_count
    
    print(f"{region} Average: ${average}")
sales = {
    "North": [1200, 850, 210, 1450, 980],
    "South": [1500, 920, 1800, 1100, 2200],
    "East": [1100, 1300, 950, 1700, 1200 ],
}

for region, sales_data in sales.items():
    calculate_average_alt(sales_data, region)



# # Analysing data for the North region

# north_total = 0
# north_count = 0


# for sale in north_sales:
#     north_total += sale # This is a short hand method of writing the addition operation below
#     # north_total = north_total + sale

# north_average = north_total/north_count
# print(f"North Average: ${calculate_average(north_sales):.2f}")
# print(f"SouthAverage: ${calculate_average(south_sales):.2f}")
# print(f"East Average: ${calculate_average(east_sales):.2f}")


# # Analysing data for the South region

# south_total = 0
# south_count = 0

# for sale in south_sales:
#     south_total += sale # This is a short hand method of writing the addition operation below
#     # south_total = south_total + sale

# south_average = south_total/south_count

# # Analysing data for the East region

# east_total = 0
# east_count = 0


# for sale in east_sales:
#     east_total += sale # This is a short hand method of writing the addition operation below
#     # east_total = east_total + sale

# east_average = east_total/east_count

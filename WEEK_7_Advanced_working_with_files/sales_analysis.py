
from sales_utils import calculate_total,calculate_average,find_top_sales,TAX_RATE
monthly_sales = [1200, 850, 2100, 1450, 980, 735, 839, 370]

total = calculate_total(monthly_sales)
average = calculate_average(monthly_sales)
top= find_top_sales(monthly_sales)

print("")
print(f"Total: ${total:,.2f}")
print(f"Average: ${average:,.2f}")
print(f"Top: ${top:,.2f}")
print(f"Tax Rate: ${TAX_RATE:,.2f}")
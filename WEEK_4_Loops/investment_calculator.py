
# Ask for initial investment
# Ask for Annual interest rate (as percentage)
# Ask for number of years 
# Calculate value each year, with compund interest
# Display year-year growth
# Show total profit at the end

print("")

investment_amt = float(input("Enter initial investment amount: "))
interest_rate = float(input("Enter Annual interest rate (%): "))
years = int(input("Enter number of years: "))

print("\n" + "="*50)
print("INVESTMENT GROWTH PROJECTION")
print("="*50)
print(f"Initial investment: ₦{investment_amt:,.2f}")
print(f"Interest rate: {interest_rate} %")
print(f"Investment period: {years} years")

current_amt = investment_amt

# use for loop to calculate and display year-year growth
for years in range(1, years + 1):

    # calculate the interest earned for teh current year

    interest_earned = current_amt *(interest_rate/100)

    #calculate curent value of investment

    current_amt = current_amt *(1 + interest_rate/100)

    # Display year-year growth

    print(f"Year {years}: ₦{current_amt:,.2f} | Interest ₦{interest_earned:,.2f}")


total_profit = current_amt - investment_amt

print("="*50)
print(f"Final amount: ₦{current_amt:,.2f}")
print(f"total_profit: ₦{total_profit:,.2f}")
print(f"Return on investment: {(total_profit/investment_amt)*100:,.2f}%")
print("="*50)
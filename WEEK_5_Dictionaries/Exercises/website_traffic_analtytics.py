
# As a data analyst , your job is to analyse the website traffic data of an ecommerce company.




#Problem
# You have a log of page visits from 50 users. You need to : 
# 1. Count how many time each page was visited.
# 2. find the most and least populous pages.
# 3. calculate what percenatge of traffic each page receives
# 4. identify pages with low traffic 

import random
from pprint import pprint

pages = [ "products", "product profile", "about", "home", "checkout", "cart", "contact"]
users = 50

log_of_pages_visited = []

for i in range(50):
    rounds = random.randint(3,20)

    for take in range(rounds):
        index = random.randint(0,6)
        log_of_pages_visited.append(pages[index])

print(len(log_of_pages_visited))
print(log_of_pages_visited[:20])

pprint(log_of_pages_visited)
# Step 1 Count page visits
# Use Dictionaries to count frequency- a fundamental data science task

page_counts = {}
 
print("")
for page in log_of_pages_visited:
    if page in page_counts:
        page_counts[page] = page_counts[page] + 1
    else:
        page_counts[page] = 1



pprint(log_of_pages_visited)
print("\n")
pprint(page_counts)


# Step 2

all_counts = page_counts.values()
max_visits = max(all_counts)
min_visits = min(all_counts)

print("\nMost popular pages:")
for(key, value) in page_counts.items():
    # In this context, the key is the page name while the value is the visit frequency
    if value == max_visits:
        print(f"   -{key}: {value} visits")

print("\nLeast popular pages:")
for(key, value) in page_counts.items():
    if value == min_visits:
        print(f"   -{key}: {value} visits")



#step 3
# calculate traffic percentage
# convert page vist count to percentage for better insight

total_visits = sum(page_counts.values())

print(f"\nTotal visits:{total_visits}")
print("\nTraffic distribution")

page_percentages = {}

for(key, value) in page_counts.items():
     # In this context, the key is the page name while the value is the visit frequency

    percentage = (value/total_visits)* 100
    page_percentages[key] = f"{percentage:.1f}"
    print(f"   {key}: {value} visits ({page_percentages[key]}%)")


# Step 4 Attend to pages needing promotion
# Concept use conditional logic with dictionary data to generate insight
low_traffic_threshold = 13 # percentage
low_traffic_pages = {}

print("\nPAGES NEEDING PROMOTION (<13% of traffic):")


for (key,value) in page_percentages.items():
    percentage_value = float(value)

    if percentage_value <= low_traffic_threshold:
        low_traffic_pages[key] = percentage_value

if len(low_traffic_pages) == 0:
    print("All pages have adequate traffic")
    
else:
    pprint(low_traffic_pages)



# print("")
# print("==================================")
# print("""
#     Student Grades Tracker Project
#     Author: Ekpjoka Chris Idokwo
#     Description: A program that tracks students grades, calculates average
#  """)
# print("=======================================")
# print("")

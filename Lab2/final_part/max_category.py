import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv", index_col ="Ticket No")

# Group by month and sum the volume
tickets_per_category = data.groupby('Category').size()

# Check the results
print(tickets_per_category)
# Extracting the minimum and maximum number of tickets per category 
min_category=tickets_per_category.min()
max_category=tickets_per_category.max()


print("Category(s) having the minimum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_category.loc[tickets_per_category==min_category].index.tolist(),min))

print("Category(s) having the maximum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_category.loc[tickets_per_category==max_category].index.tolist(),max))

# Group by subcategory and sum the tickets
tickets_per_sub_category = data.groupby('Sub Category').size()

# Check the results
print(tickets_per_sub_category)

# Extracting the minimum and maximum number of tickets per category 
min_sub_category=tickets_per_sub_category.min()
max_sub_category=tickets_per_sub_category.max()

print("Sub Category(s) having the minimum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_sub_category.loc[tickets_per_sub_category==min_sub_category].index.tolist(),min))

print("Sub Category(s) having the maximum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_sub_category.loc[tickets_per_sub_category==max_sub_category].index.tolist(),max))

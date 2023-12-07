import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")

# Group by month and sum the volume
tickets_per_state = data.groupby('State').size()

# Check the results
print(tickets_per_state)

# Extracting the minimum and maximum number of tickets 
min=tickets_per_state.min()
max=tickets_per_state.max()

print("State(s) having the minimum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_state.loc[tickets_per_state==min].index.tolist(),min))

print("State(s) having the maximum number of ticket(s) are \n{}\nwith {} ticket(s)".
      format(tickets_per_state.loc[tickets_per_state==max].index.tolist(),max))
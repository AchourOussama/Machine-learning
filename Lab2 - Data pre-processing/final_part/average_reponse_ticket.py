import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv", index_col ="Ticket No")
desc = data.describe()
print(desc) 

data['begin']=pd.to_datetime(data['Create Date'],format='%m/%d/%Y %H:%M')
data['end']=pd.to_datetime(data['Picked Date'],format='%m/%d/%Y %H:%M')

# Calculate the time difference between 't2' and 't1'
data['time_difference'] = data['end'] - data['begin']

# Check results
print(data['time_difference'])

# Calculate the average time difference
average_time_difference = data['time_difference'].mean()
print(f"Average Time Difference: {average_time_difference}")

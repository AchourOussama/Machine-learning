import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv("Lab2/final_part/Ticket_Details.csv", index_col ="Ticket No")


data['date_column'] = pd.to_datetime(data['Create Date'])

# Create a new column for the month
data['month'] = data['date_column'].dt.to_period('M')

# Check the results of the conversion
for (i,j,k) in zip(data['Create Date'],data['date_column'],data['month']) : 
    print("{}  {}  {}".format(i,j,k))

# Group by month and sum the volume
monthly_volume = data.groupby('month').size()

# Check the results
print(monthly_volume)

# Plot the results

monthly_volume.plot(kind='bar', color='blue')
plt.title('Monthly Volume')
plt.xlabel('Month')
plt.ylabel('Tickets number Volume')
plt.show()
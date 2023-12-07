import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv", index_col ="Ticket No")

# Group by month and sum the volume
customer_rate = data.groupby('Customer Rating').size()

# Check the results
print(customer_rate)

# Plot the results
customer_rate.plot(kind='bar', color='blue')
plt.title('Customer Rating')
plt.xlabel('Rate')
plt.ylabel('Customers')
plt.show()
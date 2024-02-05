import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")
priority = data.groupby('Priority')['Ticket No'].count().reset_index()

# Plot
plot=priority.plot(x = 'Priority', y = 'Ticket No', kind='bar', color='blue')
for index, row in priority.iterrows():
    plot.text(row.name, row['Ticket No'], row['Ticket No'], ha = 'center', va = 'bottom')

plt.title("Tickets by Priority")    
plt.ylabel("Tickets")
plt.show()
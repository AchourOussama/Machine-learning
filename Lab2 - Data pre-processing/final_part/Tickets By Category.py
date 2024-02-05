import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")
category_group = data.groupby('Category')['Ticket No'].count().reset_index()

# Plot results  
plot=category_group.plot(x = 'Category', y = 'Ticket No', kind='bar', color='blue')
for index, row in category_group.iterrows():
    plot.text(row.name, row['Ticket No'], row['Ticket No'], ha = 'center', va = 'bottom')
    
plt.title("Tickets by Category") 
plt.ylabel("Tickets")
plt.show()
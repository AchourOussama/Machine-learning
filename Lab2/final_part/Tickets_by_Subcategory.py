import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")
Subcategory_group = data.groupby('Sub Category')['Ticket No'].count().reset_index()

# Plot results  
plot=Subcategory_group.plot(x = 'Sub Category', y = 'Ticket No', kind='bar', color='blue')
for index, row in Subcategory_group.iterrows():
    plot.text(row.name, row['Ticket No'], row['Ticket No'], ha = 'center', va = 'bottom')
    
plt.title("Tickets by Sub Category") 
plt.ylabel("Tickets")
plt.show()
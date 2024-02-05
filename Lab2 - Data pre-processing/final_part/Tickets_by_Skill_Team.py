import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")
teams = data.groupby('Skill Team')['Ticket No'].count().reset_index()

plt.pie(teams['Ticket No'], labels = teams['Skill Team'], autopct = "%.0f%%")
plt.title("Tickets by Skill Team")
plt.show()
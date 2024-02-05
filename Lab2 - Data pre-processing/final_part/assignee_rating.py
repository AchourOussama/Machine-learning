import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("Lab2/final_part/Ticket_Details.csv")

# Extract the numerical value of each rate (ranging from 1 to 5)
data['Numeric Rating'] = data['Customer Rating'].str.extract('(\d+)').astype(float)
print("Numeric rating\n",data['Numeric Rating'])
print("\n")
# Calculate mean ratings
mean_ratings = data.groupby('Assignee')['Numeric Rating'].mean().reset_index()
print("Mean ratings\n",mean_ratings)
print("\n")
# Sort by mean rating in descending order
sorted_ratings = mean_ratings.sort_values(by='Numeric Rating', ascending=False)

# Display the assignees performances
print("Assignees ranked performance\n",sorted_ratings)
print("\n")
# Display top performer
top_performer = sorted_ratings.iloc[0]
print("Top performing assignee:{}\nscore:{}".format(top_performer['Assignee'],top_performer['Numeric Rating']))
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("salesData.csv", index_col ="month_number")

months=np.array(data.index.values)

profits = []
for column in data.columns[0:-2]:
    profit = sum(data[column])
    profits.append(profit)

plt.title('Sales Data')
plt.pie(profits, labels=data.columns[0:-2], autopct='%.1f%%')
plt.legend(data.columns[0:-2], loc=4)
plt.savefig("Figures/figureQ5.jpg")
plt.show()


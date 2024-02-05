import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salesData.csv", index_col ="month_number")
months=data.index.values

ax=plt.axes()

ax.set_xticks(range(1,13))

ax.set_xlabel("Month number")
ax.set_ylabel("Sale units in number")

ax.set_ylim([1000,18000])

for column in data.columns[0:-2]:
    values=np.array(data[column])
    plt.plot(months, values, marker='o', linewidth=2)

plt.legend(data.columns[0:-2]+' Sales Data', loc=2)
plt.title("Sales data")
plt.savefig("Figures/figureQ3.jpg")
plt.show()

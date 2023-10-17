import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salesData.csv", index_col ="month_number")

months=np.array(data.index.values)
toothpaste=np.array(data["toothpaste"])

ax=plt.axes()
ax.grid(True,linestyle="--")

ax.set_xticks(range(1,13))

ax.set_xlabel("Month number")
ax.set_ylabel("Number of units sold")

plt.scatter(months,toothpaste)
plt.legend(["Toothpaste Sales data"], loc=2)
plt.title("Toothpaste Sales data")
plt.savefig("Figures/figureQ4.jpg")
plt.show()


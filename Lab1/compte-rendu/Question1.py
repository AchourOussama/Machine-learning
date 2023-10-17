import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salesData.csv", index_col ="month_number")
months=data.index.values
profits=data["total_profit"].values


y_inf=100000
y_sup=500000

ax=plt.axes()

ax.set_xticks(range(1,13))
ax.set_yticks([100000,200000,300000,400000,500000])


ax.set_ylim([y_inf,y_sup])

ax.set_xlabel("Month number")
ax.set_ylabel("Total profit")


plt.plot(months,profits)
plt.title("Company profit per month")
plt.savefig("Figures/figureQ1.jpg")
plt.show()



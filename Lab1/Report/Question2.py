import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("salesData.csv", index_col ="month_number")
months=data.index.values
profits=data["total_profit"].values


y_inf=100000
y_sup=500000

ax=plt.axes()

ax.set_xticks(range(1,13))
ax.set_yticks(range(y_inf,y_sup+1,100000))

ax.set_ylim([y_inf,y_sup])

ax.set_xlabel("Month number")
ax.set_ylabel("Profit in dollar")

plt.plot(months,profits,marker="o",color="r" , mec="k",mfc="k", linestyle="--", linewidth="3")
plt.legend(["Profit data of last year"], loc=4)
plt.title("Company Sales data of last year")
plt.savefig("Figures/figureQ2.jpg")
plt.show()




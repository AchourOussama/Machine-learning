import matplotlib.pyplot as plt


values1 = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]

ax = plt.axes()
ax.set_xlabel("Entries")
ax.set_ylabel("Values")

plt.plot(range(len(values1)), values1, marker="s")
plt.plot(range(len(values2)), values2, marker="*", mec="g")

plt.annotate("Sommet", [7, 10])
plt.legend(["First", "Second"], loc=9)
plt.savefig("partie1/Figures/figureQ2.jpg")
plt.show()
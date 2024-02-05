import matplotlib.pyplot as plt



values1 = [1, 5, 8, 9, 2, 0, 3, 10, 4, 7]
values2 = [3, 8, 9, 2, 1, 2, 4, 7, 6, 6]

plt.plot(range(len(values1)), values1)
plt.plot(range(len(values2)), values2)

plt.savefig("partie1/Figures/figureQ1.jpg")
plt.show()    
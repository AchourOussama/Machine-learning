import matplotlib.pyplot as plt
import numpy as np

age = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
speed = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

age1 = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
speed1 = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112, 91, 80, 85])

ax = plt.axes()
ax.set_xlabel("Age")
ax.set_ylabel("Speed")

plt.scatter(age, speed)
plt.scatter(age1, speed1)
plt.savefig("partie1/Figures/figureQ3.jpg")
plt.show()
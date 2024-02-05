import matplotlib.pyplot as plt
import numpy as np

x = np.array(["MPI", "RT", "IIA", "IMI"])
y = np.array([16.5, 15.8, 14.9, 13.7])

plt.bar(x, y)

plt.show()
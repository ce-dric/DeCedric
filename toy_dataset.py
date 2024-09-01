import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)
x = np.random.rand(100, 1)
y = 5 + 2 * x + np.random.rand(100, 1)

plt.scatter(x, y)
plt.show()
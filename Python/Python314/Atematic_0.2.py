"""
Practice on plots and graphs
A perfect circle
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 200)
y = (1 - (x**2)) ** 0.5
z = -((1 - (x**2)) ** 0.5)
fig, ax = plt.subplots()
ax.plot(x, y, color="red", label="Positive 'y' value")
ax.plot(x, z, color="green", label="Negative 'y' value")
ax.set_aspect("equal")
ax.set_title("Simple plot")
plt.legend()
plt.grid()
plt.show()

"""
Practice on matplotlib integrated with numpy
"""

import matplotlib.pyplot as plt
import numpy as np

XSTART = 0
XSTOP = 2 * np.pi
INCREMENT = 0.001

x = np.arange(XSTART, XSTOP, INCREMENT)
y = np.sin(x)
z = np.cos(x)
plt.subplot(2, 1, 1)
plt.plot(x, y, "g")
plt.title("sin")
plt.xlabel("x")
plt.ylabel("sin (x)")
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(x, z, "r")
plt.title("cos")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid()
plt.show()

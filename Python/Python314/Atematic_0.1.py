"""
Current-time model for Lithium-ion batteries
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(0, 101)
INIT_CURRENT = 100
k = 6 / (np.exp(1) - 1)
voltage_discharge = (INIT_CURRENT - ((np.exp(x / (12.5625)) - 1) * k) / 100)
plt.gca().set_facecolor('white')
plt.xlabel('Time (Percentage time)', color='black')
plt.ylabel('Current (Percentage Amperes)', color='black')
plt.title('Lithium-ion Battery Voltage during Discharge')
plt.plot(x, voltage_discharge, color='black', label='Discharge rate')
plt.gca().set_aspect(2/3)
plt.grid()
plt.legend()
plt.show()

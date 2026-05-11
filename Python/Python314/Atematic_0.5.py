"""
Trial on trajectory graph
"""

import matplotlib.pyplot as plt
import numpy as np

while True:
    try:
        radians = float(input("angle(degree): "))
        velocity = float(input("velocity: "))
        acceleration = float(input("acceleration: "))
        break
    except ValueError:
        print("All the concerned variables are either integers or floats")
        continue

angle = radians * np.pi / 180

maximum_height = velocity**2 * (np.sin(angle) ** 2) / (2 * acceleration)

total_time = (2 * velocity * np.sin(angle)) / acceleration

distance = (velocity**2) * np.sin(2 * angle) / acceleration

time_stamp = np.linspace(0, total_time, 100)

range = abs(velocity * np.cos(angle) * time_stamp)

height = (velocity * np.sin(angle) * time_stamp) - (0.5 * acceleration * time_stamp**2)

print(f"maximum height = {maximum_height:.3f} metres")
print(f"time taken = {total_time:.3f} seconds")
print(f"range = {distance:.3f} metres")

plt.plot(range, height)
plt.grid()
plt.show()

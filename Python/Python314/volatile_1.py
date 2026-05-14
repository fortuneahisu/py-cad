"""This code simulates the projectile motion of an object under the influence of gravity.
It calculates the trajectory of the object and plots it using Matplotlib."""

import matplotlib.pyplot as plt
import numpy as np

GRAVITY = np.array([0.0, -9.81])
DT = 0.001

angle = np.radians(input('Angle: '))
SPEED = input('Speed: ')

position = np.array([0.0, 0.0])

velocity = np.array([SPEED * np.cos(angle), SPEED * np.sin(angle)])

x_points = []
y_points = []

while position[1] >= 0:
    x_points.append(position[0])
    y_points.append(position[1])

    velocity += GRAVITY * DT
    position += velocity * DT

plt.plot(x_points, y_points)
plt.xlabel("x position")
plt.ylabel("y position")
plt.title("Projectile Motion")
plt.grid()
plt.show()

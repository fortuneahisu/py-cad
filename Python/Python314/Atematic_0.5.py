"""
Trial on trajectory graph
"""
import numpy as np
import matplotlib.pyplot as plt
while True:
    try:
        angle = float(input('θ: '))
        u = float(input('init_velocity: '))
        g = float(input('acel_due_to_gravity: '))
        break
    except ValueError:
        print('angle;init_velocity;acel_due_to_gravity===int;float!')
        continue
theta = np.pi * angle / 180
maximum_height = u ** 2 * (np.sin(theta) ** 2) / (2 * g)
total_time = (2 * u * np.sin(theta)) / g
distance = u ** 2 * np.sin(2 * theta) / g
t = np.linspace(0, total_time, 100)
x = u * np.cos(theta) * t
y = ((u * np.sin(theta) * t) - (0.5 * (g * (t ** 2))))
print(f'maximum height = {maximum_height:.3f} metres')
print(f'time taken = {total_time:.3f} seconds')
print(f'range = {distance:.3f} metres')
plt.plot(x,y)
plt.show()

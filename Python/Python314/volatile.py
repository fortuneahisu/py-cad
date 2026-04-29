"""Built specifically for fleeting demonstration of concepts"""
import numpy as np
ANGLE = 60
GRAVITY = 9.80665
INIT_VEL = 45
KT = 0.001
x = 0
y = 0
vx = INIT_VEL * np.cos(ANGLE)
vy = INIT_VEL * np.sin(ANGLE)
position = [x, y]
velocity = [vx, vy]
print(velocity)
while True:
    vx = vx + GRAVITY * KT
    vy = vx + GRAVITY * KT
    position[0] = [vx * KT]
    position[1] = [vy * KT]
    print(velocity)
    print(position)
    break

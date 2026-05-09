"""
Motion simulation project
"""
from math import sin, cos, pi
import cmath

def motion_simulator():
    """
    Motion physics simulator
    """
    while True:
        position = np.array([0.0, 0.0])
        dt = np.array([0.001, 0.001])
        step = np.array([0.0, 0.0])
        turn_angle = 1
        angle = 0
        radians = angle/180 * pi
        control = input('Control: ').lower()
        if control == 'w':
            step += dt
        elif control == 's':
            step -= dt
        elif control == 'a':
            angle -= turn_angle
        elif control == 'd':
            angle += turn_angle
        else:
            print('Huh, 😕')
        if angle >= 360 or angle <= -360:
            angle = 0
        velocity_x = sin(radians) * step
        velocity_y = cos(radians) * step
        velocity = cmath.sqrt(velocity_x ** 2 + velocity_y ** 2)
        x += velocity_x
        y += velocity_y
        print(x)
        print(y)
        print(radians)
        print(angle)
        print(radians)
        print(step)
        print(velocity_x)
        print(velocity_y)






motion_simulator()

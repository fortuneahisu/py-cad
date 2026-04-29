"""
Motion simulation project
"""
from math import sin, cos, pi


def motion_simulator():
    """
    Motion physics simulator
    """
    step = 0
    angle = 0
    radians = angle/180 * pi              # in degrees
    x = 0                                 # basic dimensioning
    y = 0                                 # basic dimensioning
    while True:
        control = input('Enter W, A, S, D to move').lower()
        if control == 'w':
            step += 5
        elif control == 'a':
            angle -= 5
        elif control == 'd':
            angle += 5
        elif control == 's':
            step -= 5
        else:
            print('Huh, 😕')
            continue
        velocity_x = sin(radians) * step
        velocity_y = cos(radians) * step
        if angle >= 360 or angle <= -360:
            angle = 0
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

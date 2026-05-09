"""
Motion simulation project
"""
from math import sin, cos
import cmath
import numpy as np

def motion_simulator():
    """
    Motion physics simulator
    """
    pi = 3.1415926535897932384626433832795
    position = np.array([0.0, 0.0])
    step_length = np.array([1.0, 1.0])
    velocity = np.array([0, 0])
    turn_angle = pi/4
    angle = 0
    while True:
        try:
            if (angle + turn_angle) > 2*pi or (angle - turn_angle) < -2*pi:
                angle = 0
            trig_equalizers = np.array([sin(angle), cos(angle)])
            control = input('Control: ').lower()
            if control == 'w':
                position += step_length * trig_equalizers
                continue
            elif control == 's':
                position -= step_length * trig_equalizers
                continue
            elif control == 'a':
                angle -= turn_angle
                continue
            elif control == 'd':
                angle += turn_angle
                continue
            elif control == 'break':
                break
        except ValueError:
            print('Nope')
        except TypeError:
            print('Nope')






motion_simulator()

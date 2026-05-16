"""
This attempts to simulate positions vectorially
"""

import random
from math import cos, pi, sin

import matplotlib.pyplot as plt
import numpy as np



def motion_simulator():
    """
    Cartesian vectorial positioning
    """
    # pi = 3.141592653589793228841971693993114819665930005738
    # unnecessary precision to the 48th decimal
    x_path = [0]
    y_path = [0]
    position = np.array([0.000, 0.000])
    step_length = np.array([0.100, 0.100])
    turn_angle = pi / 30
    angle = 0
    while True:
        try:
            control = input("Control: ").lower()
            if control in ["break", "q", "quit", "stop"]:
                print(f"Ended at {position} facing {(angle / pi * 180) % 360} degrees")
                break
            for value in control:
                trig_equalizers = np.array([cos(angle), sin(angle)])
                if value == "w":
                    position += step_length * trig_equalizers
                    x_path.append(position[0])
                    y_path.append(position[1])
                elif value == "s":
                    position -= step_length * trig_equalizers
                    x_path.append(position[0])
                    y_path.append(position[1])
                elif value == "a":
                    angle += turn_angle
                elif value == "d":
                    angle -= turn_angle
        except ValueError as error:
            print(error)
        except AttributeError as error:
            print(error)
    travel_path(x_path, y_path)


def travel_path(x_path, y_path):
    """Trace the path of the player"""
    _, ax = plt.subplots()
    color = random.choice(["red", "blue", "green", "pink", "black"])
    ax.plot(x_path, y_path, color=color, label="Travel path")
    ax.set_aspect("equal")
    ax.set_title("Cartesian vectorial positioning")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    motion_simulator()

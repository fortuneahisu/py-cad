"""
This attempts to simulate positions vectorially
"""

from math import cos, pi, sin

import matplotlib.pyplot as plt
import numpy as np


def motion_simulator():
    """
    Cartesian vectorial positioning
    """
    # pi = 3.141592653589793228841971693993114819665930005738  # unnecessary precision to the 48th decimal
    x_path = [0]
    y_path = [0]
    position = np.array([0.000, 0.000])
    step_length = np.array([1.000, 1.000])
    turn_angle = pi / 90
    angle = 0
    while True:
        try:
            if angle % (2 * pi) == 0:
                angle = 0
            trig_equalizers = np.array([cos(angle), sin(angle)])
            control = input("Control: ").lower()
            if control == "w":
                position += step_length * trig_equalizers
                print(angle)
                print(position)
                x_path.append(position[0])
                y_path.append(position[1])
                continue
            elif control == "s":
                position -= step_length * trig_equalizers
                print(angle)
                print(position)
                x_path.append(position[0])
                y_path.append(position[1])
                continue
            elif control == "a":
                angle += turn_angle
                print(angle)
                print(position)
                x_path.append(position[0])
                y_path.append(position[1])
                continue
            elif control == "d":
                angle -= turn_angle
                print(angle)
                print(position)
                x_path.append(position[0])
                y_path.append(position[1])
                continue
            elif control in ["break", "q", "quit", "stop"]:
                print(f"Ended at {position}")
                break
        except ValueError:
            print(f"Nope, {ValueError}")
        except AttributeError:
            print(f"Nope, {AttributeError}")
    fig, ax = plt.subplots()
    ax.plot(x_path, y_path, label="Travel path")
    ax.set_aspect("equal")
    ax.set_title("Simple plot")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    motion_simulator()

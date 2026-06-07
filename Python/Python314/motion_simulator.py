"""
This attempts to simulate positions vectorially
"""

import random
from math import cos, pi, sin

import matplotlib.pyplot as plt
import numpy as np

# iter = 0
# controls = []
# random_pick = random.randint(100000, 1000000)
# while iter < random_pick:
#     controls.append(random.choice(["w", "a", "d"]))
#     iter += 1
# controls.append("q")


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
    turn_angle = pi / 36
    angle = 0
    should_quit = False
    while True:
        try:
            controls = input("Control: ").lower()
            for value in controls:
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
            for value in controls:
                if value in ["break", "q", "quit", "stop"]:
                    should_quit = True
            if should_quit:
                print(
                    f"Ended at ({position[0]:3f}, {position[1]:3f}) facing {(angle / pi * 180) % 360:3f} degrees"
                )
                break
        except ValueError as error:
            print(error)
        except AttributeError as error:
            print(error)
    travel_path(x_path, y_path)


def travel_path(x_path, y_path):
    """Trace the path of the player"""
    _, ax = plt.subplots()
    color = random.choice(["red", "blue", "green", "black"])
    ax.plot(x_path, y_path, color=color, label="Travel path")
    ax.set_aspect("equal")
    ax.set_title("Cartesian vectorial positioning")
    plt.grid()
    plt.show()


if __name__ == "__main__":
    motion_simulator()

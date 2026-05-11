"""Outdated(As of 9/5/2026)
Motion simulator"""

from math import cos, pi, sin

step = 0  # basic unit
angle = 0  # in degrees
x = 0
y = 0
while True:
    control = input("Enter W, A, S, D to move\n").lower()
    if control == "w":
        step += 5
    elif control == "a":
        angle -= 5
    elif control == "d":
        angle += 5
    elif control == "s":
        step -= 5
    else:
        print("Huh, 😕")
        continue
    radians = angle / 180 * pi
    velocity_x = sin(radians) * step
    velocity_y = cos(radians) * step
    if angle >= 360 or angle <= -360:
        angle = 0
    x += velocity_x
    y += velocity_y
    position = ((x**2) + (y**2)) ** 0.5
    print(x)
    print(y)
    print(position)
    print(angle)
    print(radians)
    print(step)
    print(velocity_x)
    print(velocity_y)

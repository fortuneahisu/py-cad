"""
Parallel preliminary model
Beta 002b
"""

import datetime
import os
from time import sleep

from constants import (
    agreement,
    climate_words,
    complements,
    curses,
    disagreement,
    friends,
    fun_words,
    i_know,
    math_words,
    small_talk,
    study_words,
    to_you_too,
    well_being_words,
)

MY_NAME = "Moutsousammy"
file = "house_chat.json"
today = datetime.date.today()
time = datetime.datetime.now().strftime("%H:%M")
print(f"My name is {MY_NAME}, I'll try to be engaging, but bear with me")
sleep(2)
libraries = [
    agreement,
    climate_words,
    complements,
    curses,
    disagreement,
    friends,
    fun_words,
    i_know,
    math_words,
    small_talk,
    study_words,
    to_you_too,
    well_being_words,
]
while True:
    if os.path.exists(file):
        with open(file, "r") as memory:
            content = memory.read()
            break
    else:
        with open(file, "w") as memory:
            memory.write(f"{'Date created': {today} {time},}")
            break

print(libraries[libraries.index(friends)])
message = input("What do you have to say? ").split()

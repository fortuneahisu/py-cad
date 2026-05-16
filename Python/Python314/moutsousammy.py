"""
Parallel preliminary model
Beta 002b
"""

import csv
import datetime
import os
# import random
from time import sleep

import motion_simulator
import progress_log
from constants import (
    agreement,
    climate_words,
    # complements,
    # curses,
    disagreement,
    # friends,
    fun_words,
    # i_know,
    math_words,
    # small_talk,
    study_words,
    # to_you_too,
    # well_being_words,
)
from module_packs import (
    # basic_modules,
    general_modules,
    math_works,
)

line = []
MY_NAME = "Moutsousammy"
NAMES = "names.csv"
SUGGESTIONS = "suggestions.txt"
today = datetime.date.today()
time = datetime.datetime.now().strftime("%H:%M")
print(f"Hi, my name is {MY_NAME}, I'll try to be engaging, but bear with me")
sleep(0.5)


name = input("What's your first name user? ").strip().capitalize()
previous_people = []


def store_info(name, memory):
    """Storing user data, if unavailable"""
    print("We don't seem to have talked before")
    while True:
        while True:
            try:
                age = int(input("I'd love to know how old you are? "))
                break
            except ValueError:
                print("Age is just a number")
                continue
        try:
            writer = csv.writer(memory)
            writer.writerow([f"{name}", f"{age}"])
            break
        except ValueError as val_err:
            print(val_err)
            continue


def check_user(name):
    """Checking if user data is stored"""
    content = "Content from names.json"
    if os.path.exists(NAMES):
        with open(NAMES, "r") as memory:
            content = csv.DictReader(memory)
            for row in content:
                previous_people.append(row["Name"])
            if name in previous_people:
                print(f"Hey! {name}. You're back again")
                sleep(0.5)
            else:
                with open(NAMES, "a", newline="") as memory:
                    store_info(name, memory)
    else:
        with open(NAMES, "w", newline="") as memory:
            writer = csv.writer(memory)
            writer.writerow(["Name", "Age"])
            store_info(name, memory)


def math_function(name, *args):
    """Math knowledge base"""
    while True:
        if "+" in message:
            while True:
                try:
                    number_1 = int(input("First number: "))
                    number_2 = int(input("Second number: "))
                    print(math_works.add(number_1, number_2))
                    print("Sorry I had to ask again")
                    break
                except ValueError:
                    print("Addition only works on numbers, Don't you think?")
                    continue
            break
        if "-" in message:
            while True:
                try:
                    number_1 = int(input("First number: "))
                    number_2 = int(input("Second number: "))
                    print(math_works.subtract(number_1, number_2))
                    print("Sorry I had to ask again")
                    break
                except ValueError:
                    print("Subtraction only works on numbers, Don't you think?")
                    continue
            break
        if "/" in message:
            while True:
                try:
                    number_1 = int(input("First number: "))
                    number_2 = int(input("Second number: "))
                    print(math_works.divide(number_1, number_2))
                    print("Sorry I had to ask again")
                    break
                except ValueError:
                    print("Division only works on numbers, Don't you think?")
                    continue
            break
        if "*" in message:
            while True:
                try:
                    number_1 = int(input("First number: "))
                    number_2 = int(input("Second number: "))
                    print(math_works.multiply(number_1, number_2))
                    print("Sorry I had to ask again")
                    break
                except ValueError:
                    print("Multiplication only works on numbers, Don't you think?")
                    continue
            break
        if "quadratic" in message:
            a = int(input("Coeffiecient of x^2 (a): "))
            b = int(input("Coefficient of x (b): "))
            c = int(input("Constant (c): "))
            print("With determinant as b^2 - 4ac")
            sleep(1)
            print("Using (-b + square root of the determinant) / (2a)")
            print("and")
            print("Using (-b - square root of the determinant) / (2a)")
            sleep(1)
            print(f"The answer is {math_works.quadratic_equation(a, b, c)}")
            sleep(1)
            print(f"{name}, isn't that neat?")
            break
        if "calculator" in message:
            print("This calculator was made for Declan, sorry for the UX")
            sleep(0.5)
            print(math_works.calculate())
            break
        affirmation = input("Do you still need help? ").lower().strip()
        if affirmation in agreement:
            sleep(1)
            print("I have some other functions to help")
            sleep(0.5)
            while True:
                try:
                    key = int(
                        input(
                            "1: Quadratic equation solver\n"
                            "2: Factorial finder\n"
                            "3: Basic calculator\n"
                            "0: Quit\n"
                        )
                    )
                    if key == 1:
                        a = int(input("Coeffiecient of x^2 (a): "))
                        b = int(input("Coefficient of x (b): "))
                        c = int(input("Constant (c): "))
                        print("With determinant as b^2 - 4ac")
                        sleep(0.5)
                        print("Using (-b + square root of the determinant) / (2a)")
                        print("and")
                        print("Using (-b - square root of the determinant) / (2a)")
                        sleep(0.5)
                        print(f"The answer is {math_works.quadratic_equation(a, b, c)}")
                        sleep(0.5)
                        print(f"{name}, isn't that neat")
                        break
                    if key == 2:
                        number = int(input("number: "))
                        print(
                            f"The factorial of {number} is {math_works.factorial(number)}"
                        )
                        if math_works.factorial(number) > 1000000:
                            sleep(0.5)
                            print("This is huge")
                        break
                    if key == 3:
                        print("This calculator was made for Declan, sorry for the UX")
                        sleep(0.5)
                        print(math_works.calculate())
                        break
                    if key == 0:
                        print("It seems I dont have what you need")
                        needs = input("What may that be? ")
                        with open(SUGGESTIONS, "a") as memory:
                            memory.write("Math needs")
                            memory.write("\n")
                            memory.write(needs)
                            memory.write("\n")
                            break
                except ValueError:
                    print("Choose a number from the menu, I don't know more than those")
                    sleep(0.5)
                    continue
            break
        if affirmation in disagreement:
            return "Great, glad I helped"
        else:
            return "Sorry, I didn't get that"


def fun_function(name, *args):
    """Fun knowledge base"""
    print("Okay, how would you like to while away time? ")
    while True:
        try:
            choice = int(
                input(
                    "1: Test questions\n"
                    "2: Whatsapp simulation\n"
                    "3: Rock-paper-scissors\n"
                    "4: Motion simulator\n"
                    "0: Quit\n"
                )
            )
            if choice == 1:
                return general_modules.test_questions()
            if choice == 2:
                return general_modules.whatsapp_simulation()
            if choice == 3:
                return general_modules.rock_paper_scissors()
            if choice == 4:
                return motion_simulator.motion_simulator()
            if choice == 0:
                needs = input(f"What would you have played instead {name}? ")
                with open(SUGGESTIONS, "a") as memory:
                    memory.write("Games needs")
                    memory.write("\n")
                    memory.write(needs)
                    memory.write("\n")
                    break
        except ValueError:
            print("You're meant to choose a value from the menu")
            continue


def study_function(name, *args):
    """Log processor access"""
    print(f"Okay {name}, I have something of a progress tracker, It's not much though")
    affirmation = input("How'd you like that? ").lower().strip()
    if affirmation in disagreement:
        print("Okay, fine. What's up now darling? ")
    elif affirmation in agreement:
        print("Nice")
        sleep(1)
        print("Today, you should study these subjects, and submit your progress here")
        sleep(1)
        progress_log.progress_log()
        print(
            "Don't worry, go back to you study desk, study these subjects, and get back to me"
        )
    else:
        print("I didn't quite get that")
        needs = input(f"What was it that you said, {name}? ")
        with open(SUGGESTIONS, "a") as memory:
            memory.write("Study needs")
            memory.write("\n")
            memory.write(needs)
            memory.write("\n")
        print("I'll see to it later")


def datetime_function(name, *args):
    """Date-time information access"""
    want = args[0]
    while True:
        if word in ["time", "now", "right now"]:
            print(f"As we speak, time is {datetime.datetime.now().strftime('%H:%M')}")
        elif word in ["date", "today"]:
            print(f"Today is {datetime.date.today()}")
        elif word in ["weather", "hot", "cold", "rain", "rainy", "chill"]:
            print(f"I'm sorry but I can't help with \"{want}\" right now")
        affirmation = input("Have I done what you wanted? ").strip().lower()
        if affirmation in agreement:
            print("Glad I could help")
            break
        if affirmation in disagreement:
            needs = input("What did you need that I couldn't provide? ")
            with open(SUGGESTIONS, "a") as memory:
                memory.write("Date-time needs")
                memory.write("\n")
                memory.write(needs)
                memory.write("\n")
            print("That will be looked into")
            break
        else:
            print(f"Sorry, I didn't get that {name}")
            break


libraries = {}
check_user(name)
for words in climate_words:
    libraries[words] = datetime_function
for words in math_words:
    libraries[words] = math_function
for words in study_words:
    libraries[words] = study_function
for words in fun_words:
    libraries[words] = fun_function
while True:
    # print(random.choice(small_talk))
    message = input("What do you have to say? ").split()
    for word in message:
        if word.lower() in libraries:
            libraries[word](name, word)
            break
    should_quit = False
    for word in message:
        if word in disagreement:
            print("Catch you later, love")
            should_quit = True
            break
    if should_quit:
        break

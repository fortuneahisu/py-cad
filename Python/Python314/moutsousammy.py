"""
Parallel preliminary model
Beta 002b
"""

import datetime
import math
import random
from time import sleep

import motion_simulator
import progress_log
from constants import (
    agreement,
    climate_words,
    # complements,
    curses,
    disagreement,
    # small_talk,
    exit_words,
    friends,
    fun_words,
    # i_know,
    math_words,
    study_words,
    # to_you_too,
    # well_being_words,
)
from file_i_o import fix_file, load_data, read_memory, write_memory
from module_packs import (
    # basic_modules,
    general_modules,
    math_works,
)

MY_NAME = "Moutsousammy"
SIBLING = "Declan"
SUGGESTIONS = "suggestions.txt"
convo_init = datetime.datetime.now().strftime("%H:%M")
print(f"Hi, my name is {MY_NAME}, I'll try to be engaging, but bear with me")


def basic_operations(message):
    """
    To reduce the length of the math_function
    Just for basic operations, as the name gives out
    """
    print("Let's try that again")
    number_1 = float(input("First number: "))
    number_2 = float(input("Second number: "))
    basic_func = {
        "+": math_works.add,
        "-": math_works.subtract,
        "/": math_works.divide,
        "*": math_works.multiply,
    }
    for operation, func in basic_func.items():
        if operation in message:
            print(func(number_1, number_2))


def math_function(name, word, message):
    """Math knowledge base"""
    while True:
        try:
            if any(op in message for op in ["+", "-", "*", "/"]):
                basic_operations(message)
                break
            break
        except ValueError:
            print("Operations only works on numbers, Don't you think?")
            continue
    if "quadratic" in message:
        a, b, c = (
            int(input("Coeffiecient of x^2 (a): ")),
            int(input("Coefficient of x (b): ")),
            int(input("Constant (c): ")),
        )
        print(
            "Using (-b + square root of the determinant) / (2a)\nand\n"
            "Using (-b - square root of the determinant) / (2a)"
        )
        print(f"The answer is {math_works.quadratic_equation(a, b, c)}")
    affirmation = input("Do you still need help? ").lower().strip()
    if affirmation in agreement:
        print(f"I have some other functions to help, {name}")
        while True:
            try:
                key = int(input("1: Factorial finder\n2: Basic calculator\n0: Quit\n"))
                if key == 1:
                    number = int(input("number: "))
                    print(f"The factorial of {number} is {math.factorial(number)}")
                    break
                if key == 2:
                    print(f"This calculator was made for {SIBLING}, sorry for the UX")
                    print(math_works.calculate())
                    break
                if key == 0:
                    needs = input(
                        "It seems I dont have what you need\nWhat may that have been? "
                    )
                    with open(SUGGESTIONS, "a", encoding="ANSI") as memory:
                        memory.write("Math needs\n")
                        memory.write(f"{needs}\n")
                        break
            except ValueError:
                print("Choose a number from the menu, I don't know more than those")
                continue
        return
    if affirmation in disagreement:
        print("Great, glad I helped")
        return
    print("Sorry, I didn't get that")
    print(f"Command triggered by: {word}")


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
                with open(SUGGESTIONS, "a", encoding="ANSI") as memory:
                    memory.write("Games needs")
                    memory.write("\n")
                    memory.write(needs)
                    memory.write("\n")
                    return "Done"
        except ValueError:
            print("You're meant to choose a value from the menu")
            print(f"I didn't use {args[0]}")
            continue
        return "Done"


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
    else:
        print("I didn't quite get that")
        needs = input(f"What was it that you said, {name}? ")
        with open(SUGGESTIONS, "a", encoding="ANSI") as memory:
            memory.write("Study needs")
            memory.write("\n")
            memory.write(needs)
            memory.write("\n")
        print("I'll see to it later")
        print(f"I didn't use {args[0]}")


def datetime_function(name, *args):
    """Date-time information access"""
    today = datetime.date.today()
    hour = datetime.datetime.now().strftime("%H")
    if int(hour) // 12:
        meridian = "PM"
    else:
        meridian = "AM"
    time = datetime.datetime.now().strftime(f"{int(hour) % 12}:%M {meridian}")
    want = args[0]
    while True:
        if want in ["time", "now", "right now"]:
            print(f"As we speak, time is {time}")
        elif want in ["date", "today"]:
            print(f"Today is {today}")
        elif want in ["weather", "hot", "cold", "rain", "rainy", "chill"]:
            print(f"I'm sorry but I can't help with \"{want}\" right now")
        affirmation = input("Have I done what you wanted? ").strip().lower()
        if affirmation in agreement:
            print("Glad I could help")
            break
        if affirmation in disagreement:
            needs = input("What did you need that I couldn't provide? ")
            with open(SUGGESTIONS, "a", encoding="ANSI") as memory:
                memory.write("Date-time needs")
                memory.write("\n")
                memory.write(needs)
                memory.write("\n")
            print("That will be looked into")
            break
        print(f"Sorry, I didn't get that {name}")
        break


def customized_output(name, database):
    """To aid flexibility of user name"""
    data = load_data(database)
    if name == "Fortune":
        print("Hold up?, That's my creators name!, anyways...")
        print("I may just be the dumbest 'AI' you'll encounter")
    elif name == "Nexus":
        print("AI to AI, you're poor. I'm looking at you TK")
    elif name == "Guess":
        name = random.choice(friends)
        print(
            f"You wanted me to guess, so your name should be {name} then. (no debate)"
        )
    elif name.lower() in curses:
        print("I doubt it, but who am I to argue?")
        print(f"Anyways, we'll continue with '{name}'")
    elif name in friends:
        print("Anybody but you bro")
        print(
            "I may just be the dumbest 'AI' you'll encounter, but not dumber than you"
        )
    for names in data:
        if name == names and name not in ["Fortune", friends, "Guess", "Nexus"]:
            print(f"What is it this time, {name}?")
            break
    return name


def main_interface():
    """Main interactive front"""
    memory = "memory.json"
    database = "names.json"
    fix_file(memory)
    fix_file(database)
    name = input("What's your first name user? ").strip().capitalize()
    name = customized_output(name, database)
    read_memory(name, SIBLING, MY_NAME)
    libraries = {}
    for words in climate_words:
        libraries[words.lower()] = datetime_function
    for words in math_words:
        libraries[words.lower()] = math_function
    for words in study_words:
        libraries[words.lower()] = study_function
    for words in fun_words:
        libraries[words.lower()] = fun_function
    while True:
        # print(random.choice(small_talk))
        message = input("What do you have to say? \n").split()
        for word in message:
            if word.lower() in libraries:
                libraries[word.lower()](name, word, message)
                break
        should_quit = False
        for word in message:
            if word in exit_words:
                print("Catch you later, love")
                should_quit = True
                break
        if should_quit:
            write_memory(name, MY_NAME, convo_init)
            break


if __name__ == "__main__":
    main_interface()

"""
Miniature Preliminary AI model
Beta 002a
"""

import csv
import datetime
import os
import random
from time import sleep

import progress_log as progress_log
from constants import (
    agreement,
    climate_words,
    complements,
    curses,
    disagreement,
    exit_words,
    friends,
    fun_words,
    i_know,
    math_words,
    # small_talk,
    study_words,
    to_you_too,
    well_being_words,
)
from file_i_o import fix_file, load_data, save_data
from module_packs import general_modules, math_works

MY_NAME = "Declan"
SISTER = "Moutsousammy"
NAMES = "names.csv"
MEMORY = "memory.json"
convo_init = datetime.datetime.now().strftime("%H:%M")
TODAY = str(datetime.datetime.now().strftime("%d/%m/%y"))
# id = str(datetime.datetime.now().strftime("%d/%m/%y %H:%M"))


def introduction():
    """Last log message from Beta 001"""
    print("\"See, I have had other trials of this before, you're the 002a version!")
    sleep(2)
    print("But they all could do only one thing")
    sleep(1.5)
    print("So my goal is to give you millions of tiny functions")
    sleep(1.5)
    print("And they all will have context based on their situation")
    sleep(1.5)
    print('This should be an extensive one"')
    sleep(1.5)
    print("\n")
    print(" " * 45 + "-Fortune, your creator")
    sleep(2)
    return "\n"


def store_info(name, memory):
    """Storing user data, if unavailable"""
    print("I don't have you in memory")
    while True:
        while True:
            try:
                age = int(input(f"How old are you, {name}? "))
                break
            except ValueError:
                print("Well expected, now be serious")
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
    previous_people = []
    if os.path.exists(NAMES):
        with open(NAMES, "r", encoding="ANSI") as memory:
            content = csv.DictReader(memory)
            for row in content:
                previous_people.append(row["Name"])
            if name in previous_people:
                customized_output(name, previous_people)
            else:
                with open(NAMES, "a", newline="", encoding="ANSI") as memory:
                    store_info(name, memory)
                customized_output(name, previous_people)
    else:
        with open(NAMES, "w", newline="", encoding="ANSI") as memory:
            writer = csv.writer(memory)
            writer.writerow(["Name", "Age"])
            store_info(name, memory)


def read_memory(name):
    """Reads the siblings shared memory before continuing"""
    memory = dict(load_data(MEMORY))
    print(f"Hey {name}")
    while True:
        try:
            for key in dict(memory):
                if TODAY == key:
                    if memory[TODAY]["last_sibling"] == SISTER:
                        print(
                            f"I see you been positive with {SISTER} aight, {memory[TODAY]['last_person']}?"
                        )
                        check_user(name)
                        return
                    if memory[TODAY]["last_sibling"] == MY_NAME:
                        check_user(name)
                        return
            print("What's the damn error")
            return
        except KeyError:
            print("First contact today ey?")
            return


def write_memory(name):
    """Wrting own metadata before closing"""
    memory = load_data(MEMORY)
    memory[TODAY] = {
        "last_sibling": MY_NAME,
        "last_person": name,
        "convo_init": convo_init,
        "convo_end": datetime.datetime.now().strftime("%H:%M"),
    }
    save_data(memory, MEMORY)


def math_function(name, *args):
    """Math knowledge base"""
    affirmation = (
        input("I should have a function on calculations, If that's what you want... ")
        .lower()
        .strip()
    )
    if affirmation in agreement:
        sleep(1)
        print("Which of 'em? ")
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
                    a = int(input("a: "))
                    b = int(input("b: "))
                    c = int(input("c: "))
                    print(math_works.quadratic_equation(a, b, c))
                    break
                if key == 2:
                    number = int(input("number: "))
                    print(math_works.factorial(number))
                    break
                if key == 3:
                    print(math_works.calculate())
                    break
                if key == 0:
                    print("Suit yourself")
                    break
            except ValueError:
                print("Choose a number from the damn menu")
                continue
    elif affirmation in disagreement:
        print(f"Anyhow it is on '{args[0]}', ey {name}? ")
    else:
        print("As good as no")


def fun_function(name, word):
    """Fun knowledge base"""
    affirmation = (
        input(f"Speaking of '{word}', would you like to have some fum? ")
        .lower()
        .strip()
    )
    if affirmation in agreement:
        print("Okay, what will it be then? ")
        while True:
            try:
                choice = int(
                    input(
                        "1: Test questions\n"
                        "2: Whatsapp simulation\n"
                        "3: Rock-paper-scissors\n"
                        "0: Quit\n"
                    )
                )
                if choice == 1:
                    general_modules.test_questions()
                    break
                if choice == 2:
                    general_modules.whatsapp_simulation()
                    break
                if choice == 3:
                    general_modules.rock_paper_scissors()
                    break
                if choice == 0:
                    print("Suit yourself")
                    break
            except ValueError:
                print("You're meant to choose a value from the menu")
                continue
    elif affirmation in disagreement:
        print(f"Aight, Whatever suits you {name}")
    else:
        print("No it is")


def study_function(name, *args):
    """Log processor access"""
    print(
        f"Okay {name}, calms. I have a function on studying, It's shallow, but It's something"
    )
    affirmation = input("How'd you like that? ").lower().strip()
    if affirmation in agreement:
        print("Nice")
        sleep(1)
        print("Today, you should study these subjects, and submit your progress here")
        sleep(1)
        progress_log.progress_log()
        print(
            "Don't worry, go back to you study desk, study these subjects, and get back to me"
        )
    elif affirmation in disagreement:
        print("Aight, bet. What's up now? ")
    else:
        print(f"I'll take that as a no for {args[0]}")


def climate_function(*args):
    """Climate information access"""
    affirmation = input(
        "What exactly do you want to know, weather?, time?, another? "
    ).strip()
    if affirmation in ["date", "today"]:
        print(f"Today is {datetime.date.today()}")
        print("It's the best i know right now")
    elif affirmation in ["time", "now", "right now"]:
        print(f"Right now?, that's {datetime.datetime.now().strftime('%H:%M')}")
    elif affirmation in ["weather", "hot", "cold", "rain", "rainy", "chill"]:
        print("Guess who's at the other side of the screen?")
        sleep(1)
        print("Look outside instead, I can't do that for now")
    elif affirmation in disagreement:
        print(f"My bad {args[0]}")
    else:
        print("I'll assume you mean no")


def well_being(word, *args):
    """Well-being function"""
    if word in [
        "how are you",
        "how are you?",
        "how are ya",
        "how body?",
        "how body",
        "how life",
        "hows it going",
        "how's it going",
    ]:
        print("Let's say I'm hangin in here fine, Thanks for asking")
    elif word in [
        "what's up",
        "whats up",
        "whats up?",
        "what's up?",
        "whats popping",
    ]:
        print("I wouldn't know, I'm dumb")
    if args[0] == "Declan":
        print(args[0])


def customized_output(name, previous_people):
    """To aid flexibility of user name"""
    if name == "Fortune":
        print("Hold up?, That's my creators name!, anyways...")
        print("I may just be the dumbest 'AI' you'll encounter")
    elif name == "Declan":
        print("Wait a minute?, That's literally my name too, beep-boop...")
        print("I may just be the dumbest 'AI' you'll encounter")
    elif name == "Nexus":
        print("AI to AI, you're crap fr. I'm looking at you TK")
    elif name == "Guess":
        name = random.choice(friends)
        print(f"Alright, {name} then. (no debate)")
    elif name.lower() in curses:
        print("I doubt it, let's use our brains here shall we?")
        print(f"Anyways, we'll continue with '{name}'")
    elif name in previous_people:
        print("What is it this time? ")
    elif name in friends:
        print("Ah shit, not you")
        print(
            "I may just be the dumbest 'AI' you'll encounter, but not dumber than you"
        )
    else:
        print(
            f"Hey {name}, My name is {MY_NAME}, and I may just be the dumbest AI you'll encounter"
        )


def interface():
    """Main UX interface"""
    # introduction()
    name = input("What's your first name, user? ").capitalize().strip()
    fix_file(MEMORY)
    read_memory(name)
    sleep(2)
    while True:
        # print(random.choice(small_talk))
        message = input().lower()
        context = {
            math_words: math_function,
            fun_words: fun_function,
            study_words: study_function,
            climate_words: climate_function,
            well_being_words: well_being,
        }
        content = {
            complements: random.choice(i_know),
            curses: random.choice(to_you_too),
        }
        if "?" in message:
            print("I can't answer questions effectively for now but...")
        for words, function in context.items():
            for word in words:
                if word in message:
                    function(name, word)
                    break
        for words, replies in content.items():
            for word in words:
                if word in message:
                    print(replies)
                    break
        for word in exit_words:
            if word in message.split():
                write_memory(name)
                return "Chiao peep"


if __name__ == "__main__":
    print(interface())

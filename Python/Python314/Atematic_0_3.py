"""
Miniature Preliminary AI model
Beta 002
"""

import datetime
import random
from time import sleep

import progress_log
from module_packs import general_modules, math_works

my_name = "Declan"
friends = [
    "Oba",
    "Obafemi",
    "Tk",
    "Towokpebe",
    "Sultan",
    "Joel",
    "Nido",
    "Junia",
    "Tobi",
]
math_words = [
    "solve",
    "calculate",
    "math",
    "add",
    "subtract",
    "divide",
    "multiply",
    "+",
    "-",
    "/",
]
fun_words = ["joy", "party", "games", "fun", "game"]
study_words = ["study", "read", "learn"]
climate_words = ["time", "date", "when", "today", "schedule", "weather"]
complements = ["nice", "lit", "impressive", "smart", "intelligent", "good", "excelent"]
curses = [
    "fuck you",
    "fucker",
    "idiot",
    "dull",
    "foolish",
    "stupid",
    "fuck",
    "gbolo",
    "mumu",
    "ass",
    "assface",
    "bamf",
    "motherfucker",
    "mother fucker",
    "bitch",
]
i_know = [
    "Why not? ",
    "Were you expecting less? ",
    "Thanks",
    "I know",
    "Really means alot",
]
to_you_too = [
    "Fuck you too, dumbass",
    "Didn't i tell you I was dumb, now you're as dumb as I am",
    "Check your head for a brain, I doubt you'll find",
    "You're as dumb as you're blind",
    "Geez, Humans never disappoint, do they?",
    "CLassic idiot, well exoected of you tho",
    "You say to me, the literal dumbest thing you'll talk to asides your self",
]
agreement = [
    "yeah",
    "yes",
    "y",
    "it is",
    "yh",
    "aight",
    "well, yes",
    "would i",
    "let's go",
    "lets go",
    "would i?",
    "yay",
    "do it then",
    "absolutely",
    "ya",
    "true",
    "done",
    "yes",
    "y",
    "fr",
    "bet",
    "you bet",
    "of course",
]
disagreement = [
    "nay",
    "nah",
    "no",
    "n",
    "hell nah",
    "hell no",
    "absolutely not",
    "why would i",
    "none",
    "why would I",
    "why would I?",
    "nothing",
    "nothing here",
    "false",
    "undone",
    "no",
]
small_talk = [
    "Okay, let's continue...",
    "Easter egg: my creator's name is FortuneTry key words about math, study or games!",
]


def introduction():
    print("\"See, I have had other trials of this before, you're the 002 version!")
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
    return "\n"
    sleep(2)


def math_function():
    affirmation = (
        input(
            "Hey!, I should have a function on calculations, If that's what you want... "
        )
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
                    )
                )
                if key == 1:
                    a = int(input("a: "))
                    b = int(input("b: "))
                    c = int(input("c: "))
                    print(math_works.quadratic_equation(a, b, c))
                    break
                elif key == 2:
                    number = int(input("number: "))
                    print(math_works.factorial(number))
                    break
                elif key == 3:
                    print(math_works.calculate())
                    break
            except ValueError:
                print("Choose from a number damn menu")
                continue
    elif affirmation in disagreement:
        print(f"Anyhow it is, ay {name}? ")
    else:
        print("As good as no")


def fun_function(word, name):
    affirmation = (
        input(f"Speaking of '{word}', would you like to have some fun? ")
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
                    )
                )
                if choice == 1:
                    general_modules.test_questions()
                    break
                elif choice == 2:
                    general_modules.whatsapp_simulation()
                    break
                elif choice == 3:
                    general_modules.rock_paper_scissors()
                    break
            except TypeError:
                print("You're meant to choose a value from the menu")
                continue
    elif affirmation in disagreement:
        print(f"Aight, Whatever suits you {name}")
    else:
        print("No it is")


def study_function(name):
    print(
        f"Okay {name}, slow down. I have a function on studying, It's shallow, but It's something"
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
        print("I'll take that as a no")


def climate_function():
    affirmation = input(
        "What exactly do you want to know, weather?, time?, another? "
    ).strip()
    if affirmation in ["date", "today"]:
        print(f"Today is {datetime.date.today()}")
        print("It's the best i know right now")
    elif affirmation in ["time", "now", "right now"]:
        print(f"Right now?, that's {datetime.datetime.now()}")
    elif affirmation in ["weather", "hot", "cold", "rain", "rainy", "chill"]:
        print("Guess who's at the other side of the screen?")
        sleep(1)
        print(f"Look outside instead, I can't do that for now")
    elif affirmation in disagreement:
        print("My bad mate")
    else:
        print("I'll assume you mean no")


def interface(my_name, friends, i_know, to_you_too):
    # introduction()
    name = input("What's your first name, user? ").capitalize().strip()
    if name == "Fortune":
        print("That's my creators name!, anyways...")
        print("I may just be the dumbest 'AI' you'll encounter")
    elif name == "Declan":
        print("That's literally my name too, beep-boop...")
        print("I may just be the dumbest 'AI' you'll encounter")
    elif name.lower() in curses:
        print("I doubt it, let's use our brains here shall we?")
        print(f"Anyways, we'll continue with '{name}'")
    elif name in friends:
        print("Ah shit, not you again")
        print(
            "I may just be the dumbest 'AI' you'll encounter, but not dumber than you"
        )
    else:
        print(
            f"Hey {name}, My name is {my_name}, and I may just be the dumbest AI you'll encounter"
        )
    sleep(2)
    while True:
        # print(random.choice(small_talk))
        message = input().lower()
        for word in math_words:
            if word in message:
                math_function()
                continue
        for word in fun_words:
            if word in message:
                fun_function(word, name)
                continue
        for word in study_words:
            if word in message:
                study_function(name)
        for word in climate_words:
            if word in message:
                climate_function()
        for word in complements:
            if word in message:
                random.choice(i_know)
        for word in curses:
            if word in message:
                random.choice(to_you_too)
        if (
            word
            in message
            not in [
                math_words,
                fun_words,
                study_words,
                climate_words,
                complements,
                curses,
            ]
        ):
            print("I can't help with that for now")
            print("Try a key word concerning math, study, fun, time or the weather")


if __name__ == "__main__":
    print(interface(my_name, friends, i_know, to_you_too))

"""
Miniature Preliminary AI model
Beta 002
"""

import random
from time import sleep

import progress_log
from module_packs import general_modules, math_works

my_name = "Declan"
math_words = ["solve", "calculate", "math", "add", "subtract", "divide", "multiply"]
fun_words = ["joy", "party", "games", "fun", "game"]
study_words = ["study", "read", "learn", "schedule"]
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
    "absolutely",
    "ya"
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
]
small_talk = [
    "Okay, let's continue...",
    "Let me just remind you that I lack context recognition, But go on...",
    "You're talking to a wall here, But hey!, no one here will judge you at least...",
    "I know, I know, knowledge problem...",
    "Sorry, not sorry, from my creator...",
    "Try key words about math, study or games!",
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
    affirmation = input(
        "Hey!, I should have a function on calculations, If that's what you want... "
    ).lower()
    if affirmation in agreement:
        sleep(1)
        print("Which of 'em? ")
        while True:
            try:
                key = int(
                    input(
                        "1: Quadratic equation solver\n2: Factorial finder\n3: Basic calculator\n"
                    )
                )
                if key == 1:
                    a = int(input("a: "))
                    b = int(input("b: "))
                    c = int(input("c: "))
                    math_works.quadratic_equation(a, b, c)
                    break
                elif key == 2:
                    number = int(input("number: "))
                    print(math_works.factorial(number))
                    break
                elif key == 3:
                    math_works.calculate()
                    break
            except TypeError:
                print("Choose from the damn menu")
                continue
    else:
        print("I need access to my function bank to help at all, remember, I'm dumb")


def fun_function(word, name):
    affirmation = input(
        f"Speaking of '{word}', would you like to have some fun? "
    ).lower()
    if affirmation in agreement:
        print("Okay, what will it be then? ")
        while True:
            try:
                choice = int(
                    input(
                        "1: Test questions\n2: Whatsapp simulation\n3: Rock-paper-scissors\n"
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


def study_function(name):
    print(
        f"Okay {name}, slow down. I have a function regarding studying, It's shallow, but It's something"
    )
    affirmation = input("How'd you like that? ").lower()
    if affirmation in agreement:
        print("Nice")
        sleep(1)
        print("Today, you should study these subjects, and submit your progress here")
        sleep(1)
        progress_log.progress_log()
        print("Don't worry, go back to you study desk, study these subjects, and get back to me")


def interface(my_name):
    # introduction()
    name = input("What's your first name, user? ").capitalize()
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


if __name__ == "__main__":
    print(interface(my_name))

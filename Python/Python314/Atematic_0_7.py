"""
Relationship between functions
Hospital game
"""

import time
from random import randint

from module_packs import basic_modules

title = "Hospital game"
basic_modules.print_title(title)


def gameplay(name):
    """Gameplay of the hospital game"""
    survival_rate = randint(1, 100)
    print("1. Give up\n2. Treat it\n3. Call your wife\n4. Ask questions")
    choice = int(input(f"What do you do {name.title()}? "))
    if choice == 1:
        give_up(survival_rate)
    elif choice == 2:
        treat_it(survival_rate)
    elif choice == 3:
        call_your_wife(name)
    elif choice == 4:
        send_a_message(name)
    else:
        print("Invalid response")


def give_up(survival_rate):
    message = 0
    if survival_rate < 50:
        message = "so..., Anyhoo tho"
    if survival_rate >= 50:
        message = "You really shouldn't have done that"
    time.sleep(1)
    print(f"You gave up, you had a {survival_rate}% chance btw, {message}")


def treat_it(survival_rate):
    print("You're doctor is trying to save your life...")
    time.sleep(1)
    print("Treating...")
    time.sleep(2)
    if survival_rate >= 50:
        print("You survived the pain, you live on 😊😊🥳")
    else:
        print("You are hospitalized 💀☠️😵")
    time.sleep(5)


def call_your_wife(name):
    print("Calling wife...")
    time.sleep(2)
    print("She's not around, leave a typed note...")
    time.sleep(1)
    input("Say something to your wife...\n")
    time.sleep(1)
    print("Sending...")
    time.sleep(1)
    print("Sent")
    time.sleep(1)
    print("You can: ")
    gameplay(name)


def send_a_message(name):
    input("Message: ")
    print("We'll see what we can do about it")
    time.sleep(2)
    gameplay(name)


def hospital_game():
    """Classic input-output code"""
    name = input("Input your first name and last name? ")
    age = input("How old are you? ")
    is_patient = input("Have you been here before?(True or False) ").title()
    while True:
        if is_patient == "True":
            print("You can visit your assigned doctor.")
            time.sleep(2)
            print("You're with your doctor")
            time.sleep(5)
            print("You have a complication")
            time.sleep(2)
            print("You can: ")
            gameplay(name)
            break
        if is_patient == "False":
            print("You have to register first")
            print(f"Name = {name}")
            print(f"Age = {age}")
            input("Input your acc number = ")
            is_patient = "True"
            continue
        print("Input true or false")
        continue


if __name__ == "__main__":
    hospital_game()

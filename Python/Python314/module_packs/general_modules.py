"""
__Module and function training__

    Returns: variant returns
"""

import random
import time
from random import randint

from module_packs import basic_modules


def test_questions():
    """
    Test to measure my knowledge of 'for' loops
    """
    basic_modules.print_title("Geography test")
    questions = [
        "What continent is Guadalupe found? ",
        "What country borders USA to the north? ",
        "What country uses more than one denomination for 1 value? ",
        "What's the capital of Russia? ",
    ]
    answers = ["south america", "canada", "nigeria", "moscow"]
    output = 0
    for idx, question in enumerate(questions):
        answer = input(question)
        if answer.strip().lower() == answers[idx]:
            output += 1
    return f"You got {output}/{len(questions)}"


def whatsapp_simulation():
    """
    Whatsapp login
    """
    whatsapp_init_login()
    print("Configuring, Please wait...")
    time.sleep(5)
    print("Done!")
    time.sleep(1)
    print("Start chatting...")
    time.sleep(2)
    print("Fatal error (Because I don't know how to continue)")
    time.sleep(2)
    return "If you can help, do well to reach out to me"


def whatsapp_init_login():
    """
    Initializes whatsapp login experience
    """
    print("Welcome to Whatsapp")
    time.sleep(2)
    input("Input your phone number: ")
    print("Looks like you're new, how would you love to signup:")
    signup_choice = (
        "E-mail verification",
        "Missed call",
        "Verify through SMS",
        "Voice call",
    )
    while True:
        for idx, options in enumerate(signup_choice):
            print(f"{idx + 1}. {options}")
        try:
            signup_option = int(input("Index: "))
            if signup_option == 1:
                time.sleep(1)
                six_random_digits()
                break
            if signup_option == 2:
                print("Calling...")
                time.sleep(2)
                print("Missed call from Whatsapp")
                time.sleep(1)
                print("Verified")
                break
            if signup_option == 3:
                time.sleep(3)
                print("You have an SMS")
                time.sleep(1)
                print("You have been verified")
                time.sleep(1)
                break
            if signup_option == 4:
                time.sleep(1)
                print(
                    f"0{randint(8, 9)}"
                    f"{randint(0, 1)}"
                    f"{randint(0, 99999999):08d} calling..."
                )
                print("1. Answer")
                print("2. Decline")
                iv = int(input("Choice: "))
                if iv == 1:
                    print("You have been verified")
                elif iv == 2:
                    print("Answer to verify")
                    continue
                break
        except TypeError:
            print("TypeError occurred")


def six_random_digits():
    """
    Generates six pseudo-random numbers
    """
    number = f"{randint(0, 999999):06d}"
    print(number)
    print("Type in the number that was sent to your e-mail")
    tries = 4
    while tries > 0:
        user_input = input("Input the 6 digits: ")
        if user_input == number:
            print("😊😊")
            break
        tries -= 1
        print(f"Input invalid, you have {tries} more tries")
    else:
        time.sleep(1)
        print("You have been locked out!\n")
        time.sleep(2)
        print("Verify your account or create a new one")
    return number


def rock_paper_scissors():
    """
    Adhoc rock, paper, scissors game
    """
    pc_wins = 0
    your_wins = 0
    rounds = 0
    while rounds != 10:
        user_choice = input("rock, paper, scissors: ").lower().strip()
        choice = ["rock", "paper", "scissors"]
        pc_choice = random.choice(choice)
        if user_choice not in ("rock", "paper", "scissors"):
            print("Unrecognized input")
        elif pc_choice == user_choice:
            print("Again!, again!, again!")
        elif (
            ((pc_choice == "rock") and (user_choice == "scissors"))
            or ((pc_choice == "paper") and (user_choice == "rock"))
            or ((pc_choice == "scissors") and (user_choice == "paper"))
        ):
            print("PC wins")
            rounds += 1
            pc_wins += 1
        else:
            print("You win")
            your_wins += 1
            rounds += 1
    if pc_wins > your_wins:
        print("Computer wins 😒😒")
    else:
        print("You win 🤩🥳")


def palindrome_checker(word: str):
    """Checks if the word is a palindrome"""
    success_check = 0
    x = 0
    half_total = len(word) // 2
    while x != half_total:
        if word[0 + x].lower() == word[-x - 1].lower():
            success_check += 1
        x += 1
    if success_check == half_total:
        return "Good one 'PAL'-indrome, pun intended"
    return "Well, NOT a palindrome"


if __name__ == "__main__":
    print(test_questions())

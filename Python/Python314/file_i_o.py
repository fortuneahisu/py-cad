"""Custom file input-output for Declan x Sammi"""

import datetime
import json
import os
import random

from constants import agreement, project_alias


def fix_file(database):
    """Fix corrupted files"""
    try:
        with open(database, "r", encoding="ANSI") as file:
            json.load(file)
    except json.JSONDecodeError:
        print(f"Warning: '{database}' was corrupted or malformed. Re-initializing...")
        create(database)
    except FileNotFoundError:
        print(f"Error: '{database}' was non-existent. Initialising...")
        create(database)


def load_data(database):
    """Load database"""
    if os.path.exists(database):
        with open(database, "r", encoding="ANSI") as file:
            return dict(json.load(file))
    create(database)
    return {}


def save_data(data, database):
    """Save database"""
    with open(database, "w", encoding="ANSI") as file:
        json.dump(data, file)


def create(database):
    """Create database"""
    with open(database, "w", encoding="ANSI"):
        data = {}
        print(f"{database} initialised")
        return save_data(data, database)


def registered(user, database):
    """Check if user is registered"""
    data = load_data(database)
    is_registered = False
    for identifier in data:
        if data[identifier]["Name"] == user:
            is_registered = True
            return is_registered
    return is_registered


def register(user, database):
    """Register user"""
    user_alias = random.choice(project_alias)
    time_stamp = datetime.datetime.now().strftime("%d%m%y%H%M%S")
    identifier = f"{user_alias}{time_stamp}"
    data = load_data(database)
    while True:
        try:
            user_age = int(input("Age: "))
            break
        except ValueError as err:
            print(err)
            continue
    while True:
        try:
            user_height = float(input("Height: "))
            break
        except ValueError as err:
            print(err)
            continue
    data[identifier] = {"Name": user, "Age": user_age, "Height": user_height}
    save_data(data, database)
    if user[-1] == "s":
        grammar = ""
    else:
        grammar = "s"
    print(f"{user}'{grammar} ID: {identifier}")


def remove(user, database):
    """Deletes user by name"""
    data = load_data(database)
    for identifier in data:
        if data[identifier]["Name"] == user:
            del data[identifier]
            break
    print(f"{user} deleted")
    return save_data(data, database)


def store_info(name, database):
    """Storing user data, if unavailable"""
    data = load_data(database)
    print("I don't have you in memory")
    while True:
        try:
            age = int(input(f"How old are you, {name}? "))
            if 0 > age or age >= 120:
                print("As hard it may seem, let's maintain civility")
                continue
            break
        except ValueError:
            print(
                random.choice(["Age is just a number", "Well expected, now be serious"])
            )
            continue
    data[name] = {"Age": age}
    save_data(data, database)


def check_user(name, database):
    """Checking if user data is stored"""
    data = load_data(database)
    for names in data:
        if name in names:
            break
    else:
        store_info(name, database)


def read_memory(name, sibling, my_name):
    """Reads the siblings shared memory before continuing"""
    memory = "memory.json"
    database = "names.json"
    today = str(datetime.datetime.now().strftime("%d/%m/%y"))
    memory = load_data(memory)
    while True:
        for key in memory:
            if today == key:
                if (
                    memory[today]["last_sibling"] == sibling
                    and memory[today]["last_person"] == name
                ):
                    print(f"Hope {sibling} wasn't a piece of work")
                    check_user(name, database)
                    return
                if memory[today]["last_sibling"] == sibling:
                    print("Sheesh, My turn")
                    check_user(name, database)
                    return
                if memory[today]["last_sibling"] == my_name:
                    print("I'm back, again")
                    check_user(name, database)
                    return
                print("What's the error this time? ")
                return
        print("First contact")
        check_user(name, database)
        return


def write_memory(name, my_name, convo_init):
    """Writing own metadata before closing"""
    memory = "memory.json"
    today = str(datetime.datetime.now().strftime("%d/%m/%y"))
    data = load_data(memory)
    data[today] = {
        "last_sibling": my_name,
        "last_person": name,
        "convo_init": convo_init,
        "convo_end": datetime.datetime.now().strftime("%H:%M"),
    }
    save_data(data, memory)


def main_menu(user, database):
    """Main interface menu"""
    menu = ["Quit", "Remove user"]
    for idx, function in enumerate(menu):
        print(f"{idx}. {function}")
    while True:
        try:
            choice = int(input("Option: "))
            if choice == 0:
                return
            if choice == 1:
                affirmation = (
                    input(f"Are you sure you want to delete {user} from the database? ")
                    .lower()
                    .strip()
                )
                if affirmation in agreement:
                    remove(user, database)
                else:
                    print(f"{user} remains in the database")
            else:
                print("Invalid choice")
                continue
            break
        except TypeError as err:
            print(err)
            continue
        except ValueError as err:
            print(err)
            continue


def auth_system():
    """Central authorisation system"""
    database = "custom_racism.json"
    fix_file(database)
    user = input("And you are? ").capitalize().strip()
    if registered(user, database):
        print(f"{user} is already tracked")
    else:
        print(f"{user} is not tracked")
        print("Registering...")
        register(user, database)
        print(f"'{user}' is now tracked")
    print("Main Menu")
    main_menu(user, database)


if __name__ == "__main__":
    auth_system()

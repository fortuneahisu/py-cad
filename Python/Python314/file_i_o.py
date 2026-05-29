"""Practice on file input-output, targetting json"""

# import datetime
import json
import os
import random

from constants import agreement, project_alias

DATABASE = "database.json"


def fix_file(DATABASE):
    """Fix corrupted files"""
    if os.path.exists(DATABASE) and os.path.getsize(DATABASE) != 0:
        return None
    create(DATABASE)
    return None


def load_data(DATABASE):
    """Load database"""
    if os.path.exists(DATABASE):
        with open(DATABASE, "r", encoding="ANSI") as file:
            return json.load(file)
    else:
        return create(DATABASE)


def save_data(data, DATABASE):
    """Save database"""
    with open(DATABASE, "w", encoding="ANSI") as file:
        json.dump(data, file)


def create(DATABASE):
    """Create database"""
    with open(DATABASE, "w", encoding="ANSI"):
        data = {}
        print("Database initialised")
        save_data(data, DATABASE)


def registered(user):
    """Check if user is registered"""
    data = load_data(DATABASE)
    is_registered = False
    for identifier in data:
        if data[identifier]["Name"] == user:
            is_registered = True
            return is_registered
    return is_registered


# datetime.date.today().strftime('%d%m%y')
def register(user):
    """Register user"""
    identifier = f"{random.choice(project_alias)}{random.randint(0, 999999):06d}"
    data = load_data(DATABASE)
    data[identifier] = {"Name": user}
    save_data(data, DATABASE)
    get_info(user)
    if user[-1] == "s":
        grammar = ""
    else:
        grammar = "s"
    print(f"{user}'{grammar} ID: {identifier}")


def remove(user):
    """Deletes user by name"""
    data = load_data(DATABASE)
    user_id = "User's identifier"
    for identifier in data:
        if data[identifier]["Name"] == user:
            user_id = identifier
    del data[user_id]
    print(f"{user} deleted")
    save_data(data, DATABASE)


def get_age():
    """Get user's age"""
    while True:
        try:
            user_age = int(input("Age: "))
            break
        except TypeError as err:
            print(err)
            continue
        except ValueError as err:
            print(err)
    return user_age


def get_height():
    """Get user's height"""
    while True:
        try:
            user_height = float(input("Height: "))
            break
        except TypeError as err:
            print(err)
            continue
        except ValueError as err:
            print(err)
    return user_height


def get_info(user):
    """Amass user's information"""
    data = load_data(DATABASE)
    for identifier in data:
        if data[identifier]["Name"] == user:
            data[identifier]["Age"] = get_age()
            data[identifier]["Height"] = get_height()
    save_data(data, DATABASE)


def main_menu(user):
    """Main interface menu"""
    menu = ["Remove user"]
    for idx, function in enumerate(menu):
        print(f"{idx + 1}. {function}")
    while True:
        try:
            choice = int(input("Option: "))
            if choice == 1:
                affirmation = (
                    input(
                        f"Are you sure you want to deleted {user} from the database? "
                    )
                    .lower()
                    .strip()
                )
                if affirmation in agreement:
                    remove(user)
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
    fix_file(DATABASE)
    user = input("And you are? ").capitalize().strip()
    if registered(user):
        print(f"{user} is already tracked")
    else:
        print(f"{user} is not tracked")
        print("Registering...")
        register(user)
        print(f"'{user}' is now tracked")
    print("Main Menu")
    main_menu(user)


if __name__ == "__main__":
    auth_system()

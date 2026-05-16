"""Module responsible for tracking my study progress after August 17th"""

import datetime
import os
from constants import agreement, disagreement
date = datetime.date.today()
FILE = "progress_log.txt"
weekday = date.strftime("%A")
subject = 0
status = 0
content = "Printed content for assertion"
subject_status = {}

subjects = {
    "Monday": ("Maths", "Physics"),
    "Tuesday": ("Physics", "Chemistry"),
    "Wednesday": ("Maths", "Python"),
    "Thursday": ("Physics", "FreeCAD"),
    "Friday": ("Chemistry", "Maths"),
    "Saturday": ("Review", "Problem sets"),
    "Sunday": ("Light study", "Python problems"),
}



def write_to_file(mode:str):
    """Writing to file"""
    with open(FILE, mode) as log:
        log.write(f"{'-' * 50}\n")
        log.write(f"{date}\n")
        log.write(f"{'-' * 50}\n")
        for item in subject_status:
            log.write(f"-> {item} | [{subject_status[item]}]\n")
        log.write(f"{'-' * 50}\n")


def check_daily_status(subjects, subject_status):
    """Checking if a day's subjects have been studied"""
    for day in subjects:
        if weekday == day:
            for subject in subjects[day]:
                print(subject)
                while True:
                    try:
                        status = input("Status: ").lower().strip()
                        if status in agreement:
                            status = "Done"
                            subject_status[subject] = status
                            break
                        if status in disagreement:
                            status = "Pending indefinitely..."
                            subject_status[subject] = status
                            break
                        else:
                            print('"status" is either "true" or "false"')
                            continue
                    except TypeError:
                        print('"status" is text (true or false)')
                        break


def progress_log():
    """Main UX interface"""
    content = []
    check_daily_status(subjects, subject_status)
    if os.path.exists(FILE):
        write_to_file("a")
    else:
        write_to_file("w")
    for item in subject_status:
        content = f"-> {item} | [{subject_status[item]}]"
        print("-" * len(content))
        print(content)
    print("-" * len(content))
    print("\nContent appended to progress_log.txt\n")


if __name__ == "__main__":
    progress_log()

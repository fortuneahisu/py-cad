"""Module responsible for tracking my progress after August 17th"""
import datetime
import os

date = datetime.date.today()
FILE = "progress_log.txt"
weekday = date.strftime("%A")
subject = 0
status = 0
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


def write_to_file(mode):
    """Writing to file"""
    with open(FILE, mode) as log:
        log.write(f"{'-' * 100}\n")
        log.write(f"{date}\n")
        log.write(f"{'-' * 100}\n")
        for item in subject_status.items():
            log.write(f"-> {item} | [{subject_status[item]}]\n")
        log.write(f"{'-' * 100}\n")


for day in subjects:
    if weekday == day:
        for subject in subjects[day]:
            print(subject)
            while True:
                try:
                    status = input("Status: ")
                    if status.lower() == "true":
                        status = "Done"
                        subject_status[subject] = status
                        break
                    elif status.lower() == "false":
                        status = "Pending indefinitely..."
                        subject_status[subject] = status
                        break
                    else:
                        print('"status" is either "true" or "false"')
                        continue
                except TypeError:
                    print('"status" is text (true or false)')

if os.path.exists(FILE):
    try:
        write_to_file("a")

    except Exception as e:
        print(f"{e} occured")
else:
    try:
        write_to_file("w")
    except Exception as e:
        print(f"{e} occured")

print("Content appended to progress_log.txt")

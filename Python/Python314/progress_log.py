"""Module responsible for tracking my study progress after August 17th"""

import datetime

from constants import agreement, disagreement
from file_i_o import fix_file, load_data, save_data

date = datetime.date.today()
TIME_STAMP = str(datetime.datetime.now().strftime("%d%m%y%H%M"))
today = date.strftime("%A")
LOG_FILE = "progress_log.json"
TIME_TABLE = "time_table.json"


def subject_status():
    """Progress status for each subject for each day"""
    time_table = load_data(TIME_TABLE)
    subjects = []
    status = False
    for day in time_table:
        if day == today:
            for subject in time_table[day]:
                while True:
                    affirmation = input(f"Has {subject} been studied? ").lower().strip()
                    if affirmation in agreement:
                        status = True
                        subjects.append({subject: status})
                        print("Great!")
                        break
                    if affirmation in disagreement:
                        status = False
                        subjects.append({subject: status})
                        print("Pending indefinitely...")
                        break
                    print("What was that? ")
                    continue
    log_file = load_data(LOG_FILE)
    log_file[f"{TIME_STAMP}"] = {today: subjects}
    save_data(log_file, LOG_FILE)


def run_daily():
    """Make sure there's one entry per day"""
    log_file = load_data(LOG_FILE)
    for unique_id in log_file:
        if TIME_STAMP[0:5] == unique_id[0:5]:
            print("You've inputted for today, come tomorrow")
            return True
    return False


def gold_star():
    """A little something to cheer you up"""
    log_file = load_data(LOG_FILE)
    for unique_id in log_file:
        if TIME_STAMP == unique_id:
            for subject_pair in log_file[TIME_STAMP][today]:
                for subject in subject_pair:
                    if subject_pair[subject] is False:
                        return False
    return True


def progress_log():
    """Main UX interface"""
    fix_file(LOG_FILE)
    if run_daily():
        while True:
            affirmation = input("or do you want to edit your input? ")
            if affirmation in agreement:
                subject_status()
                if gold_star():
                    print("Nice, you've had it for today")
                    print("Don't forget tomorrow")
                elif not gold_star():
                    print("Awwn, tomorrow is another day mate")
                break
            if affirmation in disagreement:
                print("Make sure to study tomorrow")
                break
            print("I did not get that")
            continue
        return
    subject_status()
    if gold_star():
        print("Hurray!, You completed today. Have a good night rest, chum")
    elif not gold_star():
        print("You'll get it later")
    return


if __name__ == "__main__":
    progress_log()

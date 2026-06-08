"""Module responsible for tracking my study progress after August 17th"""

import datetime

from constants import agreement, disagreement
from file_i_o import create, fix_file, load_data, save_data

date = datetime.date.today()
TIME_STAMP = str(datetime.datetime.now().strftime("%d%m%y"))
today = date.strftime("%A")
LOG_FILE = "progress_log.json"
TIME_TABLE = "time_table.json"
STREAK = "streak.json"


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
    """Making sure there's one entry per day"""
    log_file = load_data(LOG_FILE)
    for unique_id in log_file:
        if TIME_STAMP == unique_id:
            print("You've inputted for today, come tomorrow")
            return True
    return False


def gold_star():
    """A little something to cheer you up"""
    log_file = load_data(LOG_FILE)
    golden = True
    for unique_id in log_file:
        if TIME_STAMP == unique_id:
            for subject_pair in log_file[TIME_STAMP][today]:
                for subject in subject_pair:
                    if subject_pair[subject] is False:
                        golden = False
    streak = load_data(STREAK)
    streak[TIME_STAMP] = golden
    save_data(streak, STREAK)
    return golden


def streak_count():
    """The streak counter"""
    streak = load_data(STREAK)
    consecutive_count = 0
    for key in streak:
        if streak[key] is True:
            consecutive_count += 1
        elif streak[key] is False:
            consecutive_count = 0
    if consecutive_count == 0:
        print("Keep studying and your streak count will continue to grow")
    elif consecutive_count == 1:
        print("Nice, now keep pushing")
    elif consecutive_count == 7:
        print("A week of dedication, you're on fire")
    elif consecutive_count == 30:
        print("One month of focus, congrats on this one")
    elif consecutive_count == 90:
        print("Impressive, I don't think you need me anymore")
        print("But feel free to keep recording your progress")
    elif consecutive_count == 365:
        print("One year of straight bars, I'm officially rendered useless")
    else:
        print(f"{consecutive_count} times in a row, keep it up")


def sync_log_streak():
    log = load_data(LOG_FILE)
    streak = load_data(STREAK)
    log_keys = []
    streak_keys = []
    for key in log:
        log_keys.append(key)
    for key in streak:
        streak_keys.append(key)
    if log_keys == streak_keys:
        return
    else:
        print("Falsification detected")
        print("Re-initialising streak data and log data...")
        create(LOG_FILE)
        create(STREAK)


def progress_log():
    """Main UX interface"""
    fix_file(LOG_FILE)
    fix_file(STREAK)
    sync_log_streak()
    if run_daily():
        while True:
            affirmation = input("or do you want to edit your input? ").lower().strip()
            if affirmation in agreement:
                print("Your streak data will be unaffected by this edition")
                subject_status()
                print("Don't forget tomorrow")
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
        streak_count()
    else:
        print("You'll get it later")
    return


if __name__ == "__main__":
    progress_log()

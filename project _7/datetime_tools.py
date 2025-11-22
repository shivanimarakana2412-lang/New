from datetime import datetime
import time

def current_datetime():
    """Returns the current date and time."""
    now = datetime.now()
    return now.strftime("%d-%m-%Y %H:%M:%S")


def date_difference(fdate_str, sdate_str):
    """Calculates difference between two dates."""
    fdate = datetime.strptime(fdate_str, "%Y-%m-%d")
    sdate = datetime.strptime(sdate_str, "%Y-%m-%d")
    diff = sdate - fdate
    return diff.days


def format_date():
    """Returns formatted date and converts back to datetime."""
    now = datetime.now()
    formatted = now.strftime("%d-%m-%Y %H:%M:%S")
    converted = datetime.strptime(formatted, "%d-%m-%Y %H:%M:%S")
    return formatted, converted


def stopwatch():
    """Simple user-controlled stopwatch."""
    input("Press Enter to start the stopwatch...")
    start = datetime.now()

    input("Press Enter to stop the stopwatch...")
    end = datetime.now()

    total_time = end - start
    return round(total_time.total_seconds(), 2)


def countdown(sec):
    """Countdown timer using time.sleep."""
    while sec > 0:
        mins, secs = divmod(sec, 60)
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        sec -= 1
    return "Time's up!"
import datetime
import os
from colorama import init, Fore, Back, Style

init(autoreset=True)

# -------------------------------
# CONFIGURATION DATA
# -------------------------------

BS_YEAR = 2082

# Month configuration: name, total_days, starting_weekday
# Weekday index: 0=Sun, 1=Mon, ... 6=Sat

BS_MONTHS = {
    1: {"name": "Baisakh", "days": 31, "start": 1},
    2: {"name": "Jestha", "days": 31, "start": 4},
    3: {"name": "Asar", "days": 32, "start": 0},
    4: {"name": "Shrawan", "days": 31, "start": 4},
    5: {"name": "Bhadra", "days": 31, "start": 0},
    6: {"name": "Asoj", "days": 31, "start": 3},
    7: {"name": "Kartik", "days": 30, "start": 6},
    8: {"name": "Mangsir", "days": 29, "start": 1},
    9: {"name": "Push", "days": 30, "start": 2},
    10: {"name": "Magh", "days": 29, "start": 4},
    11: {"name": "Falgun", "days": 30, "start": 5},
    12: {"name": "Chaitra", "days": 30, "start": 0},
}

WEEKDAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


# -------------------------------
# UTILITY FUNCTIONS
# -------------------------------

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def highlight_day(day, current_day):
    if day == current_day:
        return Back.GREEN + Fore.WHITE + f"{day:>2}" + Style.RESET_ALL
    return f"{day:>2}"


def highlight_weekday(day_name):
    if day_name == "Sat":
        return Fore.RED + day_name + Style.RESET_ALL
    return day_name


# -------------------------------
# CALENDAR GENERATOR
# -------------------------------

def print_month(month_number, current_day=None):
    month = BS_MONTHS[month_number]

    print(f"\n{month['name']} {BS_YEAR}".center(40))
    print("-" * 40)

    # Print weekdays header
    for wd in WEEKDAYS:
        print(highlight_weekday(wd).center(5), end="")
    print()

    start = month["start"]
    total_days = month["days"]

    day_counter = 1

    # First empty spaces
    for _ in range(start):
        print("     ", end="")

    while day_counter <= total_days:
        weekday_index = (start + day_counter - 1) % 7

        day_display = highlight_day(day_counter, current_day)
        print(day_display.center(5), end="")

        if weekday_index == 6:
            print()

        day_counter += 1

    print("\n")


# -------------------------------
# SIMPLE AD → BS CONVERTER
# (Based on your previous mapping logic)
# -------------------------------

def convert_ad_to_bs():
    today = datetime.date.today()

    # Base mapping (example: April 14 = Baisakh 1)
    base_ad = datetime.date(today.year, 4, 14)
    delta_days = (today - base_ad).days

    if delta_days < 0:
        base_ad = datetime.date(today.year - 1, 4, 14)
        delta_days = (today - base_ad).days

    month = 1
    day = 1 + delta_days

    for m in range(1, 13):
        if day <= BS_MONTHS[m]["days"]:
            return m, day
        else:
            day -= BS_MONTHS[m]["days"]

    return 12, day


# -------------------------------
# MAIN MENU
# -------------------------------

def main():
    clear_screen()

    print("NEPALI CALENDAR SYSTEM".center(40))
    print("""
1. Show Current Nepali Date
2. Show All Months
3. Show Specific Month
""")

    choice = int(input("Enter choice (1-3): "))

    if choice == 1:
        month, day = convert_ad_to_bs()
        print_month(month, day)

    elif choice == 2:
        for m in range(1, 13): 
            print_month(m)

    elif choice == 3:
        m = int(input("Enter month number (1-12): "))
        if 1 <= m <= 12:
            print_month(m)
        else:
            print("Invalid month!")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()

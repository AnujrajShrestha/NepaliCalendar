from flask import Flask, render_template
import datetime

app = Flask(__name__)

BS_YEAR = 2082

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
# AD → BS Conversion
# -------------------------------
def convert_ad_to_bs():
    today = datetime.date.today()

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
# Generate Calendar Grid
# -------------------------------
def generate_calendar(month, current_day=None):
    data = BS_MONTHS[month]
    start = data["start"]
    days = data["days"]

    calendar = []
    week = [""] * 7

    day_counter = 1

    # Fill first week
    for i in range(start, 7):
        week[i] = day_counter
        day_counter += 1

    calendar.append(week)

    # Remaining weeks
    while day_counter <= days:
        week = [""] * 7
        for i in range(7):
            if day_counter <= days:
                week[i] = day_counter
                day_counter += 1
        calendar.append(week)

    return calendar


# -------------------------------
# ROUTES
# -------------------------------

@app.route("/")
def index():
    current_month, current_day = convert_ad_to_bs()
    calendar = generate_calendar(current_month, current_day)

    return render_template(
        "month.html",
        month=BS_MONTHS[current_month]["name"],
        year=BS_YEAR,
        calendar=calendar,
        weekdays=WEEKDAYS,
        current_day=current_day
    )


@app.route("/month/<int:month_id>")
def show_month(month_id):
    if month_id not in BS_MONTHS:
        return "Invalid month"

    calendar = generate_calendar(month_id)

    return render_template(
        "month.html",
        month=BS_MONTHS[month_id]["name"],
        year=BS_YEAR,
        calendar=calendar,
        weekdays=WEEKDAYS,
        current_day=None
    )


# -------------------------------
if __name__ == "__main__":
    app.run(debug=True)
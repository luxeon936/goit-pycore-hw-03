from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    """
    Calculation of celebration dates

    Returns:
        List of celebration dates
    """
    today = datetime.now().date()
    upcoming_birthdays = []
    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        if birthday_this_year.weekday() in [5, 6]:
            birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day
                                                             + (7 - birthday_this_year.weekday()))
        if birthday_this_year <= today + timedelta(days=7):
            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": birthday_this_year.strftime("%Y.%m.%d"),
                }
            )
    return upcoming_birthdays
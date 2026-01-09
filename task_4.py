from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    date_today = datetime.today().date()
    upcoming_birthday = []
    for user in users:
        name = user["name"]
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=date_today.year)
        if birthday_this_year < date_today:
            birthday_this_year = birthday_this_year.replace(year=date_today.year + 1)
        days_until_birthday = (birthday_this_year - date_today).days
        if 0 <= days_until_birthday <= 7:
            if birthday_this_year.weekday() == 5:
                birthday_this_year += timedelta(days=2)
            elif birthday_this_year.weekday() == 6:
                birthday_this_year += timedelta(days=1)
            
            upcoming_birthday.append({
                "name": name,
                "congratulation_date": birthday_this_year
            })

    return upcoming_birthday
    

users = [
    {"name": "John Doe", "birthday": "1985.01.15"},
    {"name": "Jane Smith", "birthday": "1990.01.14"}
]


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

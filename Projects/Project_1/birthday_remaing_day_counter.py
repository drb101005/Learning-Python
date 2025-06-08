from datetime import datetime, timedelta

birth_input = input("Enter your birth date (YYYY-MM-DD): ")
birth_date = datetime.strptime(birth_input, "%Y-%m-%d").date()
today = datetime.today().date()
next_birthday = birth_date.replace(year=today.year)

if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

days_left = (next_birthday - today).days

print(f" Your next birthday is in {days_left} day(s)!")

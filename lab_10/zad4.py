from datetime import date, timedelta


def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
        age -= 1

    birth_date_next_year = birth_date.replace(year=today.year)

    if birth_date_next_year < today:
        birth_date_next_year = birth_date_next_year.replace(year=today.year + 1)

    days_left = (birth_date_next_year - today).days

    months = today.month - birth_date.month
    if months < 0:
        months += 12
    days = today.day - birth_date.day
    if days < 0:
        months -= 1
        days += (birth_date_next_year - timedelta(days=1)).day

    print(f"Dzisiaj masz {age} lat, {months} miesięcy i {days} dni.")
    print(f"Do twoich kolejnych urodzin pozostało {days_left} dni.")


calculate_age(date(1999, 4, 27))

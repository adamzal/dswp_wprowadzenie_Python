from datetime import datetime
import pytz


def display_time_in_different_timezones():
    time_str = input("Podaj czas w formacie HH:MM:SS: ")
    time_parts = time_str.split(':')

    if len(time_parts) != 3:
        print("Nieprawidłowy format czasu!")
        return

    hour, minute, second = map(int, time_parts)
    time = datetime.now().replace(hour=hour, minute=minute, second=second)

    timezones = {
        'Tokyo': 'Asia/Tokyo',
        'Waszyngton': 'America/New_York',
        'Sydney': 'Australia/Sydney',
        'Londyn': 'Europe/London'
    }

    print("Czas w różnych strefach czasowych:")

    for city, timezone in timezones.items():
        city_time = time.astimezone(pytz.timezone(timezone))
        print(f"{city}: {city_time.strftime('%H:%M:%S')}")


display_time_in_different_timezones()

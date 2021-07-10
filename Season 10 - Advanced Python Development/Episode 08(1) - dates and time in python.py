# Date and Time in Python

from datetime import datetime, timezone, timedelta

print(datetime.now())   # shows general system time on which you are currently working on

print(datetime.now(timezone.utc))   # Comes with an aware object, which shows offset

# timedelta - shows the difference in time

today = datetime.now(timezone.utc)
tomorrow = today + timedelta(days=1)

print(today)        # prints today's date and time
print(tomorrow)     # prints tomorrow's date and same time

print(today.strftime('%d-%m-%Y %H:%M:%S'))
"""
Y - four digits

strftime means string format time
strptime means string parse time

"""
# asking user for the date

user_date = input('Enter date in YYYY-MM-DD (including - hyphens) : ')
user_date = datetime.strptime(user_date, '%Y-%m-%d')

print(user_date)


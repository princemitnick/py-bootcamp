import datetime as dt

now = dt.datetime.now()

year = now.year
wd = now.weekday()
day = now.day


date_of_birth = dt.datetime(year=1995, month=12, day=23)

print(date_of_birth)
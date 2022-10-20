
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month > 12 or month < 1:
        return "Invalid month"
    elif is_leap(year):
        months[1] = 29
        return months[month-1]
    else:
        return months[month-1]


days = days_in_month(year=2016, month=2)

print(days)

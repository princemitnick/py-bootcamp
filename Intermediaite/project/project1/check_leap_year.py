def check_leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        return True
    # Else it is not a leap year
    else:
        return False


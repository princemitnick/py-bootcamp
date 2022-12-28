from datetime import date


print(date.today())

birthday = (2000, 2, 9)

h = date(1999, 2, 3)

birthdate = "1999-08-09"

birthdate_list = birthdate.split("-")

m = date(int(birthdate_list[0]), int(birthdate_list[1]), int(birthdate_list[2]))

print(m.day)
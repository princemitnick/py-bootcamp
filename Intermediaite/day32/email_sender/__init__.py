import email
import smtplib

import pandas
import datetime as dt


data = pandas.read_csv("./data/birthdays.csv").to_dict(orient="records")
CONNECTION = "smtp-mail.outlook.com"
EMAIL_FROM = "ingjeanbaptiste@hotmail.com"
USER = "ingjeanbaptiste@hotmail.com"
PASSWORD = "enidepack@404"

birthday_today = []
now = (dt.datetime.now().month, dt.datetime.now().day)

for person in data:

    birth = dt.datetime(year=person['year'], month=person['month'], day=person['day'])
    if now == (birth.month, birth.day):
        birthday_today.append(person)
    else:
        pass


if len(birthday_today) == 0:
    print("No one has his birthday today")
else:
    for person in birthday_today:
        letter = """"""
        with open("./data/letter_1.txt") as data_file:
            for line in data_file:
                letter += line.replace("[NAME]", person['name'])
            msg = email.message_from_string(letter)
            msg['Subject'] = "Happy Birthday!"
            with smtplib.SMTP(CONNECTION) as connection:
                connection.starttls()
                connection.login(USER, PASSWORD)
                connection.sendmail(from_addr=EMAIL_FROM, to_addrs=person['email'], msg=msg.as_string())

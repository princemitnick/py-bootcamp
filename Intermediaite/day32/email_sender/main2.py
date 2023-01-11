import random
import smtplib
from datetime import datetime

import pandas

EMAIL = "ingjeanbaptiste@hotmail.com"
PASSWORD = "enidepack@404"

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("./data/birthdays.csv")

birthdays_dict = {(data_row ["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"data/letter_{random.randint(1,2)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=birthday_person['email'],
            msg=f"Subject: Happy Birthday\n\n {contents}"
        )

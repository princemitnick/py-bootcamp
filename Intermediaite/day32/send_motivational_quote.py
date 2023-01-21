import random
import smtplib
import email
import datetime as dt


quotes = []
with open("./email_sender/quotes.txt") as quotes_files:
    for qt in quotes_files:
        quotes.append(qt)

quote = random.choice(quotes)
text = quote.split("-")[0]
author = quote.split("-")[1]

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

now = dt.datetime.now()

message = f"""
{text}
\t\t\t\t\t\t\t\t{author}

From Prince.
"""
msg = email.message_from_string(message)
msg['Subject'] = f"Quote for {days[now.weekday()]}"

with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    connection.starttls()
    connection.login("ingjeanbaptiste@hotmail.com", "enidepack@404")
    connection.sendmail(from_addr="ingjeanbaptiste@hotmail.com", to_addrs="barnabeebarthelemy@gmail.com", msg=msg.as_string())


import smtplib
import email

my_email = "ingjeanbaptiste@hotmail.com"
password = "enidepack@404"
message = """
Hello Everyone,

I'd like you to announce my immediate retirement from club 
and national team.

Prince
"""
msg = email.message_from_string(message)
msg['Subject'] = "Greetings"

print(msg)

with smtplib.SMTP("smtp-mail.outlook.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="ingjeanbaptiste@gmail.com", msg=msg.as_string())

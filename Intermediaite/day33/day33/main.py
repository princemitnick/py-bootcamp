import requests
from datetime import datetime
import smtplib
import email

MY_LAT = 18.971188
MY_LONG = -72.285217
EMAIL = "ingjeanbaptiste@hotmail.com"
PASSWORD = "enidepack@404"


def is_iss_overhead():
    ISS_API_URL = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=ISS_API_URL)
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_nigh():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    SUNRISE_SUNSET_API = "https://api.sunrise-sunset.org/json"
    response = requests.get(url=SUNRISE_SUNSET_API, params=parameters)

    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise = int(sunrise.split("T")[1].split(":")[0])
    sunset = int(sunset.split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


if is_iss_overhead() and is_nigh():
    msg = """
    Subject:Look UP
    The ISS is above you in the sky!
    """
    message = email.message_from_string(msg)
    with smtplib.SMTP("smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login("ingjeanbaptiste@hotmail.com", "enidepack@404")
        connection.sendmail(from_addr="ingjeanbaptiste@hotmail.com", to_addrs="ingjeanbaptiste@gmail.com",
                            msg=message.as_string())

    print("Done")
else:
    print("noo")
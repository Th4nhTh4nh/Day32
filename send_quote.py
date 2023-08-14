import smtplib
import datetime
import random

MY_EMAIL = "phamdatthanh213@gmail.com"
MY_PASSWORD = "iaojfqjfdmylcdtn"
"""
def send_email(line):
    my_email = "phamdatthanh213@gmail.com"
    my_pass = "xtyaryflvnifqeyb"
    with smtplib.SMTP("smtp.google.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="thanh1thanh.ph@gmail.com",
            msg=f"Subject:Quote\n\n{line}",
        )
"""

now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    # send_email(quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}",
        )
# my_email = "phamdatthanh213@gmail.com"
# password = "xtyaryflvnifqeyb"
# with smtplib.SMTP("smtp.gmail.com") as connection:
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#   from_addr=my_email,
#   to_addrs="thanh1thanh.ph@gmail.com",
#   msg="Subject:Hello\n\nThis is the body of my email",
# )

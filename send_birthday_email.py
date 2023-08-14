##################### Normal Starting Project ######################
import pandas
import datetime
import random
import smtplib

MY_EMAIL = "phamdatthanh213@gmail.com"
MY_PASSWORD = "iaojfqjfdmylcdtn"
now = datetime.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {
    (data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()
}
# print(birthdays_dict)
if today in birthdays_dict:
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    person = birthdays_dict[today]
    with open(file_path) as letter:
        contents = letter.read()
        sent_letter = contents.replace("[NAME]", person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=person["email"],
            msg=f"Subject:TEST\n\n{sent_letter}",
        )

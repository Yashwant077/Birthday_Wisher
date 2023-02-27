import pandas
import random
import smtplib
from datetime import datetime

MY_EMAIL = "yashwant07081@gmail.com"
MY_PASSWORD = "abcd1234@"   # it will not gonna work for you

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
print(birthday_dict)
today = datetime.now()
today_tuple = (today.month, today.day)

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    file_path = f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )

"""
In smtp.SMTP(), the values varies according to sender's mail provider. 
The values for some of the famous mail providers is as follows:
1. Gmail(smtp.gmail.com)
2. Yahoo(smtp.mail.yahoo.com)
3. Hotmail(smtp.live.com)
4. Outlook(smtp-mail.outlook.com)
"""

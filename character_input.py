"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""


import datetime


user_name = input("what is your name > ")
user_age = input("What is you are > ")

integer_age = int(user_age)

year = (100 - integer_age) * 365

today = datetime.date.today()

future = today + datetime.timedelta(days=year)  # (100 - integer_age) * 365)
print("You are ", integer_age, "year old,", user_name + ".", "Today is", str(today) + ".")
print("In ", future, "you will be a centenarian")

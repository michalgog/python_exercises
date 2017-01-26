"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

# import date module
import datetime

# what about timedelta?

# getting data from user
user_name = input("what is your name > ")
user_age = input("What is you are > ")

# changing user_age to integer, it was a string before
integer_age = int(user_age)

# defining the variable year
year = (100 - integer_age) * 365

# defining actually date
today = datetime.date.today()

# calculating future date when user hits the 100 years old
future = today + datetime.timedelta(days=year)  # (100 - integer_age) * 365)

# printing data
print("You are ", integer_age, "year old,", user_name + ".", "Today is", str(today) + ".")
print("In ", future, "you will be a centenarian")

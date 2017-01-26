"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
they guessed too low, too high, or exactly right.
"""

import random
import itertools

# computer random choice
numbers = random.randint(1, 9)

# user set to False for while loop
user = False

# while loop is used for iteration
while not user:
    # module for infinite iteration in for loop
    for i in itertools.count():
        user_num = int(input("Enter digit from 1 to 9: "))
        if 0 < user_num < 10:
            # setting user to True allows program to
            user = True
            print("user choice", user_num)
        elif user_num == numbers:
            print("You guessed the digit.")
        else:
            print("Wrong digit, please choose from 1 to 9.")
        print("computer choice", numbers)
        print("user's tries:", i)


'''
What was changed?

if user_num > 0 and user_num < 10:

to

if 0 < user_num < 10:

and this:

numbers = list(range(1, 10))
computer_choice = random.choice(numbers)

to

number = random.randint(1, 10)
'''






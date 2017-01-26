"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

while True:
    try:

        user_string = input("Please enter the string: ")
        check_user_input = user_string[::-1]

        if user_string == check_user_input:
            print("Yes, it is palindrome.")
            continue
        elif user_string != check_user_input:
            print("Sorry, your word is not a palindrome.")
    except ValueError:
            print("Unknown error occurred")

"""
Ask the user for a number and determine whether the number is prime or not.
"""


def get_number(prompt):
    return int(input(prompt))


def is_prime(number):
    """return True for prime numbers, False otherwise"""
    if number == 1:
        prime = True
    elif number == 2:
        prime = False
    else:
        prime = True
        for check_number in range(2, (number / 2) + 1):
            if number % check_number == 0:
                prime = False
                break
    return prime


def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "not"
    print(number, " is", descriptor, "prime.", sep="", end="\n\n")


while 1 == 1:
    print_prime(get_number("Enter a number to check. Ctrl+C to exit. "))

'''
for num in range(1, 101):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        print(num)
'''

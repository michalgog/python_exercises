# num = input("Pick a number: ")
# check = int(num)
# double_check = check % 2
#
#
# if double_check == 0 or double_check / 4:
#     print (num, "is even")
#     print (num, "is multiple of 4")
# elif double_check == 1:
#     print (num, "is odd")
# else:
#     print("Is not a number")

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))

if num % 4 == 0:
    print(num, "is a multiple of 4")
elif num % 2 == 0:
    print(num, "is an even number")
else:
    print(num, "is an odd number")

if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)













#
# if double_check == 1:
#     print (num, "is a odd number.")
# elif check % 2 is 0:
#     print ('wrrrrrrrrr')
# elif check / 4 and double_check == 0:
#     print ("Your choice", num, "is multiple of 4.")
# else:
#     print (num, "is even.")
#


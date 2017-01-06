num = int(input("Enter number: "))

listRange = list(range(1, num + 1))

divList = []

for number in listRange:
    if num % number == 0:
        divList.append(number)

print(divList)


# even_list = []
# odd_list = []
#
# if user_num % 2 == 0:
#     even_list.append(user_num)
#     print("even list")
# elif user_num % 2 == 1:
#     odd_list.append(user_num)
#     print("Odd list")
# else:
#     print("Error")




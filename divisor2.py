num = int(input("Enter number: "))

listRange = list(range(1, num + 1))

divList = []

for number in listRange:
    if num % number == 0:
        divList.append(number)

print(divList)




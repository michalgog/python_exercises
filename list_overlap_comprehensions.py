"""
write a program that returns a list that contains only the elements that are common between the lists
(without duplicates).
Make sure your program works on two lists of different sizes.
"""

import random

list_no_1 = []
list_no_2 = []

for i in range(10):
    list_no_1.append(random.randint(0, 30))
    list_no_2.append(random.randint(0, 30))

print(list_no_1)
print(list_no_2)

new_set1 = set(list_no_1)
new_set2 = set(list_no_2)

print("the common int is: ", (new_set1 & new_set2))


'''
random.sample(range(a,b), x)
x is a length of list.
'''

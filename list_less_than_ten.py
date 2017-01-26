"""
Write a program that prints out all the elements of the list that are less than 5.
"""

list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

list_b = [i for i in list_a if i < 5]

print(list_b)


"""
Write a function list_to_set(input_list) that takes a
list as input and returns a set containing unique elements 
from the list.
"""


def list_to_set(input_list):
    result_set = set(input_list)
    return result_set


my_list = [1, 2, 2, 3, 4, 4, 5]

result_set = list_to_set(my_list)
print("Original List:", my_list)
print("Set from List:", result_set)

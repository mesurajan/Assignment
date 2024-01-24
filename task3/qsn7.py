"""
Write a function remove_duplicates(input_list) that takes a list as an argument and
returns a new list with duplicates removed using a set.
"""


# ---->Solution :
input_list = [1, 2, 2, 3, 4, 4, 5]

# using a set to remove duplicates while preserving the order
remove_duplicates = list(dict.fromkeys(input_list))
"""
dict.fromkeys(iterable, value) is a class method that creates a new dictionary with keys taken 
from the iterable (input_list in this case).
The values for all keys are set to a default value, which is None if not specified.
and
The list() constructor is used to convert the dictionary keys into a list.
This operation effectively removes duplicates because a dictionary cannot have duplicate keys.
The result, which is a list without duplicates, is assigned to the variable remove_duplicates.
"""


print("Original List:", input_list)
print("List with Duplicates Removed:", remove_duplicates)

breakpoint()


def remove_duplicates(input_list):
    unique_elements = set()
    unique_list = [
        x for x in input_list if not (x in unique_elements or unique_elements.add(x))
    ]
    return unique_list


new_list = [1, 2, 3, 3, 4, 5, 6, 6, 7, 8]
result_list = remove_duplicates(new_list)
print("original list:", new_list)
print("List without Duplicates:", result_list)

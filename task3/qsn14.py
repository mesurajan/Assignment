"""
Given a tuple with repeated elements, write a program 
to count the occurrences of a specific element within
the tuple.

"""


def count_occurrences(input_tuple, target_element):
    occurrences = input_tuple.count(target_element)
    return occurrences


# Example usage:
my_tuple = (1, 2, 3, 1, 4, 1, 5, 1)

target_element = 1

result = count_occurrences(my_tuple, target_element)
print(f"The element {target_element} occurs {result} times in the tuple.")

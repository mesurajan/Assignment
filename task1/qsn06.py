"""
Reverse a given string without using the reverse function or slicing. 
"""
# SOLUTIONS--->

original_string = input("Enter a string: ")


reversed_string = ""
index = len(original_string) - 1

while index >= 0:
    reversed_string += original_string[index]
    index -= 1


print("Original String:", original_string)
print("Reversed String:", reversed_string)

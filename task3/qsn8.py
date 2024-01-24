"""
Given the sets A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7, 8}, write a
program to find and print the union of the sets.
"""
# ---->Solution
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8, 9, 10, 11, 12}
union = set_A | set_B
print(f"The union of {set_A} and {set_B} is : \n", union)

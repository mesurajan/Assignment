"""
Create two sets, set_a and set_b, each with some common and some unique elements. Write a program to 
find and print the symmetric difference of the two sets.
"""

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


symmetric_difference = set_a.symmetric_difference(set_b)


print("Set A:", set_a)
print("Set B:", set_b)
print("Symmetric Difference:", symmetric_difference)

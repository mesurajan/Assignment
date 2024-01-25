"""
Given three sets, set1, set2, and set3, write a program to find 
and print the intersection of all three sets.
"""

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {5, 8, 9, 10}


intersection_result = set1.intersection(set2, set3)

print("Set 1:", set1)
print("Set 2:", set2)
print("Set 3:", set3)
print("Intersection of all three sets:", intersection_result)

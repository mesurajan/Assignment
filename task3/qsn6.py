"""
Create two sets, set1 and set2, each containing at least 5 unique integers.
Write a program to find and print the intersection of the two sets.
"""
# ---->Solution
set1 = {1, 2, 3, 4, 5, 6, 7, 8}
set2 = {5, 6, 7, 8, 9, 10, 11}

intersection_set = set1 & set2
print("Intersection of set1 and set2:", intersection_set)

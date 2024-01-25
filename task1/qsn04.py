"""
WAP to demonstrate the use case of insert() 
and extend() methods in Python lists. 
"""
# SOLUTION--->

fruits = ["apple", "banana", "orange"]


print("Original list:", fruits)
fruits.insert(1, "grape")
print("After insert():", fruits)


additional_fruits = ["kiwi", "melon", "pear"]
fruits.extend(additional_fruits)
print("After extend():", fruits)


vegetables = ["carrot", "broccoli", "spinach"]
fruits.extend("pineapple")
print("After extend() with string:", fruits)

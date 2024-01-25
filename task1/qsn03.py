"""
Create a list of integers and then write a Python program to find  
the sum of all the elements in the list. 
"""
# SOLUTION--->
import math

numbers = [1, 2, 3, 4, 5]


sum_of_elements = 0
for num in numbers:
    sum_of_elements += num

# Display the result
print(f"The sum of all elements in the list is: {sum_of_elements}")

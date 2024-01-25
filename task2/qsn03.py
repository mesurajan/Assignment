"""
Write a program that takes a number as input and prints its 
factorial using a while loop.
"""
# Take input from the user
number = int(input("Enter a number: "))

# Initialize variables
factorial = 1
current_number = 1


while current_number <= number:
    factorial *= current_number
    current_number += 1


print(f"The factorial of {number} is: {factorial}")

"""
Create a program that uses a loop to print the multiplication 
table of a given number. 
"""
# SOLUTIONS--->

try:
    number = int(input("Enter a number to generate its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()


print(f"Multiplication table for {number}:")

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

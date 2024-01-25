"""
Create a program that uses the continue statement to skip printing even
numbers in a loop
"""

for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

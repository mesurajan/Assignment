"""
Implement a program that iterates over a list of numbers
and prints only the even ones. 
"""

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even numbers:")
for number in number_list:
    if number % 2 == 0:
        print(number)

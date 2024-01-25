"""
Write a program that iterates over a list of numbers and breaks the loop when 
a negative number is encountered. 
"""

numbers_list = [3, 7, 1, -2, 9, 5, -4, 8]


for number in numbers_list:
    if number < 0:
        print("Negative number encountered. Breaking the loop.")
        break
    else:
        print(number)

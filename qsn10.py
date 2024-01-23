"""
Implement a program that counts the number of vowels in 
a given string using a loop.
"""
# SOLUTIONS--->

input_string = input("Enter a string: ")


vowel_count = 0


for char in input_string:
    if char.lower() in "aeiou":
        vowel_count += 1


print(f"Number of vowels in the string: {vowel_count}")
"""
we are learning to push data 
"""

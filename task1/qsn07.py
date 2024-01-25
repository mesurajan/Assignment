"""
Write a Python program to check if a given string is a palindrome. 
"""
# SOLUTIONS--->

input_string = input("Enter a string: ")


cleaned_string = "".join(input_string.split()).lower()


is_palindrome = True
length = len(cleaned_string)

for i in range(length // 2):
    if cleaned_string[i] != cleaned_string[length - i - 1]:
        is_palindrome = False
        break


if is_palindrome:
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")

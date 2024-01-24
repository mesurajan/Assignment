"""
Implement a program that calculates and prints the sum
of digits of a given number using a while loop.
"""
user_input = int(input("Enter a number: "))
number = abs(user_input)

# Initialize sum to 0
digit_sum = 0
while number > 0:
    # Extract the last digit
    digit = number % 10
    
    # Add the digit to the sum
    digit_sum += digit
    
    # Remove the last digit
    number //= 10



print(f"The sum of digits of {user_input} is: {digit_sum}")

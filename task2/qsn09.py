"""
Implement a program that uses the else clause in a loop to print a message
only if the loop completes without hitting a break statement.
"""

for number in range(1, 6):
    if number == 4:
        print("Breaking the loop when number is 4.")
        break
    print(number)
else:
    print("Loop completed without hitting a break statement.")

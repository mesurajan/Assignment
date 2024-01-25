"""
Write a program to print a pattern of stars in the shape
of a right-angled triangle.
"""

num_rows = int(input("Enter the number of rows for the triangle: "))


for i in range(1, num_rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

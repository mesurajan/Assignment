"""
Create a program to generate a multiplication
table in a matrix format.
"""

table_size = int(input("Enter the size of the multiplication table: "))


for i in range(1, table_size + 1):
    for j in range(1, table_size + 1):
        print(f"{i * j:4}", end="")
    print()

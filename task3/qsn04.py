"""
Write a function swap_elements(tuple_var) 
that takes a tuple as an argument and returns
a new tuple where the first and last elements are
swapped.
"""
# ---->Solution
original_tuple_var = ("apple", 3.14, 42)

tuple_var = (original_tuple_var[-1], *original_tuple_var[1:-1], original_tuple_var[0])

print("The Original data is:", original_tuple_var)
print("The data after swapping is:", tuple_var)


"""
just an example i tried just for fun :


original_tuple_var = input("Enter the data to be tupled: ")
# Convert the input string to a tuple
tuple_var = tuple(original_tuple_var)
# Check if the tuple has at least two elements
if len(tuple_var) >= 2:
    # Swapping the first and last elements
    tuple_var = (tuple_var[-1], *tuple_var[1:-1], tuple_var[0])
else:
    print("The input should have at least two elements.")
print("The Original data is:", original_tuple_var)
print("The data after swapping is:", tuple_var)

"""

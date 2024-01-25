"""
Write a program to remove duplicate elements from a list.
"""
# SOLUTIONS--->

original_list = [1, 2, 3, 2, 4, 5, 6, 1, 7, 8, 8, 9]


unique_list = []
for item in original_list:
    if item not in unique_list:
        unique_list.append(item)


print("Original List:", original_list)
print("List after removing duplicates:", unique_list)


"""
In this program:
1.The original_list contains duplicate elements.
2.A new list called unique_list is used to store elements without duplicates
3.A loop iterates through each element in the original_list.
4.If an element is not already present in the unique_list, it is appended to the unique_list.
5.The final result is a list without duplicate elements.

"""

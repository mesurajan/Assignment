"""
Write a function merge_dicts(dict1, dict2) that takes two dictionaries
as arguments and returns a new dictionary containing the combined key-value
pairs of both dictionaries. If there are common keys, the values from the
second dictionary should overwrite the values from the first dictionary.
Given the dictionary grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92},
write a program that calculates and prints the average grade.
"""


# --->Solution
def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries, overwriting values
    from the second dictionary.
    """
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        merged_dict[key] = value
    return merged_dict


# Given:
grades = {"Alice": 90, "Bob": 85, "Charle": 92}

# grades that has to be merged(self entered ):
Additional_grades = {"Surajan": 97, "milan": 97, "Ram": 88}

merged_grade = merge_dicts(grades, Additional_grades)
print("The Merged grade is :", merged_grade)

# calculating avg:

total_grade = sum(merged_grade.values())
num_students = len(merged_grade)
avg_grade = total_grade / num_students
print("The average grade of students is :", avg_grade)

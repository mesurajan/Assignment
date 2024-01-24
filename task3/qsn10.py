"""
Write a function update_grade(student_dict, student_name, new_grade) 
that takes a dictionary of students, the name of a student, and a new grade.
Update the grade of the specified student and return the modified dictionary.
 
"""
students = {
    "Surajan": {"age": 21, "grade": "B"},
    "Milan": {"age": 20, "grade": "A+"},
    "Avay": {"age": 25, "grade": "A++"},
    "Sid": {"age": 18, "grade": "A-"},
    "Shishir": {"age": 35, "grade": "A++"},
    "Chirag": {"age": 19, "grade": "A+++"},
}
name_to_update_grade = "Surajan"
new_grades = "A+"

if name_to_update_grade in students:
    students[name_to_update_grade]["grade"] = new_grades
    print(f"The upgraded grades of {name_to_update_grade} is {new_grades}:")
else:
    print("Student grade not upgraded in directory")

print("The updated directory is :\n")
print(students)

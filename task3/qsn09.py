"""
Create a nested dictionary called students with keys as student names and values as
dictionaries containing 'age' and 'grade' for each student. Add information for at least three students. 
"""
# ---->Solution
students = {
    "Surajan": {"age": 21, "grade": "A"},
    "Milan": {"age": 20, "grade": "A+"},
    "Avay": {"age": 25, "grade": "A++"},
    "Sid": {"age": 18, "grade": "A-"},
    "Shishir": {"age": 35, "grade": "A++"},
    "Chirag": {"age": 19, "grade": "A+++"},
}
for x, i in students.items():
    print(f"The name of student is :{x}")
    print(f"Age  :{i['age']}")
    print(f"Grade :{i['grade']}")
    print("--" * 20)

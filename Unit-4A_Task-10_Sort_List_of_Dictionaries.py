# List of student dictionaries
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 72},
    {"name": "Charlie", "marks": 90},
    {"name": "David", "marks": 65}
]

# Sort in ascending order
ascending = sorted(students, key=lambda x: x["marks"])

print("Students sorted in Ascending Order:")
for student in ascending:
    print(student)

# Sort in descending order
descending = sorted(students, key=lambda x: x["marks"], reverse=True)

print("\nStudents sorted in Descending Order:")
for student in descending:
    print(student)
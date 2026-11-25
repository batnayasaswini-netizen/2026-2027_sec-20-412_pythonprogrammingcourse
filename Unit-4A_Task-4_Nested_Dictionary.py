# Creating a nested dictionary to store student details

students = {
    101: {
        "name": "Rahul",
        "marks": 85
    },
    102: {
        "name": "Priya",
        "marks": 90
    },
    103: {
        "name": "Arun",
        "marks": 78
    }
}

# Printing student name and marks

print("Student Details:")

for roll_no, details in students.items():
    print("Roll Number:", roll_no)
    print("Name:", details["name"])
    print("Marks:", details["marks"])
    print("-------------------")
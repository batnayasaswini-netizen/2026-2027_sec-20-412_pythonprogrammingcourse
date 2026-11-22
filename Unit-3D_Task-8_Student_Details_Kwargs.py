def student_details(**kwargs):
    print("Student Name:", kwargs['name'])
    print("Subject Marks:")

    for subject, marks in kwargs.items():
        if subject != 'name':
            print(subject, ":", marks)


# Function call
student_details(
    name="Rahul",
    Maths=90,
    Science=85,
    English=88,
    Computer=95
)
student = {"name": "John", "age": 20, "grade": "A"}

print(student.keys())       # Display keys
print(student.values())     # Display values
print(student.items())      # Display key-value pairs
print(student.get("name"))  # Get a value

student.update({"age": 21}) # Update value
print(student)

student.pop("grade")        # Remove an item
print(student)
# Create a dictionary of subject marks
marks = {
    "Maths": 95,
    "Science": 90,
    "English": 85,
    "Computer": 98
}

# Print dictionary keys
print("Dictionary Keys:")
for key in marks.keys():
    print(key)

# Print dictionary values
print("\nDictionary Values:")
for value in marks.values():
    print(value)

# Print dictionary items (key-value pairs)
print("\nDictionary Items:")
for key, value in marks.items():
    print(key, ":", value)
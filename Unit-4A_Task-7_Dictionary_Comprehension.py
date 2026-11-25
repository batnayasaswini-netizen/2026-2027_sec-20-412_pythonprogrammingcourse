# Create a dictionary of numbers and their squares
n = int(input("Enter the range: "))

squares = {x: x**2 for x in range(1, n + 1)}

print("Dictionary of numbers and their squares:")
print(squares)
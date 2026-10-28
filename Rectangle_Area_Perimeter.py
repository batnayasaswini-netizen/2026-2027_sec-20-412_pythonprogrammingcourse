length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculating area (length × width)
area = length * width

# Calculating perimeter (2 × (length + width))
perimeter = 2 * (length + width)

# Displaying the results
print(f"\nArea of the rectangle: {area:.2f}")
print(f"Perimeter of the rectangle: {perimeter:.2f}")
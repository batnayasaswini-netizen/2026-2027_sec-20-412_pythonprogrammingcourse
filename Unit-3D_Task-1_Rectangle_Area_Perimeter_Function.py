def rectangle(length, breadth):
    area = length * breadth
    perimeter = 2 * (length + breadth)
    return area, perimeter

# Taking input from the user
length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

# Calling the function
area, perimeter = rectangle(length, breadth)

# Displaying the results
print("Area of rectangle:", area)
print("Perimeter of rectangle:", perimeter)
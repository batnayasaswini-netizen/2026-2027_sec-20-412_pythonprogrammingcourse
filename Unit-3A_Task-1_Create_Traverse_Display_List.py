# Create a list
my_list = []

# Get the number of elements
n = int(input("Enter the number of elements: "))

# Insert elements into the list
for i in range(n):
    element = input("Enter element: ")
    my_list.append(element)

# Display the list
print("\nElements in the list are:")
print(my_list)

# Traverse the list
print("\nTraversing the list:")
for element in my_list:
    print(element)
# Global variable
x = 10

def display():
    # Local variable
    x = 20
    print("Value of x inside function:", x)

# Calling the function
display()

# Printing the global variable
print("Value of x outside function:", x)
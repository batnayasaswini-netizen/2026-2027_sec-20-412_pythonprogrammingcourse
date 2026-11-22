# Arithmetic Operations on Two Numbers

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nArithmetic Operations:")

print("Addition (+)       =", num1 + num2)
print("Subtraction (-)    =", num1 - num2)
print("Multiplication (*) =", num1 * num2)

if num2 != 0:
    print("Division (/)       =", num1 / num2)
    print("Floor Division (//)=", num1 // num2)
    print("Modulus (%)        =", num1 % num2)
else:
    print("Division (/): Not possible (division by zero)")
    print("Floor Division (//): Not possible")
    print("Modulus (%): Not possible")

print("Exponentiation (**) =", num1 ** num2)
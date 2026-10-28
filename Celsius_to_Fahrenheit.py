# Python program to convert Celsius to Fahrenheit

# Take temperature input from the user in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Apply the conversion formula: (Celsius * 9/5) + 32
fahrenheit = (celsius * 9/5) + 32

# Display the result formatted to two decimal places
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

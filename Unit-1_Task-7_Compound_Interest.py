# Program to calculate Compound Interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time (in years): "))

# Calculate compound amount
amount = principal * (1 + rate / 100) ** time

# Calculate compound interest
compound_interest = amount - principal

# Display the result
print("Principal Amount:", principal)
print("Total Amount:", round(amount, 2))
print("Compound Interest:", round(compound_interest, 2))
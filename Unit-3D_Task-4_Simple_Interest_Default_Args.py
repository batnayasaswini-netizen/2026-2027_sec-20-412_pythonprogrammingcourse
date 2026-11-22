def simple_interest(principal, time, rate=5):
    SI = (principal * time * rate) / 100
    return SI

# Calling the function using the default rate
result1 = simple_interest(1000, 2)
print("Simple Interest with default rate:", result1)

# Calling the function with an explicit rate
result2 = simple_interest(1000, 2, 10)
print("Simple Interest with explicit rate:", result2)
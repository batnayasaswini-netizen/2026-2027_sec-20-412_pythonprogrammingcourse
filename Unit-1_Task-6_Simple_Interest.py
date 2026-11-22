# Python Program to Calculate Simple Interest

def simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si


# Example
principal = 1000
rate = 5
time = 2

result = simple_interest(principal, rate, time)

print("Simple Interest Calculator")
print("--------------------------")
print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time:", time, "years")
print("Simple Interest:", result)


# Five Test Cases
print("\n----- FIVE TEST CASES -----")

# Test Case 1
print("Test Case 1:", simple_interest(1000, 5, 2))

# Test Case 2
print("Test Case 2:", simple_interest(2000, 10, 3))

# Test Case 3
print("Test Case 3:", simple_interest(5000, 8, 2))

# Test Case 4
print("Test Case 4:", simple_interest(10000, 6, 5))

# Test Case 5
print("Test Case 5:", simple_interest(1500, 4, 3))
def find_sum(*args):
    total = 0
    for num in args:
        total += num
    return total

# Function calls
print("Sum =", find_sum(10, 20))
print("Sum =", find_sum(10, 20, 30))
print("Sum =", find_sum(1, 2, 3, 4, 5))
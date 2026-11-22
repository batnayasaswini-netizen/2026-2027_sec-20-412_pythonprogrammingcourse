from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using map() with lambda to find squares
squares = list(map(lambda x: x * x, numbers))
print("Squares:", squares)

# Using filter() with lambda to find even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)

# Using reduce() with lambda to find the sum
total = reduce(lambda x, y: x + y, numbers)
print("Sum of Numbers:", total)
# Matrix operations using nested lists

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Addition
add = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

# Subtraction
sub = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]

# Multiplication
mul = [[sum(A[i][k] * B[k][j] for k in range(2))
        for j in range(2)] for i in range(2)]

print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)
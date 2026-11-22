# Tuple operations

# 1. Concatenation
t1 = (10, 20, 30)
t2 = (40, 50)
t3 = t1 + t2
print("Concatenation:", t3)

# 2. Slicing
print("Slicing:", t3[1:4])

# 3. Unpacking
a, b, c, d, e = t3
print("Unpacking:", a, b, c, d, e)
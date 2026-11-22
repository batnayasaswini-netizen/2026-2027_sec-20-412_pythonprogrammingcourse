# Demonstration of Operator Precedence and Associativity

# Operator Precedence
a = 10 + 5 * 2
b = (10 + 5) * 2

print("Operator Precedence:")
print("10 + 5 * 2 =", a)
print("(10 + 5) * 2 =", b)

# Operator Associativity
x = 20 - 10 - 5
y = 20 / 10 * 2

print("\nOperator Associativity:")
print("20 - 10 - 5 =", x)
print("20 / 10 * 2 =", y)

# Right-to-left Associativity
z = 2 ** 3 ** 2
print("2 ** 3 ** 2 =", z)
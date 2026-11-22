# Program to demonstrate string creation and basic operations

# 1. String Creation
str1 = "Hello"
str2 = "World"

print("String 1:", str1)
print("String 2:", str2)

# 2. String Concatenation
result = str1 + " " + str2
print("\nString Concatenation:", result)

# 3. String Repetition
repeat = str1 * 3
print("String Repetition:", repeat)

# 4. String Slicing
text = "Python Programming"

print("\nOriginal String:", text)
print("First 6 characters:", text[0:6])
print("Characters from index 7 to 17:", text[7:18])
print("First 3 characters:", text[:3])
print("Last 5 characters:", text[-5:])
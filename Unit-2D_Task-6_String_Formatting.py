# Demonstration of String Formatting in Python

name = "Alice"
age = 20
marks = 95.5

# 1. Using format() method
print("Using format() method:")
print("My name is {}. I am {} years old and scored {} marks.".format(name, age, marks))

# 2. Using f-strings
print("\nUsing f-strings:")
print(f"My name is {name}. I am {age} years old and scored {marks} marks.")

# 3. Using % operator
print("\nUsing % operator:")
print("My name is %s. I am %d years old and scored %.1f marks." % (name, age, marks))
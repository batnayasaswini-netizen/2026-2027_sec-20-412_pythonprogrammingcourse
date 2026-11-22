def calculate(m1, m2, m3):
    total = m1 + m2 + m3
    average = total / 3

    return total, average


# Taking marks as input
a = int(input("Enter marks of Subject 1: "))
b = int(input("Enter marks of Subject 2: "))
c = int(input("Enter marks of Subject 3: "))

# Function call
total, average = calculate(a, b, c)

# Displaying results
print("Total Marks =", total)
print("Average Marks =", average)
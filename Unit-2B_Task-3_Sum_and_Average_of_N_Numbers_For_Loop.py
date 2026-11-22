n = int(input("Enter the number of values: "))

sum = 0

for i in range(n):
    num = float(input("Enter a number: "))
    sum = sum + num

average = sum / n

print("Sum =", sum)
print("Average =", average)
n = int(input("Enter the number of elements: "))

largest = float('-inf')

for i in range(n):
    num = float(input("Enter a number: "))

    if num > largest:
        largest = num

print("The largest number is:", largest)
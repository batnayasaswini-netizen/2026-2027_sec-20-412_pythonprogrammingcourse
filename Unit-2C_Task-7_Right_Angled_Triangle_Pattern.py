# Read the number of rows
rows = int(input("Enter the number of rows: "))

# Read the symbol to print
symbol = input("Enter the symbol to print (* or 0): ")

# Print the right-angled triangle pattern
for i in range(1, rows + 1):
    print(symbol * i)
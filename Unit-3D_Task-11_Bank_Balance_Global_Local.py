# Global balance
balance = 1000

# Function to deposit money using global variable
def deposit(amount):
    global balance
    balance += amount
    print("Amount deposited:", amount)
    print("Updated balance:", balance)

# Function using a local variable
def local_deposit(amount):
    balance = 500  # Local variable
    balance += amount
    print("Local balance:", balance)

# Main program
print("Initial bank balance:", balance)

deposit(500)

local_deposit(200)

print("Final bank balance:", balance)
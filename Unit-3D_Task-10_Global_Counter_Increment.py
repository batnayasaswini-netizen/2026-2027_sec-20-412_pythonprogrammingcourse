counter = 0  # Global variable

def increment():
    global counter
    counter += 1
    print("Counter:", counter)

# Function calls
increment()
increment()
increment()
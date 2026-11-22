# Create a set
fruits = {"apple", "banana", "mango"}

# Membership testing
print("apple" in fruits)
print("grapes" not in fruits)

# Add an element
fruits.add("orange")
print("After add:", fruits)

# Remove an element
fruits.remove("banana")
print("After remove:", fruits)

# Discard an element
fruits.discard("grapes")
print("After discard:", fruits)
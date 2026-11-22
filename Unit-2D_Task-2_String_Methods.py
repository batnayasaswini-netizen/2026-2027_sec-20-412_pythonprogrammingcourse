# Program to demonstrate Python String Methods

# Original string
text = "  Hello Python Programming  "

# 1. upper() - Converts string into uppercase
print("Uppercase:", text.upper())

# 2. lower() - Converts string into lowercase
print("Lowercase:", text.lower())

# 3. strip() - Removes spaces from beginning and end
print("Strip:", text.strip())

# 4. split() - Splits string into a list
words = "Hello Python Programming"
print("Split:", words.split())

# 5. join() - Joins elements of a list into a string
my_list = ["Hello", "Python", "Programming"]
print("Join:", " ".join(my_list))

# 6. replace() - Replaces a word with another word
print("Replace:", words.replace("Python", "Java"))

# 7. find() - Returns the position of a substring
print("Find:", words.find("Python"))
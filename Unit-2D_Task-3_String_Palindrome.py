string = input("Enter a string: ")

# Reverse the string
reverse = string[::-1]

# Check whether the string is a palindrome
if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
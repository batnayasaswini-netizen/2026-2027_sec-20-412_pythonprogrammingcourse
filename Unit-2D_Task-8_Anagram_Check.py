str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Convert strings to lowercase and sort them
str1 = str1.lower()
str2 = str2.lower()

if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
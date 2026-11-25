# Two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Create a copy of the first dictionary
merged_dict = dict1.copy()

# Merge the second dictionary into the copy
merged_dict.update(dict2)

# Display the results
print("First Dictionary:", dict1)
print("Second Dictionary:", dict2)
print("Merged Dictionary:", merged_dict)
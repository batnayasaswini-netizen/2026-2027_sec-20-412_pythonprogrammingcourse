with open("sample.txt", "r") as f:
    data = f.read()

with open("copy.txt", "w") as f:
    f.write(data)

print("File copied successfully!")
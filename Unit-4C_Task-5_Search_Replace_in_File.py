file = open("sample.txt", "r")
data = file.read()
file.close()

data = data.replace("Python", "Java")

file = open("sample.txt", "w")
file.write(data)
file.close()

print("Word replaced successfully!")
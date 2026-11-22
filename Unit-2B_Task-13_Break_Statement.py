# 1.using for loop
# Demonstrating break statement using for loop

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("Loop terminated")

#2. using while loop 

# Demonstrating break statement using while loop

i = 1

while i <= 10:
    if i == 5:
        break
    print(i)
    i = i + 1

print("Loop terminated")
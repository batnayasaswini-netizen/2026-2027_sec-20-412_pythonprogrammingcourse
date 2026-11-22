# 1.using for loop
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

    # 2.using while loop
    i = 0

while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)
    
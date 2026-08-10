# Print 1 to 100 in snakes and ladder pattern.
num = 1

for row in range(10):
    li = []

    for col in range(10):
        li.append(num)
        num = num + 1

    if row % 2 != 0:
        li.reverse()

    for i in li:
        print(i, end="\t")

    print()
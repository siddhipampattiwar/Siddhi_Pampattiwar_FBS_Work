# Python Program to Find the Union of two Lists
li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

union = []

for i in li1:
    if i not in union:
        union.append(i)

for i in li2:
    if i not in union:
        union.append(i)

print("Union:", union)
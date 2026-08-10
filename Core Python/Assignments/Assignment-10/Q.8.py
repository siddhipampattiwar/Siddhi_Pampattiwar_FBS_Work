# Write a program to create a duplicate of an existing list. It should not point to same list.
li = [10, 20, 30, 40, 50]

new = []

for i in li:
    new.append(i)

print("Original list:", li)
print("Duplicate list:", new)
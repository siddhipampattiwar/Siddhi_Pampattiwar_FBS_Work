# Write a program to remove duplicates from the list.
li = [10, 20, 10, 30, 20, 40, 30]

new = []

for i in li:
    if i not in new:
        new.append(i)

print("List after removing duplicates:", new)
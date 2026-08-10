# Write a program to remove all occurrences of a given element in the list.
li = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to remove: "))

new = []

for i in li:
    if i != num:
        new.append(i)

print("List after removing:", new)
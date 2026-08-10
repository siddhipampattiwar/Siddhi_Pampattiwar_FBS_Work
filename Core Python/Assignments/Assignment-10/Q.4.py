# Write a program to reverse the list.
li = [10, 20, 30, 40, 50]

rev = []

for i in range(len(li) - 1, -1, -1):
    rev.append(li[i])

print("Reversed list:", rev)
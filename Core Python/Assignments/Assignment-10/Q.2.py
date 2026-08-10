# Write a program to find maximum and minimum element in a list.
li = [10, 25, 5, 40, 15]

max = li[0]
min = li[0]

for i in li:
    if i > max:
        max = i

    if i < min:
        min = i

print("Maximum element:", max)
print("Minimum element:", min)
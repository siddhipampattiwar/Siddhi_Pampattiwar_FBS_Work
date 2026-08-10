# Write a program to find the second largest element in the list.
li = [10, 25, 40, 15, 30]

max = li[0]
second = li[0]

for i in li:
    if i > max:
        second = max
        max = i
    elif i > second and i != max:
        second = i

print("Second largest element:", second)
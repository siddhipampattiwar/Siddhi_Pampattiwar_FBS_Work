# Write a program to create a new list from existing list which contains cube of each number of list.
li = [1, 2, 3, 4, 5]

cube = []

for i in li:
    cube.append(i * i * i)

print("Cube list:", cube)
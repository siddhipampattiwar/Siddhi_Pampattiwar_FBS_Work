# Python Program to Find the Intersection of Two Lists
li1 = [10, 20, 30, 40]
li2 = [30, 40, 50, 60]

intersection = []

for i in li1:
    if i in li2:
        intersection.append(i)

print("Intersection:", intersection)
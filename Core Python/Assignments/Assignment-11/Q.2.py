# Python Program to Merge Two Lists and Sort it
li1 = [30, 10, 50]
li2 = [40, 20, 60]

# Merge two lists
li = li1 + li2

# Sort using Bubble Sort
for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Merged and sorted list:", li)
# Python Program to Find the Second Largest Number in a List Using Bubble Sort
li = [10, 40, 20, 50, 30]

# Bubble Sort
for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if li[j] > li[j + 1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Sorted list:", li)
print("Second largest:", li[-2])
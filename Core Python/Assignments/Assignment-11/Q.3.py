# Python Program to Sort the List According to the Second Element in Sublist
li = [[1, 5], [2, 3], [3, 8], [4, 1]]

for i in range(len(li)):
    for j in range(0, len(li) - i - 1):
        if li[j][1] > li[j + 1][1]:
            temp = li[j]
            li[j] = li[j + 1]
            li[j + 1] = temp

print("Sorted list:", li)